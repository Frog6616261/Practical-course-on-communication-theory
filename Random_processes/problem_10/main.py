import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fftshift, fft
from RandomProcessGenerator import RandomProcessGenerator


# 1. Задание теоретической автокорреляционной функции
b_xi = [10, 1, 5, 1, 3, 1, 1, 1]

# 2. Инициализация генератора
gen = RandomProcessGenerator(b_xi)

# 3. Генерация выборки ξ(t)
xi = gen.generate(N=2048)

# 4. Оценка автокорреляционной функции
lags, r_est = gen.acf(xi)

# 5. Теоретический спектр (по заданной АКФ)
Nfft = gen.Nfft
S_theor = np.real(fft(gen.b_xi, n=Nfft))
freqs_theor = np.fft.fftfreq(Nfft, d=1)
S_theor = fftshift(S_theor)
freqs_theor = fftshift(freqs_theor)

# 6. Оценённый спектр из выборки
freqs_est, S_est = gen.spectrum(xi, Nfft=Nfft)

# =======================
# === 7. Визуализация ===
# =======================

plt.figure(figsize=(12, 8))

# --- АКФ ---
plt.subplot(2, 1, 1)
plt.plot(lags, r_est, label="Оценённая АКФ", color='C0')
plt.stem(np.arange(len(b_xi)), np.array(b_xi)/np.max(b_xi), linefmt='C1-', markerfmt='C1o', basefmt=" ", label="Теоретическая АКФ")
plt.title("Автокорреляционная функция ξ(t)")
plt.xlabel("Лаг τ")
plt.ylabel("Rξ(τ), норм.")
plt.legend()
plt.grid(True)

# --- Спектр ---
plt.subplot(2, 1, 2)
plt.plot(freqs_est, S_est / np.max(S_est), label="Оценённый спектр", color='C0')
plt.plot(freqs_theor, S_theor / np.max(S_theor), label="Теоретический спектр", color='C1', linestyle='--')
plt.title("Спектральная плотность мощности ξ(t)")
plt.xlabel("Частота f")
plt.ylabel("Sξ(f), норм.")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
