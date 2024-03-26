Environment Variables Required or Setup in setting.py file: 
  DB_User (database username)
  DB_Host (database host)
  DB_Name (database name)
  DB_Password (database password)
  DB_Port (database port)

Steps: Running catalyst_count in pycharm:
Clone repository catalyst_count
   git clone https://github.com/chapparu/catalyst_count.git
Now install packages using below command
  cd /catalyst_count
   pip install -r requirements.txt
 
for creating table schema into database
 python manage.py makemigrations
 python manage.py migrate

Configuring Project
  In pycharm click on "Add configuration"
  Click on + and select python.
  Name “Anything”
  Script Path : in the Django project select manage.py file For example: C:\Users\ruchita.rehpade\Desktop\py_test\catalyst_count\manage.py
  Parameters : runserver --noreload ip:port
  Click on Apply then Click ok.
  Goto File Menu >> Settings >> Project: catalyst_count
  Click on Python Interpreter
  Select system interpreter, then you will be shown installed packages
  Click on Apply and click ok
Set environment variables on system
  To set variables, Press window button, search environment variables.
  It will open window Click on Environment Variables button.
  It will open window On System Variables click on New button And add all variables then, click on ok.
Run Project
 Click on the run project button shown in Pycharm.
 It will shows Console output with Project running IP and Port
