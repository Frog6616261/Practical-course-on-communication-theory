import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

# === Определение треугольной функции ===
def triangle(x, w):
    f = np.zeros_like(x)
    mask = np.abs(x) < w/2
    f[mask] = 1 - (2/w) * np.abs(x[mask])
    return f

def get_spec_analytical(N, Fs, w):
    k = np.arange(N)

    a = np.floor(w*Fs)
    b = np.floor((a + 1) / 2)

    spec = 2*np.exp(-1j*(pi*k)/(2*N)*(b + a + 3))*np.sin((2*pi)/(2*N)*(b - a))/np.sin(pi*k/N) + 2/(w*Fs)*(1/np.power((1-np.exp(-1j*(2*pi*k)/N)), 2))*(1 - (a+1)*np.exp(-1j*(2*pi*k*a)/N) + a*np.exp(-1j*(2*pi*k)*(a+1)/N))

    return spec

# === Функция вычисления спектра ===
def analytical_spectrum(N, Fs, T, w):
    """
    Вычисляет спектр треугольной функции.

    Параметры:
    N  - количество отсчетов
    Fs - частота дискретизации
    T  - длина временного промежутка (T > w)
    w  - ширина треугольной функции

    Возвращает:
    freqs_shifted - массив частот
    fft_db        - амплитудный спектр в dB
    t             - массив времени
    signal        - сам сигнал (треугольник)
    """
    if T <= w:
        raise ValueError("Длина временного промежутка T должна быть больше ширины w.")

    dt = 1.0 / Fs
    # Отсчеты начинаются с x = -w/2
    t_start = -w/2
    t_end = t_start + T
    t = np.linspace(t_start, t_end, N, endpoint=False)

    # Сигнал
    signal = triangle(t, w)

    # Спектр через FFT
    fft_vals = get_spec_analytical(N, Fs, w)
    fft_freqs = np.fft.fftfreq(N, d=dt)

    fft_shifted = np.fft.fftshift(np.abs(fft_vals)) / N
    freqs_shifted = np.fft.fftshift(fft_freqs)

    eps = 1e-12
    fft_db = 20 * np.log10(fft_shifted + eps)

    return freqs_shifted, fft_db, t, signal

# === Параметры ===
w = 2.0     # ширина треугольной функции
T = 8.0     # длина временного промежутка (T > w)
Fs = 200    # частота дискретизации
N = int(T * Fs)   # количество отсчетов

# === Получение спектра ===
freqs, spec_analytic_db, t, signal = analytical_spectrum(N, Fs, T, w)

# === Теоретический спектр через sinc^2 ===
F_theoretical = w * (np.sinc(freqs * w))**2
spec_np_db = 20 * np.log10(np.abs(F_theoretical) + 1e-12)

# === Визуализация ===
plt.figure(figsize=(12,5))

# Сигнал
plt.subplot(1,2,1)
plt.plot(t, signal)
plt.title("Треугольная функция")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid(True)

# Спектр
plt.subplot(1,2,2)
plt.plot(freqs, spec_np_db, label="FFT np")
plt.plot(freqs, spec_analytic_db, label="Analytical", linestyle="--")
plt.title("Амплитудный спектр (FFT) в dB")
plt.xlabel("Частота [Hz]")
plt.ylabel("Амплитуда [dB]")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

