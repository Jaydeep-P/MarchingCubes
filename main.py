import functions as f
from sphere import Sphere

width = 100  #w*w*w = 1,000,000
numSpheres = 10

def main():

	facets = []

	arr = [[[0 for x in range(width)] for y in range(width)] for z in range(width)]

	slist = [f.newSphere() for x in range(numSpheres)]


	for x in range(width):
		for y in range(width):
			for z in range(width):
				val = 0
				for s in slist:
					val+= s.getVal([x,y,z])
				arr[x][y][z] = val


	# f.makegif(arr,width)
	# f.printArr(arr)
	# f.print3DModel(arr)

	facets = f.makeFacets(arr)
	f.makeSTL(facets)


if __name__ == '__main__':
	main()