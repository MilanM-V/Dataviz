import pandas as pd
import sys
import codecs

if sys.stdout.encoding!='utf-8':
    sys.stdout=codecs.getwriter('utf-8')(sys.stdout.buffer,'strict')


import partie_milan
#import partie_membre2
#import partie_membre3
#import partie_membre4
#import partie_membre5


def build():
    #Charger les données

    df=pd.read_csv("data_propre.csv")

    #Lire le template HTML
    with open("template.html","r",encoding="utf-8") as f:
        page=f.read()


    injections_modules=[partie_milan]
    #injections_modules=[partie_milan,partie_membre2,partie_membre3,partie_membre4,partie_membre5]

    for module in injections_modules:
        try:
            elements_html=module.generer_html(df)
            
            for placeholder,html_genere in elements_html.items():
                page=page.replace(placeholder,html_genere)
                
        except Exception as e:
            print(f"Erreur dans {module.__name__} : {e}")


    with open("rendu_final.html","w",encoding="utf-8") as f:
        # Encoder automatiquement toutes les images du dossier 'img' en base64 pour éviter 
        # les bugs de sécurité locale (tainted canvas) lors de l'ouverture sous le protocole file://
        import base64
        import os
        import re
        
        # Trouver toutes les images définies avec des guillemets doubles ou simples de manière robuste
        matches_double=re.findall(r'src="([^"]+)"',page)
        matches_single=re.findall(r"src='([^']+)'",page)
        matches=[m for m in (matches_double+matches_single) if m.startswith('img/')]
        
        for img_path in set(matches):
            if os.path.exists(img_path):
                ext=os.path.splitext(img_path)[1].lower().replace('.','')
                mime="image/png" if ext == "png" else "image/jpeg"
                with open(img_path,"rb") as img_f:
                    encoded=base64.b64encode(img_f.read()).decode('utf-8')
                base64_data=f"data:{mime};base64,{encoded}"
                page=page.replace(f'src="{img_path}"',f'src="{base64_data}"')
                page=page.replace(f"src='{img_path}'",f"src='{base64_data}'")
                print(f"Image en ligne : {img_path} convertie avec succès !")
            else:
                print(f"Attention : Image introuvable : {img_path}")

        f.write(page)


    print("rendu_final.html généré")
  


if __name__=="__main__":
    build()
