from astropy.io import fits as pyfits
import numpy as np
import scipy as sc
import sys



fits=sys.argv[1]
 
images2=pyfits.open(str(fits)+'.fits')

wlvac = np.array([])
wlair = np.array([])

for i in np.arange(8575):

	vac    = 10.**(4.179 + 6.E-6*i)
	wlvac  = np.append(wlvac, vac)
	
	air    = vac/(1 + (6.4328E-5 + 2.94981E-2/(146.0-(1.0E4/vac)**2)+2.5540E-4/(41.0-(1.0E4/vac)**2)))
	wlair  = np.append(wlair, air)


#vac_ = open(sys.argv[1]+'vac.dat', 'a')
air_ = open(str(fits)+'.fitsair.dat', 'a')

for j in np.arange(len(wlvac)):

#	vac_.write(str(wlvac[j])+'\t'+str(images2[1].data[j])+'\t'+str(float(1.0))+'\n') # Vacuum 
	air_.write(str(wlair[j])+'\t'+str(images2[1].data[j])+'\t'+str(float(1.0))+'\n') # Air 

#vac_.close()
air_.close()

