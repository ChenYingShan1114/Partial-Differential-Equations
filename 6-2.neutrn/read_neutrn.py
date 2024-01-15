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

path = 'nAve.txt'
nAve_plot = []
fo = open(path, 'r')
for line in fo:
    nAve_plot.append(float(line))
fo.close()
nAve = np.array(nAve_plot)
print(nAve.size)

path = 'tplot.txt'
t_plot = []
fo = open(path, 'r')
for line in fo:
    t_plot.append(float(line))
fo.close()
t = np.array(t_plot)
print(t.size)

path = 'xplot.txt'
x_plot = []
fo = open(path, 'r')
for line in fo:
    x_plot.append(float(line))
fo.close()
x = np.array(x_plot)
print(x.size)

T, X = np.meshgrid(t, x)

path = 'nnplot.txt'
data_list = []
nn_plot = []
fo = open(path, 'r')
for line in fo:
    s = line.split(',')
    for i in range(len(s)):
        data_list.append(float(s[i]))
    nn_plot.append(data_list)
    data_list = []
fo.close()
nn = np.array(nn_plot)
print(nn.shape)

path = 'nnaplot.txt'
data_list = []
nna_plot = []
fo = open(path, 'r')
for line in fo:
    s = line.split(',')
    for i in range(len(s)):
        data_list.append(float(s[i]))
    nna_plot.append(data_list)
    data_list = []
fo.close()
nna = np.array(nna_plot)
print(nna.shape)

path = 'nnaplot1.txt'
data_list = []
nna1_plot = []
fo = open(path, 'r')
for line in fo:
    s = line.split(',')
    for i in range(len(s)):
        data_list.append(float(s[i]))
    nna1_plot.append(data_list)
    data_list = []
fo.close()
nna1 = np.array(nna1_plot)
print(nna1.shape)

fig = plt.figure(figsize=(16,8))
format(fig)

ax1 = fig.add_subplot(2, 3, 1, projection = '3d')
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.plot_surface(X, T, nn, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax1.set_xlabel('x')
ax1.set_ylabel('Time')
ax1.set_zlabel('n(x,t)')
ax1.set_title('Neutron diffusion by FTCS scheme')
ax1.grid()

ax1 = fig.add_subplot(2, 3, 2, projection = '3d')
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.plot_surface(X, T, nna1, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax1.set_xlabel('x')
ax1.set_ylabel('Time')
ax1.set_zlabel('$\mathrm{n_a(x,t)}$')
ax1.set_title('Analytical solution for $j=0$')
ax1.grid()

ax1 = fig.add_subplot(2, 3, 3, projection = '3d')
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.plot_surface(X, T, abs(nn - nna1), rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax1.set_xlabel('x')
ax1.set_ylabel('Time')
ax1.set_zlabel('$\mathrm{| n_a(x,t) - n(x,t) |}$')
ax1.set_title('Maximum error = ' + str(np.max(np.abs(nna1-nn))))
ax1.grid()

ax1 = fig.add_subplot(2, 3, 5, projection = '3d')
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.plot_surface(X, T, nna, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax1.set_xlabel('x')
ax1.set_ylabel('Time')
ax1.set_zlabel('$\mathrm{n_a(x,t)}$')
ax1.set_title('Analytical solution')
ax1.grid()

ax1 = fig.add_subplot(2, 3, 6, projection = '3d')
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.plot_surface(X, T, abs(nn - nna), rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax1.set_xlabel('x')
ax1.set_ylabel('Time')
ax1.set_zlabel('$\mathrm{| n_a(x,t) - n(x,t) |}$')
ax1.set_title('Maximum error = ' + str(np.max(np.abs(nna-nn))))
ax1.grid()
plt.savefig('neutrn.png')

fig = plt.figure(figsize=(16,8))
format(fig)

ax1 = fig.add_subplot(1, 1, 1)

ax1.plot(t, nAve, '.')
ax1.set_xlabel('Time')
ax1.set_ylabel('Average density')
plt.show()
