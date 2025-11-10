# test_md5.py
import hashlib

target = "98b6a84b03f5aca7e23a13c627d62037"

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

# Remplace 'words.txt' par le chemin de ta liste de mots (un mot par ligne)
with open('words.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f, 1):
        word = line.strip()
        if not word:
            continue
        if md5(word) == target:
            print(f"Trouvé ! plaintext = '{word}' (ligne {i})")
            break
    else:
        print("Aucun mot de la liste ne correspond.")
