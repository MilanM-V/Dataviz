import pandas as pd
import plotly.express as px

def generer_html(df=None):
    # 1. Charger les données (fallback sur data_propre.csv si non fourni)
    if df is None:
        try:
            df = pd.read_csv("data_propre.csv")
        except FileNotFoundError:
            # Pour l'instant on utilise de fausses données pour tester si le fichier n'existe pas
            df = pd.DataFrame({
                "Catégorie": ["Type 1", "Type 2", "Type 1", "Type 2", "Type 1"],
                "Valeur": [23, 45, 12, 67, 34],
                "Latitude": [48.8566, 45.7640, 43.7102, 50.6292, 47.2184],
                "Longitude": [2.3522, 4.8357, 7.2620, 3.0573, -1.5536],
                "Nom de la ville": ["Paris", "Lyon", "Nice", "Lille", "Nantes"],
                "Population": [10, 20, 15, 25, 18],
            })
    
    # 2. Créer le graphique avec Plotly
    # ──────────────────────────────────────
    fig = px.bar(
        df,
        x=df["Catégorie"].tolist(),
        y=df["Valeur"].tolist(),
        title="Mon Super Graphique à moi",
    )
    
    # Rendre le graphique invisible (transparent) pour qu'il prenne le CSS du HTML
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#333"),
        margin=dict(l=20, r=20, t=40, b=20)
    )

    # full_html=False → on ne génère pas toute une page web, juste le <div>
    # include_plotlyjs=False → Plotly.js est déjà dans le template
    graph_html = fig.to_html(full_html=False, include_plotlyjs=False)

    fig_geo = px.scatter_geo(
        df,
        lat=df["Latitude"].tolist(),
        lon=df["Longitude"].tolist(),
        hover_name=df["Nom de la ville"].tolist(),
        scope="europe",
        title="Carte des Villes"
    )
    fig_geo.update_traces(marker=dict(size=15, color="red", opacity=1))
    # On zoome manuellement sur la France
    fig_geo.update_geos(
        center=dict(lon=2.2137, lat=46.2276),
        lataxis_range=[41, 52],
        lonaxis_range=[-5, 10]
    )
    carte_html = fig_geo.to_html(full_html=False, include_plotlyjs=False)
    
    # ──────────────────────────────────────
    # 3. (Optionnel) Ajouter des métriques
    # ──────────────────────────────────────
    # Si tu as des chiffres clés (Moyenne, Max...), mets-les ici
    
    return {
        "<!-- INJECTER_GRAPH_1 -->": graph_html,
        "<!-- INJECTER_STAT_1 -->": f"{df['Valeur'].mean():.1f}<span class='stat-highlight-suffix'>k</span>",
        "<!-- INJECTER_STAT_1_LABEL -->": "Moyenne",
        "<!-- INJECTER_GRAPH_3 -->": carte_html,
    }

# ══════════════════════════════════════════════════════════════════
# CE BLOC SERT UNIQUEMENT À TESTER TON CODE TOUT SEUL (sans build.py)
# ══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    res = generer_html()
    html_complet = f"""
    <!DOCTYPE html>
    <html><head>
    <meta charset="utf-8">
    <script src="https://cdn.plot.ly/plotly-3.4.0.min.js"></script>
    <link rel="stylesheet" href="style.css">
    </head><body style="font-family:sans-serif; padding:2rem; background: var(--bg);">
    <h2>Test — partie_milan.py</h2>
    {res["<!-- INJECTER_GRAPH_1 -->"]}
    <hr>
    <h3>{res["<!-- INJECTER_STAT_1_LABEL -->"]} : {res["<!-- INJECTER_STAT_1 -->"]}</h3>
    <hr>
    {res["<!-- INJECTER_GRAPH_3 -->"]}
    </body></html>
    """
    
    with open("test_milan.html", "w", encoding="utf-8") as f:
        f.write(html_complet)
        
    print(f"Ouvre test_milan.html dans Chrome pour voir le resultat")
