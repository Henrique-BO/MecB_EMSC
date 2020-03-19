import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constantes do problema
m = 10.0
k = 3553.0
c = 37.7
g = 9.81

# EDO: retorna a derivada do vetor de estados dy/dt em funcao do estado atual y e do tempo t
def massa_mola_amort(y, t, F, c):
    x, v = y # position and velocity
    force = F(t)
    dydt = [v, -k/m*x -c/m*v + force/m]
    return dydt

# Funcao que desenha os graficos necessarios
def draw_plots(sol, t, F, title):
    # x(t) * t
    plt.subplot(2, 2, 1)
    plt.plot(t, sol[:, 0], 'b')
    plt.xlabel('t (s)')
    plt.ylabel('x (m)')
    plt.grid()

    # v(t) * t
    plt.subplot(2, 2, 2)
    plt.plot(t, sol[:, 1], 'g')
    plt.xlabel('t (s)')
    plt.ylabel('v (m/s)')
    plt.grid()

    # x(t) * v(t)
    plt.subplot(2, 2, 3)
    plt.plot(sol[:, 1], sol[:, 0], 'r')
    plt.xlabel('v (m/s)')
    plt.ylabel('x (m)')
    plt.grid()

    # F(t) * t
    plt.subplot(2, 2, 4)
    plt.plot(t, [F(t0) for t0 in t], 'y')
    plt.xlabel('t (s)')
    plt.ylabel('F (N)')
    plt.grid()

    plt.suptitle(title)
    plt.show()

# F(t) = 0.0
def F_zero(t):
    return 0

### CASO A ###
# Condicoes iniciais
t = np.linspace(0, 3, 100)
x0 = 0.10
v0 = 0.0
F = F_zero
# Resolve a EDO
solA = odeint(massa_mola_amort, [x0, v0], t, args=(F, c))
# Graficos
draw_plots(solA, t, F, "Caso A")


### CASO B ###
# Condicoes iniciais
t = np.linspace(0, 3, 100)
x0 = 0.0
v0 = 1.0
F = F_zero
# Resolve a EDO
solB = odeint(massa_mola_amort, [x0, v0], t, args=(F, c))
# Graficos
draw_plots(solB, t, F, "Caso B")


### CASO C ###
# Condicoes iniciais
t = np.linspace(0, 3, 100)
x0 = 0.10
v0 = 1.0
F = F_zero
c = 377
# Resolve a EDO
solC = odeint(massa_mola_amort, [x0, v0], t, args=(F, c))
# Graficos
draw_plots(solC, t, F, "Caso C")


### CASO D ###
def F_D(t):
    F0 = 1000
    omega = np.pi
    theta = np.pi/2
    return F0*np.sin(omega*t + theta)
# Condicoes iniciais
t = np.linspace(0, 5, 100)
x0 = 0.0
v0 = 0.0
F = F_D
c = 37.7
# Resolve a EDO
solD = odeint(massa_mola_amort, [x0, v0], t, args=(F, c))
# Graficos
draw_plots(solD, t, F, "Caso D")


### CASO E ###
def F_E(t):
    return 1000 if t >= 0.5 else 0
# Condicoes iniciais
t = np.linspace(0, 5, 100)
x0 = 0.0
v0 = 0.0
F = F_E
c = 37.7
# Resolve a EDO
solE = odeint(massa_mola_amort, [x0, v0], t, args=(F, c))
# Graficos
draw_plots(solE, t, F, "Caso E")

#TODO: Analisar os graficos -- obter frequencias de oscilacao, interpretar resultado, apresentar equacoes (jupyter notebook provavelmente)