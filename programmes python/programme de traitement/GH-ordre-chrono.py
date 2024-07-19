#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:44:33 2024

@author: saraguinane
"""

import pandas as pd

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv('/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ppl-TOUT-hourly_Nan.csv')

# Convertir la colonne 'time_stamp' en datetime avec le format spécifié
df['time_stamp'] = pd.to_datetime(df['time_stamp'], format='%Y-%m-%dT%H:%M:%SZ')

# Trier les lignes par ordre chronologique des dates
df.sort_values(by='time_stamp', inplace=True)

# Écrire le DataFrame trié dans un nouveau fichier CSV
df.to_csv('/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ppl-TOUT-hourly_Nan_chrono.csv', index=False)

