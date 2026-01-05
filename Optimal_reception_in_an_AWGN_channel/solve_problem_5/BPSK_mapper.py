import numpy as np


def int_to_bits_lsb(value: int, length: int) -> np.ndarray:

    if value < 0:
        raise ValueError("value >= 0 must be")
    if value >= (1 << length):
        raise ValueError("value size not combinian into import length")

    return np.array([(value >> i) & 1 for i in range(length)],
                    dtype=np.uint8)


def bits_to_int_lsb(bits):
    value = 0

    for i, bit in enumerate(bits):
        value |= int(bit) << i
    
    return value



class BPSK_mapper:

    def __init__(self, bit_rate, E_symb_avg=1):

        self._bit_rate              = bit_rate
        self._num_bits_in_qam       = 1
        self._symbol_rate           = self._bit_rate/self._num_bits_in_qam
        self._T_symb                = 1/self._symbol_rate
        self._E_symb_avg            = E_symb_avg
        self._E_bit_avg             = E_symb_avg
        self._mod_signals           = self._get_mod_arr()

  

    def _get_mod_arr(self):
        arr_signals = np.zeros(2, dtype=complex)

        for numb in range(0, 2):
            bits = int_to_bits_lsb(numb, 1)
            arr_signals[numb] = (1/np.sqrt(2))*((1 - 2*bits[0]) + 1j*(1 - 2*bits[0]))

        return arr_signals * np.sqrt(self._E_symb_avg)
    

    def get_average_energy(self):

        return sum(x * x for x in self._mod_signals) / 2
    

    def get_baseband_signal(self, bit_sequence):

        if ((np.size(bit_sequence) % self._num_bits_in_qam) != 0): raise ValueError("the number of bits is not a multiple of the number of bits per symbo")

        bit_seq_sz = np.size(bit_sequence)

        def baseband_signal_t(t):
            
            n = t // self._T_symb
            start_bits = int(n*self._num_bits_in_qam)
            end_bits = int((n+1)*self._num_bits_in_qam)

            if start_bits >= bit_seq_sz or end_bits > bit_seq_sz: raise ValueError("There aren't bits for do modulating")

            cur_num = bits_to_int_lsb(bit_sequence[start_bits:end_bits])

            return self._mod_signals[cur_num]
        
        def baseband_signal(t_arr):
            if np.isscalar(t_arr):
                return baseband_signal_t(t_arr)

            result = np.zeros_like(t_arr, dtype=complex)

            for i in range(0, np.size(t_arr)):
                result[i] = baseband_signal_t(t_arr[i])
            
            return result

        return baseband_signal
    

    def get_modulate_sequence_and_time(self, t_start, t_end, numb_of_points, bit_sequence):
        
        if (t_end - t_start) <= 0:  raise ValueError("t_end <= t_start")
        if ((t_end - t_start) // self._T_symb + 1) * self._num_bits_in_qam > np.size(bit_sequence): raise ValueError("Шnsufficient bits to form the baseband signal")
        if numb_of_points <= 0: raise ValueError("numb_points must be > 0")

        t = np.linspace(t_start, t_end, numb_of_points)
        result = np.zeros(numb_of_points, dtype=complex)

        for i in range(0, numb_of_points):
            n = (t[i] - t[0]) // self._T_symb

            if n >= np.size(numb_of_points):
                result[i] = 0
                continue

            start_bits = int(n*self._num_bits_in_qam)
            end_bits = int((n+1)*self._num_bits_in_qam)

            cur_signal_val = bits_to_int_lsb(bit_sequence[start_bits:end_bits])
            
            result[i] = self._mod_signals[cur_signal_val]

        return result, t
    

    
    
    
    
