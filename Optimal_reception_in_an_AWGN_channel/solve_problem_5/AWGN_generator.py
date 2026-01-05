import numpy as np
import Converter_dB as conv_dB


def add_AWGN_into_sequence(signal_seq, snr_db):

    power_signal = np.mean(np.power(np.abs(signal_seq), 2))
    snr_linear = conv_dB.convert_SNR_dB_to_SNR(snr_db)
    power_noise = power_signal / snr_linear

    if np.iscomplexobj(signal_seq):
        noise = np.sqrt(power_noise/2) * (np.random.randn(*signal_seq.shape) + 1j*np.random.randn(*signal_seq.shape))
    else:
        noise = np.sqrt(power_noise) * np.random.randn(*signal_seq.shape)
    
    return signal_seq + noise
