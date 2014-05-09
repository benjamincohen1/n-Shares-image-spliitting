from PIL import Image
import sys


##Key array:
##[(R, R-mult),
##(G, G-mult),
##(B, B-mult)]
##
def affine(file, key):
	img = Image.open(file)
	img_pixels = img.load()
	
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			img_pixels[i,j] = apply_key(img_pixels[i, j], key)
	
	img.save("%s_affine_out.png" % (file))
	return img

def apply_key(pixel, key):
	r = (key[0][0]*pixel[0] + key[0][1]) % 256
	g = (key[1][0]*pixel[1] + key[1][1]) % 256
	b = (key[2][0]*pixel[2] + key[2][1]) % 256
	return (r, g, b)

def main():
	if len(sys.argv) < 3:
		print "Usage: python caesar.py 'image' r-multiplier r-shift [g-m g-s b-m b-s]\n"
		print "If no g and b keys are given, the r key will apply to all three channels."
		return
	elif len(sys.argv) < 8:
		#Assume image, r key.
		key = [(int(sys.argv[2]), int(sys.argv[3]))]*3
	else:
		#assume image, rgb key.
		key = [(int(sys.argv[2]), int(sys.argv[3])),
				(int(sys.argv[4]), int(sys.argv[5])),
				(int(sys.argv[6]), int(sys.argv[7]))]
	img = affine(sys.argv[1], key)	
	img.show()

main()