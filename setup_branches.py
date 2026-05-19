import os
import subprocess

branches = ['Adam', 'Lois', 'Evan', 'Mamadou']

def run_cmd(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

for b in branches:
    lower_b = b.lower()
    run_cmd(f"git checkout {b}")
    run_cmd(f"git mv partie_milan.py partie_{lower_b}.py")
    
    with open(f"partie_{lower_b}.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("milan", lower_b).replace("Milan", b)
    
    with open(f"partie_{lower_b}.py", "w", encoding="utf-8") as f:
        f.write(content)
        
    run_cmd(f"git add .")
    run_cmd(f'git commit -m "Setup partie_{lower_b}.py pour {b}"')
    run_cmd(f"git push origin {b}")

run_cmd("git checkout main")
run_cmd("git rm partie_milan.py")
run_cmd('git commit -m "Remove partie_milan from main"')
run_cmd("git push origin main")
