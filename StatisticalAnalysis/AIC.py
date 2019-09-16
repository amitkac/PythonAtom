
# ----------------------------------------------
# Author: Amit Kachroo <amit.kachroo@okstate.edu>
import numpy as np


class AIC(object):

    def __init__(self, yPred, y, nParam):
        self._yPred = yPred
        self._y = y
        self.nParam = nParam

    @property
    def yPred(self):
        return self._yPred

    @yPred.setter
    def yPred(self, val):
        if type(val) not in (float, int, list, np.ndarray):
            raise TypeError("Expected int, float, list or numpy array ")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        if type(val) not in (float, int, list, np.ndarray):
            raise TypeError("Expected int, float, list or numpy array ")

    def aicValue(self):
        if len(self.y) != len(self.yPred):
            raise TypeError("length of y and yPred has to be same")
        n = len(self.y)
        residue = self.y-self.yPred
        rss = np.sum(np.power(residue, 2))
        aicScore = n*np.log(rss/n)+2*self.nParam
        return aicScore
