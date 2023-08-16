import pandas as pd
from pathlib import Path

# Help
# pip freeze > requirements.txt
# pip install -r requirements.txt
# To do: fazer um script para atualizar de forma automática

file = Path(__file__).parent.joinpath("data").joinpath("cargas2011a2021.xlsx")

cargas_portos = pd.read_excel(file)

display(cargas_portos)