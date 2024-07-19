#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:50:56 2024

@author: saraguinane
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec
import csv

def lire_concentrations_de_csv_ref(C_ref):
    concentrations_ref = []
    with open(C_ref, newline='') as csvfile:
        lecteur = csv.reader(csvfile)
        next(lecteur)  # Skip the header if exists
        for ligne in lecteur:
            concentration = float(ligne[1])  # Assuming the second column contains concentrations
            concentrations_ref.append(concentration)
    return concentrations_ref

def lire_fichier_csv(C_ppl):
    alt_a_concentrations = []
    temperatures_celsius = []
    with open(C_ppl, newline='') as csvfile:
        lecteur = csv.reader(csvfile)
        next(lecteur)  # Skip the header if exists
        for ligne in lecteur:
            alt_a_concentrations.append(float(ligne[3]))  # Example: Second column for concentrations
            temperature_fahrenheit = float(ligne[5])  # Example: Sixth column for Fahrenheit temperature
            temperature_celsius = (temperature_fahrenheit - 32) * 5.0/9.0
            temperatures_celsius.append(temperature_celsius)
    return alt_a_concentrations, temperatures_celsius

# Example paths to CSV files (replace with your actual paths)
C_ppl = '/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ppl-TOUT-hourly_Nan_chrono_off.csv'
C_ref = '/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ref-hourly-TOUT_chrono_Nan_off.csv'


# Read concentrations and temperatures from CSV files
concentrations_ref = lire_concentrations_de_csv_ref(C_ref)
alt_a_concentrations, temperatures_celsius = lire_fichier_csv(C_ppl)

# Convert lists to numpy arrays for ease of use with numpy functions
ref = np.array(concentrations_ref)
ppl = np.array(alt_a_concentrations)
temperature = np.array(temperatures_celsius)

# Filtrer les données pour les températures >= -10°C
seuil=-10
coeff = 1.2
mask_high = temperature >= seuil
ref_filtre_h = ref[mask_high]
ppl_filtre_h = ppl[mask_high] * coeff
temperature_filtre_h = temperature[mask_high]

# Filtrer les données pour les températures < -10°C
mask_low = temperature < seuil
ref_filtre_b = ref[mask_low]
ppl_filtre_b = ppl[mask_low] * coeff * (-0.1 * temperature[mask_low])
temperature_filtre_b = temperature[mask_low]

# Combine the filtered data
ref_filtre = np.concatenate((ref_filtre_b, ref_filtre_h))
ppl_filtre = np.concatenate((ppl_filtre_b, ppl_filtre_h))
temperature_filtre = np.concatenate((temperature_filtre_b, temperature_filtre_h))

# Régression linéaire sur les données filtrées
pente, ordonnee = np.polyfit(ref_filtre, ppl_filtre, 1)
print("PENTE =", pente)
print("ORDONNEE A L'ORIGINE =", ordonnee)

# Calcul du coefficient de détermination R²
corr_matrix = np.corrcoef(ref_filtre, ppl_filtre)
corr = corr_matrix[0, 1]
R_sq = corr**2
print("COEFFICIENT DE DÉTERMINATION (R²) =", R_sq)

# Calcul du coefficient de détermination R²
corr_matrix = np.corrcoef(ref, ppl)
corr = corr_matrix[0, 1]
R_sq = corr**2
print("COEFFICIENT DE DÉTERMINATION origine(R²) =", R_sq)



# Création de la figure
fig = plt.figure(figsize=(6, 9))
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1])

# Tracé des points de mesure avec les cercles colorés en fonction de la température
ax0 = plt.subplot(gs[0])
sc = ax0.scatter(ref_filtre, ppl_filtre, c=temperature_filtre, cmap='coolwarm', edgecolor='k')
ax0.plot(ref_filtre, ordonnee + pente * ref_filtre, 'r', label='Régression linéaire')
ax0.legend()
plt.colorbar(sc, ax=ax0, label='Température (°C)')

# Tracé des résidus
ax1 = plt.subplot(gs[1])
sc = ax1.scatter(ref_filtre, ppl_filtre - (ordonnee + pente * ref_filtre), c=temperature_filtre, cmap='coolwarm', edgecolor='k')
ax1.set_title("Résidus (écarts entre les points et la modélisation affine)")
ax1.set_ylabel('ppl - ppl_modèle')
ax1.set_xlabel('ref')
ax1.plot((np.min(ref_filtre), np.max(ref_filtre)), (0, 0), color='red')  # Trace l’horizontale y = 0
plt.colorbar(sc, ax=ax1, label='Température (°C)')

plt.tight_layout()
plt.show()
