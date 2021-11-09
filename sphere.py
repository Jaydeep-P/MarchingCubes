class Sphere(object):

	def __init__(self, radius=0,center=[0,0,0],velocity=[0,0,0]):
		super(Sphere, self).__init__()
		self.r = radius
		self.c = center
		self.v = velocity

	def updatePos(self,width):
		for i in range(3):
			self.c[i] += self.v[i]
			self.c[i] = (self.c[i] + width)%width	#roll over (this is shit, do collision with bounding box)

	def getVal(self,pos):
		a = (pos[0]-self.c[0])
		b = (pos[1]-self.c[1])
		c1 = (pos[2]-self.c[2])
		d = a*a + b*b + c1*c1
		d+= 0.01
		return (self.r*self.r)/d
