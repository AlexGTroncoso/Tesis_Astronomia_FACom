import matplotlib.pyplot as plt
import astropy.units as u
import thejoker as tj
import numpy as np

from thejoker import JokerPrior, TheJoker, RVData
from thejoker.plot import plot_rv_curves

# Definiendo las variables
t = [59616.23644604064, 59650.10541174411, 59656.05310538688, 59657.12322433722, 59658.06083902933, 59661.1028844865, 59664.12167293875, 59666.11853265618]
rv = [315.6384, 315.5357, 315.5778, 315.5968, 315.5781, 315.5318, 315.5052, 315.5417] * u.km/u.s
err = [0.013, 0.0098, 0.0114, 0.0136, 0.0091, 0.012, 0.0102, 0.0118] * u.km/u.s
data = tj.RVData(t=t, rv=rv, rv_err=err)

## Definiendo los priors
data = RVData(t=t, rv=rv, rv_err=err)
prior = JokerPrior.default(P_min=2*u.day, P_max=100*u.day,sigma_K0= ((max(rv)-min(rv))/2), sigma_v = np.mean(rv))
joker = TheJoker(prior)
print("Listo la definición de prior")

## Generando los priors sample
rng = np.random.default_rng(seed=42) # pequeño retraso en el tiempo 
prior_samples1 = prior.sample(size=6_000_000, rng=rng) # Este es el número de priors que se generan
print("Listo los priors samples")

samples1 = joker.rejection_sample(data, prior_samples1, max_posterior_samples=256)
samples1 = samples1.wrap_K()
print(samples1)
samples1.write("TJ_samples_srich.hdf5", overwrite=False)  #Es la forma de guardar los posterior en un archivo para poder llamarlos luego
print("Listo los posteriors samples")

