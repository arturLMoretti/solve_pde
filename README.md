# PDE Solver

## Descrição
Pacote em Python para resolução de Equações Diferenciais Parciais (EDPs) utilizando o método de Diferenças Finitas.

---

## Funcionalidades
- Solução de EDPs 1D
- Implementação do método de diferenças finitas explícito
- Funções auxiliares para condições iniciais e de contorno
- Visualização dos resultados com gráficos


## Instalação

1. Clone o repositório:
  ```bash
    git clone https://github.com/seu_usuario/pde-solver.git
    cd pde-solver
    make install
    ```

## Como usar

Exemplo de uso para resolver a equação do calor 1D:

```python
import numpy as np
from pde_solver.fdm import heat_equation_1d
from pde_solver.conditions import initial_condition_sin
from pde_solver.plotter import plot_solution

# Definição do domínio
L = 1.0
nx = 51
dx = L / (nx - 1)
x = np.linspace(0, L, nx)

# Definição dos parâmetros
alpha = 0.01
dt = 0.0005
t_max = 0.1

# Condição inicial
u0 = initial_condition_sin(x)

# Solução numérica
u_final = heat_equation_1d(u0, alpha, dx, dt, t_max)

# Visualização
plot_solution(x, u0, u_final, t_max)

```

## Documentação
Fórmulas Utilizadas: Método de diferenças finitas explícito para a equação do calor 1D

Estabilidade: O passo de tempo dt deve satisfazer a condição de estabilidade de Fourier (Fo <= 0.5)

## Contribuição

Pull requests são bem-vindos. Para mudanças maiores, abra uma issue para discutirmos o que você gostaria de modificar.

## Licença

MIT License
