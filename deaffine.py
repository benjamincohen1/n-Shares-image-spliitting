from PIL import Image
import sys
from fractions import gcd

"""
Naive implementation of modular inverse.  Since we are only calculating inverses mod 256,
the low speed doesn't matter.
"""
def naive_inverse(a, n=256):
	for b in range(0, 256):
		if (a*b)%256 == 1:
			return b
	raise ValueError("%d has no inverse mod %d" % (a, n))
	return None
	
##Key array:
##[(R-mult, R),
##(G-mult, G),
##(B-mult, B)]
##
def deaffine(file, key):
	img = Image.open(file)
	img_pixels = img.load()
	
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			img_pixels[i,j] = apply_key(img_pixels[i, j], key)
	
	img.save("%s_deaffine_out.png" % (file))
	return img

def apply_key(pixel, key):
	r = ((pixel[0] - key[0][1]) * key[0][0]) % 256
	g = ((pixel[1] - key[1][1]) * key[1][0]) % 256
	b = ((pixel[2] - key[2][1]) * key[2][0]) % 256
	return (r, g, b)
	
def main():
	gcdwarning = "You chose an alpha%s value with no inverse.  This program cannot reverse the cipher."
	if len(sys.argv) < 3:
		print "Usage: python affine.py 'image' r-multiplier r-shift [g-m g-s b-m b-s]\n"
		print "If no g and b keys are given, the r key will apply to all three channels."
		print "Input the original key used to encrypt the image, not the inverse."
		return
	elif len(sys.argv) < 8:
		#Assume image, r key.
		if gcd(int(sys.argv[2]), 256) != 1:
			print gcdwarning % ('')
			return
		key = [(int(sys.argv[2]), int(sys.argv[3]))]*3
	else:
		#assume image, rgb key.
		if gcd(int(sys.argv[2]), 256) != 1:
			print gcdwarning % (' R')
			return
		if gcd(int(sys.argv[4]), 256) != 1:
			print gcdwarning % (' G')
			return
		if gcd(int(sys.argv[6]), 256) != 1:
			print gcdwarning % (' B')
			return
		key = [(naive_inverse(int(sys.argv[2])), int(sys.argv[3])),
				(naive_inverse(int(sys.argv[4])), int(sys.argv[5])),
				(naive_inverse(int(sys.argv[6])), int(sys.argv[7]))]
	img = deaffine(sys.argv[1], key)	
	img.show()

main()