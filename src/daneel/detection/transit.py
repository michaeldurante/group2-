import batman, numpy as np
import matplotlib.pyplot as plt

p = batman.TransitParams()
p.t0 = 0.0 # relative time, days
p.per = 1.27492504 # orbital period, days
p.rp = 0.12252744516353857 # Rp / Rstar
p.a = 3.784036086440643 # a / Rstar
p.inc = 88.49 # degrees
p.ecc = 0.0085; p.w = 88.95
p.limb_dark = "quadratic"
p.u = [0.086066667, 0.1542]
t = np.linspace(-0.075, 0.075, 1000)
flux = batman.TransitModel(p,t).light_curve(p)

plt.plot(t,flux)
plt.xlabel('prova')
# plt.show()

plt.savefig("WASP-121b_assignment1_taskF.png")