liste_aprenant =[]
id_apprenant = []


def affiche_menu() :
    print("MENU")
    print("1. Ajouter des Apprenants ")
    print("2. Enregistrer les presences")
    print("3. Afficher les Apprenants Présents")
    print("4. Taux de presence ")
    print("5. Quitter")

def AjouterApprenant():
    apprenants = {}
    while True:
        while True:
            nom = input("Saisir votre nom ")
            if nom.isalpha():
                break
            else:
                print("Nom invalide. Veuillez réessayer.")
        while True:
            prenom = input("Saisir votre prenom ")
            if prenom.isalpha():
                break
            else:
                print("Prenom invalide. Veuillez réessayer.")

        
        promo = input("Saisir votre promo ")

        while True :
            identifiant  =int(input("Saisir votre identifiant ")) 
            if identifiant not in id_apprenant:
                 break
            else:
                 print('Veuillez saisir un id unique ')


        apprenants= {
            "nom" : nom ,
            "prenom" : prenom,
            "promo" : promo,
            "identifiant" : identifiant
        }

        id_unique = apprenants['identifiant']
        print('id' , id_unique)

      
        liste_aprenant.append(apprenants)
        id_apprenant.append(id_unique)
        print(id_apprenant)
        print(liste_aprenant)
            
      

        arret=input("Voulez vous ajouter un autre (Oui/Non)")
        if arret.lower() == 'non' :
            break

def  EnregistrerPresence():
    print('=== Enregistrement des Presences ===')
    if len(liste_aprenant)==0:
        print('Aucun apprents dans la liste')
    else:
        for apprenti in liste_aprenant:
            print(f"Aprenant {apprenti['nom']}")
            presence = input('Present(1) ou Abscent (2) ')
            if presence == '1':
                apprenti['presence'] = 'present' 
            elif presence== '2':
                apprenti['presence'] = 'abscent'     
            print(f"Aprenant {apprenti['nom']} a bien ete marquer {apprenti['presence']}")
        

def  AfficherApprenantsPrésents():
    print('=== Liste des Present ===')
    if len(liste_aprenant)==0:
        print('Aucun apprenants dans la liste')
    else:
        for apprenti in liste_aprenant:
            if apprenti['presence']== 'present' :
                print(f'{apprenti['nom']} {apprenti['prenom']}')


def TauxPresence():
    t_present = 0
    total =0
    for apprenti in liste_aprenant:
        total = total +1
        if apprenti['presence'] == 'present' :
           t_present = t_present + 1
    if total == 0 :
        print('Pas de taux disponible')
    else :
        taux = (t_present/total)*100
        print (taux)

    

    

def main ():
    while True:
        affiche_menu()
        choix = input('Choisissez un choix ')
        if choix == '1':
            AjouterApprenant()

        elif choix =='2':
             EnregistrerPresence()
        
        elif choix =='3':
             AfficherApprenantsPrésents()

        elif choix == '4':
            TauxPresence()
        
        elif choix=='5':
            break

        else:
            print('Veuillez choisir une des options proposer')


    

main()