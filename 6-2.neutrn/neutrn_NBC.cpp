// neutrn - Program to solve the neutron diffusion equation.
// using the Forward Time Centered Space (FTCS) scheme.
#include <iostream>
#include <fstream>
#include <assert.h>  
#include <cmath>
#include "Matrix.h"
using namespace std;

int main() {

  //* Initialize parameters (time step, grid spacing, etc.).
  cout << "Enter time step: "; double tau; cin >> tau;
  cout << "Enter the number of grid points: "; int N; cin >> N;
  cout << "Enter system length: "; double L; cin >> L;  
  // The system extends from x=-L/2 to x=L/2
  double h = L/(N-2);  // Grid size
  double D = 1.;       // Diffusion coefficient
  double C = 1.;       // Generation rate
  double coeff = D*tau/(h*h);
  double coeff2 = C*tau;
  double alpha = 0.;
  if( coeff < 0.5 )
    cout << "Solution is expected to be stable" << endl;
  else
    cout << "WARNING: Solution is expected to be unstable" << endl;

  //* Set initial and boundary conditions.
  Matrix nn(N), nn_new(N);
  nn.set(0.0);     // Initialize density to zero at all points
  nn(N/2) = 1/h;   // Initial cond. is delta function in center
  //// The boundary conditions are nn(1) = nn(N) = 0
  nn_new.set(0.0);  // End points are unchanged during iteration

  //* Set up loop and plot variables.
  int iplot = 1;                 // Counter used to count plots
  cout << "Enter number of time steps: "; int nStep; cin >> nStep;
  int plot_step = 200;           // Number of time steps between plots
  int nplots = nStep/plot_step + 1;  // Number of snapshots (plots)
  Matrix xplot(N), tplot(nplots), nnplot(N,nplots), nAve(nplots), nnaplot1(N,nplots), nnaplot(N,nplots);
  int i,j;
  for( i=1; i<=N; i++ )
    xplot(i) = (i-3.0/2.0)*h - L/2;   // Record the x scale for plots

  //* Loop over the desired number of time steps.
  int iStep;
  for( iStep=1; iStep<=nStep; iStep++ ) {

    //* Compute new density using FTCS scheme.
    for( i=2; i<=(N-1); i++ )
      nn_new(i) = nn(i) + coeff*(nn(i+1) + nn(i-1) - 2*nn(i))
	                    + coeff2*nn(i);
    nn_new(1) = nn_new(2);
    nn_new(N) = nn_new(N-1);
    nn = nn_new;     // Reset density to new values
  
    //* Periodically record density for plotting.
    if( (iStep%plot_step) < 1 ) { // Every plot_step steps ...
	  double nSum = 0;
      for( i=1; i<=N; i++ ) {      
        nnplot(i,iplot) = nn(i);  // Record tt(i) for plotting 
		nSum += nn(i);
	  }
	  nAve(iplot) = nSum/N;
      tplot(iplot) = iStep*tau;   // Record time for plots
      iplot++;
    }
  }
  nplots = iplot-1;  // Number of plots actually recorded

  //* Set the analytical solution.
  for ( j=1; j<=nplots; j++ ){
    for ( i=1; i<=N; i++ ){
      for ( int k=0; k<=0; k++){
        if ( k==0 ){
          alpha = C - D * k * k * M_PI * M_PI / L / L; 
          nnaplot(i,j) = nnaplot(i,j) + 1 / L *cos(k * M_PI / 2) * cos(k * M_PI / L * (xplot(i) + L/2)) * exp(alpha * tplot(j));
        }
        else{
        alpha = C - D * k * k * M_PI * M_PI / L / L;
        nnaplot(i,j) = nnaplot(i,j) + 2 / L *cos(k * M_PI / 2) * cos(k * M_PI / L * (xplot(i) + L/2)) * exp(alpha * tplot(j));
        }
      }
      nnaplot1(i,j) = 1 / L * exp(C * tplot(j));
    }
  }
  
  //* Print out the plotting variables: tplot, xplot, nnplot, nAve
  ofstream tplotOut("tplot.txt"), xplotOut("xplot.txt"), 
	       nnplotOut("nnplot.txt"), nAveOut("nAve.txt"), nnaplot1Out("nnaplot1.txt"), nnaplotOut("nnaplot.txt");
  for( i=1; i<=nplots; i++ ) { 
    tplotOut << tplot(i) << endl;
	nAveOut << nAve(i) << endl;
  }
  for( i=1; i<=N; i++ ) {
    xplotOut << xplot(i) << endl;
    for( j=1; j<nplots; j++ )
      nnplotOut << nnplot(i,j) << ", ";
    nnplotOut << nnplot(i,nplots) << endl;
    for( j=1; j<nplots; j++ )
      nnaplot1Out << nnaplot1(i,j) << ", ";
    nnaplot1Out << nnaplot1(i,nplots) << endl;
    for( j=1; j<nplots; j++ )
      nnaplotOut << nnaplot(i,j) << ", ";
    nnaplotOut << nnaplot(i,nplots) << endl;
  }
}
