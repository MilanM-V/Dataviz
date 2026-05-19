# 📊 Tutoriel Zéro à Héros : Plotly pour le Challenge Datavis

Bienvenue dans le guide ultime de création de graphiques ! Si tu n'y connais rien, pas de panique : **Plotly Express** est conçu pour faire des graphiques professionnels en 1 à 2 lignes de code.

Dans ce tutoriel, tu vas apprendre à créer des barres, des cartes, des indicateurs, et même des menus interactifs. 🚀

---

## 🛠️ 0. La base absolue (À mettre en haut de ton fichier)

Pour que la magie opère, il faut deux bibliothèques : Pandas (pour lire les données) et Plotly Express (pour dessiner).

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go # Optionnel, pour des trucs très avancés
```

---

## 📊 1. Les Graphiques Classiques

La règle avec `plotly.express` est toujours la même :
`px.nom_du_graphique(dataframe, x="colonne_x", y="colonne_y")`

### 📈 Graphique en Barres (Bar Chart)
Idéal pour comparer des quantités (ex: nombre d'étudiants par région).

```python
fig = px.bar(
    df, 
    x="Région", 
    y="Nombre d'étudiants",
    title="Répartition des étudiants par région",
    color="Région", # Met une couleur différente par région
    text_auto=True  # Affiche la valeur au-dessus des barres !
)
```

### 📉 Graphique en Ligne (Line Chart)
Idéal pour montrer une évolution dans le temps.

```python
fig = px.line(
    df,
    x="Année",
    y="Taux de réussite",
    title="Évolution de la réussite au bac (2015-2023)",
    markers=True # Ajoute des petits points sur la ligne
)
```

### 🥧 Camembert (Pie Chart)
Idéal pour des pourcentages (attention, ne pas l'utiliser s'il y a plus de 5 parts).

```python
fig = px.pie(
    df,
    names="Filière", # Les catégories (ex: S, ES, L)
    values="Effectif", # Les nombres
    title="Répartition par filière",
    hole=0.4 # Transforme le camembert en "Donut" (plus joli !)
)
```

### 🔴 Nuage de points (Scatter Plot)
Idéal pour voir si deux choses sont corrélées (ex: Salaire vs Âge).

```python
fig = px.scatter(
    df,
    x="Âge",
    y="Salaire moyen",
    color="Sexe", # Couleur différente homme/femme
    size="Effectif", # La taille du point dépend du nombre de personnes !
    title="Corrélation Âge / Salaire"
)
```

---

## 🗺️ 2. Les Cartes (Génial pour impressionner le jury !)

Si vous avez une colonne avec des noms de pays, de régions ou des coordonnées GPS (Lat/Lon), les cartes sont vos meilleures amies.

### 📍 Carte avec des points (Scatter Geo)
Si vous avez la longitude et latitude :

```python
fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    color="Taux de chômage", # La couleur du point dépend du taux
    size="Population", # La taille du point dépend de la population
    hover_name="Nom de la ville", # Ce qui s'affiche quand on passe la souris
    title="Carte des Villes"
)
fig.update_geos(fitbounds="locations") # Pour zoomer automatiquement sur la France !
```

### 🗺️ Carte coloriée par zone (Choropleth)
Idéal si vous avez des noms de pays ou un code de région.

```python
fig = px.choropleth(
    df,
    locations="Code Pays", # Ex: 'FRA', 'DEU'
    color="PIB",
    hover_name="Nom du Pays",
    color_continuous_scale="Viridis", # Palette de couleur sympa
    title="PIB par pays en Europe"
)
fig.update_geos(scope="europe") # Restreindre la vue à l'Europe
```

---

## 🔢 3. Les Indicateurs (Les gros chiffres "KPI")

Dans notre poster (template.html), on a une zone pour mettre des gros chiffres en haut (les KPI).
Il y a deux façons de les faire.

### Méthode A : Avec Plotly
```python
fig = go.Figure(go.Indicator(
    mode = "number+delta", # Affiche le nombre + la différence avec hier
    value = 450,
    title = {"text": "Étudiants Inscrits"},
    delta = {'reference': 400, 'position': "bottom"} # Indique +50 (car 450 par rapport à 400)
))
```

### Méthode B : Plus simple, en HTML direct !
Comme `partie_milan.py` retourne du texte HTML, tu peux juste écrire une belle "boîte" HTML pour ton indicateur :

```python
mon_kpi_html = f"""
<div style="background: #e8f5ec; padding: 20px; border-radius: 10px; text-align: center;">
    <h3 style="color: #2d8a4e; margin: 0; font-size: 2.5rem;">{df['Étudiants'].sum()}</h3>
    <p style="color: #6b7280; margin: 0;">Total des Étudiants</p>
</div>
"""
# Plus tard tu retournes mon_kpi_html !
```

---

## 🎛️ 4. Ajouter de l'interactivité (Menus & Boutons)

Rendre un graphique interactif rajoute beaucoup de points ! On peut ajouter un menu déroulant pour changer la donnée affichée.

```python
# Un simple graphique
fig = px.bar(df, x="Mois", y="Revenus")

