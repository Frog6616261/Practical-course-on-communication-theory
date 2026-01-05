import numpy as np
import matplotlib.pyplot as plt

def plot_constellation(signals_tx, signals_rx, title="Constellation diagram"):
    plt.figure()
    plt.scatter(signals_rx.real, signals_rx.imag, s=5, alpha=0.6, label='rx, out of channel')
    plt.scatter(signals_tx.real, signals_tx.imag, s=5, alpha=0.6, label='tx, out of transmitter')
    plt.axhline(0)
    plt.axvline(0)
    plt.xlabel("In-phase (I)")
    plt.ylabel("Quadrature (Q)")
    plt.title(title)
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()
