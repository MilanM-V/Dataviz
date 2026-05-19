import subprocess
import os

team = ['Adam', 'Lois', 'Evan', 'Mamadou', 'Milan']

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

# Update all python files to return a dictionary
run("git checkout main")
for name in team:
    filename = f"partie_{name.lower()}.py"
    if not os.path.exists(filename):
        continue
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple replace if it still returns graph_html directly
    if "return graph_html" in content:
        content = content.replace("return graph_html", f"""return {{
        "<!-- INJECTER_GRAPH_X -->": graph_html,
        # "<!-- INJECTER_STAT_X -->": "Valeur",
        # "<!-- INJECTER_STAT_X_LABEL -->": "Label",
    }}""")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

# Update build.py to import everyone
build_content = open("build.py", "r", encoding="utf-8").read()
# Let's just do a manual rewrite of the imports and injections
build_content = build_content.replace("import partie_milan", "import partie_milan\nimport partie_adam\nimport partie_lois\nimport partie_evan\nimport partie_mamadou")
build_content = build_content.replace("injections_modules = [partie_milan]", "injections_modules = [partie_milan, partie_adam, partie_lois, partie_evan, partie_mamadou]")
with open("build.py", "w", encoding="utf-8") as f:
    f.write(build_content)

run("git add .")
run('git commit -m "Préparation de build.py et des fichiers Python pour toute l\'équipe"')
run("git push origin main")

# Merge back into everyone
for name in team:
    run(f"git checkout {name}")
    run("git merge main")
    run(f"git push origin {name}")

run("git checkout Milan")
