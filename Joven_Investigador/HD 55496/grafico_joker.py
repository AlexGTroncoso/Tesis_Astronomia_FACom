#!/usr/bin/env python
# coding: utf-8

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
t = [59616.23644604064, 59650.10541174411, 59656.05310538688, 59657.12322433722, 59658.06083902933, 59661.1028844865, 59664.12167293875, 59666.11853265618]
rv = [315.6384, 315.5357, 315.5778, 315.5968, 315.5781, 315.5318, 315.5052, 315.5417] * u.km/u.s
err = [0.013, 0.0098, 0.0114, 0.0136, 0.0091, 0.012, 0.0102, 0.0118] * u.km/u.s
data = tj.RVData(t=t, rv=rv, rv_err=err)
#ax = data.plot()  
data = RVData(t=t, rv=rv, rv_err=err)
samples = tj.JokerSamples.read("samples.hdf5")

fig, ax = plt.subplots(1, 1, figsize=(8, 5), layout="tight")
ax.scatter(samples['P'].value, samples['K'].to(u.km/u.s).value,
           marker='.', color='k', alpha=0.45)
ax.set_xlabel("$P$ [day]")
ax.set_ylabel("$K$ [km/s]")
#ax.set_xlim(0, 256)
#ax.set_ylim(0.75, 3.)

#ax.scatter(61.942, 1.3959, marker='o', color='#31a354', zorder=-100)

fig, ax = plt.subplots(1, 1, figsize=(8, 5), layout="tight")
t_grid = np.linspace(59614, 59668, 1024)
plot_rv_curves(samples, t_grid, rv_unit=u.km/u.s, data=data, ax=ax,
               plot_kwargs=dict(color='#1A70D8'),data_plot_kwargs=dict(color="tab:red"))
               
ax.set_xlim(59614, 59668)
ax.set_ylim(315.35,315.8)
plt.show()
