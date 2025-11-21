import numpy as np
from numpy.fft import fft, ifft, fftshift
from scipy.signal import correlate


class RandomProcessGenerator:
    """
    Генератор случайного процесса ξ с заданной автокорреляционной функцией.
    """

    def __init__(self, b_xi):
        """
        :param b_xi: теоретическая автокорреляционная функция (массив)
        """
        self.b_xi = np.array(b_xi)
        self.Nfft = 1024  # длина для преобразований Фурье

        # Теоретический спектр (по теореме Винера–Хинчина)
        self.S_xi = np.real(fft(self.b_xi, n=self.Nfft))

        # Импульсная характеристика фильтра h(t)
        H = np.sqrt(np.maximum(self.S_xi, 0))  # модуль передаточной функции
        self.h = np.real(ifft(H))  # импульсная характеристика (действительная часть)

    def generate(self, N=2048):
        """
        Генерирует реализацию случайного процесса ξ длиной N.

        :param N: длина выборки
        :return: массив ξ
        """
        eta = np.random.normal(0, 1, N)  # белый шум
        xi = np.convolve(eta, self.h, mode="same")  # метод скользящего среднего
        return xi

    @staticmethod
    def acf(x):
        """
        Оценка автокорреляционной функции (симметричная, нормированная).
        """
        r = correlate(x, x, mode='full', method='fft')
        r = r / np.max(r)  # нормировка
        lags = np.arange(-len(x) + 1, len(x))
        return lags, r

    @staticmethod
    def spectrum(x, Nfft=1024):
        """
        Вычисление оценки спектра по БПФ.
        """
        S = np.abs(fft(x, n=Nfft)) ** 2
        freqs = np.fft.fftfreq(Nfft, d=1)
        return fftshift(freqs), fftshift(S)
