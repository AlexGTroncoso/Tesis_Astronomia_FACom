from astropy.io import fits as pyfits
import numpy as np
import scipy as sc
import sys

#from __future__ import print_function, division
from PyAstronomy import pyasl
import numpy as np




fits=sys.argv[1]
 
images2=pyfits.open(str(fits)+'.fits')

VCA = np.array([])

for k in range(len(images2[1].data)):
               VCA = np.append(VCA, images2[1].data[k][0])
            
               
wlvac = np.array([])
wlair = np.array([])

for i in np.arange(51450):

	vac    = 10.**(4.179 + 6.E-6*i)
	wlvac  = np.append(wlvac, vac)
	
	#air    = vac/(1 + (6.4328E-5 + 2.94981E-2/(146.0-(1.0E4/vac)**2)+2.5540E-4/(41.0-(1.0E4/vac)**2)))
	# Aquí estoy utilizando la ecuación de Morton (1991, ApJS, 77, 119)
	#air = VCA[i] / (1.0 + 2.735182E-4 + 131.4182 / VCA[i]**2 + 2.76249E8 / VCA[i]**4)   #Esto lo estoy agregando de aquí: https://www.sdss3.org/dr8/spectro/spectra.php
	# Aquí estoy utilizando la libreria de python
	air = pyasl.vactoair2(VCA[i])
	wlair  = np.append(wlair, air)


#vac_ = open(sys.argv[1]+'vac.dat', 'a')
air_ = open(str(fits)+'.fitsair.txt', 'a')

for j in np.arange(len(wlvac)):

#	vac_.write(str(wlvac[j])+'\t'+str(images2[1].data[j])+'\t'+str(float(1.0))+'\n') # Vacuum 
	air_.write(str(wlair[j])+'\t'+str(images2[1].data[j][1])+'\t'+str(float(1.0))+'\n') # Air 

#vac_.close()
air_.close()