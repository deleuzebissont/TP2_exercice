# exercice a
print("Hello World!")
# exercice b
name = input("Quel est ton nom ? : ")
print(f"Bonjour! {name}")
# exercice c
nb_etoile = int(input("Combien d'etoiles voulez vous ? : "))
while nb_etoile != 0: # tant que le nombre d etoile n est pas egal a 0, j execute le code
    nb_etoile -= 1 # a chaque ligne, je veux qu il y ait une etoile en moins
    print(nb_etoile * "*")
print("Fini.")
