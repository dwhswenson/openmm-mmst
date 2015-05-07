from simtk.openmm.opemm import CustomIntegrator

class MMSTIntegrator(CustomIntegrator):
    """Integrator for an MMST trajectory.

    Attributes
    ----------
    stepSize : float
    Hmatrix : list of list of System
    """
    def __init__(self, stepSize, Hmatrix):
        pass

class VerletMMSTIntegrator(MMSTIntegrator):
    # Exists mainly for testing
    def step(self, nsteps):
        pass

class RungeKuttaMMSTIntegrator(MMSTIntegrator):
    def step(self, nsteps):
        pass

# TODO
class AdaptiveGear6MMSTIntegrator(MMSTIntegrator):
    # see DWHS's dissertation for the discussion of this
    pass
