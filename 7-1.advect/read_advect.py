import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

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


fig1 = plt.figure(figsize=(16,8))
format(fig1)
fig1.suptitle('Advection Equation of method_tau')

fig2 = plt.figure(figsize=(16,8))
format(fig2)
fig2.suptitle('Wave Pulse of method_tau')
filename = ['FTCS_0.002', 'Lax_0.02', 'Lax_0.015', 'Lax-Wendroff_0.015', 'upwind_0.002', 'upwind_0.02', 'upwind_0.015', 'test']

for k in range(8):
    path = 'a_'+filename[k]+'.txt'
    a_list = []
    fo = open(path, 'r')
    for line in fo:
        a_list.append(float(line))
    fo.close()
    a = np.array(a_list)

    path = 'x_'+filename[k]+'.txt'
    x_list = []
    fo = open(path, 'r')
    for line in fo:
        x_list.append(float(line))
    fo.close()
    x = np.array(x_list)

    path = 'tplot_'+filename[k]+'.txt'
    tplot_list = []
    fo = open(path, 'r')
    for line in fo:
        tplot_list.append(float(line))
    fo.close()
    tplot = np.array(tplot_list)

    T, X = np.meshgrid(tplot, x)

    path = 'aplot_'+filename[k]+'.txt'
    data_list = []
    aplot = []
    fo = open(path, 'r')
    for line in fo:
        s = line.split(',')
        for i in range(len(s)):
            data_list.append(float(s[i]))
        aplot.append(data_list)
        data_list = []
    fo.close()
    aplot = np.array(aplot)
    print(k)

    ax1 = fig1.add_subplot(2, 4, k+1, projection = '3d')
    #ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

    ax1.plot_surface(X, T, aplot, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax1.set_xlabel('x')
    ax1.set_ylabel('t')
    ax1.set_zlabel('a(x,t)')
    ax1.set_title(filename[k])
    ax1.grid()


    ax1 = fig2.add_subplot(2, 4, k+1)

    ax1.plot(x, aplot[:, 0], '-', label = 'Initial')
    ax1.plot(x, a, '--', label = 'Final')
    ax1.set_xlabel('x')
    ax1.set_ylabel('a(x,t)')
    ax1.set_title(filename[k])
    ax1.legend()
plt.tight_layout()
plt.savefig('advect2.png')
plt.close()
plt.tight_layout()
plt.savefig('advect1.png')
plt.close()
