import numpy as np


def convert_SNR_to_SNR_dB(SNR):

    return 10*np.log10(SNR)


def convert_SNR_dB_to_SNR(SNR_dB):

    return np.power(10, SNR_dB/10)