import os
import sqlite3
import json

from platform import system
from flask import Flask
from flask import request,Response
from flask_restplus import Api
from flask import g


 

app = Flask(__name__)
api = Api(app)


if system()=='Windows':
    DATABASE ='C:/Users/admin/Desktop/Unificater_dev/Ramu/IssueTracker/sqllite_db.db'
elif system()=='Linux':
    DATABASE ='/home/brituser/Issue_tracker/IssueTracker/sqllite_db.db'

def db_conn():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/addissue',methods = ['POST'])
def create_issue():
    try:
        if request.method=='POST':
            d= request.get_json()
            #d= request.data
            db_conn().row_factory=dict_factory
            sql_cursor=db_conn().cursor()

            sql_cursor.execute(f'''insert into PROD_ISSUE_TRACKER
                            (issueName,startDate,endDate,issuedetails,resolutionDetails,category,stakeHolder)
                            values
                            {d['issueName'],d['startDate'],d['endDate'],d['issuedetails'],
                            d['resolutionDetails'],d['category'],d['stakeHolder']}''')
            
            db_conn().commit()
            sql_cursor.execute("SELECT * From PROD_ISSUE_TRACKER")
            data ={'status':200,'message':'successful','data':sql_cursor.fetchall()}
            return json.dumps(data)
    except Exception as ex:
        data ={'status':400,'message':'error','data':str(ex)}
        return Response(json.dumps(data))
    finally:
        close_connection

@app.route('/clearissue', methods = ['DELETE'])
def drop_items():
    try:
        if request.method=='DELETE':
            print()
            sql_cursor=db_conn().cursor()
            sql_cursor.execute("Delete from PROD_ISSUE_TRACKER")
            db_conn().commit()
            sql_cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='PROD_ISSUE_TRACKER'")
            db_conn().commit()
            data ={'status':202,'message':'successful','data':'deleted all rows'}
            return Response(json.dumps(data))
    except Exception as ex:
        data ={'status':400,'message':'error','data':str(ex)}
        return Response(json.dumps(data))
    finally:
        close_connection

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 2232))
    app.run(host = '127.0.0.1', port=port)