import numpy as np
from pde_solver.fdm import heat_equation_1d
from pde_solver.conditions import initial_condition_sin
from pde_solver.plotter import plot_solution

# Configuração do domínio
L = 1.0
nx = 51
dx = L / (nx - 1)
x = np.linspace(0, L, nx)

# Parâmetros físicos
alpha = 0.01
dt = 0.0005
t_max = 0.1

# Condição inicial
u0 = initial_condition_sin(x)

# Resolução
u_final = heat_equation_1d(u0, alpha, dx, dt, t_max)

# Gráfico
plot_solution(x, u0, u_final, t_max)
