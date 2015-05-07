# openmm-mmst

Tools to use the Meyer-Miller-Stock-Thoss (mapped electron) Hamiltonian in
OpenMM.

*PRE-RELEASE: No guarantee that anything in this works at all.*

The implementation here is as a Python-based OpenMM `CustomIntegrator`.
Several specific integration schemes will be implemented, including leapfrog
Verlet, 4th order Runge-Kutta, and adaptive 6th order Gear.


### About the MMST Hamiltonian

* [H.D. Meyer and W.H. Miller. JCP **70**, 3214
  (1979)](http://dx.doi.org/10.1063/1.437910): Original paper, a bit hard to
  read.
* [G. Stock and M. Thoss. PRL **78**, 578
  (1997)](http://dx.doi.org/10.1103/PhysRevLett.78.578): Clear derivation
  by Stock and Thoss.
* [N. Ananth, C. Venkataraman, and W.H. Miller. JCP, **127**, 084114
  (2007)](http://dx.doi.org/10.1063/1.2759932): Differences in what can be
  captured by including various levels of quantum effects with MMST-based
  dynamics.
* [A. Gosolov and D. Reichman. JCP **114**, 1065
  (2001)](http://dx.doi.org/10.1063/1.1332812): Interesting work covering a
  few practical approaches to the MMST Hamiltonian.
* [S. Bonella and D. Coker. JCP **122**, 194102
  (2005)](http://dx.doi.org/10.1063/1.1896948): A practical way to use the
  MMST for larger systems.

### About OpenMM

* [OpenMM website](http://www.openmm.org/)
