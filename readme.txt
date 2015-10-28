(Lohith Ravuru,140050041)
(Jagadeesh Boddeda,140050053)
(Nihal Poosa,140050062)


Group number :27
Group name   : code2code
Group Honour code: We pledge on our honour that we have not given or received any unauthorized assistance on this assignment or any previous task.

number_of_late_days_taken:  3 


Lohith    - 100%
Jagadeesh - 100%
Nihal     - 100%


The commands to be entered:

$python manage.py runserver


->to run algorithm:

We assumed that input_programmes are given as an csv input or else the one in the resources folder of lab11 is used.We have to manually change the input_programmes.csv if we need to run it as per another input_programmes2.csv(say).

1)If the csv file is uploaded in http://127.0.0.1:8000/branch/list/ run the following command

$python algo.py input_programmes.csv csv_files/csv_files/input_options.csv

2)If the csv file is manually placed in the mysite/ folder which contains algo.py then run the following command

$python algo.py input_programmes.csv input_options.csv


IMPORT: 

 http://127.0.0.1:8000/branch/list/ 

•This link is for importing the data and saving into a csv file inside the static folder.We will update it to the database in the next submission.
•The uploaded file is stored in the mysite/csv_files/ folder

LINKS:

1)http://127.0.0.1:8000/admin :
•This has all the registered users and all the database about model Info.
•Super user login credentials are 
	login: "admin"
	password: "admin" 

2)http://127.0.0.1:8000/register :
•This is the link where a new user can register.
•The username and password will be saved in database and can be found out in the admin site, if the registration is successful.

3)http://127.0.0.1:8000/login :
•This is the login link where the students login to submit and edit their data (Name, Roll Number, Present branch etc)
•After loging in the students are redirected to http://127.0.0.1:8000/form where they fill their data and submit.

4)http://127.0.0.1:8000/form :
•This the link the students will be redirected to after logging in.
•Presently the filled data is getting updated in the database but it does not load the previously stored data, which will be done in late days.
•There is a logout option, which redirects to http://127.0.0.1:8000/logout where the session can be logged out.
•Presently, after submitting the form this will be redirected to http://127.0.0.1:8000/hello which will be changed to "submission successful" page in the next submission.

5)http://127.0.0.1:8000/logout :
•Open this link will logout the session.



