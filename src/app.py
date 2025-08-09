from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Iam, Swarm!'

# Build the database URI from environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Optional: Validate environment variables
if not all([db_user, db_password, db_host, db_port, db_name]):
    raise ValueError("Missing one or more required environment variables for DB connection.")

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional but recommended

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
