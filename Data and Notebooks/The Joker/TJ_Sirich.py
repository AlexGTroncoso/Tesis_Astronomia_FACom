import matplotlib.pyplot as plt
import thejoker.units as xu
import astropy.units as u
import statistics as stat
import thejoker as tj
import pandas as pd
import numpy as np
import arviz as az
import pymc as pm
import math 
import h5py
import os


from astropy.visualization.units import quantity_support
from thejoker import JokerPrior, TheJoker, RVData
from thejoker.plot import plot_rv_curves
from os.path import join

# Lee el archivo de texto y crea un DataFrame
nombres_columnas = ['Estrella', 'TYC', '2MASS']
data = pd.read_csv('Nombres_de_Estrellas.txt', delimiter=' ', names=nombres_columnas, header=None)  # Si el archivo está tabulado, usa '\t' como 

columns = ["Star","Date","RV","err_RV","S/N"]
Estrella = {}
mean = []
range = []
std = []
for i in data["Estrella"]:
    Estrella[i] = pd.read_csv(i+'.dat', delimiter='\t', names=columns, header=None)
    #print(Estrella[i])
    mean.append(np.mean(Estrella[i]["RV"]))
    range.append(np.max(Estrella[i]["RV"])-np.min(Estrella[i]["RV"]))
    std.append(np.std(Estrella[i]["RV"]))

# Obtén la ruta absoluta
file_path = os.path.abspath('news_RV/Sirich_2M22045404-1148287.csv')

# Luego intenta leer el archivo
df = pd.read_csv(file_path)
df_ordenado = df.sort_values(by='JD')
df_ordenado = df_ordenado[df_ordenado['STARFLAG']==0].reset_index(drop=True)

t = np.concatenate((np.array(df_ordenado["JD"]),np.array(Estrella["Si_rich"]["Date"])))-2400000.5
rv = np.concatenate((np.array(df_ordenado["VHELIO"]),np.array(Estrella["Si_rich"]["RV"]))) * u.km/u.s
err = np.concatenate((np.array(df_ordenado["VRELERR"]),np.array(Estrella["Si_rich"]["err_RV"]))) * u.km/u.s
data = tj.RVData(t=t, rv=rv, rv_err=err)
print("Definido data")

data = RVData(t=t, rv=rv, rv_err=err)
#prior = JokerPrior.default(P_min=2*u.day, P_max=1e3*u.day,sigma_K0= 30*u.km/u.s,sigma_v=100*u.km/u.s)
prior = JokerPrior.default(P_min=350*u.day, P_max=450*u.day,sigma_K0= 30*u.km/u.s,sigma_v=100*u.km/u.s)
joker = TheJoker(prior)
print("Listo la definición de prior")

## Generando los priors sample
rng = np.random.default_rng(seed=42) # pequeño retraso en el tiempo 
prior_samples = prior.sample(size=10_000_000, rng=rng) # Este es el número de priors que se generan
print("Listo los priors samples")

samples = joker.rejection_sample(data, prior_samples, max_posterior_samples=256)
samples = samples.wrap_K()
print(samples)
samples.write("TJ_samples_Sirich.hdf5", overwrite=True)  #Es la forma de guardar los posterior en un archivo para poder llamarlos luego
print("Listo los posteriors samples")

