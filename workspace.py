from EnMcalc import *

ca = cap_area_r(area=10, r=(10*10**-3))
cb = cap_area_r(area=10, r=(5*10**-3))

# print(ceq_parallel_2cs(ca, cb))

q = ceq_parallel_2cs(ca, cb)

va = pot_diff_cap(q, ca)
vb = pot_diff_cap(q, cb)
ua = pot_energy_cap(q, va)
ub = pot_energy_cap(q, vb)
print(ua + ub)