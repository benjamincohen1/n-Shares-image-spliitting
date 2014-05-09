from PIL import Image
import random
WHITE = 255
BLACK = 0
def split2shares(img):
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


	im.show()
	im2.save("rand1.png")
	im3.save("rand2.png")

	return im2, im3

def superimpose(img1, img2):

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
	    	if i1[i,j] == (BLACK, BLACK, BLACK) or i2[i,j] == (BLACK, BLACK, BLACK):
	    		iNewPixels[i,j] = (BLACK, BLACK, BLACK)
	    	else:
				iNewPixels[i,j] = (WHITE, WHITE, WHITE)
	iNew.show()
	iNew.save('out.png')
	return iNew



def main():
	i1, i2 = split2shares("test.jpg")
	iNew = superimpose("rand1.png", "rand2.png")

	# iNew.show()
if __name__ == "__main__":
	main()