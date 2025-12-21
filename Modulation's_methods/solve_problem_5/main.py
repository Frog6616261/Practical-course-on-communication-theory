import numpy as np
import matplotlib.pyplot as plt
import random

from scipy.fft import fft, ifft, fftfreq, fftshift

from QAM_mapper import QAM_mapper
from MSK_mapper import MSK_mapper
from plotting_funcs import plot_constellation

PI = np.pi



## Model parameters

T_signal = 0.01
dt = 1e-5
df = 1/dt
t = np.linspace(0, T_signal, int(T_signal*df), endpoint=False)


bit_rate = 10e3

numb_bits = 1024
bit_sequence = [random.randint(0, 1) for _ in range(numb_bits)]


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[4:7])

qam16 = QAM_mapper(16, bit_rate)
msk = MSK_mapper(bit_rate, 1, 0.5)

#baseband_msk_signal = msk.get_baseband_signal(bit_sequence)
baseband_qam16_signal = qam16.get_baseband_signal(bit_sequence)

qam16_s = baseband_qam16_signal(t)
#msk_s = baseband_msk_signal(t)

# Визуализация
plt.figure(figsize=(12, 4))
plt.plot(t, np.angle(qam16_s))
plt.title("qam16 модулированный сигнал")
plt.xlabel("Отсчёты")
plt.ylabel("Амплитуда")
plt.grid(True)
plt.show()



# ## Spectrum's func of inform signal
# def X_l(f):
#     def X_l_uniq(f):
#         if ((f < -INFO_SPEC_BANWIND/2) or (INFO_SPEC_BANWIND/2 < f)):
#             return 0

#         return AMP_INFO_SPEC * (f + INFO_SPEC_BANWIND/2) / INFO_SPEC_BANWIND
    
#     result = np.zeros(np.size(f))

#     for i in range(0, np.size(f)):
#         result[i] = X_l_uniq(f[i])

#     return result


# ## Time-dimention teoretical functions
# A = AMP_INFO_SPEC
# w = INFO_SPEC_BANWIND / 2
# f_0 = pass_freq

# def x_l_teor(t):

#     return A / (8*(PI**3)*w*(t*t)) * ((2*PI*w*t + 1j)*np.sin(2*PI*w*t) - (2*PI*1j*w*t)*np.cos(2*PI*w*t))

# def x_teor(t):

#     return np.real(x_l_teor(t) * np.exp(2*PI*1j*f_0*t))

# def x_a_teor(t):

#     return 0.5*x_teor(t) + (0.5j)*np.imag(x_l_teor(t)*np.exp(2*PI*1j*f_0*t))

# def envelope_amp_teor(t):

#     return np.abs(x_l_teor(t))

# def envelope_phase_teor(t):

#     return np.angle(x_l_teor(t))


# ## Create modulator object
# cem = ComplexEnvelopeModulator(pass_freq)


# ## Find time-dimention function
# x_l = cem.get_baseband_signal(x_teor)
# x = cem.get_bandpass_signal(x_l_teor)
# x_a = cem.get_analitic_signal(x_l_teor)
# envelope_amp = cem.get_signalS_envelope_amp(x_l_teor)
# envelope_phase = cem.get_signalS_envelope_phase(x_l_teor)


# ## Calculate error
# t = np.arange(t_start, t_end, dt)

# err_x_l = np.abs(x_l(t) - x_l_teor(t))
# err_x = np.abs(x(t) - x_teor(t))
# err_x_a = np.abs(x_a(t) - x_a_teor(t))
# err_envelope_amp = np.abs(envelope_amp(t) - envelope_amp_teor(t))
# err_envelope_phase = np.abs(envelope_phase(t) - envelope_phase_teor(t))


# ## Find spectrum
# N = np.size(t)
# T = dt
# freq = fftfreq(N,T)
# spec_analitic = X_l(freq)

# X_l_teor = np.abs(fft(x_l_teor(t))) * (1.0/N)
# X_teor = np.abs(fft(x_teor(t))) * (1.0/N)
# X_a_teor = np.abs(fft(x_a_teor(t))) * (1.0/N)

# X_l_prac = np.abs(fft(x_l(t))) * (1.0/N)
# X_prac = np.abs(fft(x(t))) * (1.0/N)
# X_a_prac = np.abs(fft(x_a(t))) * (1.0/N)



