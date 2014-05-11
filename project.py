from PIL import Image
import random
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

	fName = 'encrypted-' + str(n) + '.png'
	im3.save(fName)

	fName2 = 'encrypted-' + str(n-1) + '.png'
	im2.save(fName2)
	
	if n > 2:
		split2shares(fName2, n-1)
	# else:
		# shares.append(im2)
	# im.show()
	# im2.save("rand1.png")
	# im3.save("rand2.png")

	# return shares



def superimpose(numImages):

	i1 = Image.open('encrypted-' + str(1) + '.png')
	size = i1.size
	
	p = [Image.open('encrypted-' + str(n) + '.png').load() for n in range(1,numImages + 1)]

	iNew = Image.open('encrypted-' + str(1) + '.png')
	iNewPixels = iNew.load()


	for i in range(size[0]):    # for every pixel:
	    for j in range(size[1]):
	    	# print i1[i,j]
	    	tmp = [1 for x in p if x[i,j] == (BLACK, BLACK, BLACK)]
	    	if tmp != []:
	    		iNewPixels[i,j] = (BLACK, BLACK, BLACK)
	    	else:
				iNewPixels[i,j] = (WHITE, WHITE, WHITE)
	iNew.show()
	iNew.save('out.png')
	return iNew


def main():
	n = 5

	split2shares("test.jpg", n)


	iNew = superimpose(n)

	# iNew.show()
if __name__ == "__main__":
	main()