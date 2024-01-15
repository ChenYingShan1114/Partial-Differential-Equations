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

path = 'x_weight.txt'
x_list = []
fo = open(path, 'r')
for line in fo:
    x_list.append(float(line))
fo.close()
x = np.array(x_list)  

path = 'y_weight.txt'
y_list = []
fo = open(path, 'r')
for line in fo:
    y_list.append(float(line))
fo.close()
y = np.array(y_list)  

Y, X = np.meshgrid(y, x)

path = 'phi_origin.txt'
data_list = []
phi_origin = []
fo = open(path, 'r')
for line in fo:
    s = line.split(',')
    for i in range(len(s)):
        data_list.append(float(s[i]))
    phi_origin.append(data_list)
    data_list = []
fo.close()
phi_origin = np.array(phi_origin)

Ex_origin, Ey_origin = np.gradient(phi_origin)
magnitude = np.sqrt(Ex_origin * Ex_origin + Ey_origin * Ey_origin)
Ex_origin = -Ex_origin / magnitude
Ey_origin = -Ey_origin / magnitude

path = 'phi_weight.txt'
data_list = []
phi_weight = []
fo = open(path, 'r')
for line in fo:
    s = line.split(',')
    for i in range(len(s)):
        data_list.append(float(s[i]))
    phi_weight.append(data_list)
    data_list = []
fo.close()
phi_weight = np.array(phi_weight)

Ex_weight, Ey_weight = np.gradient(phi_weight)
magnitude = np.sqrt(Ex_weight * Ex_weight + Ey_weight * Ey_weight)
Ex_weight = -Ex_weight / magnitude
Ey_weight = -Ey_weight / magnitude

fig1 = plt.figure(figsize=(16,8))
format(fig1)

ax1 = fig1.add_subplot(2, 3, 1, projection = '3d')
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.contour(X, Y, phi_origin, levels = 100, cmap='viridis', linewidths = 1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('$\Phi(x,y)$')
ax1.set_title('Nearest grid')
ax1.grid()

ax1 = fig1.add_subplot(2, 3, 2)
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.quiver(X[::4,::4], Y[::4,::4], Ex_origin[::4,::4], Ey_origin[::4,::4])
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Nearest grid E field (direction)')
ax1.set_xlim([0, 1])
ax1.set_ylim([0, 1])

ax1 = fig1.add_subplot(2, 3, 4, projection = '3d')
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.contour(X, Y, phi_weight, levels = 50, cmap='viridis', linewidths = 1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('$\Phi(x,y)$')
ax1.set_title('Weighting grid')
ax1.grid()

ax1 = fig1.add_subplot(2, 3, 5)
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.quiver(X[::4,::4], Y[::4,::4], Ex_weight[::4,::4], Ey_weight[::4,::4])
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Weighting grid E field (direction)')
ax1.set_xlim([0, 1])
ax1.set_ylim([0, 1])

ax1 = fig1.add_subplot(1, 3, 3)
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)
ax1.plot(y, phi_origin[int(0.5*y.size), :], label = 'Nearest grid', color = 'yellowgreen')
ax1.plot(y, phi_weight[int(0.5*y.size), :], label = 'Weighting grid', color = 'coral')
print(np.max(np.abs(phi_origin[int(0.5*y.size), :] - phi_weight[int(0.5*y.size), :])))
ax1.set_xlabel('y')
ax1.set_ylabel('$\Phi(x=L/2,y)$')
ax1.legend()

plt.tight_layout()
#plt.show()
plt.savefig('fftpoi.png')
plt.close()
