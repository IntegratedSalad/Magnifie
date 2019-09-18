from web_app import ALLOWED_EXTENSIONS
from web_app import UPLOAD_FOLDER
from web_app import MOVIE_FOLDER
from os import mkdir
from os import path













def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def proceed_movie_maker():
	import cv2
	from shutil import copyfile
	from shutil import rmtree

	mkdir(path.join(MOVIE_FOLDER, 'temp'))



