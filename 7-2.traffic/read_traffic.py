import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from numpy import inf

import matplotlib as mpl
def format(fig):
    mpl.rcParams['font.family'] = 'STIXGeneral'
    plt.rcParams['xtick.labelsize'] = 19
    plt.rcParams['ytick.labelsize'] = 19
    plt.rcParams['font.size'] = 19
    plt.rcParams['figure.figsize'] = [5.6*6, 4*3]
    plt.rcParams['axes.titlesize'] = 18
    plt.rcParams['axes.labelsize'] = 18
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markersize'] = 6
    plt.rcParams['legend.fontsize'] = 15
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['axes.linewidth'] = 1.5
    # plt.style.use('dark_background')


def ax_format(ax, xmaj, xmin, ymaj, ymin):
    ax.xaxis.set_tick_params(which='major', size=5, width=1,
                            direction='in', top='on')
    ax.xaxis.set_tick_params(which='minor', size=3, width=1,
                            direction='in', top='on')
    ax.yaxis.set_tick_params(which='major', size=5, width=1,
                            direction='in', right='on')
    ax.yaxis.set_tick_params(which='minor', size=3, width=1,
                            direction='in', right='on')
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(xmaj))
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(xmin))
    ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(ymaj))
    ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(ymin))

path = 'xplot.txt'
xplot_list = []
fo = open(path, 'r')
for line in fo:
    xplot_list.append(float(line))
fo.close()
xplot = np.array(xplot_list)

path = 'tplot.txt'
tplot_list = []
fo = open(path, 'r')
for line in fo:
    tplot_list.append(float(line))
fo.close()
tplot = np.array(tplot_list)

T, X = np.meshgrid(tplot, xplot)

path = 'rplot.txt'
data_list = []
rplot = []
fo = open(path, 'r')
for line in fo:
    s = line.split(',')
    for i in range(len(s)):
        data_list.append(float(s[i]))
    rplot.append(data_list)
    data_list = []
fo.close()
rplot = np.array(rplot)

path = 'xsplot.txt'
xsplot_list = []
fo = open(path, 'r')
for line in fo:
    xsplot_list.append(float(line))
fo.close()
xsplot = np.array(xsplot_list)

fig = plt.figure(figsize=(16,8))
format(fig)

ax1 = fig.add_subplot(1, 2, 1, projection = '3d')
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.plot_surface(X, T, rplot, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax1.set_xlabel('x')
ax1.set_ylabel('t')
ax1.set_zlabel(r'$\rho$')
ax1.set_title('Density versus position and time')
ax1.grid()

ax1 = fig.add_subplot(1, 2, 2)
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

a = ax1.contour(X, T, rplot)
ax1.plot(xsplot, tplot, 'o', markersize = 1, color = 'red', label = 'shock wave $x_s$')
ax1.clabel(a, inline=True)
ax1.set_xlabel('x')
ax1.set_ylabel('t')
ax1.set_title('Density contours')
ax1.legend()
ax1.grid()

plt.tight_layout()
#plt.show()
plt.savefig('traffic.png')

