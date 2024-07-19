#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:32:29 2024

@author: saraguinane
"""

import pandas as pd

# Lire le fichier CSV
df = pd.read_csv('/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ppl-TOUT-hourly.csv')

# Supprimer les lignes avec des valeurs manquantes dans les colonnes spécifiées
df.dropna(subset=['time_stamp', 'pm2.5_alt_a', 'pm2.5_alt_b', 'pm2.5_atm_a', 'pm2.5_atm_b', 'temperature'], inplace=True)

# Écrire le dataframe nettoyé dans un nouveau fichier CSV
df.to_csv('/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ppl-TOUT-hourly_Nan.csv', index=False)
