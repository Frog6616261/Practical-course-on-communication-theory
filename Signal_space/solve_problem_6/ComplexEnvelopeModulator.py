import numpy as np
from scipy.integrate import quad

PI = np.pi
BAND_DOWN = -1e4
BAND_UP = 1e4


class ComplexEnvelopeModulator:

    def __init__(self, pass_freq, band_down=None, band_up=None):

        self._pass_freq     = pass_freq
        self._band_down     = band_down if (band_down is not None) else BAND_DOWN
        self._band_end      = band_up if (band_up is not None) else BAND_UP

    
    def get_bandpass_signal(self, x_l):
        f_0 = self._pass_freq

        def x(t):
            x_i_t = np.real(x_l(t))
            x_q_t = np.imag(x_l(t))

            return (x_i_t * np.cos(2*PI*f_0*t) + x_q_t * ((-1) * np.sin(2*PI*f_0*t)))

        return x
    

    def get_analitic_signal(self, x_l):
        f_0 = self._pass_freq

        def x_a(t):
            x_i_t = np.real(x_l(t))
            x_q_t = np.imag(x_l(t))

            s_t = np.sin(2*PI*f_0*t)
            c_t = np.cos(2*PI*f_0*t)

            return (0.5)*(x_i_t*c_t - x_q_t*s_t) + (0.5j)*(x_q_t*c_t + x_i_t*s_t) 

        return x_a
    

    def get_baseband_signal(self, x, start=None, end=None):
        f_0            = self._pass_freq
        band_down      = start if (start is not None) else self._band_down
        band_up        = end if (end is not None) else self._band_end

        f_2 = lambda t: 1/(PI * t)
        
        def x_l(t):
            freq = np.fft.fftfreq(np.size(t), )
            H_t = np.fft.ifft((-1j) * np.sign(freq) * np.fft.fft(x(t)))

            s_t = np.sin(2*PI*f_0*t)
            c_t = np.cos(2*PI*f_0*t)

            return (x(t)*c_t + H_t*s_t) + (1j) * (x(t)*(-1)*s_t + H_t*c_t)

        return x_l    


    def get_signalS_envelope_amp(self, x_l):
        def envelope_amp(t):
            x_i_t = np.real(x_l(t))
            x_q_t = np.imag(x_l(t))

            return np.abs(x_i_t*x_i_t  + x_q_t*x_q_t)

        return envelope_amp
    

    def get_signalS_envelope_phase(self, x_l):
        def envelope_phase(t):
            x_i_t = np.real(x_l(t))
            x_q_t = np.imag(x_l(t))

            return np.arctan(x_q_t/x_i_t)

        return envelope_phase
    
    
