#!make

# Installation and configuration commands for macOS
brew:
	brew update
	brew install pyenv postgresql@15 pgvector
	echo "All Homebebrew packages installed."

# Setup Python environment for macOS
python:
	@pyenv install $(PYTHON_VERSION)
	@pyenv local $(PYTHON_VERSION)
	@echo "Python $(PYTHON_VERSION) installed and set locally."

# Create the virtual environment for macOS
venv:
	@python3 -m venv .venv
	@echo "Virtual environment '.venv' created."

# Install Python requirements in the virtual environment for macOS
reqs:
	@source .venv/bin/activate && python -m pip install --upgrade pip setuptools wheel
	@source .venv/bin/activate && python -m pip install -r requirements.txt
	@echo "Virtual environment successfully created with requirements installed"

all:
	@make venv
	@make reqs