import requests

# Interroge l'API
def rechercher_pokemon(nom):
    url = f"https://pokeapi.co/api/v2/pokemon/{nom}"
    reponse = requests.get(url)

    # Pokémon inconnu ou autre erreur
    if reponse.status_code == 404:
        print("\nLa ressource n'existe pas")
        return None
    elif reponse.status_code != 200:
        print("\nUne erreur est survenue lors de la requête")
        return None
    else:
        data = reponse.json()
        return data

# Affiche les infos d'un pokémon
def afficher_fiche(data):
    print("\nFiche Pokémon")
    pk_nom = data['name']
    pk_taille = data['height']
    pk_poids = data['weight']
    
    pk_types = []
    for type in data['types']:
        pk_types.append(type['type']['name'])
    
    pk_stats = []
    for stat in data['stats']:
        pk_stats.append({"nom": stat['stat']['name'], "valeur": stat['base_stat']})
        
    print(f"Nom : {pk_nom}")
    print(f"Taille : {pk_taille}")
    print(f"Poids : {pk_poids}")
    print(f"Types : {', '.join(pk_types)}")
    print(f"PV : {pk_stats[0]['valeur']}")
    print(f"Attaque : {pk_stats[1]['valeur']}")
    print(f"Défense : {pk_stats[2]['valeur']}")    
    
# Affiche le récap final de l'équipe
def afficher_equipe(equipe):
    print("\nÉquipe finale :")
    for i, pokemon in enumerate(equipe, start=1):
        data = pokemon['data']
        
        pk_types = []
        for type in data['types']:
            pk_types.append(type['type']['name'])   
        types = ', '.join(pk_types)
            
        pv = data['stats'][0]['base_stat']
        attaque = data['stats'][1]['base_stat']
        defense = data['stats'][2]['base_stat']
        
        print(f"\n{i}. {pokemon['nom']}")
        print(f"Types : {types}")
        print(f"PV : {pv} | Attaque : {attaque} | Défense : {defense}")
        print()

# Compose une équipe de 3 Pokémons
def main(): 
    print("==============================================")  
    print("Bienvenue dans le générateur d'équipe Pokémon.")
    print("==============================================\n")
    print("Votre équipe peut contenir 3 Pokémons.")
    
    equipe = []
    while len(equipe) < 3:
        nom = input("\nEntrez le nom d'un Pokémon : ")
        data = rechercher_pokemon(nom)
        
        if data == None:
            print("Pokémon introuvable")
            
        # Empêche les doublons dans l'équipe
        elif nom in [pokemon['nom'] for pokemon in equipe]:
            print("\nCe Pokémon est déjà dans votre équipe")
        else:
            afficher_fiche(data)
            choix = input("\nVoulez-vous ajouter ce Pokémon à votre équipe ? : ")
            
            if choix.lower() == "oui":
                equipe.append({"nom": nom, "data": data})
                print(f"\n{nom} a été ajouté à votre équipe.")
   
    afficher_equipe(equipe)
    
# programme principal
main()
    
