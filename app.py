from flask import Flask
from flask_migrate import Migrate

from database import db

app = Flask(__name__)

# configuracion de la base de datos
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'indumontajes'

FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
db.init_app(app)

# configurar flask_migrate
migrate = Migrate()
migrate.init_app(app, db)

# configuracion de flask-wtf
app.config['SECRET_KEY'] = 'juankk'
