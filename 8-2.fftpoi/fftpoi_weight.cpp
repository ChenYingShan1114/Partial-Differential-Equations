// fftpoi - Program to solve the Poisson equation using
// MFT method (periodic boundary conditions)
#include <iostream>
#include <fstream>
#include <assert.h>  
#include <cmath>
#include "Matrix.h"
using namespace std;
#include "fft.h"
#include "fft2.h"
#include "ifft2.h"
//void fft2( Matrix& RealA, Matrix& ImagA);
//void ifft2( Matrix& RealA, Matrix& ImagA);

int main() {

  //* Initialize parameters (system size, grid spacing, etc.)
  double eps0 = 8.8542e-12;   // Permittivity (C^2/(N m^2))
  int N = 128;   // Number of grid points on a side (square grid)
  double L = 1;    // System size
  double h = L/N;  // Grid spacing for periodic boundary conditions
  Matrix x(N), y(N);
  int i,j,ii,jj;
  for( i=1; i<=N; i++ )
    x(i) = (i-0.5)*h;  // Coordinates of grid points
  y = x;               // Square grid
  cout << "System is a square of length " << L << endl;

  //* Set up charge density rho(i,j)
  Matrix rho(N,N);
  rho.set(0.0);     // Initialize charge density to zero
  cout << "Enter number of line charges: "; int M = 2; // cin >> M;
  for( i=1; i<=M; i++ ) {
    double d = 0.01;
    cout << "For charge #" << i << endl;
    cout << "Enter x coordinate: "; double xc = 0.5; cout << xc << endl;
    cout << "Enter y coordinate: "; double yc = 0.5 + pow(-1, i-1) * d / 2; cout << yc << endl;
    for ( int k=1; k<N; k++){
      if (xc >= x(k) && xc <= x(k+1)){
        ii = k;
      }
      if (yc >= y(k) && yc <= y(k+1)){
        jj = k;
      }
    }
    cout << "Enter charge density: "; double q = pow(-1, i-1); cout << q << endl;
//    rho(ii,jj) += q/(h*h);
    double delta_x = x(ii+1) - xc, delta_y = y(jj+1) - yc;
    rho(ii,jj) += q/(h*h)*delta_x*delta_y/h/h;
    rho(ii+1,jj) += q/(h*h)*delta_y*(h-delta_x)/h/h;
    rho(ii,jj+1) += q/(h*h)*delta_x*(h-delta_y)/h/h;
    rho(ii+1,jj+1) += q/(h*h)*(h-delta_x)*(h-delta_y)/h/h;
//    cout << rho(ii,jj) << " " << rho(ii+1,jj) << " " << rho(ii,jj+1) << " " << rho(ii+1,jj+1) << endl;
    cout << ii << " " << jj << " " << rho(ii,jj) + rho(ii+1,jj) + rho(ii,jj+1) + rho(ii+1,jj+1) << endl;
  }

  //* Compute matrix P
  const double pi = 3.141592654;
  Matrix cx(N), cy(N);
  for( i=1; i<=N; i++ )
    cx(i) = cos((2*pi/N)*(i-1));
  cy = cx;
  Matrix RealP(N,N), ImagP(N,N);
  double numerator = -h*h/(2*eps0);
  double tinyNumber = 1e-20;  // Avoids division by zero
  for( i=1; i<=N; i++ )
   for( j=1; j<=N; j++ )
     RealP(i,j) = numerator/(cx(i)+cy(j)-2+tinyNumber);
  ImagP.set(0.0);

  //* Compute potential using MFT method
  Matrix RealR(N,N), ImagR(N,N), RealF(N,N), ImagF(N,N);
  for( i=1; i<=N; i++ )
   for( j=1; j<=N; j++ ) {
     RealR(i,j) = rho(i,j);
     ImagR(i,j) = 0.0;       // Copy rho into R for input to fft2
   }
  fft2(RealR,ImagR);   // Transform rho into wavenumber domain
  // Compute phi in the wavenumber domain
  for( i=1; i<=N; i++ )
   for( j=1; j<=N; j++ ) {
    RealF(i,j) = RealR(i,j)*RealP(i,j) - ImagR(i,j)*ImagP(i,j);
    ImagF(i,j) = RealR(i,j)*ImagP(i,j) + ImagR(i,j)*RealP(i,j);
   }
  Matrix phi(N,N);
  ifft2(RealF,ImagF);    // Inv. transf. phi into the coord. domain
  for( i=1; i<=N; i++ )
   for( j=1; j<=N; j++ )
     phi(i,j) = RealF(i,j);

  //* Print out the plotting variables: x, y, phi
  ofstream xOut("x_weight.txt"), yOut("y_weight.txt"), phiOut("phi_weight.txt");
  for( i=1; i<=N; i++ ) {
    xOut << x(i) << endl;
    yOut << y(i) << endl;
    for( j=1; j<N; j++ )
      phiOut << phi(i,j) << ", ";
    phiOut << phi(i,N) << endl;
  }
}
/***** To plot in MATLAB; use the script below ********************
load x.txt; load y.txt; load phi.txt;
%* Compute electric field as E = - grad phi
[Ex Ey] = gradient(flipud(rot90(phi)));
magnitude = sqrt(Ex.^2 + Ey.^2);
Ex = -Ex ./ magnitude;     % Normalize components so
Ey = -Ey ./ magnitude;     % vectors have equal length
%* Plot potential and electric field
figure(1); clf;
contour3(x,y,flipud(rot90(phi,1)),35);
xlabel('x'); ylabel('y'); zlabel('\Phi(x,y)');
figure(2); clf;
quiver(x,y,Ex,Ey)        % Plot E field with vectors
title('E field (Direction)'); xlabel('x'); ylabel('y');
axis('square');  axis([0 1 0 1]);
******************************************************************/
