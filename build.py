import pandas as pd
import sys
import codecs

if sys.stdout.encoding!='utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')


import partie_milan
#import partie_membre2
#import partie_membre3
#import partie_membre4
#import partie_membre5


def build():
    #Charger les données

    df = pd.read_csv("data_propre.csv")

    #Lire le template HTML
    with open("template.html","r",encoding="utf-8") as f:
        page=f.read()


    injections_modules=[partie_milan]
    #injections_modules=[partie_milan, partie_membre2, partie_membre3, partie_membre4, partie_membre5]

    for module in injections_modules:
        try:
            elements_html=module.generer_html(df)
            
            for placeholder,html_genere in elements_html.items():
                page=page.replace(placeholder,html_genere)
                
        except Exception as e:
            print(f"Erreur dans {module.__name__} : {e}")


    with open("rendu_final.html","w",encoding="utf-8") as f:
        f.write(page)


    print("rendu_final.html généré")
  


if __name__=="__main__":
    build()
