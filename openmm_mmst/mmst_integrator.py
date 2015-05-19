from simtk.openmm.openmm import CustomIntegrator

class NonadiabaticIntegrator(CustomIntegrator):
    """Integrator for an MMST trajectory.

    Attributes
    ----------
    stepSize : float
    Hmatrix : list of list of System
    """
    def __init__(self, stepSize, Hmatrix):
        self.Hmatrix = Hmatrix
        pass

class VerletMMSTIntegrator(NonadiabaticIntegrator):
    # Exists mainly for testing
    def step(self, nsteps):
        pass

class RungeKuttaMMSTIntegrator(NonadiabaticIntegrator):
    def step(self, nsteps):
        pass

# TODO
class AdaptiveGear6MMSTIntegrator(NonadiabaticIntegrator):
    # see DWHS's dissertation for the discussion of this
    pass

# TODO: actually, this isn't MMST specific: same setup should be usable for
# surface hopping. But I'll save that for (much) later.
