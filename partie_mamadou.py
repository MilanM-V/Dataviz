"""
partie_mamadou.py — Espace de travail de Mamadou
==============================================
Ta seule mission : coder la fonction generer_html(df)
qui retourne une STRING de HTML contenant tes graphiques.

Exemple de test :
    python partie_mamadou.py
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

    # ──────────────────────────────────────
    # 3. (Optionnel) Ajouter des métriques
    # ──────────────────────────────────────
    # Tu peux ajouter du HTML brut autour de ton graphique
    # Exemple :
    # metric = f'<p style="font-size:0.9rem; color:#6b7280;">Moyenne : {df[col].mean():.1f}</p>'

    # ──────────────────────────────────────
    # 4. Retourner le HTML final
    # ──────────────────────────────────────
    return graph_html


# ══════════════════════════════════════════
# TEST LOCAL — lance : python partie_mamadou.py
# ══════════════════════════════════════════
if __name__ == "__main__":
    # Crée des données fictives pour tester
    mock_data = pd.DataFrame({
        "Catégorie": ["A", "B", "C", "D", "E"],
        "Valeur": [23, 45, 12, 67, 34],
    })

    html = generer_html(mock_data)
    print(f"✅ HTML généré : {len(html)} caractères")

    # Sauvegarde un aperçu pour tester dans le navigateur
    with open("test_mamadou.html", "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html><head>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head><body style="font-family:sans-serif; padding:2rem;">
<h2>Test — partie_mamadou.py</h2>
{html}
</body></html>""")

    print("📄 Ouvre test_mamadou.html dans Chrome pour voir le résultat")