# Ajout d'un menu déroulant (Dropdown) magique !
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(label="Voir Revenus", method="update", args=[{"y": [df["Revenus"]]}]),
                dict(label="Voir Dépenses", method="update", args=[{"y": [df["Dépenses"]]}]),
                dict(label="Voir Bénéfices", method="update", args=[{"y": [df["Bénéfices"]]}]),
            ]),
            direction="down",
            showactive=True,
            x=0.5, # Centré horizontalement
            y=1.15 # Juste au-dessus du graphique
        )
    ]
)
```

---

## 🛠️ 5. Le "Tooltip" (Informations au survol)

Par défaut, Plotly affiche des infos quand on passe la souris. Tu peux l'améliorer avec l'argument `hover_data` !

```python
fig = px.bar(
    df, 
    x="Ville", 
    y="Population",
    # On ajoute le maire et le budget dans l'infobulle (tooltip) sans les dessiner !
    hover_data=["Nom du Maire", "Budget Annuel"] 
)
```

---

## 📦 6. Comment renvoyer plusieurs graphiques ?

Si ta partie (`partie_milan.py`) doit contenir 2 graphiques et 1 indicateur HTML, comment on fait pour tout renvoyer au `build.py` ? C'est super simple, on additionne les textes (strings) !

```python
def generer_html(df):
    
    # 1. Mon indicateur
    kpi = f"<h2>Mon chiffre clé : {df['Notes'].mean()} / 20</h2>"
    
    # 2. Mon premier graph
    fig1 = px.pie(df, names="Sexe", values="Nombre")
    html1 = fig1.to_html(full_html=False, include_plotlyjs=False)
    
    # 3. Mon deuxième graph
    fig2 = px.bar(df, x="Âge", y="Salaire")
    html2 = fig2.to_html(full_html=False, include_plotlyjs=False)
    
    # 4. On additionne TOUT et on renvoie !
    html_final = kpi + "<br>" + html1 + "<br>" + html2
    
    return html_final
```

---

## ✨ 7. Le bout de code "Design Pro" à copier-coller

Pour que vos graphiques Plotly s'intègrent parfaitement dans le poster clair qu'on a fait, ajoutez **TOUJOURS** ces 5 lignes de code juste avant le `fig.to_html(...)` :

```python
fig.update_layout(
    template="plotly_white",           # Fond blanc propre
    paper_bgcolor="rgba(0,0,0,0)",     # Rend le fond du conteneur transparent
    plot_bgcolor="rgba(0,0,0,0)",      # Rend le fond du graphique transparent
    font=dict(family="Inter, sans-serif", size=12), # La même police que le poster
    margin=dict(l=20, r=20, t=40, b=20) # Enlève les marges moches
)
```

Avec ça, vous êtes parés pour faire des graphiques incroyables. Bon code à tous ! 🚀
