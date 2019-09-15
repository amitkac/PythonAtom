import distibutionFitting as distFit
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
# from statsmodels.api import Poisson


def main():

    # x = [x for x in range(1000)]
    data = np.random.normal(2, 3, 1000)
    z = distFit.Fitting(data, 'Normal')
    p = z.fitDistribution()
    k = distFit.Fitting(data, 'Nakagami').fitDistribution()
    print(p)
    plt.figure()
    plt.hist(data, bins=15, density=True, alpha=0.6, color='green')
    # plt.hold(True)
    xx = np.arange(-15, 15, 0.5)
    zz = ss.norm.pdf(xx, p[0], p[1])
    plt.plot(xx, zz, 'ok', linewidth=2)
    kk = ss.nakagami.pdf(xx, k[0], k[1], k[2])
    plt.plot(xx, kk, '+r', linewidth=2)
    plt.ylim([0, 0.2])
    plt.show()


if __name__ == '__main__':
    main()
    # x = [x for x in range(1000)]
    # y = type(x)
    # if y in (list, int):
    #     print('true')
    # else:
    #     print('false')
    # print(y)
    # y = np.random.poisson(2, 10)
    # print(y)
    # val = 'Normal'
    # if val not in ('Normal', 'Weibull', 'Lognormal', 'Rayleigh',
    #                'Nakagami', 'Gamma', 'Poisson', 'All'):
    #     print('false')
    # else:
    #     print('true')
    # x = [1:1:100]
    # print(x)
