import numpy as np
import matplotlib.pyplot as plt



def plot_constellation(samples: np.ndarray, title: str = "Сигнальное созвездие"):
    """
    Строит сигнальное созвездие по комплексным отсчётам.

    samples — numpy-массив комплексных чисел
    """
    if not np.iscomplexobj(samples):
        raise ValueError("samples должен быть массивом комплексных чисел")

    plt.figure()
    plt.scatter(samples.real, samples.imag, s=10, alpha=0.7)
    plt.axhline(0)
    plt.axvline(0)
    plt.grid(True)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.xlabel("In-phase (I)")
    plt.ylabel("Quadrature (Q)")
    plt.title(title)
    plt.show()