import numpy as np
import matplotlib.pyplot as plt
import random

from scipy.stats import norm

from Converter_dB import convert_SNR_dB_to_SNR, convert_SNR_to_SNR_dB
from AWGN_generator import add_AWGN_into_sequence
from Plotting_constelation import plot_constellation
from BPSK_mapper import BPSK_mapper
from BPSK_receiver import BPSK_receiver


PI = np.pi

## task addendum, not official
# An error may occur here due to the way the function=demodulate_symbols_in_time  operates.
# For large values of bit_num, an error accumulates when the signal 
# is divided into symbol periods and assigned to specific symbols. 
# As a result, part of the bits is lost during demodulation. 
# To avoid this, increase the bit_rate, or reduce the subdivision of 
# the time variable t, but not excessively, since the function may 
# incorrectly compute the intervals. Alternatively, to avoid this issue, 
# use a fixed number of samples by rewriting the demodulation function.
##

## Model parameters
Energy_of_impulse = 1


bit_rate = 1 # need correct setting
numb_bits = int(40000)



# snrs_dB
SNRs_dB = np.arange(10, 11, 0.25)

# result BERs
BERs = np.zeros(np.size(SNRs_dB))
BERs_teor= np.zeros(np.size(SNRs_dB))


## Create objects
bpsk_mapper = BPSK_mapper(bit_rate, Energy_of_impulse)
bpsk_demod = BPSK_receiver(bit_rate, Energy_of_impulse, np.array([0.5, 0.5]))


## Start performind model of receiving
for num_ex in range(0, np.size(SNRs_dB)):
    cur_SNR_dB = SNRs_dB[num_ex]

    # Generate bit sequene
    bit_seq_tx = [random.randint(0, 1) for _ in range(numb_bits)]

    # Set correct time division
    T_symb = bpsk_mapper._T_symb
    dt = T_symb/3 + 1e-6
    t_start = 0
    t_end = t_start + np.size(bit_seq_tx)/bit_rate - dt
    t = np.arange(t_start, t_end, dt)

    # Mapping
    baseband_signal = bpsk_mapper.get_baseband_signal(bit_seq_tx)
    baseband_signals_out = baseband_signal(t)
    
    # add AWGN
    baseband_signal_with_noise = add_AWGN_into_sequence((baseband_signals_out), cur_SNR_dB)

    # demodulate
    bit_seq_rx = bpsk_demod.demodulate_symbols_in_time(t, baseband_signal_with_noise, cur_SNR_dB)

    # pltting constelation
    if cur_SNR_dB == 10: 
        plot_constellation(baseband_signals_out, baseband_signal_with_noise, "Constelation for SNR_dB=" + str(cur_SNR_dB))

    # solving BER
    num_errors = np.sum(bit_seq_tx != bit_seq_rx) # there is may be an error
    BERs[num_ex] = num_errors / np.size(bit_seq_tx)

    # Theoretical value of error's probability
    BERs_teor[num_ex] = norm.sf(np.sqrt(2*convert_SNR_dB_to_SNR(cur_SNR_dB)))

    print(cur_SNR_dB)



## Plotting results BER curves
fig5, axs = plt.subplots(1, 1, figsize=(10, 8))

axs.semilogy(SNRs_dB, BERs, '.', label='Practical error\'s probability')
axs.semilogy(SNRs_dB, BERs_teor , '--', label='Teoretical error\'s probability')
axs.set_title('curves of BER')
axs.legend()
axs.set_xlabel('SNR dB')
axs.set_ylabel('BER')
axs.grid(True)

plt.tight_layout()
plt.show()



