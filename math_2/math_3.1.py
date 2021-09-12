# polar coordinates to Cartesian coordinate system
import numpy as np

phi = float(input('Enter angular coordinate in degrees: '))
r = float(input('Enter radial coordinate by number: '))

def Polar_to_Cartesian(phi: float, r: float) -> list:
    # degrees to radian:
    phi = phi/180 * np.pi

    # convert coordinates to x, y
    x = (r * np.cos(phi)).round(4)
    y = (r * np.sin(phi)).round(4)
    return [x, y]

x, y = Polar_to_Cartesian(phi, r)
print(f'({r},{phi}) = ({x}, {y})')
