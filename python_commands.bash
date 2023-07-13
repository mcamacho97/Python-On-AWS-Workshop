# Create virtual environment
python -m venv env

# Activate virtual environment
source env/Scripts/activate
. env/Scripts/Activate.ps1 # for powershell

# Desactivate virtual environment
deactivate

# Install python packages
pip install boto3

# List python packages
pip freeze

# Remove python packages
pip uninstall boto3

# Creating a requirements.txt file
pip freeze > requirements.txt

# Install python packages
pip install -r requirements.txt