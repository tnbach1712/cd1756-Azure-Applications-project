import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'bachtnstorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ErB416CX+BvbbfiLZ9Nhm1FoitzPo4tJisdJDgw/s1ti3t+8g6OMfYiSCX68GOUljoxMpH4z/+al+ASt74L9Lg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # server = '192.168.49.1'  # e.g., 'localhost\sqlexpress' or IP address
    # database = 'bachtnsqlserver01'
    # username = 'sa'
    # password = '!6Den10kytu@'
    SQL_DRIVER = '{ODBC Driver 17 for SQL Server}' 

    SQL_SERVER = os.environ.get('SQL_SERVER') or '192.168.49.1'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'bachtnsqlserver01' #'bachtn-sqlserver-01'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sa' #'bachtn'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '!6Den10kytu@'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQL_CONN_STR = f'DRIVER={SQL_DRIVER};SERVER={SQL_SERVER};DATABASE={SQL_DATABASE};UID={SQL_USER_NAME};PWD={SQL_PASSWORD}'

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "YEp8Q~xd_UcG8KOxCcv-SpXmpg6tQj8HuwRHRcWe"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "eef84f2a-99f2-49ea-b886-ff525085c9b4"

    REDIRECT_PATH = "/callback"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session