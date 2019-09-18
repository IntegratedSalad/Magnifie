import os
from werkzeug.utils import secure_filename
from flask import Flask

ALLOWED_EXTENSIONS = {'jpg', 'bmp', 'jpeg', 'png'}

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(app.instance_path, 'htmlfi')
MOVIE_FOLDER = os.path.join(app.instance_path, 'htmlfo')

os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)
os.makedirs(os.path.join(app.instance_path, 'htmlfo'), exist_ok=True)
app.config['SECRET_KEY'] = '5101dddda8481eb81aceb6882a21fddb'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from web_app import routes
