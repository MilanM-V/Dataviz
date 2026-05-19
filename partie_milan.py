"""
partie_milan.py — Espace de travail de Milan
==============================================
Ta seule mission : coder la fonction generer_html(df)
qui retourne une STRING de HTML contenant tes graphiques.

Exemple de test :
    python partie_milan.py
"""

import pandas as pd
import plotly.express as px


def generer_html(df):
    """
    Génère le HTML de ta partie.

    Args:
        df: DataFrame pandas avec les données du CSV

    Returns:
        str: bloc HTML (graphiques + métriques)
    """

    # ──────────────────────────────────────
    # 1. Crée tes graphiques Plotly
    # ──────────────────────────────────────
    # Exemple — à remplacer le jour J par tes vrais graphiques
    fig = px.bar(
        df,
        x=df.columns[0],   # première colonne (à adapter)
        y=df.columns[1],   # deuxième colonne (à adapter)
        title="Mon graphique",
        color_discrete_sequence=["#2d8a4e"],  # couleur du thème
    )

    # Style du graphique pour matcher le poster
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=40, b=20),
        font=dict(family="Inter, sans-serif", size=12),
    )

    # ──────────────────────────────────────
    # 2. Convertir en HTML
    # ──────────────────────────────────────
    # full_html=False  → juste la div, pas une page entière
    # include_plotlyjs=False → Plotly.js est déjà dans le template
    graph_html = fig.to_html(full_html=False, include_plotlyjs=False)

    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        color="Catégorie",
        size="Population",
        hover_name="Nom de la ville",
        zoom=4,
        center={"lat": 46.2276, "lon": 2.2137}, # Centre sur la France
        mapbox_style="carto-positron",
        title="Carte des Villes"
    )
    carte_html = fig.to_html(full_html=False, include_plotlyjs=False)
    # ──────────────────────────────────────
    # 3. (Optionnel) Ajouter des métriques
    # ──────────────────────────────────────
    # Tu peux ajouter du HTML brut autour de ton graphique
    # Exemple :
    # ──────────────────────────────────────
    # 4. Retourner les éléments avec leurs destinations
    # ──────────────────────────────────────
    # Au lieu de retourner une seule chaîne de texte, tu retournes
    # un dictionnaire qui associe : "PLACEHOLDER" -> "HTML"
    
    return {
        "<!-- INJECTER_GRAPH_1 -->": graph_html,
        "<!-- INJECTER_STAT_1 -->": f"{df[df.columns[1]].mean():.1f}<span class='stat-highlight-suffix'>k</span>",
        "<!-- INJECTER_STAT_1_LABEL -->": "Moyenne",
        "<!-- INJECTER_GRAPH_3 -->": carte_html,
        # "<!-- INJECTER_GRAPH_2 -->": mon_autre_graph_html,
    }

# ══════════════════════════════════════════
# TEST LOCAL — lance : python partie_milan.py
# ══════════════════════════════════════════
if __name__ == "__main__":
    # Crée des données fictives pour tester
    mock_data = pd.DataFrame({
        "Catégorie": ["Type 1", "Type 2", "Type 1", "Type 2", "Type 1"],
        "Valeur": [23, 45, 12, 67, 34],
        "Latitude": [48.8566, 45.7640, 43.7102, 50.6292, 47.2184],
        "Longitude": [2.3522, 4.8357, 7.2620, 3.0573, -1.5536],
        "Nom de la ville": ["Paris", "Lyon", "Nice", "Lille", "Nantes"],
        "Population": [10, 20, 15, 25, 500000000],
    })

    resultats = generer_html(mock_data)
    html_complet = "<br>".join(resultats.values())
    
    print(f"Genere {len(resultats)} elements. Total : {len(html_complet)} caracteres")

    # Sauvegarde un aperçu pour tester dans le navigateur
    with open("test_milan.html", "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html><head>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<link rel="stylesheet" href="style.css">
</head><body style="font-family:sans-serif; padding:2rem; background: var(--bg);">
<h2>Test — partie_milan.py</h2>
{html_complet}
</body></html>""")

    print("Ouvre test_milan.html dans Chrome pour voir le resultat")
