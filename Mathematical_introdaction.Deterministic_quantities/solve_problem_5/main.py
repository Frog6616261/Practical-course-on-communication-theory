import matplotlib.pyplot as plt
import numpy as np
from AnalyzerDFT import AnalyzerDFT

pi = np.pi

import numpy as np

## Model Parametrs      ------------------------------------------------------------------------------------------------------------------------

t_start     = 0
t_end       = 100
l           = 10
freq_disc   = 2


## funcs                ------------------------------------------------------------------------------------------------------------------------
def get_s(x, l):

    x = np.asarray(x)  # приводим к массиву, если подали число
    y = np.zeros_like(x, dtype=float)  # по умолчанию всё 0
    mask = (x >= 0) & (x <= l)         # маска для интервала
    y[mask] = np.sin(np.pi * x[mask] / l)
    return y

def func_s(x):

    return get_s(x, l)


def get_s_spec_analytic(w, l):

    w = np.asarray(w, dtype=float)  # поддержка массивов

    term1 = (1 - np.exp(-1j * (w - np.pi/l) * l)) / (1j * (w - np.pi/l))
    term2 = (1 - np.exp(-1j * (w + np.pi/l) * l)) / (1j * (w + np.pi/l))

    return 0.5 * (term1 - term2)


def get_fft_numpy_spec(fs, t_start, t_end, l):
    """
    Численное ДПФ функции s(x) через numpy.fft
    
    Аргументы:
        fs      : float — частота дискретизации (Гц)
        t_start : float — начало временного промежутка
        t_end   : float — конец временного промежутка
        l       : float — параметр импульса
    Возвращает:
        freqs   : np.ndarray — массив частот (Гц)
        spectrum: np.ndarray — значения спектра (комплексные)
    """

    t = np.arange(t_start, t_end, 1/fs)
    N = len(t)
    
    s = get_s(t, l)
    
    spectrum = np.fft.fft(s, n=N)    
    freqs = np.fft.fftfreq(N, d=1/fs)    

    return freqs, spectrum


## Solve values         ------------------------------------------------------------------------------------------------------------------------
dt = np.double(1/freq_disc)
N = np.floor((t_end - t_start) * freq_disc) + 1
time_arr = np.arange(N) * dt + t_start 

dw =  freq_disc / N
w_arr = np.arange(N) * dw    

# Analytic
s_val = get_s(time_arr, l)
s_amp_spec_analytic = np.abs(get_s_spec_analytic(w_arr, l))

# np
w_arr_fft_np, s_spec_fft_np = get_fft_numpy_spec(freq_disc, t_start, t_end, l)
s_amp_spec_fft_np = np.abs(s_spec_fft_np)

# my
dft_analyst = AnalyzerDFT(freq_disc, func_s, t_start, t_end)
s_amp_spec_my_dft = (dft_analyst._amp_spec).copy()
w_arr_my_dft = (dft_analyst._w_arr).copy()

# Переводим в dB: 20*log10(|y|)
yA_db = 20 * np.log10(np.abs(s_amp_spec_analytic))
yN_db = 20 * np.log10(np.abs(s_amp_spec_fft_np))
yM_db = 20 * np.log10(np.abs(s_amp_spec_my_dft))

# if no, babah
if (not(len(w_arr) == len(w_arr_fft_np) == len(w_arr_my_dft))): print("not same w arr")

## Plotting angry a     ------------------------------------------------------------------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(w_arr, yA_db, ':', label='Analytic')
plt.plot(w_arr_fft_np, yN_db, ':', label='numpy')
plt.plot(w_arr_my_dft, yM_db, ':', label='my dft')


plt.xlabel('x')
plt.ylabel('Amp, dB')
plt.title('Crazy hamburger dB')
plt.legend()
plt.grid(True)
plt.show()