from scipy.constants import speed_of_light, G, pi, pico, micro
from divergenceAndCurl import *
from sympy import symbols, diff

class Gravity:
    """
    Einstien field equation
    Ruv - 1/2Rguv = 8piG/c^4Tuv
    """


    def __init__(self, spacetime):
        self.spacetime = spacetime
        self.k = (8 * pi * G) / (speed_of_light ** 4) # Einstien Gravitational Constant
    def calculate_metric_tensor(self):
        pass

class Electromagnetism:
    """
    Maxwell's equations
    ∇·E = ρ/𝜀0
    ∇·B = 0
    ∇×E = -∂B/∂t
    ∇×B = μ0(J+𝜀0∂E/∂t)
    """

    def __init__(self, electric_field, magnetic_field, charge_of_surface, volume_of_surface, velocity_of_charges, operation):
        self.electric = electric_field
        self.magnetic = magnetic_field
        self.charge = charge_of_surface
        self.volume = volume_of_surface
        self.velocity = velocity_of_charges
        self.op = operation
        return self.calculate()

    def calculate(self):
        𝜀0 = 8.8541878128(13) * pico # Vacuum Permittivity
        μ0 = 1.25663706212(19) * micro # Magnetic Constant
        ρ = self.charge / self.volume # Electric Charge Density
        j = ρ * self.velocity # Current Density

        if self.op == div(self.electric):
            return ρ / 𝜀0
        elif self.op == div(self.magnetic):
            return 0
        elif self.op == curl(self.electric):
            return -(diff(self.magnetic, symbols('t')))
        elif self.op == curl(self.magnetic):
            return μ0 * (j + 𝜀0 * diff(self.electric, symbols('t')))
        
        





