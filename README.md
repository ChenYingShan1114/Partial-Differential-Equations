
# Partial Differential Equation
## Reference
A. L. Garcia, "Numerical Methods for Physics": \
    Chapter 6 Partial Differential Equations I: Foundations and Basic Explicit Methods \
    Chapter 7 Partial Differential Equations II: Advanced Explicit Methods \
    Chapter 8 Partial Differential Equations III: Relaxation and Spectral Methods
## Exercisies
### 6-1.dftcs
(a) Write a function to evaluate Equation (6.16) numerically for $T(x,t)$ and reproduce Figure 6.6. \
(b) Use the function from part (a) in the **dftcs.cpp** program to produce a graph of $|T_a (x,t)-T_c (x,t)|$, the absolute difference between the analytical temperature profile, $T_a$, and the profile obtained by FTCS scheme, $T_c$.

### 6-2.neutrn
Consider the Neumann boundary conditions:
```math
\frac{\partial n}{\partial x}|_{x=-\frac{L}{2}}=\frac{\partial n}{\partial x}|_{x=\frac{L}{2}}=0
```
(a) Using separation of variables show that this system is always supercritical. \
(b) Modify **neutrn.cpp** to implement these boundary conditions by setting $n_1^n=n_2^n$ and $n_N^n=n_{N-1}^n$. In this case the spatial discretization is $x_i=(i-3/2)h-L/2$ with $h=L/(N-2)$ for these boundary conditions. Compare the program’s output with the result predicted in part (a).

### 7-1.advect
The “upwind” scheme for solving the advection equation uses a left derivation for the $\partial/\partial x$ term,
```math
\frac{a_i^{n+1}-a_i^n}{\tau}=-c\frac{a_i^n-a_{i-1}^n}{h}
```
Modify the **advect.cpp** program to use this scheme, and compare it with the others discussed in this section for the cases shown in Figures 7.3-7.7. For what values of $\tau$ is it stable?

### 7-2.traffic
Call $x_s(t)$ the position of the shock wave (see Figures 7.18 and 7.24). The velocity of the shock is given by
```math
\frac{dx_s}{dt}=\frac{F(\rho_+ )-F(\rho_- )}{\rho_+-\rho_-}
```
where $F(x,t)=\rho(x,t)v(x,t)$ is the flow and $\rho_±=\lim_{\epsilon \rightarrow 0} \rho(x_s±\epsilon)$, that is, the density on each side of the shock front. \
(a) Show that
```math
\frac{dx_s}{dt}=\frac{1}{2} (c(\rho_+ )+c(\rho_- ))
```
when $v$ is linear in the density. \
(b) Use the density profile computed by the **traffic.cpp** program to compute $x_s(t)$ given that $x_s(0)=-L/4$. Compare your results with the locations of steep gradients in the contour plot produced by **traffic.cpp**.

### 8-1.relax
A major issue with relaxation methods is their computational speed. \
(a) Run the **relax.cpp** program using the Jacobi method for different-sized systems ($N_x=N_y=10$ to $50$). Graph the number of iterations performed versus system size. Fit the data to a power law and approximate the exponent. \
(b) Repeat part (a) using a bad initial guess. Set the potential initially to zero everywhere in the interior. \
(c) Using SOR, repeat parts (a) and (b). Compare the Jacobi and SOR methods (use the optimum value for $\omega$).

### 8-2.fftpoi
The **fftpoi.cpp** program use a rather coarse method for placing the charges on the grid: It assigns a charge to the nearest grid point. Modify the program so that it proportionally assigns a fraction of the charge to each of the nearest four grid points as $\rho_{ij}=\lambda \delta_x \delta_y/h_x h_y$ (see the following figure). Compare with the unmodified version by plotting $\Phi(x=L/2,y)$ for a dipole with charges at $(x,y)=(L/2,(L+d)/2)$ and $(L/2,(L-d)/2)$. Take $L=1$ and $d=1/100$.
