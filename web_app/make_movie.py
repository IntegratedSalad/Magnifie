from movie_funcs import *


def start_movie_maker():
	import cv2
	from shutil import copyfile
	from shutil import rmtree

	mkdir(path.join(MOVIE_FOLDER, 'temp')) # make temp

	
	debug_reset()

	remove_temp(False)
	make_temp()
	copy_img()
	base_image = Image.open(TMP_FOLDER + '/base_img.jpg')

	make_movie_from_image(base_image, base_image.width / 2, base_image.height  / 2, 1.0, 0.001)



