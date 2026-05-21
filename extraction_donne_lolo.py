import pandas as pd

# 1. Charger le fichier Excel
# Remplacez 'votre_fichier.xlsx' par le chemin réel de votre fichier
df = pd.read_excel('Dataviz_2026_données.xlsx', sheet_name='Propre')

# 2. Définir la population urbaine pour 2016 et 2022
# Dans l'onglet 'Propre', 'Libellé degré de densité' contient 'Urbain' ou 'Rural'
df['PMUN16_urbain'] = df['Population en 2016'].where(df['Libellé degré de densité'] == 'Urbain', 0)
df['PMUN22_urbain'] = df['Population en 2022'].where(df['Libellé degré de densité'] == 'Urbain', 0)

# 3. Grouper par département ('Code dep') pour agréger les populations
stats_dep = df.groupby('Code dep').agg(
    pop_totale_2016=('Population en 2016', 'sum'),
    pop_urbaine_2016=('PMUN16_urbain', 'sum'),
    pop_totale_2022=('Population en 2022', 'sum'),
    pop_urbaine_2022=('PMUN22_urbain', 'sum')
).reset_index()

# 4. Calculer les taux d'urbanisation (en %)
stats_dep['taux_urb_2016'] = (stats_dep['pop_urbaine_2016'] / stats_dep['pop_totale_2016']) * 100
stats_dep['taux_urb_2022'] = (stats_dep['pop_urbaine_2022'] / stats_dep['pop_totale_2022']) * 100

# 5. Calculer l'évolution du taux en points de pourcentage (2022 - 2016)
stats_dep['evolution_points'] = stats_dep['taux_urb_2022'] - stats_dep['taux_urb_2016']

# Arrondir les résultats pour la lisibilité
stats_dep['taux_urb_2016'] = stats_dep['taux_urb_2016'].round(2)
stats_dep['taux_urb_2022'] = stats_dep['taux_urb_2022'].round(2)
stats_dep['evolution_points'] = stats_dep['evolution_points'].round(2)

# 6. Afficher les colonnes essentielles
print(stats_dep[['Code dep', 'taux_urb_2016', 'taux_urb_2022', 'evolution_points']])


# 7. Sauvegarder le résultat dans un nouveau fichier Excel
stats_dep.to_excel('evolution_taux_urbanisation.xlsx', index=False)
print("Fichier 'evolution_taux_urbanisation.xlsx' sauvegardé avec succès !")
