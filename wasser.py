from matplotlib import pyplot as plt
import numpy as np

def r(x):
    return np.exp(-.3466*x)

def g(x):
    return np.exp(-.1161*x)

def b(x):
    return np.exp(-.03289*x)

if __name__ == '__main__':
    y = np.zeros(10)
    x = np.linspace(0., 10., 200)
    Y, R = np.meshgrid(y, r(x))
    Y, G = np.meshgrid(y, g(x))
    Y, B = np.meshgrid(y, b(x))
    R = R.transpose()
    G = G.transpose()
    B = B.transpose()
    X = np.array([R, G, B]).transpose()
    plt.imshow(X, extent=(0., 1., x[-1], x[0]), interpolation=None)
    plt.axis('tight')
    plt.xticks([])
    plt.ylabel("Tiefe in [m]")
    plt.savefig('wasser.png')
