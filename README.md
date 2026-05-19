# 🚀 Guide de Démarrage : Challenge Datavis BUT SD 2025

Bienvenue dans l'espace de travail du projet ! Ce dépôt contient toute l'architecture "Zéro Bug" pour réaliser notre poster final sans stress le jour J.

Voici le guide pas-à-pas pour récupérer le projet, travailler sur votre partie et fusionner le tout.

---

## 🛠️ 1. Installation initiale (à faire une seule fois)

Ouvrez un terminal (Git Bash, PowerShell ou VS Code) et tapez ces commandes :

```bash
# 1. Cloner le projet sur votre machine
git clone https://github.com/MilanM-V/Dataviz.git

# 2. Entrer dans le dossier
cd Dataviz

# 3. Récupérer toutes les branches
git fetch --all
```

---

## 👨‍💻 2. Travailler sur sa partie

Chacun a sa propre branche avec son fichier python personnalisé (ex: `partie_lois.py`). **Ne travaillez jamais sur la branche `main` !**

### A. Se positionner sur sa branche
```bash
# Remplacez "Prenom" par votre prénom (Milan, Adam, Lois, Evan, Mamadou)
git checkout Prenom
```

### B. Coder ses graphiques
1. Ouvrez votre fichier (ex: `partie_adam.py`).
2. C'est ici que vous utilisez **Plotly** pour créer vos graphiques.
3. Pour tester le rendu de **votre** graphique uniquement, lancez la commande :
```bash
python partie_adam.py
```
> 👉 Cela va générer un fichier `test_adam.html`. Ouvrez-le dans Chrome pour voir si votre graphique s'affiche bien !

### C. Sauvegarder son travail
Régulièrement, pensez à sauvegarder vos modifications sur GitHub :
```bash
# Ajouter tous vos changements
git add .

# Valider les changements avec un message
git commit -m "Ajout du graphique sur la population"

# Envoyer sur GitHub
git push origin Prenom
```

---

## 🎨 3. Le design (Template et CSS)

La branche `main` contient la structure visuelle globale du poster.
- `template.html` : L'architecture de la page.
- `style.css` : Les couleurs et le design.

**Le jour J :**
1. On se met d'accord sur le thème de couleur (voir `style.css`).
2. On adapte le titre et les sous-titres dans `template.html`.
3. On remplit les "KPI" avec les vrais chiffres.

---

## 🧩 4. Assemblage final (Le jour J)

Quand tout le monde a fini ses graphiques, il faut fusionner pour créer le rendu final. Cette étape est généralement gérée par une seule personne (ex: Milan).

```bash
# 1. Se mettre sur la branche principale
git checkout main

# 2. Récupérer le travail de tout le monde
git merge origin/Adam
git merge origin/Lois
git merge origin/Evan
git merge origin/Mamadou

# 3. Mettre à jour build.py
```
Dans `build.py`, enlevez les `#` devant les `import` et configurez les `<!-- INJECTER_GRAPH_X -->` pour qu'ils pointent vers les bonnes personnes.

```bash
# 4. Lancer l'assemblage !
python build.py
```
> 🎉 Et voilà ! Le fichier **`rendu_final.html`** est généré. C'est ce fichier (et lui seul) qui sera présenté au jury !

---

## 🚨 En cas de problème de fusion (Merge Conflict)
Si Git refuse de fusionner, c'est que plusieurs personnes ont modifié le même fichier.
**Pas de panique !**
1. Restez sur votre branche perso.
2. Demandez de l'aide à Milan ou à celui qui gère le Git.
3. Le principe de cette architecture est que chacun a **son propre fichier**, donc les conflits devraient être quasi-inexistants !

---

## 🔄 5. Récupérer les mises à jour du design

Si quelqu'un modifie le design global (`template.html` ou `style.css`) sur la branche `main`, voici la commande magique pour récupérer ces changements sur votre branche sans écraser votre travail :

```bash
# 1. Sauvegardez d'abord votre travail en cours
git commit -am "Sauvegarde avant mise a jour"

# 2. Récupérez les nouveautés de la branche main
git merge origin/main
```
Cela mettra à jour votre template localement !
