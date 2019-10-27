from web_app import movie_funcs

def start_movie_maker():
	from PIL import Image
	# from shutil import copyfile
	# from shutil import rmtree

	#remove_temp(False)
	#movie_funcs.make_temp()
	
	movie_funcs.reset()
	ext = movie_funcs.copy_img()
	base_image = Image.open(movie_funcs.TMP_FOLDER + '/base_img.{0}'.format(ext))

	movie_funcs.make_movie_from_image(base_image, base_image.width / 2, base_image.height  / 2, ext, 1.0, 0.001)


	"""After the movie is done, delete input file, delete tmp in htmlfo"""

	"""JPG: WORKS BMP: JPEG: PNG: """
