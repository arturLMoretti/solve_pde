PDE Solver
Este projeto oferece uma implementação simples de métodos numéricos para resolver equações diferenciais parciais (EDPs). O foco inicial é a solução da equação do calor unidimensional utilizando o método de diferenças finitas explícitas.

💡 Funcionalidades
Resolução numérica da equação do calor 1D usando o método de diferenças finitas.

Condições iniciais configuráveis, incluindo uma onda senoidal e uma distribuição gaussiana.

Visualização das soluções com gráficos utilizando matplotlib.

Configuração fácil com o gerenciador de dependências Poetry.

🚀 Instruções de Uso
Requisitos
Antes de começar, você precisará do Python 3.8+ e do Poetry instalado. Caso não tenha o Poetry, você pode instalá-lo aqui.

Instalação
Clone o repositório:

bash
Copy
Edit
git clone https://github.com/usuario/pde_solver.git
cd pde_solver
Instale as dependências usando o Poetry:

bash
Copy
Edit
poetry install
Ative o ambiente virtual:

bash
Copy
Edit
poetry shell
Rodar o Jupyter Notebook:

bash
Copy
Edit
make notebook
Ou, se preferir, abra o arquivo main.py diretamente.

Exemplo de Uso
No Jupyter Notebook ou no script Python, você pode usar o seguinte código para rodar a solução da equação do calor:

python
Copy
Edit
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
🧪 Testes
Para rodar os testes do projeto (se houver), use:

bash
Copy
Edit
make test
📂 Estrutura do Projeto
bash
Copy
Edit
pde_solver/
├── pde_solver/
│   ├── __init__.py
│   ├── fdm.py
│   ├── conditions.py
│   ├── plotter.py
├── main.py
├── Makefile
├── pyproject.toml
pde_solver/: Contém os módulos principais para a resolução da EDP.

main.py: Arquivo principal para rodar a simulação.

Makefile: Automatiza tarefas como instalar dependências e rodar o Jupyter.

pyproject.toml: Arquivo de configuração do Poetry.

📚 Tecnologias
Python 3.x

NumPy: Para manipulação de arrays e cálculo numérico.

Matplotlib: Para visualização gráfica dos resultados.

Poetry: Para gerenciamento de dependências e ambiente.

Jupyter Notebook: Para interação e visualização durante o desenvolvimento.

🔧 Como Contribuir
Fork o repositório.

Crie uma branch com suas mudanças (git checkout -b feature/your-feature).

Faça o commit das suas alterações (git commit -m 'Adicionando nova funcionalidade').

Faça o push para sua branch (git push origin feature/your-feature).

Abra um Pull Request.

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais informações.

📋 Dicas para modificar ou expandir:
Você pode facilmente adicionar novos métodos de solução de EDPs (como Crank-Nicolson) ou outras equações (como equações de ondas).

Também pode configurar diferentes tipos de condições iniciais ou de contorno.