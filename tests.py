import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# Links: https://www.youtube.com/watch?v=w5JhFN0CwOE
#        https://acervolima.com/o-que-o-atributo-tearoff-faz-em-um-menu-tkinter/
#        https://python-graph-gallery.com/182-vertical-lollipop-plot/

# Help
# pip freeze > requirements.txt
# pip install -r requirements.txt
# To do: fazer um script para atualizar de forma automática

file = Path(__file__).parent.joinpath("data").joinpath("cargas2011a2021.xlsx")
cargas_portos = pd.read_excel(file)

# years = cargas_portos["Ano"].drop_duplicates().to_list()

years = [2015]

harbors = ["Guaruja", "Maceio", "Manaus", "Candeias"]

cargas_portos_filtered = cargas_portos.loc[cargas_portos["Porto"].isin(harbors)]
cargas_portos_filtered = cargas_portos_filtered.loc[cargas_portos["Ano"].isin(years)]

harbor_names = cargas_portos_filtered["Porto"].drop_duplicates().to_list()
harbor_range = range(1, len(harbor_names))

option_column = "ValorKgCarga"

agregated_values = pd.DataFrame(columns=["Porto", option_column])

for harbor in harbor_names:
    value_column = cargas_portos_filtered.loc[cargas_portos_filtered["Porto"] == harbor].ValorKgCarga.sum()
    agregated_values.loc[len(agregated_values.index)] = [harbor, value_column]

agregated_values_ordered = agregated_values.sort_values(by="ValorKgCarga")

plt.hlines(y=harbor_range, xmin=0, xmax=agregated_values_ordered["ValorKgCarga"], color="skyblue")
plt.plot(agregated_values_ordered["ValorKgCarga"], harbor_range, "o")

plt.yticks(harbor_range, agregated_values_ordered["Porto"])
plt.title("A vertical lolipop plot", loc="left")
plt.xlabel("value of the variable")
plt.ylabel("Ports")

plt.show()
    


