#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install thejoker


# In[ ]:


import math
import numpy as np


import thejoker as tj
import astropy.units as u
import matplotlib.pyplot as plt


from astropy.visualization.units import quantity_support
from thejoker import JokerPrior, TheJoker, RVData
from sklearn.metrics import mean_squared_error
from thejoker.plot import plot_rv_curves
from tqdm import tqdm


# In[ ]:




# In[ ]:


t = [59616.23644604064, 59650.10541174411, 59656.05310538688, 59657.12322433722, 59658.06083902933, 59661.1028844865, 59664.12167293875, 59666.11853265618]
rv = [315.6384, 315.5357, 315.5778, 315.5968, 315.5781, 315.5318, 315.5052, 315.5417] * u.km/u.s
err = [0.013, 0.0098, 0.0114, 0.0136, 0.0091, 0.012, 0.0102, 0.0118] * u.km/u.s
data = tj.RVData(t=t, rv=rv, rv_err=err)



# In[ ]:


data = RVData(t=t, rv=rv, rv_err=err)
prior = JokerPrior.default(P_min = 2*u.day, P_max = 200*u.day,sigma_K0 = ((max(rv)-min(rv))/2), sigma_v=np.mean(rv))
joker = TheJoker(prior)

rng = np.random.default_rng(seed=42)
prior_samples = prior.sample(size=100000, rng=rng)

samples = joker.rejection_sample(data, prior_samples)
samples = samples.wrap_K()
samples.write("samples.hdf5", overwrite=True)

print(samples)
print("Listo")




