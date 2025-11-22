import numpy as np
from scipy.signal import hilbert

PI = np.pi


class ComplexEnvelopeModulator:

    def __init__(self, pass_freq):

        self._pass_freq     = pass_freq

    
    def get_bandpass_signal(self, x_l):
        f_0 = self._pass_freq

        def x(t):
            x_l_t = x_l(t)
            x_i_t = np.real(x_l_t)
            x_q_t = np.imag(x_l_t)

            return (x_i_t * np.cos(2*PI*f_0*t) + x_q_t * ((-1) * np.sin(2*PI*f_0*t)))

        return x
    

    def get_analitic_signal(self, x_l):
        f_0 = self._pass_freq

        def x_a(t):
            x_l_t = x_l(t)
            x_i_t = np.real(x_l_t)
            x_q_t = np.imag(x_l_t)

            s_t = np.sin(2*PI*f_0*t)
            c_t = np.cos(2*PI*f_0*t)

            return (0.5)*(x_i_t*c_t - x_q_t*s_t) + (0.5j)*(x_q_t*c_t + x_i_t*s_t) 

        return x_a
    

    def get_baseband_signal(self, x):
        f_0 = self._pass_freq

        def x_l(t):
            x_t = x(t)
            H_t = np.imag(hilbert(x_t))*0.5

            s_t = np.sin(2*PI*f_0*t)
            c_t = np.cos(2*PI*f_0*t)

            return (x_t*c_t + H_t*s_t) + (1j) * (x_t*(-1)*s_t + H_t*c_t)

        return x_l    


    def get_signalS_envelope_amp(self, x_l):
        def envelope_amp(t):
            x_l_t = x_l(t)
            x_i_t = np.real(x_l_t)
            x_q_t = np.imag(x_l_t)

            return np.sqrt(x_i_t*x_i_t  + x_q_t*x_q_t)

        return envelope_amp
    

    def get_signalS_envelope_phase(self, x_l):
        def envelope_phase(t):
            x_l_t = x_l(t)
            x_i_t = np.real(x_l_t)
            x_q_t = np.imag(x_l_t)

            return np.arctan(x_q_t/x_i_t)

        return envelope_phase
    
    
