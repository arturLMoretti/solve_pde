import numpy as np

def heat_equation_1d(u0, alpha, dx, dt, t_max):
    u = u0.copy()
    u_new = u0.copy()
    n_steps = int(t_max / dt)

    r = alpha * dt / dx**2
    if r > 0.5:
        raise ValueError("Estável apenas para r <= 0.5.")

    for _ in range(n_steps):
        u_new[1:-1] = u[1:-1] + r * (u[2:] - 2*u[1:-1] + u[:-2])
        u[:] = u_new[:]

    return u
