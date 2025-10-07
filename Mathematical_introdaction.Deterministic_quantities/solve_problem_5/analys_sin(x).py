import matplotlib.pyplot as plt
import numpy as np
from AnalyzerDFT import AnalyzerDFT

pi = np.pi

import numpy as np

## Model Parametrs      ------------------------------------------------------------------------------------------------------------------------

t_start     = 0
t_end       = 20
l           = 3
freq_disc   = 100


## funcs                ------------------------------------------------------------------------------------------------------------------------
def get_s(x, l):

    x = np.asarray(x)  # convert number to array
    y = np.zeros_like(x, dtype=float)  # all is 0
    mask = (x >= 0) & (x <= l)         # mask for interval
    y[mask] = np.sin(np.pi * x[mask] / l)
    return y


def func_s(x):

    return get_s(x, l)


def get_s_spec_analytic(w, l):

    w = np.asarray(w, dtype=float) 
    w2 = np.square((w.copy()))

    return (pi*l*(1j * np.sin(l*w) - np.cos(l*w) - 1)/(l*l*w2 - pi*pi))


def get_fft_numpy_spec(fs, t_start, t_end, l):

    L = np.floor((t_end - t_start)*fs) + 1
    dt = 1/fs 
    t = np.arange(L) * dt 
    N = len(t)
    
    s = get_s(t, l)
    
    spec_all = np.fft.fft(s, n = N)
    freqs_all = np.fft.fftfreq(N, d = dt)

    return freqs_all, spec_all



## Solve values         ------------------------------------------------------------------------------------------------------------------------
dt = np.double(1/freq_disc)
N = np.floor((t_end - t_start) * freq_disc) + 1
time_arr = np.arange(N) * dt + t_start 

dw =  freq_disc / N
w_arr = np.arange(N) * dw    

# analytic
s_val = get_s(time_arr, l)
s_amp_spec_analytic = np.abs(get_s_spec_analytic(w_arr, l))

# np
w_arr_fft_np, s_spec_fft_np = get_fft_numpy_spec(freq_disc, t_start, t_end, l)
s_amp_spec_fft_np = np.abs(s_spec_fft_np)

# my
dft_analyst = AnalyzerDFT(freq_disc, func_s, t_start, t_end)
s_amp_spec_my_dft = (dft_analyst._amp_spec).copy()
w_arr_my_dft = (dft_analyst._w_arr).copy()

# Translate to dB: 20*log10(|y|)
yA_db = 20 * np.log10(np.abs(s_amp_spec_analytic))
yN_db = 20 * np.log10(np.abs(s_amp_spec_fft_np))
yM_db = 20 * np.log10(np.abs(s_amp_spec_my_dft))


## Plotting      ------------------------------------------------------------------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(w_arr, yA_db, 'o', label='Analytic')
plt.plot(w_arr_fft_np, yN_db, 'o', label='numpy')
plt.plot(w_arr_my_dft, yM_db, 'o', label='my dft')


plt.xlabel('freq Hz')
plt.ylabel('Amp, dB')
plt.title('Analysis DFT')
plt.legend()
plt.grid(True)
plt.show()

