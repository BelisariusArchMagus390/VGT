class Cluster:
    def __init__(self):
        self.data = [
            ["Maceio", "Coari", "Itacoatiara"],
            ["Manaus", "Santana"],
            ["Ladario", "Porto Murtinho", "Almeirim"],
            ["Itapoa", "Navegantes", "Sao Francisco do Sul", "Aracaju"],
            ["Vitoria do Xingu", "Caracarai", "Humaita", "Maragogipe", "Sao Simao"],
        ]

        """self.data = [
            ["Duque de Caxias", "Itaguai", "Mangaratiba", "Niteroi"],
            ["Vila Velha", "Vitoria"],
            ["Pontal do Parana", "Sao Joao da Barra", "Sao Simao", "Pederneiras"],
        ]"""

    def get_data(self):
        return self.data
