import numpy as np

from Converter_dB import convert_SNR_dB_to_SNR, convert_SNR_to_SNR_dB


PI = np.pi

def int_to_bits_lsb(value: int, length: int) -> np.ndarray:

    if value < 0:
        raise ValueError("value >= 0 must be")
    if value >= (1 << length):
        raise ValueError("value size not combinian into import length")

    return np.array([(value >> i) & 1 for i in range(length)],
                    dtype=np.uint8)



class BPSK_receiver:

    def __init__(self, bit_rate, avg_signal_energy, prob_m_arr):

        self._bit_rate              = bit_rate
        self._T_symb                = 1/self._bit_rate
        self._E_symb_avg            = avg_signal_energy
        self._mod_symbols           = self._get_mod_arr()
        self._demod_symbols         = self._get_demod_dict()
        self._prob_m                = prob_m_arr



    def _get_mod_arr(self):
        arr_signals = np.zeros(2, dtype=complex)

        for numb in range(0, 2):
            bits = int_to_bits_lsb(numb, 1)
            arr_signals[numb] = (1/np.sqrt(2))*((1 - 2*bits[0]) + 1j*(1 - 2*bits[0]))

        return arr_signals * np.sqrt(self._E_symb_avg)
    

    def _get_demod_dict(self):
        dict_simbols = {}

        for num in range(0, 2):
            dict_simbols[self._mod_symbols[num]] = int_to_bits_lsb(num, 1)

        return dict_simbols
    

    def _demodulate_signal(self, t, symb_seq, snr_db):
        # by distanse metric, MAP algorithm

        if (np.size(t) - np.size(symb_seq) != 1): raise ValueError("not correctlength in input params, t must be greater than symb_seq by 1")

        snr_lin = convert_SNR_dB_to_SNR(snr_db)
        N_0 = self._E_symb_avg/snr_lin

        dist_m = np.zeros(np.size(self._mod_symbols))

        for m in range(0, np.size(self._mod_symbols)):
            signal_m = self._mod_symbols[m]
            cur_dist_m = 0

            for i in range(0, (np.size(t) - 1)):
                cur_dist_m += np.power(np.abs(symb_seq[i] - signal_m), 2) * (t[i+1]-t[i])

            dist_m[m] = N_0 * np.log(self._prob_m[m]) - cur_dist_m

        return self._demod_symbols[self._mod_symbols[np.argmax(dist_m)]]
    

    def demodulate_symbols_in_time(self, t, signals_in, snr_db):

        if not(np.size(t) >= 2):  raise ValueError("t size must be >= 2")
        if not(np.all(np.diff(t) >= 0)):  raise ValueError("t[i] >= t[i+1]")
        if np.size(t) != np.size(signals_in): raise ValueError("not same length t and symbols_in")

        demod_seq = []

        cur_num_t_start = 0

        for i in range(1, np.size(t)):

            if (t[i] - t[cur_num_t_start] >= self._T_symb):
                cur_bit_seq = self._demodulate_signal(t[cur_num_t_start:(i+1)], signals_in[cur_num_t_start:i], snr_db)
                cur_num_t_start = i
                demod_seq.append(cur_bit_seq)

            elif (t[i] == t[-1]) and (cur_num_t_start != i):
                cur_bit_seq = self._demodulate_signal(t[cur_num_t_start:(i+1)], signals_in[cur_num_t_start:i], snr_db)
                demod_seq.append(cur_bit_seq)

            else:
                continue

        return np.concatenate(demod_seq)