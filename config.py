import os

from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_openapi3 import OpenAPI, Info

info = Info(title='Product Hub API', version='1.0.0')
app = OpenAPI(
    __name__,
    info=info,
    doc_prefix='/product-hub',
)
db_url = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
