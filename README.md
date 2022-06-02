


### Installation
installing jotforms
Install via git clone:

        $ git clone git://github.com/jotform/jotform-api-python.git
        $ cd jotform-api-python
        
Install via pip (latest version)

        $ pip install git+git://github.com/jotform/jotform-api-python.git


### Authentication

JotForm API requires API key for all user related calls. You can create your API Keys at  [API section](http://www.jotform.com/myaccount/api) of My Account page.

install google api sdk

        pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

with your email get a Google Cloud Platform project with the Google sheets API enabled. To create a project and enable an API check this link https://developers.google.com/workspace/guides/create-project


install requests
    
            pip install requests


get the google sheets with your data and copy its id from the url 


in the script replace my jotformapi key with yours, my googlesheetid with yours and my sheetname with yours.

after that you have installed the dependencies you dont need to do this again on subsequent runs just use the command 
python quickstart.py

