from PIL import Image
import random
import sys

WHITE = 255
BLACK = 0
def split2shares(img, n):
	
	im = Image.open(img)
	imPixels = im.load()

	im2 = Image.open(img)

	im3 = Image.open(img)


	# print(im.format, im.size, im.mode)

	for i in range(im.size[0]):    # for every pixel:
		    for j in range(im.size[1]):
		    	if ((imPixels[i,j][0] + imPixels[i,j][2] + imPixels[i,j][1])/3) <128:
		    		imPixels[i,j] = (BLACK, BLACK, BLACK)
		    	else:
	        		imPixels[i,j] = (WHITE, WHITE, WHITE)

	pixels = im.load()

	pixels2 = im2.load()
	pixels3 = im3.load()

	for i in range(im.size[0]):    # for every pixel:
	    for j in range(im.size[1]):
	    	r = random.randint(0,1)
	    	if r == 0:
	        	pixels2[i,j] = (WHITE, WHITE, WHITE)
	        else:
	        	pixels2[i,j] = (BLACK, BLACK, BLACK)

	for i in range(im.size[0]):    # for every pixel:
	    for j in range(im.size[1]):
	    	r = random.randint(0,1)
	    	if imPixels[i,j] == (WHITE, WHITE, WHITE):
	    		pixels3[i,j] = pixels2[i,j]
	    	else:
	    		if pixels2[i,j] == (WHITE, WHITE, WHITE):
	        		pixels3[i,j] = (BLACK, BLACK, BLACK)
	        	else:
	        		pixels3[i,j] = (WHITE, WHITE, WHITE)

	fName = "share" + str(n) + ".png"
	im3.save(fName)

	fName2 = "share" + str(n-1) + ".png"
	im2.save(fName2)

	if n > 2:
		fName2 = "share" + str(n-1) + ".png"
		split2shares(fName2, n-1)



	# im2.save("%s_share1.png" % (img))
	# im3.save("%s_share2.png" % (img))

	# return im2, im3

def superimpose(numImages, prob=False):
	name = None
	fName = "share" + str(1) + ".png"

	i1 = Image.open(fName)
	size = i1.size
	
	p = [Image.open("share" + str(n) + ".png").load() for n in range(1,numImages + 1)]

	iNew = Image.open(fName)
	iNewPixels = iNew.load()


	for i in range(size[0]):    # for every pixel:
	    for j in range(size[1]):
	    	# print i1[i,j]
	    	tmp = [1 for x in p if x[i,j] == (BLACK, BLACK, BLACK)]
	    	if prob:
	    		cond = len(tmp) > numImages//4
	    	else:
	    		cond = len(tmp) != 0
	    	if cond:
	    		iNewPixels[i,j] = (BLACK, BLACK, BLACK)
	    	else:
				iNewPixels[i,j] = (WHITE, WHITE, WHITE)

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
		print """Usage: python nshares.py 'image to encrypt' [number of shares]
			  \nDefaults to 2 shares.\nUse the -p flag to turn on probabilistic superimposing"""
	elif len(sys.argv) == 2:
		#Assume they only gave us an input image.
		shares = 2
		split2shares(sys.argv[1], shares)
		# str1, str2 = "%s_share1.png" % (sys.argv[1]), "%s_share2.png" % (sys.argv[1])
		superimpose(shares, sys.argv[1])
	elif len(sys.argv) > 2:
		#image and number of shares
		shares = int(sys.argv[2])
		if shares < 2:
			print "Must have more than two shares"
		split2shares(sys.argv[1], shares)
		if ('-p' in sys.argv or '-P' in sys.argv):
			superimpose(shares, True)
		else:
			superimpose(shares)


		
if __name__ == "__main__":
	main()