# ## PLotting errors
# plt.figure(figsize=(10, 6))

# plt.semilogy(t, err_x_l,            '.', label='err x_l')
# plt.semilogy(t, err_x,              '.', label='err x')
# plt.semilogy(t, err_x_a,            '.', label='err x_a')
# plt.semilogy(t, err_envelope_amp,   '.', label='err envelope amplitude')
# plt.semilogy(t, err_envelope_phase, '.', label='err envelope phase')

# plt.xlabel('t')
# plt.ylabel('Error')
# plt.title('Error curves of all functions')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()


# # Plotting specturms
# fig1, axs = plt.subplots(2, 1, figsize=(10, 8))

# axs[0].plot(freq, X_l_teor,            '.', label='X_l teor')
# axs[0].plot(freq, X_teor,              '.', label='X teor')
# axs[0].plot(freq, X_a_teor,            '.', label='X_a teor')
# axs[0].plot(freq, spec_analitic,            '.', label='X_l analitic')
# axs[0].set_title('Spectrum curves of teoretical functions')
# axs[0].set_xlabel('freq Hz')
# axs[0].set_ylabel('Amp')
# axs[0].legend()
# axs[0].grid(True)

# axs[1].plot(freq, X_l_prac,            '.', label='X_l prac')
# axs[1].plot(freq, X_prac,              '.', label='X prac')
# axs[1].plot(freq, X_a_prac,            '.', label='X_a prac')
# axs[1].plot(freq, spec_analitic,            '.', label='X_l analitic')
# axs[1].set_title('Spectrum curves of practical functions')
# axs[1].set_xlabel('freq Hz')
# axs[1].set_ylabel('Amp')
# axs[1].legend()
# axs[1].grid(True)

# plt.tight_layout()
# plt.show()

# # Plotting time-dimention evnvelope with basepass signal
# fig2, axs2 = plt.subplots(3, 2, figsize=(10, 12))

# axs2[0][0].plot(t, x_teor(t),            '.-', label='x teor')
# axs2[0][0].plot(t, envelope_amp_teor(t),              '.-', label='envelope amp teor')
# axs2[0][0].set_title('Signal curves of teoretical functions with envelope')
# axs2[0][0].set_xlabel('time sec')
# axs2[0][0].set_ylabel('Amp')
# axs2[0][0].legend()
# axs2[0][0].grid(True)

# axs2[0][1].plot(t, envelope_phase_teor(t),              '.', label='envelope phase teor')
# axs2[0][1].set_title('Phase curve of teoretical envelope')
# axs2[0][1].set_xlabel('time sec')
# axs2[0][1].set_ylabel('radian')
# axs2[0][1].legend()
# axs2[0][1].grid(True)


# axs2[1][0].plot(t, x(t),            '.-', label='x prac')
# axs2[1][0].plot(t, envelope_amp(t),              '.-', label='envelope amp prac')
# axs2[1][0].set_title('Signal curves of practical functions with envelope')
# axs2[1][0].set_xlabel('time sec')
# axs2[1][0].set_ylabel('Amp')
# axs2[1][0].legend()
# axs2[1][0].grid(True)

# axs2[1][1].plot(t, envelope_phase(t),            '.', label='envelope phase teor')
# axs2[1][1].set_title('Phase curve of practical envelope')
# axs2[1][1].set_xlabel('time sec')
# axs2[1][1].set_ylabel('radian')
# axs2[1][1].legend()
# axs2[1][1].grid(True)


# axs2[2][0].plot(t, x_teor(t),            '.-', label='x teor')
# axs2[2][0].plot(t, envelope_amp(t),              '.-', label='envelope amp prac')
# axs2[2][0].set_title('Perform teoretical signal with practical envelope')
# axs2[2][0].set_xlabel('time sec')
# axs2[2][0].set_ylabel('Amp')
# axs2[2][0].legend()
# axs2[2][0].grid(True)

# axs2[2][1].plot(t, envelope_phase(t),            '.', label='envelope phase prac')
# axs2[2][1].plot(t, envelope_phase_teor(t),            '.', label='envelope phase teor')
# axs2[2][1].set_title('Perform phase of envelopes')
# axs2[2][1].set_xlabel('time sec')
# axs2[2][1].set_ylabel('radian')
# axs2[2][1].legend()
# axs2[2][1].grid(True)

# plt.tight_layout()
# plt.show()

