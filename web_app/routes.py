from os import path
from flask import render_template, url_for, request, flash, redirect
from web_app import app
from werkzeug.utils import secure_filename
from web_app import utils

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		if 'img_upload' not in request.files:
			return redirect(request.url) # redirect somewhere else
		f = request.files['img_upload']
		if f.filename == '':
			return redirect(request.url)

		if f and utils.allowed_file(f.filename):
			f.save(path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
			utils.proceed_movie_maker()
			return redirect(request.url)

	else:
		return render_template('home.html')
