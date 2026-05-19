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
import partie_adam
import partie_lois
import partie_evan
import partie_mamadou
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

    injections_modules = [partie_milan, partie_adam, partie_lois, partie_evan, partie_mamadou]
    # injections_modules = [partie_milan, partie_membre2, partie_membre3, partie_membre4, partie_membre5]

    for module in injections_modules:
        print(f"⚙️  Génération : {module.__name__}...")
        try:
            # Récupère un dictionnaire { "<!-- PLACEHOLDER -->": "HTML", ... }
            elements_html = module.generer_html(df)
            
            for placeholder, html_genere in elements_html.items():
                page = page.replace(placeholder, html_genere)
                print(f"   ✅ Injecté dans {placeholder}")
                
        except Exception as e:
            print(f"   ❌ Erreur dans {module.__name__} : {e}")

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
