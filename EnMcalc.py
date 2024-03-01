from math import cos, pi
from sympy import integrate, symbols
epsilon_0 = (8.8542*10**-12)
k = 1 / (4 * pi * epsilon_0)

def flux_sheet(theta, e_field, x, y):
    area = x * y 
    rad = theta * (pi / 180)
    return abs(e_field) * abs(area) * cos(rad)


def elec_field(r, q):
    return (k * q) / (r**2)


def elec_force(q_2, r, q_1):
    return q_1*elec_field(q_2, r)


def pot_diff_q(q, r):
    return (k*(q / r))


def pot_diff_e(e, r1, r2):
    e, r = symbols('e r')
    e = 1/r**2
    r1, r2 = symbols('r1 r2')
    return integrate(e, (r, r1, r2))

def pot_diff_cap(q, c):
    return q / c


def cap_area_r(area, r):
    return (area * epsilon_0) / r


def ceq_parallel_2cs(c_1, c_2):
    return 1 / ( (1/c_1) + (1/c_2))


def pot_energy_cap(q, v):
    return 0.5*(q*v)