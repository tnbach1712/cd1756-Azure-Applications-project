import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'bachtndemo01'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'GEJDjuqqlW3IH3qpXXqVje/McAFXcbBuqxGZhGnZbv8ujQjgxAV5VF1mIrI/dOkLHNqKCeio11tU+AStH9jEGw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_DRIVER = '{ODBC Driver 18 for SQL Server}' 

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'bachtn-db.database.windows.net' # or '192.168.49.1'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'bachtnsqlserver01' #'bachtn-sqlserver-01'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'bachtn' #'sa'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '!6Den10kytu@'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + '/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://bachtn:!6Den10kytu@bachtn-db.database.windows.net/bachtnsqlserver01?driver=ODBC+Driver+17+for+SQL+Server'


    AUTHORITY = "https://login.microsoftonline.com/f958e84a-92b8-439f-a62d-4f45996b6d07"  # For multi-tenant app, else put tenant name
    
    REDIRECT_PATH = "/auth"
    CLIENT_ID = "f6c5dfde-8726-4e06-8d43-1f089be51a51"
    CLIENT_SECRET = "vbl8Q~6bLYfS8b_WKn_nMjB3At18a2jQVQbYka4u"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session