import matplotlib.pyplot as plt

def plot_solution(x, u0, u_final, t_max, title='Equação do Calor 1D'):
    plt.plot(x, u0, label='t=0')
    plt.plot(x, u_final, label=f't={t_max}')
    plt.xlabel('x')
    plt.ylabel('u')
    plt.legend()
    plt.title(title)
    plt.grid(True)
    plt.savefig(f"{title}.png")
