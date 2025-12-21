import numpy as np


PI = np.pi

def int_to_bits_lsb(value: int, length: int) -> np.ndarray:

    if value < 0:
        raise ValueError("value >= 0 must be")
    if value >= (1 << length):
        raise ValueError("value size not combinian into import length")

    return np.array([(value >> i) & 1 for i in range(length)],
                    dtype=np.uint8)



class MSK_mapper:

    def __init__(self, bit_rate, signal_energy=1, h=0.5):

        self._h             = h
        self._bit_rate      = bit_rate
        self._T             = 1/self._bit_rate
        self._E             = signal_energy

    
    def _get_theta_n(self, bit_sequence, n):
        
        if (n >= np.size(bit_sequence)): raise ValueError("n >= size of bit sequence")

        theta = 0

        for i in range(0, n):
            theta += (2*bit_sequence[i] - 1)

        theta_n = PI*self._h*theta

        return theta_n

    
    def get_average_energy(self):

        return self._E
    

    def get_baseband_signal(self, bit_sequence):

        def baseband_signal_t(t):
            n = t // self._T
            theta_n = self._get_theta_n(bit_sequence, n)

            phi_t = theta_n + (PI*self._h*(2*bit_sequence[n] - 1)) * (t - n*self._T)/self._T


            return np.sqrt(2*self._E/self._T)*np.exp(1j*phi_t)

        def baseband_signal(t_arr):
            result = np.zeros_like(t_arr, dtype=complex)

            for i in range(0, np.size(t_arr)):
                result[i] = baseband_signal_t(t_arr[i])
            
            return result

        return baseband_signal
    