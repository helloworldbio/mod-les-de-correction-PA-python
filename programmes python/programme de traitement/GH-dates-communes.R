import pandas as pd
import csv

# lecture les fichiers CSV
df_purple = pd.read_csv('/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ppl-TOUT-hourly_Nan_chrono.csv')
df_ref = pd.read_csv('/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ref-hourly-TOUT_chrono_Nan.csv')


# Convertit les dates en objets DATETIME
df_purple['time_stamp'] = pd.to_datetime(df_purple['time_stamp'])
df_ref['time_stamp'] = pd.to_datetime(df_ref['time_stamp'])


# Liste pour stocker les valeurs de time_stamp

# Chemins vers vos fichiers CSV (assurez-vous que ces chemins sont corrects)
purple_csv = '/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ppl-TOUT-hourly_Nan_chrono.csv'
ref_csv = '/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ref-hourly-TOUT_chrono_Nan.csv'

# Extrait des csv la liste avec la ligne des date
# Lire les fichiers CSV en dataframes pandas
df_purple = pd.read_csv(purple_csv)
df_ref = pd.read_csv(ref_csv)

# Convertir les colonnes 'time_stamp' en objets datetime si ncessaire
df_purple['time_stamp'] = pd.to_datetime(df_purple['time_stamp'])
df_ref['time_stamp'] = pd.to_datetime(df_ref['time_stamp'])

# Obtenir les listes de dates (time_stamp)  partir des dataframes
dates_purple = df_purple['time_stamp'].tolist()
dates_ref = df_ref['time_stamp'].tolist()

# Affichage des listes de dates (time_stamp)
print("voila la liste purple",dates_purple)
print("voila la liste ref",dates_ref)

# Trouve les dates communes
         
CMr = []
CMp = []
for j in range(len(dates_purple)):
    for i in range(len(dates_ref)):
        if dates_purple[j] == dates_ref[i]:
            CMr.append(i)
            CMp.append(j)
print(CMr)
print(CMp)

# Crer une liste contenant uniquement les dates associes  ces indices
common_dates = [dates_ref[i] for i in CMr]  # Utiliser les indices de CMr pour obtenir les dates communes de dates_ref
# ou
# common_dates = [dates_purple[j] for j in CMp]  # Utiliser les indices de CMp pour obtenir les dates communes de dates_purple

# Afficher les dates communes
print("Dates communes:")
print(common_dates)


# Filtre les DataFrames pour ne conserver que les dates communes
df_purple_filtered = df_purple[df_purple['time_stamp'].isin(common_dates)]
df_ref_filtered = df_ref[df_ref['time_stamp'].isin(common_dates)]

# Affiche les premires lignes des DataFrames filtrs
print("\nAperu du fichier purple filtr:")
print(df_purple_filtered.head())

print("\nAperu du fichier ref filtr:")
print(df_ref_filtered.head())

# Enregistre les DataFrames filtrs dans de nouveaux fichiers CSV
df_purple_filtered.to_csv('/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ppl-TOUT-hourly_Nan_chrono_off.csv', index=False)
df_ref_filtered.to_csv('/Users/saraguinane/Documents/administratif/stage recherche/39603/3-ref-hourly-TOUT_chrono_Nan_off.csv', index=False)

print("Les fichiers filtrs ont t enregistrs avec succs.")
