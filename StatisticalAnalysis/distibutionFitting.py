# log likelihood assumes that each data point is generated independently
# of other data points.
# The reason why we take loglikelihood is that because logarithmic functions
# are monotonically increasing.


# https://stackoverflow.com/questions/36931415
# /using-properties-in-python-classes-cause-maximum-recursion-depth-exceeded

# import statsmodels.api as sm
import numpy as np
import scipy.stats as ss


class Fitting(object):
    ''' This class fits the differnt distributions by utilizing the statsmodels
    library'''

    def __init__(self, data, fitType='Normal'):
        self._fitType = fitType
        self._x = data  # very important

    @property
    def x(self):
        return self._x

    @property
    def fitType(self):
        return self._fitType

    @x.setter
    def x(self, val):
        if type(val) not in (float, int, list, np.ndarray):
            raise TypeError("Expected int, float, list or numpy array ")

    @fitType.setter
    def fitType(self, val):
        if val not in ('Normal', 'Weibull', 'Lognormal', 'Rayleigh',
                       'Nakagami', 'Gamma', 'All'):
            raise TypeError(
                "Expected distribution not in the list or missing letter.")

    def fitDistribution(self):

        if self.fitType == 'Normal':
            statsNormal = ss.norm.fit(self.x)
            # print('Normal: ', *statsNormal)
            return statsNormal

        elif self.fitType == 'Weibull':
            statsWeibull = ss.weibull_min.fit(self.x)
            # print('Weibull:', *statsWeibull)
            return statsWeibull

        elif self.fitType == 'Lognormal':
            statsLogNormal = ss.lognorm.fit(self.x)
            # print('Lognormal:', *statsLogNormal)
            return statsLogNormal

        elif self.fitType == 'Rayleigh':
            statsRayleigh = ss.rayleigh.fit(self.x)
            # print('Rayleigh: ', *statsRayleigh)
            return statsRayleigh

        elif self.fitType == 'Nakagami':
            statsNakagami = ss.nakagami.fit(self.x)
            # print('Nakagami', *statsNakagami)
            return statsNakagami

        elif self.fitType == 'Gamma':
            statsGamma = ss.gamma.fit(self.x)
            # print('Gamma', *statsGamma)
            return statsGamma

        elif self.fitType == 'All':
            statsNormal = ss.norm.fit(self.x)
            print(*statsNormal)
            statsWeibull = ss.weibull_min.fit(self.x)
            print(*statsWeibull)
            statsLogNormal = ss.lognorm.fit(self.x)
            print(*statsLogNormal)
            statsRayleigh = ss.rayleigh.fit(self.x)
            print(*statsRayleigh)
            statsNakagami = ss.nakagami.fit(self.x)
            print(*statsNakagami)
            statsGamma = ss.gamma.fit(self.x)
            print(*statsGamma)
