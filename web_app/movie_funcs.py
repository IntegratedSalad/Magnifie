from PIL import Image, ImageFilter
import cv2 as cv
import os
import shutil
import numpy as np

OUTPUT_FOLDER = '/Users/buppo/Python Programs/environments/Magnifie/instance/htmlfo/temp'
THIS_FOLDER = os.path.dirname(os.path.realpath(__file__))
HTMLFI_FOLDER = os.path.join(THIS_FOLDER, 'htmlfi')
TMP_FOLDER = os.path.join(HTMLFI_FOLDER, 'tmp')

FRAMES = 24
SECONDS = 10

def copy_img():
	print("Copying image...")
	shutil.copy(os.path.join(HTMLFI_FOLDER,'img.jpg'), TMP_FOLDER + '/base_img.jpg')

def remove_temp(warn):

	if warn:
		inpt = input(f'Will remove {TMP_FOLDER}. (Y/N)')

		if inpt.lower() in ['n']:
			return
	
	shutil.rmtree(TMP_FOLDER)


def make_temp():
	os.mkdir(TMP_FOLDER)

def debug_reset():
	try:
		remove_temp(False)
	except:
		pass
	make_temp()
	copy_img()


def zoom_in(input_image):

	# We must provide an offset which will function as a "camera" - x, y position of left-upper corner of snippet box.
	# We must provide rectangular area that will function as a "cut box" dimensions.

	BOX = (200, 200) # Rectangular area - size of our capturing box

	CAMERA_X = (input_image.width / 2) # middle X of our box
	CAMERA_Y = (input_image.height / 2) # middle Y of our box

	# Zoom level
	MAGNITUDE = 1.3

	_w, _h = input_image.width, input_image.height

	_w *= MAGNITUDE # must be variadic for "animation" effect.
	_h *= MAGNITUDE

	return_image = input_image.resize((int(_w), int(_h))) # resized image

	crop_diff_x = abs(input_image.width - return_image.width) # difference after resizing 
	crop_diff_y = abs(input_image.height - return_image.height) # difference after resizing

	#print((crop_diff_x + input_image.width == return_image.width)) # True

	x = CAMERA_X + crop_diff_x
	y = CAMERA_Y + crop_diff_y

	#x, y = CAMERA_X + crop_diff_x, CAMERA_Y + crop_diff_y # middle x and middle y after the difference


	left  = (x - BOX[0])
	upper = (y - BOX[1])
	right = (x + BOX[0])
	lower = (y + BOX[1])


	return return_image.crop((left, upper, right, lower))

def zoom_at(img, x, y, zoom):
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)


def make_frame_animation(base_img, x, y, start_zoom, magnitude): # duration of zoom and duration of move must be added

	# todo: apply blur at the end and start

	blur_range = 10 # frames

	blur_radius = 30

	print("Making frames...")

	if FRAMES * SECONDS > 0:

		zoom = start_zoom

		for frame in range(FRAMES * SECONDS):

			if frame in range(blur_range):

				img = base_image

				image_blurred = img.filter(filter=ImageFilter.GaussianBlur(radius=blur_radius))

				if blur_radius <= 0:
					blur_radius = 0
				else:
					blur_radius -= 1

				image_blurred.save(TMP_FOLDER + '/' + str(frame) + '.jpg')

			else:

				img = base_image

				img = zoom_at(img, x, y, zoom)

				zoom += magnitude

				img.save(TMP_FOLDER + '/' + str(frame) + '.jpg')


	else:
		raise ValueError('Frames or seconds cannot be <= 0!')


def sort_dir(dirname):

	new = list()

	for file in os.listdir(dirname):

		if file.split('.')[0].isdigit():
			new.append(file)

	return sorted(new, key=lambda f: int(f.split('.')[0]))


def write_movie(dirname):

	print("Writing movie...")

	output = "movie.mp4"
	frame = cv.imread(os.path.join(dirname, 'base_img.jpg'))
	height, width, channels = frame.shape

	fourcc = cv.VideoWriter_fourcc(*'mp4v')
	out = cv.VideoWriter(os.path.join(OUTPUT_FOLDER, output), fourcc, 24.0, (width, height))

	for file in sort_dir(dirname):

		image_path = os.path.join(dirname, file)
		frame = cv.imread(image_path)

		out.write(frame)

	out.release()
	cv.destroyAllWindows()


def make_movie_from_image(image, x, y, start_zoom, magnitude):
	make_frame_animation(image, x, y, start_zoom, magnitude)
	write_movie(TMP_FOLDER)
	remove_temp(False)


