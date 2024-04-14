from flask import Flask, request, jsonify, render_template_string
import pyodbc
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database connection parameters
server = 'bachtn-db.database.windows.net'  # e.g., 'localhost' or '192.168.1.5'
database = 'bachtnsqlserver01'
username = 'bachtn'
password = '!6Den10kytu@'
driver = '{ODBC Driver 17 for SQL Server}'

# Connection string
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Route to fetch all items from a table 'Items'
@app.route('/users')
def get_users():
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        items = cursor.fetchall()
        # Assume each item is a tuple (id, name, description)
        return jsonify([{'id': row[0], 'pass': row[1]} for row in items])

### PUBLIC PROPERTIES ###

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://bachtn:!6Den10kytu@bachtn.database.windows.net/bachtn?driver=ODBC+Driver+17+for+SQL+Server'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define the model
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password_hash': self.password_hash
        }

@app.route('/items')
def get_items():
    items = Users.query.all()
    return jsonify([item.to_dict() for item in items])


if __name__ == '__main__':
    app.run(debug=True)
