#Lien github: https://github.com/moussacode/Atelier_12_Python_Application-de-pointage.git

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
            nom = input("Saisir votre nom ").strip()
            if nom.isalpha():
                break
            else:
                print("Nom invalide. Veuillez réessayer.")
        while True:
            prenom = input("Saisir votre prenom ").strip()
            if prenom.isalpha():
                break
            else:
                print("Prenom invalide. Veuillez réessayer.")

        
        promo = input("Saisir votre promo ").strip()

        while True:
            try:
                identifiant = int(input("Saisir votre identifiant : "))
                if identifiant >= 1 :
                    if  identifiant not in id_apprenant:
                        break
                    else:
                        print('Veuillez saisir un id unique')
                else:
                    print("L'identifiant doit être un nombre positif")
            except ValueError:
                print("L'identifiant doit être un nombre entier")


        apprenants= {
            "nom" : nom ,
            "prenom" : prenom,
            "promo" : promo,
            "identifiant" : identifiant,
            "presence": "non-pointer"
        }

        id_unique = apprenants['identifiant']
        print('id' , id_unique)

      
        liste_aprenant.append(apprenants)
        id_apprenant.append(id_unique)
        
        print(f" {nom} {prenom} (ID: {identifiant}) a été ajouté avec succès!")
        
        continuer = input("Ajouter un autre apprenant ? (oui/non) : ").strip().lower()
        if continuer != 'oui':
            break

def  EnregistrerPresence():
    print('=== Enregistrement des Presences ===')
    if len(liste_aprenant)==0:
        print('Aucun apprents dans la liste')
    else:
        while True:
            try:
                print('==== Liste des Apprenants ====')
                for apprenti in liste_aprenant:
                    
                    print(f"ID : {apprenti['identifiant']} {apprenti['nom']} | {apprenti['prenom']} | {apprenti['presence']}"  )
                choix_apprenant = int(input("Choisir l'id apprenant a pointer"))
                for apprenti in liste_aprenant:
                    if choix_apprenant == apprenti['identifiant']:
                        print(f"Vous avez choisi : ID({apprenti['identifiant']}) {apprenti['nom']} {apprenti['prenom']} {apprenti['presence']}"  )
                        presence = input('Present(1) ou Abscent (2) ').strip()
                        if presence == '1':
                            apprenti['presence'] = 'present' 
                        elif presence== '2':
                            apprenti['presence'] = 'abscent'     
                        print(f"Aprenant {apprenti['nom']} a bien ete marquer {apprenti['presence']}")

                    else:
                        print('Choisir un  Id apprenant de la liste ')

                print("q : Pour Quitter | Appuyer Entrer pour contunier")
                quitter = input('Voulez vous quitter :   ').strip()
                if quitter.lower() == "q":
                    break

            except ValueError:
                print("L'identifiant doit être un nombre entier")

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
    total = 0
    for apprenti in liste_aprenant:
        total = total + 1
        if apprenti['presence'] == 'present' :
           t_present = t_present + 1
    if total == 0 :
        print('Pas de taux disponible')
    else :
        taux = (t_present/total)*100
        print (f"Taux de presence {taux} %")

    

    

def main ():
    while True:
        affiche_menu()
        choix = input('Choisissez un choix ').strip()
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