# Define o ambiente do poetry
VENV_NAME=.venv

# Criar o ambiente e instalar dependências
install:
	poetry install

# Rodar o Jupyter Notebook
notebook:
	poetry run jupyter notebook

# Ativar o shell do poetry
shell:
	poetry shell

# Rodar os testes (se tiver algum no futuro)
test:
	poetry run pytest

# Limpar o ambiente (opcional)
clean:
	rm -rf $(VENV_NAME)
