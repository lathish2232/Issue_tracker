#create table saparately before runining flask app
import sqlite3
conn = sqlite3.connect('C:/Users/admin/Desktop/Unificater_dev/Ramu/IssueTracker/sqllite_db.db')
sql_cursor= conn.cursor()
sql_cursor.execute('''CREATE TABLE PROD_ISSUE_TRACKER
             (issueId INTEGER PRIMARY KEY AUTOINCREMENT,issueName text, startDate text,endDate Date, issuedetails text,
             resolutionDetails text,category text,stakeHolder text)''')
conn.commit()
conn.close()