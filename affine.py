from PIL import Image
import sys
from fractions import gcd

##Key array:
##[(R-mult, R),
##(G-mult, G),
##(B-mult, B)]
##
def affine(file, key):
	img = Image.open(file)
	img_pixels = img.load()
	#loop through every pixel
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			img_pixels[i,j] = apply_key(img_pixels[i, j], key) #apply the cipher
	
	img.save("%s_affine_out.png" % (file)) #save the image and return it
	return img

def apply_key(pixel, key):
	#affine cipher: an + b
	r = (key[0][0]*pixel[0] + key[0][1]) % 256 
	g = (key[1][0]*pixel[1] + key[1][1]) % 256
	b = (key[2][0]*pixel[2] + key[2][1]) % 256
	return (r, g, b)




def main():
	gcdwarning = "You chose an alpha%s value that is not easily decrypted. You won't be able to decrypt the image with this program."
	if len(sys.argv) < 3:
		print "Usage: python affine.py 'image' r-multiplier r-shift [g-m g-s b-m b-s]\n"
		print "If no g and b keys are given, the r key will apply to all three channels."
		return
	elif len(sys.argv) < 8:
		#Assume image, r key.
		if gcd(int(sys.argv[2]), 256) != 1:
			print gcdwarning % ('')
		key = [(int(sys.argv[2]), int(sys.argv[3]))]*3
	else:
		#assume image, rgb key.
		if gcd(int(sys.argv[2]), 256) != 1:
			print gcdwarning % (' R')
		if gcd(int(sys.argv[4]), 256) != 1:
			print gcdwarning % (' G')
		if gcd(int(sys.argv[6]), 256) != 1:
			print gcdwarning % (' B')
		key = [(int(sys.argv[2]), int(sys.argv[3])),
				(int(sys.argv[4]), int(sys.argv[5])),
				(int(sys.argv[6]), int(sys.argv[7]))]
	img = affine(sys.argv[1], key)	
	img.show()


main()