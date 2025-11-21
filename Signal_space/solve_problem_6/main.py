import numpy as np
import matplotlib.pyplot as plt

from ComplexEnvelopeModulator import ComplexEnvelopeModulator

PI = np.pi


## Model parameters

pass_freq = 1e9

AMP_INFO_SPEC = 5
INFO_SPEC_BANWIND = 1e2

Fs = 1e3
dt = 1/Fs
t_start = 1e-4
t_end = 2


## Spectrum's func of inform signal
def X_l(f):
    if (f < -INFO_SPEC_BANWIND/2 or INFO_SPEC_BANWIND/2 < f): return 0

    return AMP_INFO_SPEC * (f + INFO_SPEC_BANWIND/2) / INFO_SPEC_BANWIND


## Time-dimention teoretical functions
A = AMP_INFO_SPEC
w = INFO_SPEC_BANWIND / 2
f_0 = pass_freq

def x_l_teor(t):

    return A / (2*w) * ((w/t)*np.sin(2*PI*w*t) + (2j/(t*t))*np.sin(2*PI*w*t) + (2*w/(1j*t))*np.cos(2*PI*w*t))

def x_teor(t):

    return np.real(x_l_teor(t) * np.exp(2*PI*1j*f_0*t))

def x_a_teor(t):

    return 0.5*x_teor(t) + (0.5j)*x_l_teor(t)

def envelope_amp_teor(t):

    return np.abs(x_l_teor(t))

def envelope_phase_teor(t):

    return np.angle(x_l_teor(t))


## Create modulator object
info_band_down = -INFO_SPEC_BANWIND/2 - 10
info_band_up = INFO_SPEC_BANWIND/2 + 10

cem = ComplexEnvelopeModulator(pass_freq, info_band_down, info_band_up)


## Find time-dimention function
x_l = cem.get_baseband_signal(x_teor)
x = cem.get_bandpass_signal(x_l_teor)
x_a = cem.get_analitic_signal(x_l_teor)
envelope_amp = cem.get_signalS_envelope_amp(x_l_teor)
envelope_phase = cem.get_signalS_envelope_phase(x_l_teor)


## Calculate error
t = np.arange(t_start, t_end, dt)

err_x_l = np.abs(x_l(t) - x_l_teor(t))
err_x = np.abs(x(t) - x_teor(t))
err_x_a = np.abs(x_a(t) - x_a_teor(t))
err_envelope_amp = np.abs(envelope_amp(t) - envelope_amp_teor(t))
err_envelope_phase = np.abs(envelope_phase(t) - envelope_phase_teor(t))


## Find spectrum

## PLotting errors
plt.figure(figsize=(10, 6))

plt.semilogy(t, err_x_l,            '.', label='err x_l')
plt.semilogy(t, err_x,              '.', label='err x')
plt.semilogy(t, err_x_a,            '.', label='err x_a')
plt.semilogy(t, err_envelope_amp,   '.', label='err envelope amplitude')
plt.semilogy(t, err_envelope_phase, '.', label='err envelope phase')

plt.xlabel('t')
plt.ylabel('Error')
plt.title('Error curves of all functions')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# plt.figure()

# plt.plot(x, ksi_prob_density_analytic, 'o', label='Analytic func Ksi')
# plt.hist(ksi_samples_scipy,  density=True, bins='auto', alpha=0.6, label='scipy Ksi')
# plt.hist(ksi_samples_my, density=True, bins='auto', alpha=0.6, label='my Ksi')

# plt.xlabel('Random variable')
# plt.ylabel('Probability')
# plt.title("Probability density, lambda = " + str(lambd))
# plt.legend()
# plt.grid(True)
# plt.show()

