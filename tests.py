import pandas as pd
from pathlib import Path
from IPython.display import display

# Links: https://www.youtube.com/watch?v=w5JhFN0CwOE
#        https://acervolima.com/o-que-o-atributo-tearoff-faz-em-um-menu-tkinter/

# Help
# pip freeze > requirements.txt
# pip install -r requirements.txt
# To do: fazer um script para atualizar de forma automática

file = Path(__file__).parent.joinpath("data").joinpath("cargas2011a2021.xlsx")
cargas_portos = pd.read_excel(file)

years = cargas_portos["Ano"].drop_duplicates().to_list()

# years = [2011]

harbors = ["Guaruja"]

print(type(years[0]))

# cargas_portos_year = cargas_portos.loc[(cargas_portos["Ano"].isin(years))]

# cargas_portos_year = cargas_portos_year.loc[(cargas_portos["Porto"].isin(harbors))]

# cargas_portos_filtered = cargas_portos_year.to_numpy().tolist()
