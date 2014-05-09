from PIL import Image
import random
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
def split2shares(img):
	im = Image.open(img)
	imPixels = im.load()

	im2 = Image.open(img)

	im3 = Image.open(img)


	# print(im.format, im.size, im.mode)

	for i in range(im.size[0]):    # for every pixel:
		    for j in range(im.size[1]):
		    	if ((imPixels[i,j][0] + imPixels[i,j][2] + imPixels[i,j][1])/3) <128:
		    		imPixels[i,j] = BLACK
		    	else:
	        		imPixels[i,j] = WHITE


	pixels = im.load()

	pixels2 = im2.load()
	pixels3 = im3.load()

	for i in range(im.size[0]):    # for every pixel:
	    for j in range(im.size[1]):
	    	r = random.randint(0,1)
	    	if r == 0:
	        	pixels2[i,j] = WHITE
	        else:
	        	pixels2[i,j] = BLACK

	for i in range(im.size[0]):    # for every pixel:
	    for j in range(im.size[1]):
	    	r = random.randint(0,1)
	    	if imPixels[i,j] == WHITE:
	    		pixels3[i,j] = pixels2[i,j]
	    	else:
	    		if pixels2[i,j] == WHITE:
	        		pixels3[i,j] = BLACK
	        	else:
	        		pixels3[i,j] = WHITE


	im2.save("%s_share1.png" % (img))
	im3.save("%s_share2.png" % (img))

	return im2, im3

def superimpose(img1, img2, name=None):

	i1 = Image.open(img1)
	size = i1.size
	i1 = i1.load()

	i2 = Image.open(img2)
	i2 = i2.load()

	iNew = Image.open(img2)
	iNewPixels = iNew.load()


	for i in range(size[0]):    # for every pixel:
	    for j in range(size[1]):
	    	# print i1[i,j]
	    	if i1[i,j] == BLACK or i2[i,j] == BLACK:
	    		iNewPixels[i,j] = BLACK
	    	else:
				iNewPixels[i,j] = WHITE
	if name is None:
		iNew.save('out.png')
	else:
		iNew.save('%s_out.png' % (name))
	iNew.show()
	return iNew



def main():
	"""
	i1, i2 = split2shares("test.jpg")
	iNew = superimpose("rand1.png", "rand2.png")
	"""
	if len(sys.argv) == 1:
		print "Usage: python nshares.py 'image to encrypt' [number of shares] \n Defaults to 2 shares."
	else if len(sys.argv) == 2:
		#Assume they only gave us an input image.
		s1, s2 = split2shares(sys.argv[1])
		str1, str2 = "%s_share1.png" % (sys.argv[1]), "%s_share2.png" % (sys.argv[1])
		superimpose(str1, str2, sys.argv[1])
	else if len(sys.argv) > 2:
		#image and number of shares
		img = sys.argv[1]
		shares = int(sys.argv[2])
		
if __name__ == "__main__":
	main()