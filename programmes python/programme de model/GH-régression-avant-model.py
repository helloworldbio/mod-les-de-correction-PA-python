#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:36:20 2024

@author: saraguinane
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:15:11 2024

@author: saraguinane
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec
import csv

def lire_concentrations_de_csv_ref(C_ref):
    concentrations_ref = []
    for file in C_ref:
        with open(file, newline='') as csvfile:
            lecteur = csv.reader(csvfile)
            next(lecteur)  # Skip the header if exists
            for ligne in lecteur:
                concentration = float(ligne[1])  # Assuming the second column contains concentrations
                concentrations_ref.append(concentration)
    return concentrations_ref

def lire_fichier_csv(C_ppl):
    alt_a_concentrations = []
    temperatures_celsius = []
    for file in C_ppl:
        with open(file, newline='') as csvfile:
            lecteur = csv.reader(csvfile)
            next(lecteur)  # Skip the header if exists
            for ligne in lecteur:
                alt_a_concentrations.append(float(ligne[4]))  # Example: Fourth column for concentrations
                temperature_fahrenheit = float(ligne[5])  # Example: Sixth column for Fahrenheit temperature
                temperature_celsius = (temperature_fahrenheit - 32) * 5.0/9.0
                temperatures_celsius.append(temperature_celsius)
    return alt_a_concentrations, temperatures_celsius

# Chemins des fichiers CSV
purple_air_file_2019 = '/Users/saraguinane/Documents/administratif/stage recherche/starter-pack/TOUT/ppl_2019_hourly_Nan_off_sorted_bis.csv'
ref_file_2019 = '/Users/saraguinane/Documents/administratif/stage recherche/starter-pack/TOUT/ref_2019_hourly_Nan_off_sorted_bis.csv'
purple_air_file_2020 = '/Users/saraguinane/Documents/administratif/stage recherche/starter-pack/TOUT/purple_filtered_hour_2020_Nan_off.csv'
ref_file_2020 = '/Users/saraguinane/Documents/administratif/stage recherche/starter-pack/TOUT/ref_filtered_hour_2020_Nan_off.csv'
purple_air_file_2021 = '/Users/saraguinane/Documents/administratif/stage recherche/starter-pack/TOUT/ppl_2021_hourly_Nan_off_sorted_bis.csv'
ref_file_2021 = '/Users/saraguinane/Documents/administratif/stage recherche/starter-pack/TOUT/ref_2021_hourly_Nan_off_sorted_bis.csv'
purple_air_file_2022 = '/Users/saraguinane/Documents/administratif/stage recherche/starter-pack/TOUT/24691_2022_Nan_off_filtr.csv'
ref_file_2022 = '/Users/saraguinane/Documents/administratif/stage recherche/starter-pack/TOUT/datetime_PMval_2022_ref_br_Nan_off_filtr.csv'
purple_air_file_2023 = '/Users/saraguinane/Documents/administratif/stage recherche/starter-pack/TOUT/ppl_2023_hourly_Nan_off_sorted_bis.csv'
ref_file_2023 = '/Users/saraguinane/Documents/administratif/stage recherche/starter-pack/TOUT/ref_2023_hourly_Nan_off_sorted_bis.csv'

# Concaténation des chemins de fichiers dans des listes
C_ppl = [
    purple_air_file_2019, purple_air_file_2020, purple_air_file_2021,
    purple_air_file_2022, purple_air_file_2023
]

C_ref = [
    ref_file_2019, ref_file_2020, ref_file_2021,
    ref_file_2022, ref_file_2023
]

# Lecture des concentrations et des températures à partir des fichiers CSV
concentrations_ref = lire_concentrations_de_csv_ref(C_ref)
alt_a_concentrations, temperatures_celsius = lire_fichier_csv(C_ppl)

# Conversion des listes en tableaux numpy pour faciliter leur manipulation avec les fonctions numpy
ref_filtre = np.array(concentrations_ref)
ppl_filtre = np.array(alt_a_concentrations)
temperature_filtre = np.array(temperatures_celsius)



# Régression linéaire sur les données filtrées
pente, ordonnee = np.polyfit(ref_filtre, ppl_filtre, 1)
print("PENTE =", pente)
print("ORDONNÉE À L'ORIGINE =", ordonnee)

# Calcul du coefficient de détermination R²
corr_matrix = np.corrcoef(ref_filtre, ppl_filtre)
corr = corr_matrix[0, 1]
R_sq = corr**2
print("COEFFICIENT DE DÉTERMINATION (R²) =", R_sq)



# Création de la figure avec deux sous-graphiques
fig = plt.figure(figsize=(8, 12))
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1])  # 2 lignes, la première avec un rapport de hauteur de 2, la seconde avec 1

# Premier sous-graphique : Scatter plot avec régression linéaire
ax0 = plt.subplot(gs[0])
sc = ax0.scatter(ref_filtre, ppl_filtre, c=temperature_filtre, cmap='coolwarm', edgecolor='k')
ax0.plot(ref_filtre, ordonnee + pente * ref_filtre, 'r', label='Régression linéaire')
ax0.legend()
plt.colorbar(sc, ax=ax0, label='Température (°C)')
ax0.set_xlabel('Concentration de référence')
ax0.set_ylabel('Concentration Purple Air')
ax0.set_title('Régression linéaire entre Concentrations de référence et Purple Air')

# Deuxième sous-graphique : Scatter plot des résidus
ax1 = plt.subplot(gs[1])
sc = ax1.scatter(ref_filtre, ppl_filtre - (ordonnee + pente * ref_filtre), c=temperature_filtre, cmap='coolwarm', edgecolor='k')
ax1.set_title("Résidus (écarts entre les points et la modélisation affine)")
ax1.set_ylabel('ppl - ppl_modèle')
ax1.set_xlabel('ref')
ax1.plot((np.min(ref_filtre), np.max(ref_filtre)), (0, 0), color='red')  # Trace l’horizontale y = 0
plt.colorbar(sc, ax=ax1, label='Température (°C)')

# Ajustement de la disposition des sous-graphiques
plt.tight_layout()
plt.show()
