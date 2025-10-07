import matplotlib.pyplot as plt
import numpy as np
from AnalyzerDFT import AnalyzerDFT

pi = np.pi

import numpy as np

## Model Parametrs      ------------------------------------------------------------------------------------------------------------------------

t_start     = 0
t_end       = 3
a           = 1
b           = 3
freq_disc   = 300


## funcs                ------------------------------------------------------------------------------------------------------------------------
def get_s(x, a, b):

    x = np.asarray(x)  # rebuild for array
    y = np.zeros_like(x, dtype=float)  # all is 0
    mask = (x >= a) & (x <= b)         # mask for interval
    y[mask] = 1

    return y

def get_analytic_dft_spec(Fd, a, b, t_start, t_end):
    N = np.floor((t_end - t_start)*Fd) + 1
    is_same = np.abs(t_start + np.floor((a - t_start)*Fd)*(1/Fd) - a) < 1e-15 
    p_start = np.int64(np.floor((a - t_start)*Fd) + int(not(is_same)))
    p_end = np.int64(np.floor((b- t_start)*Fd)) 
    l0 = p_start - p_end + 1

    k = np.arange(N)
    spec = np.exp(-1j*np.pi*k/N * (2*p_start + l0 - 1)) * (np.sin(np.pi*k*l0 / N) / np.sin(np.pi*k/N))

    return spec



def func_s(x):

    return get_s(x, a, b)


def get_s_spec_analytic(w, a, b):

    w = np.asarray(w, dtype=float)

    return ((b-a)*np.exp(-1j*w/2*(b+a))*np.sinc(w/2*(b-a)))


def get_fft_numpy_spec(fs, t_start, t_end, a, b):

    L = np.floor((t_end - t_start)*fs) + 1
    dt = 1/fs 
    t = np.arange(L) * dt 
    N = len(t)
    
    s = get_s(t, a, b)
    
    spec_all = np.fft.fft(s, n = N)
    freqs_all = np.fft.fftfreq(N, d = dt)

    return freqs_all, spec_all



## Solve values         ------------------------------------------------------------------------------------------------------------------------
dt = np.double(1/freq_disc)
N = np.floor((t_end - t_start) * freq_disc) + 1
time_arr = np.arange(N) * dt + t_start 

dw =  freq_disc / N
w_arr = np.arange(N) * dw    

# analytic spector
s_val = get_s(time_arr, a, b)
s_spec_analytic = (get_s_spec_analytic(w_arr, a, b))

# analytic dft
s_spec_analytic_dft = get_analytic_dft_spec(freq_disc, a, b, t_start, t_end)

# np
w_arr_fft_np, s_spec_fft_np = get_fft_numpy_spec(freq_disc, t_start, t_end, a, b)
s_spec_fft_np = (s_spec_fft_np)

# my
dft_analyst = AnalyzerDFT(freq_disc, func_s, t_start, t_end)
s_spec_my_dft = (dft_analyst._amp_spec).copy()
w_arr_my_dft = (dft_analyst._w_arr).copy()

# Translate to dB: 20*log10(|y|)
yA_db = 20 * np.log10(np.abs(s_spec_analytic))
yAdft_db = 20 * np.log10(np.abs(s_spec_analytic_dft))
yN_db = 20 * np.log10(np.abs(s_spec_fft_np))
yM_db = 20 * np.log10(np.abs(s_spec_my_dft))


## Plotting     ------------------------------------------------------------------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(w_arr[:int(N/2)], yA_db[:int(N/2)], 'o', label='Analytic')
plt.plot(w_arr[:int(N/2)], yAdft_db[:int(N/2)], 'o', label='Analytic dft')
plt.plot(w_arr_fft_np[:int(N/2)], yN_db[:int(N/2)], 'o', label='numpy')
plt.plot(w_arr[:int(N/2)], yM_db[:int(N/2)], 'o', label='my dft')


plt.xlabel('freq Hz')
plt.ylabel('Amp, dB')
plt.title('Analysis DFT')
plt.legend()
plt.grid(True)
plt.show()

