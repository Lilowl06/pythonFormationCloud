n = input("Tape un nombre entier : ") # par défaut c'est l'entrée standard qui est prise et c'est le terminal.
                            # input a une fonction print intégré car il affiche ce que l'on a écrit dans input
# print(type(n)) --> toute valeur saisie via la fonction input est de type str

square = int(n) * int(n)

print("Le carré de", n, "vaut", square, sep=" ") # le séparateur par défaut de print entre les multis-arguments. Le séparateur est définissable.
                                                    # 'sep =' est ne argument nommé.

print("Le carré de %s vaut %d" % (n,square)) # l'élément spécifie après les guillemets devra se substitué à %s (strings) %d (digit/number)
                                                # souvent le convertion explicite ne pose pas de problème de int vers str mais l'inverse pas
