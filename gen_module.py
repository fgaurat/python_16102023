import importlib

# Étape 1: Générez le fichier module
module_name = "module_temporaire"
code = """
def saluer():
    return "Bonjour depuis le module généré !"
"""

with open(f"{module_name}.py", "w") as f:
    f.write(code)

# Étape 2: Importez le module
module_temporaire = importlib.import_module(module_name)

# Utilisez une fonction du module généré
print(module_temporaire.saluer())

import os
os.remove(f"{module_name}.py")