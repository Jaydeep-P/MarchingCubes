import functions as f
from sphere import Sphere

import time

numFrames = 1

width = 100  #w*w*w = 1,000,000

# 1000 takes 4.5 hours
# 500 takes 2022 seconds or 30 mins
# 200 takes 147 seconds or 2.5 mins
# 100 takes 18 seconds ## 5 seconds 45 mins
# 10 takes 0.018 seconds

# exactly a N^3 algorithm

numSpheres = 8

def main():

	arr = [[[0 for x in range(width)] for y in range(width)] for z in range(width)]

	slist = [f.newSphere() for x in range(numSpheres)]

	# f.makegif(arr,width)
	# f.printArr(arr)
	# f.print3DModel(arr)

	for index in range(numFrames):
		start_time = time.time()
		for x in range(width):
			for y in range(width):
				for z in range(width):
					val = 0
					for s in slist:
						val+= s.getVal([x,y,z])
					arr[x][y][z] = val
		facets = f.makeFacets(arr)
		f.makeSTL(facets,index)
		for i in range(len(slist)):
			slist[i].updatePos(width)
		print("- %s s -" % (time.time() - start_time))
		print('-',100*((index+1)/numFrames),'%')


if __name__ == '__main__':
	main()