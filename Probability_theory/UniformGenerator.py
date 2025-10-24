import numpy as np


SEED_CONST = np.uint32(17)
Y_CONST = np.uint32(23)

class UniformGenerator:
    
    def __init__(self, seed=None):
        self._seed = SEED_CONST if (seed is not None) else  seed
        self._y = Y_CONST
        self._cur_sample = self._seed
    
    def _get_next_sample(self, cur_sample):
        return ()


    def _check_by_Pirson(self):


    def _check_by_Kolmogorov(self):


    def generate_samples(self, n):
        return

    def reset(self):
        self._cur_sample = self._seed
