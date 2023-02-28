# Setup steps

    clone this repo


# install virtualenv and Create virtual environment
    pip install virtualenv or sudo apt install virtualenv

    virtualenv -p python3.10.6 env


# Install Postgres

    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib postgresql-client
    sudo service postgresql start
    
 
 # Create DB
    psql -U postgres
    CREATE ROLE dbadmindashboard WITH LOGIN ENCRYPTED PASSWORD 'FCRacm123987';
    CREATE DATABASE dbdashboard WITH OWNER dbadmindashboard;
    GRANT ALL PRIVILEGES ON DATABASE dbdashboard TO dbadmindashboard;
    
# Install requirements
    pip install  pip install -r requirements.txt
    pip install 'djangorestframework-simplejwt[crypto]'
    

# Settings
    add settings.ini in the path dashboard/dashboard/settings/ example: dashboard/dashboard/settings/settings.ini
    
    
# If you use pycharm, you can modify your project in this way 
    Go to file and open "settings" or you can use ctrl+alt+s
    select "project" and open python interpreter
    select in add interpreter and select existing
    search your directory bin of your virtual environment and click in apply 
     
    



