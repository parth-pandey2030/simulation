from scipy.constants import speed_of_light, G, pi 
from divergenceAndCurl import *
class Gravity:
    """
    Einstien field equation
    Ruv - 1/2Rguv = 8piG/c^4Tuv
    """
    k = (8 * pi * G) / (speed_of_light ** 4)
    def __init__(self, spacetime):
        self.spacetime = spacetime
        
    def calculate_metric_tensor(self):
        pass

class Electromagnetism:
    """
    Maxwell's equations
    ∇*E = ρ/𝜀0
    ∇
    ∇
    ∇
    ∇
    """



