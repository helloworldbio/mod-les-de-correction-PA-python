#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:13:14 2024

@author: saraguinane
"""

# Fichiers CSV

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Chemins des fichiers CSV


purple_air_file = '/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ppl-TOUT-hourly_Nan_chrono_off.csv'
ref_file = '/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ref-hourly-TOUT_chrono_Nan_off.csv'



# Initialisation des listes pour stocker les données
dates = []
purple_air_concentrations = {'alt-a': [], 'alt-b': [], 'atm-a': [], 'atm-b': []}
ref_concentrations = []

# Lecture du fichier Purple Air
with open(purple_air_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')  # Colonne 1 (indice 0) pour les dates au format 'YYYY-MM-DD'
        purple_air_concentrations['alt-a'].append(float(row[1]))  # Colonne 2 (indice 1) pour alt-a
        purple_air_concentrations['alt-b'].append(float(row[2]))  # Colonne 3 (indice 2) pour alt-b
        purple_air_concentrations['atm-a'].append(float(row[3]))  # Colonne 4 (indice 3) pour atm-a
        purple_air_concentrations['atm-b'].append(float(row[4]))  # Colonne 5 (indice 4) pour atm-b
        dates.append(date)

# Lecture du fichier de référence
with open(ref_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header
    for row in reader:
        concentration = float(row[1])  # On suppose que la concentration est en colonne 2 (indice 1)
        ref_concentrations.append(concentration)

# Vérifier que les deux fichiers ont le même nombre de lignes
if len(dates) != len(ref_concentrations):
    raise ValueError("Les fichiers CSV ne contiennent pas le même nombre de lignes.")

# Création de la disposition des sous-graphiques
fig = plt.figure(figsize=(15, 10))
gs = fig.add_gridspec(2, 2)  # Une grille 2x2 pour 4 sous-graphiques

# Plot pour alt-a
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(dates, purple_air_concentrations['alt-a'], label='alt-a', color='purple')
ax1.plot(dates, ref_concentrations, label='Référence', color='blue')
ax1.set_title('alt-a')
ax1.set_xlabel('Date')
ax1.set_ylabel('Concentration')
ax1.legend()
ax1.grid(True)
plt.xticks(rotation=45)

# Plot pour alt-b
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(dates, purple_air_concentrations['alt-b'], label='alt-b', color='purple')
ax2.plot(dates, ref_concentrations, label='Référence', color='blue')
ax2.set_title('alt-b')
ax2.set_xlabel('Date')
ax2.set_ylabel('Concentration')
ax2.legend()
ax2.grid(True)
plt.xticks(rotation=45)

# Plot pour atm-a
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(dates, purple_air_concentrations['atm-a'], label='atm-a', color='purple')
ax3.plot(dates, ref_concentrations, label='Référence', color='blue')
ax3.set_title('atm-a')
ax3.set_xlabel('Date')
ax3.set_ylabel('Concentration')
ax3.legend()
ax3.grid(True)
plt.xticks(rotation=45)

# Plot pour atm-b
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(dates, purple_air_concentrations['atm-b'], label='atm-b', color='purple')
ax4.plot(dates, ref_concentrations, label='Référence', color='blue')
ax4.set_title('atm-b')
ax4.set_xlabel('Date')
ax4.set_ylabel('Concentration')
ax4.legend()
ax4.grid(True)
plt.xticks(rotation=45)

# Ajustement de la disposition et affichage
plt.tight_layout()
plt.show()
