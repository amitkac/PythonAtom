# ----------------------------------------------
# Author: Amit Kachroo <amit.kachroo@okstate.edu>

import distibutionFitting as distFit
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
from AIC import AIC
# from statsmodels.api import Poisson


def main():

    # x = [x for x in range(1000)]
    data = np.random.normal(2, 3, 1000)
    z = distFit.Fitting(data, 'Normal')
    p = z.fitDistribution()
    k = distFit.Fitting(data, 'Nakagami').fitDistribution()
    # print(p)
    plt.figure()
    counts, bins, bars = plt.hist(data, bins=62,
                                  density=True, alpha=0.6,
                                  color='green')
    binCenters = 0.5*(bins[1:]+bins[:-1])

    zz = ss.norm.pdf(binCenters, p[0], p[1])
    plt.plot(binCenters, zz, 'ok', linewidth=2)
    kk = ss.nakagami.pdf(binCenters, k[0], k[1], k[2])
    # print(len(kk))
    plt.plot(binCenters, kk, '+r', linewidth=2)
    plt.ylim([0, 0.2])
    plt.show()
    # print(counts.shape)
    aicNorm = AIC(np.array(zz),
                  np.array(counts), 2).aicValue()
    aicNakagami = AIC(kk, counts, 3).aicValue()
    print(aicNorm, aicNakagami)


if __name__ == '__main__':
    main()
