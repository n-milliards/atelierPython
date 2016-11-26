def demander_nom(taille_nom):
    reponse = input("-- Entrez un nom : ")
    if(len(reponse) >= taille_nom):
        reponse = input("-- Entrez plutôt un diminutif, je n'arrive pas à retenir les trucs longs : ")
    else:
        reponse = input("-- C'est un peu court... Donnez-moi un truc plus impressionnant : ")

    return reponse

nom = demander_nom(6)
message = "-- Tut tut tut... Réveillez-vous " + nom + " !"

print(message)
