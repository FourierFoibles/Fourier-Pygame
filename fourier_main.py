import pygame,sys
from pygame.locals import *
import numpy as np
from dft import *
import statistics

runtime=0
rad_freq=[]
x_coords=[]
y_coords=[]
complex_coords=[]
path=[]
epi_no =50


pygame.init()                                 # initialise pygame and zone
ZONE=pygame.display.set_mode((800,800))


def get_orbit(centre,radius,freq,phase):   # function to return the centre of the next epicycle/ the orbit of the epicycle of given centre, radius,frequency etc.
	freq=2*np.pi*freq
	orbit_x= centre[0]+radius*np.cos(freq*runtime +phase)
	orbit_y= centre[1]-radius*np.sin(freq*runtime +phase)
	return (orbit_x,orbit_y)

def epicycle(centre,radius,freq,phase): # draws a line which rotates as an epicycle depending on given centre 
	orbit_centre=get_orbit(centre,radius,freq,phase)
	pygame.draw.line(ZONE, (255,0,0), centre, orbit_centre, width=1)
	pygame.draw.circle(ZONE, (0,0,0), orbit_centre, 3,3)

with open('square100-400.txt') as f: # reads in text file and  turns it into a list of x and y coordinates
    lines = f.readlines()
    for l in lines:
    	l.replace('\n','')
    	coords=str(l).split(',')
    	x_coords.append(float(coords[0]))
    	y_coords.append(float(coords[1]))

x_mean= statistics.mean(x_coords)
y_mean= statistics.mean(y_coords)

for i in range(0,len(x_coords)):                 #shifts all the coordinates so they are centered around (0,0) (likely unnecessary)
	x_coords[i]=x_coords[i]-x_mean
for i in range(0,len(y_coords)):
	y_coords[i]=y_coords[i]-y_mean

for i in range(0,len(x_coords)):                 # converts xs and ys to complex numbers
	complex_coords.append(complex(x_coords[i],y_coords[i]))



for h in complex_coords:                         # checks there are no duplicate coords
        while complex_coords.count(h) != 1:
                complex_coords.pop(complex_coords.index(h))
    	

weights=dft_1(complex_coords) # preforms the dft function I've put in another file on the series of complex numbers which should form the path

for item in weights:             # takes the fourier coefficients and extracts magnitude/frequency and phase info
	if item[1]!=0:
		radius=abs(item[0])/len(weights)
		frek=item[1]/len(weights)
		if item[0].real !=0:
			phas=math.atan(item[0].imag/item[0].real)
		else:
			phas=0
		rad_freq.append([radius,frek,phas])

def sorter(e):  # sorts epicycles in terms of size
	return e[0]
rad_freq.sort(reverse=True,key=sorter)

while len(rad_freq) > epi_no: # limits number of epicycles
	rad_freq.pop(-1)


while True:

	ZONE.fill((255,255,255))
	epi_centre=(400,400)
	n=0
	for pairing in rad_freq:                                 # Loops over radius/frequency/phase list and draws epicycles accordingly
		epicycle(epi_centre,pairing[0],pairing[1],pairing[2])
		epi_centre=get_orbit(epi_centre,pairing[0],pairing[1],pairing[2])
		if rad_freq.index(pairing) == len(rad_freq)-1:             #if it's the last epicycle, draw a path
			path.append(epi_centre)

		for pair in path:             #draws path
			pygame.draw.circle(ZONE, (0,0,255), pair, 1,1)

	while len(path)>=10000: # if path gets too big, get rid of bits at the start
		path.pop(0)

	
	runtime+=0.5 # makes animation run w.r.t. frames 

	pygame.display.update()
	for event in pygame.event.get():
		if event.type== QUIT:
			pygame.quit()
			sys.exit()
