import numpy as np
import pygame, sys
pygame.init()

M=1.989 * 10**30.  #Mass of the central object
m=5.972 * 10**24.  #Mass of the orbiting object
G=6.6743 * 10**-11.   #Gravitational constant
r=150000000.  #Initial distance of orbiting object from central object
theta=0
dr=0
dtheta=1649.69/263000.   #Initial angular velocity of orbiting object. Can be calculated as period of rotation/time(s)
dt=0.5.  #Time step for derivative calculations
x=0
y=0
t=0
xs=[]
ys=[]
line=[]
c=0
white=(255,255,255)
myfont = pygame.font.SysFont("kohinoorbangla", 20)

while t<200000:
	ddr=(r*(dtheta**2))-(M*G/r**2)
	ddtheta=-(2*dr*dtheta)/r
	dr=dr+ddr*dt
	dtheta=dtheta+ddtheta*dt
	r=r+dr*dt 
	theta=theta+dtheta*dt
	x=r*np.cos(theta)
	y=r*np.sin(theta)
	#print('({}, {}), ({}, {})'.format(str(x/1000000), str(y/1000000), str(dr), str(dtheta)))
	xs.append((x/1000000)+200)
	ys.append((-y/1000000)+250)
	t+=1

x1=xs[0]
y1=ys[0]

class Circle:
	def __init__(self):
		self.pos=[xs[0],ys[0]]
		self.color = white
		self.radius = 1.5

	def draw_line(self):
		pygame.draw.circle(screen, self.color, (self.pos[0], self.pos[1]), self.radius)

for i in range(len(xs)):
	line.append(Circle())

for i in range(len(ys)):
	line[i].pos=xs[i],ys[i]

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Orbital Motion Simulator')
clock = pygame.time.Clock()
running = True
while running:

	screen.fill((0,0,0))
	pygame.draw.circle(screen, (250,100,0),(xs[0]-149.99622954135873,ys[0]),10)

	for circle in line:
		circle.draw_line()

	pygame.draw.circle(screen, (0,230,250),(x1,y1),10)

	if c-1<len(xs):
		x1=xs[c+1]
		y1=ys[c+1]
		#print('x1={}, y1={}'.format(str(x1),str(y1)))
		c+=1
	else:
		c=0

	xtext = myfont.render("X = {}".format(str(x1)), 1, (255,255,255))
	screen.blit(xtext, (5,10))

	ytext = myfont.render("Y = {}".format(str(y1)), 1, (255,255,255))
	screen.blit(ytext, (5,30))

	pygame.display.flip()
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False

pygame.quit()

