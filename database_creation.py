from models import db
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/dylanwalls/Documents/Bitprop/tenant_inspections/inspections/inspection_management.db'
db.init_app(app)

with app.app_context():
    db.create_all()
    print('Database created')
