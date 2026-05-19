"""
build.py — Chef d'orchestre
=============================
Ce script assemble le rendu final :
1. Lit le template.html
2. Charge les données CSV
3. Appelle chaque partie_xxx.generer_html(df)
4. Injecte le HTML généré dans le template
5. Sauvegarde rendu_final.html

Usage :
    python build.py
"""

import pandas as pd
import sys
import codecs

# Force l'encodage UTF-8 pour les emojis dans la console Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

# === Import des parties de chaque membre ===
import partie_milan
# import partie_membre2
# import partie_membre3
# import partie_membre4
# import partie_membre5


def build():
    # ──────────────────────────────────────
    # 1. Charger les données
    # ──────────────────────────────────────
    print("📂 Chargement des données...")
    df = pd.read_csv("data_propre.csv")
    print(f"   ✅ {len(df)} lignes, {len(df.columns)} colonnes")

    # ──────────────────────────────────────
    # 2. Lire le template HTML
    # ──────────────────────────────────────
    print("📄 Lecture du template...")
    with open("template.html", "r", encoding="utf-8") as f:
        page = f.read()

    # ──────────────────────────────────────
    # 3. Générer le HTML de chaque membre
    # ──────────────────────────────────────
    # Chaque placeholder du template sera remplacé
    # par le HTML retourné par generer_html(df)
    #
    # Format : ("<!-- PLACEHOLDER -->", module)
    # ──────────────────────────────────────

    injections = {
        "<!-- INJECTER_GRAPH_1 -->": partie_milan,
        # "<!-- INJECTER_GRAPH_2 -->": partie_membre2,
        # "<!-- INJECTER_GRAPH_3 -->": partie_membre3,
        # "<!-- INJECTER_GRAPH_4 -->": partie_membre4,
        # "<!-- INJECTER_GRAPH_5 -->": partie_membre5,
    }

    for placeholder, module in injections.items():
        print(f"⚙️  Génération : {module.__name__}...")
        try:
            html_genere = module.generer_html(df)
            page = page.replace(placeholder, html_genere)
            print(f"   ✅ {module.__name__} injecté")
        except Exception as e:
            print(f"   ❌ Erreur dans {module.__name__} : {e}")
            # En cas d'erreur, on injecte un message visible
            page = page.replace(
                placeholder,
                f'<div style="color:red; padding:1rem;">❌ Erreur : {e}</div>'
            )

    # ──────────────────────────────────────
    # 4. Sauvegarder le rendu final
    # ──────────────────────────────────────
    with open("rendu_final.html", "w", encoding="utf-8") as f:
        f.write(page)

    print()
    print("=" * 45)
    print("✅ rendu_final.html généré avec succès !")
    print("   Ouvre-le dans Chrome pour voir le résultat")
    print("=" * 45)


if __name__ == "__main__":
    build()
