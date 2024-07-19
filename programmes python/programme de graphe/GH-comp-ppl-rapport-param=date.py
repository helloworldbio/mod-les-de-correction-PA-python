#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:17:57 2024

@author: saraguinane
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:18:31 2024

@author: saraguinane
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

#%% Importation des fichiers

# Fichiers CSV
ref_file = '/Users/saraguinane/Documents/administratif/stage recherche/annuel/ref_filtered_hour_2020_Nan_off.csv'
purple_air_file = '/Users/saraguinane/Documents/administratif/stage recherche/annuel/purple_filtered_hour_2020_Nan_off.csv'

# Initialisation des listes pour stocker les données
dates = []
purple_air_concentrations = []
ref_concentrations = []
temperatures = []

# Lecture du fichier Purple Air
with open(purple_air_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')  # Adapted date format
        concentration = float(row[4])
        temperature_fahrenheit = float(row[5])  # Assuming temperature is in the sixth column
        temperature_celsius = (temperature_fahrenheit - 32) * 5/9  # Convert °F to °C
        dates.append(date)
        purple_air_concentrations.append(concentration)
        temperatures.append(temperature_celsius)

# Lecture du fichier de référence
with open(ref_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header
    for row in reader:
        concentration = float(row[1])
        ref_concentrations.append(concentration)

# Vérifier que les deux fichiers ont le même nombre de lignes
if len(dates) != len(ref_concentrations):
    raise ValueError("Les fichiers CSV ne contiennent pas le même nombre de lignes.")

# Calcul du rapport des concentrations
rapport_concentrations = [ref / ppl if ppl != 0 else None for ref, ppl in zip(ref_concentrations, purple_air_concentrations)]

# Filtrer les None values (si nécessaire)
filtered_rapport_concentrations = [r for r in rapport_concentrations if r is not None]
filtered_temperatures = [temp for r, temp in zip(rapport_concentrations, temperatures) if r is not None]
filtered_dates = [date for r, date in zip(rapport_concentrations, dates) if r is not None]

# Convertir les dates en échelle numérique
numeric_dates = [date.timestamp() for date in filtered_dates]

#%% Tracé graphique du rapport en fonction de la température

# Tracé des données
plt.figure(figsize=(10, 5))
scatter = plt.scatter(filtered_temperatures, filtered_rapport_concentrations, 
                      c=numeric_dates, cmap='Spectral', label='Rapport Ref/Purple Air')
plt.xlabel('Température (°C)')
plt.ylabel('Rapport Concentration Ref/Concentration Purple Air')
plt.title('Rapport des concentrations en fonction de la température')
plt.grid(True)

# Ajouter une barre colorée avec les dates
cbar = plt.colorbar(scatter, label='Date')
cbar.ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: datetime.fromtimestamp(x).strftime('%Y-%m-%d')))

plt.tight_layout()

# Afficher le graphe
plt.show()
