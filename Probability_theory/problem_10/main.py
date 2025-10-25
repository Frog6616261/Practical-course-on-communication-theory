import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import logistic

from KsiGenerator import KsiGenerator


## Model parameters

lambd = 23.45

a = None
c = None
m = None
seed = None

numb_random_variable = 1000
numb_points_for_analitic = 1000


## scipy realisation
ksi_samples_scipy = logistic.rvs(size=numb_random_variable, loc=0, scale=(1/lambd))


## My Generation

ksi_gen = KsiGenerator(lambd, seed, a, c, m)
ksi_samples_my = ksi_gen.generate_samples(numb_random_variable)


## Analytic function

def get_ksi_prob_density(x):
    return lambd*np.exp(-lambd*x)/(np.power((1+np.exp(-lambd*x)), 2)) 

x = np.linspace(np.min(ksi_samples_scipy), np.max(ksi_samples_scipy), numb_points_for_analitic)
ksi_prob_density_analytic = get_ksi_prob_density(x)


## PLotting

plt.figure()

plt.plot(x, ksi_prob_density_analytic, 'o', label='Analytic func Ksi')
plt.hist(ksi_samples_scipy,  density=True, bins='auto', alpha=0.6, label='scipy Ksi')
plt.hist(ksi_samples_my, density=True, bins='auto', alpha=0.6, label='my Ksi')

plt.xlabel('Random variable')
plt.ylabel('Probability')
plt.title("Probability density, lambda = " + str(lambd))
plt.legend()
plt.grid(True)
plt.show()

