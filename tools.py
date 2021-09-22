# Modules tools

def example():
    print("Simple exemple")
# je vais l'importer dans dictionary.py

def separator(charactere, times):
    row = ""
    for n in range(times) :
        row += charactere
    print(row)

'''
Il existe 3 types de modules :
Les modules personnalisés (comme ci-dessus) : exemple tools
Les modules natifs (core) : exemple random, os
Les module communautaires : on laisse de coté pour le moment
'''