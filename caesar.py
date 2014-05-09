from PIL import Image
import sys

def caesar(file, key, keyG=None, keyB=None):
	if keyG is not None and keyB is not None:
		keyR = key
	else:
		keyR, keyG, keyB = key, key, key
	img = Image.open(file)
	img_pixels = img.load()
	
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			img_pixels[i,j] = apply_key(img_pixels[i, j], keyR, keyG, keyB)
	
	img.save("%s_caesar_out.png" % (file))
	return img

def apply_key(pixel, r, g, b):
	out_tuple = ((pixel[0]+r) % 256, (pixel[1]+g) % 256, (pixel[2]+b) % 256)
	return out_tuple

def main():
	if len(sys.argv) < 3:
		print "Usage: python caesar.py 'image' r [g b]\nIf no g and b keys are given, the r key will apply to all three channels."
		return
	elif len(sys.argv) < 5:
		#Assume image, r key. maybe g, but no b for sure.
		img = caesar(sys.argv[1], int(sys.argv[2]))
	else:
		img = caesar(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
	img.show()

main()