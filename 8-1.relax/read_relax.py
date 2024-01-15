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

path = 'x.txt'
x_list = []
fo = open(path, 'r')
for line in fo:
    x_list.append(float(line))
fo.close()
x = np.array(x_list)  

path = 'y.txt'
y_list = []
fo = open(path, 'r')
for line in fo:
    y_list.append(float(line))
fo.close()
y = np.array(y_list)  

Y, X = np.meshgrid(y, x)

path = 'phi.txt'
data_list = []
phi = []
fo = open(path, 'r')
for line in fo:
    s = line.split(',')
    for i in range(len(s)):
        data_list.append(float(s[i]))
    phi.append(data_list)
    data_list = []
fo.close()
phi = np.array(phi)

fig1 = plt.figure(figsize=(16,8))
format(fig1)

ax1 = fig1.add_subplot(1, 2, 1, projection = '3d')
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

ax1.plot_surface(X, Y, phi, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('$\Phi(x,y)$')
ax1.grid()

ax1 = fig1.add_subplot(1, 2, 2)
#ax_format(ax1, 0.5e-13, 0.1e-13, 0.5e-13, 0.1e-13)

a = ax1.contour(X, Y, phi)
ax1.clabel(a, inline=True)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
#ax1.set_zlabel('$\Phi(x,y)$')
ax1.grid()

plt.tight_layout()
#plt.show()
#plt.savefig('relax1.png')
plt.close()


system_size = np.linspace(10, 50, 9)
iter_Jacobi_4 = np.array([28, 60, 60, 80, 100, 119, 135, 150, 162])
iter_Jacobi_5 = np.array([43, 158, 103, 196, 197, 254, 311, 374, 437])
iter_Jacobi_6 = np.array([58, 249, 173, 483, 291, 636, 473, 624, 699])
iter_SOR_4 = np.array([20, 31, 42, 53, 64, 74, 85, 96, 106])
iter_SOR_5 = np.array([22, 34, 46, 58, 70, 82, 93, 105, 116])
iter_SOR_6 = np.array([26, 40, 53, 67, 80, 93, 106, 118, 131])
iter_Jacobi_bad_4 = np.array([113, 240, 399, 583, 789, 1013, 1251, 1502, 1764])
iter_Jacobi_bad_5 = np.array([150, 330, 566, 850, 1177, 1545, 1949, 2387, 2856])
iter_Jacobi_bad_6 = np.array([187, 421, 734, 1118, 1569, 2083, 2656, 3287, 3973])
iter_SOR_bad_4 = np.array([21, 31, 42, 53, 64, 75, 85, 96, 107])
iter_SOR_bad_5 = np.array([24, 37, 48, 59, 70, 82, 94, 106, 118])
iter_SOR_bad_6 = np.array([28, 43, 57, 71, 85, 98, 110, 123, 137])

fig1 = plt.figure(figsize=(16,8))
format(fig1)

ax1 = fig1.add_subplot(2, 2, 1)
ax1.plot(system_size, iter_Jacobi_4, '--o', label = 'error = 1e-4')
ax1.plot(system_size, iter_Jacobi_5, '--o', label = 'error = 1e-5')
ax1.plot(system_size, iter_Jacobi_6, '--o', label = 'error = 1e-6')
ax1.set_xlabel('system size $N$')
ax1.set_ylabel('# of iterations')
ax1.set_title('Jacobi method with perfect initial guess')
ax1.legend()

ax1 = fig1.add_subplot(2, 2, 2)
ax1.plot(system_size, iter_SOR_4, '--o', label = 'error = 1e-4')
ax1.plot(system_size, iter_SOR_5, '--o', label = 'error = 1e-5')
ax1.plot(system_size, iter_SOR_6, '--o', label = 'error = 1e-6')
ax1.set_xlabel('system size $N$')
ax1.set_ylabel('# of iterations')
ax1.set_title('SOR method with perfect initial guess')
ax1.legend()

ax1 = fig1.add_subplot(2, 2, 3)
ax1.plot(system_size, iter_Jacobi_bad_4, '--o', label = 'error = 1e-4')
ax1.plot(system_size, iter_Jacobi_bad_5, '--o', label = 'error = 1e-5')
ax1.plot(system_size, iter_Jacobi_bad_6, '--o', label = 'error = 1e-6')
ax1.set_xlabel('system size $N$')
ax1.set_ylabel('# of iterations')
ax1.set_title('Jacobi method with bad initial guess')
ax1.legend()

ax1 = fig1.add_subplot(2, 2, 4)
ax1.plot(system_size, iter_SOR_bad_4, '--o', label = 'error = 1e-4')
ax1.plot(system_size, iter_SOR_bad_5, '--o', label = 'error = 1e-5')
ax1.plot(system_size, iter_SOR_bad_6, '--o', label = 'error = 1e-6')
ax1.set_xlabel('system size $N$')
ax1.set_ylabel('# of iterations')
ax1.set_title('SOR method with bad initial guess')
ax1.legend()

plt.tight_layout()
#plt.show()
plt.savefig('relax.png')
#plt.close()

