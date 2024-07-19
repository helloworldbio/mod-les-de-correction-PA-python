#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:15:04 2024

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
import matplotlib.colors as mcolors

#%%importation des fichiers

# Fichiers CSV
ref_file = '/Users/saraguinane/Documents/administratif/stage recherche/annuel/ref_filtered_TOUT.csv'
purple_air_file = '/Users/saraguinane/Documents/administratif/stage recherche/annuel/purple_filtered_TOUT.csv'

# Initialisation des listes pour stocker les données
dates = []
purple_air_concentrations = []
ref_concentrations = []
temperatures = []

# Lecture du fichier Purple Air
# Lecture du fichier Purple Air
with open(purple_air_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')  # Adapted date format
        concentration = float(row[4])  # Read concentration from the 5th column
        temperature_fahrenheit = float(row[5])  # Assuming temperature is in the 6th column
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
filtered_ref_concentrations = [ref for ref, r in zip(ref_concentrations, rapport_concentrations) if r is not None]

# Créer une colormap personnalisée basée sur 'Purples' mais évitant les teintes trop claires
purples = plt.cm.Purples(np.linspace(0.3, 1, 256))  # Ajuster la plage pour éviter les teintes trop claires
custom_purples = mcolors.LinearSegmentedColormap.from_list('custom_purples', purples)

#%%tracé graphique du rapport en fonction de la température

# Tracé des données
plt.figure(figsize=(10, 5))
scatter = plt.scatter(filtered_temperatures, filtered_rapport_concentrations, 
                      c=filtered_ref_concentrations, cmap='Spectral', label='Rapport Ref/Purple Air')
plt.xlabel('Température (°C)')
plt.ylabel('Rapport Concentration Ref/Concentration Purple Air')
plt.title('Rapport des concentrations en fonction de la température')
plt.grid(True)
cbar = plt.colorbar(scatter)
cbar.set_label('Concentration de Référence')
plt.tight_layout()

# Afficher le graphe
plt.show()
