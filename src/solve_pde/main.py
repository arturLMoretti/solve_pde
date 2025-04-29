import numpy as np
from src.solve_pde.pde_solver.fdm import heat_equation_1d
from src.solve_pde.pde_solver.conditions import initial_condition_sin, initial_condition_gaussian
from src.solve_pde.pde_solver.plotter import plot_solution

# Domínio
L = 1.0
nx = 51
dx = L / (nx - 1)
x = np.linspace(0, L, nx)

# Parâmetros
alpha = 0.01
dt = 0.0005
t_max = 0.1

# Escolher condição inicial
u0 = initial_condition_gaussian(x, center=0.5, width=0.1)
# ou: u0 = initial_condition_sin(x)

# Resolver
u_final = heat_equation_1d(u0, alpha, dx, dt, t_max)

# Plotar
plot_solution(x, u0, u_final, t_max)
