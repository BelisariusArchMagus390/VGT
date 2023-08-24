import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# Links: https://www.youtube.com/watch?v=w5JhFN0CwOE
#        https://acervolima.com/o-que-o-atributo-tearoff-faz-em-um-menu-tkinter/

# Help
# pip freeze > requirements.txt
# pip install -r requirements.txt
# To do: fazer um script para atualizar de forma automática

file = Path(__file__).parent.joinpath("data").joinpath("cargas2011a2021.xlsx")
cargas_portos = pd.read_excel(file)

# years = cargas_portos["Ano"].drop_duplicates().to_list()

years = [2011]

harbors = ["Guaruja"]


