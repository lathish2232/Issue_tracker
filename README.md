# Issue_tracker
-----------------------using python and SQLlite DB created issue tracker --------------------

1.endpoint:- [POST]<br>
http://127.0.0.1:2232/addissue<br>
payload:-<br>
{"issueName":"issue 1",
"startDate":"2021-2-19",
"endDate":"2021-2-20",
"issuedetails":"issue 1 raised ",
"resolutionDetails" :"issue 1 Resolved",
"category":"Medium",
"stakeHolder":"Ravi"}


2.endpoint:- [GET]<br>
http://localhost:2232/issues<br>
note:- it will return all created Issues.



3.endpoint:- [DELETE]<br>
http://127.0.0.1:2232/clearissue<br>
note:-no payload is required it will delete all issues one shot 
