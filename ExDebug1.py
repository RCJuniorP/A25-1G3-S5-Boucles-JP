def environnement_optimal(temp : float, poussiere : str, humidite : float, afficher_messages : bool) -> None|bool:
    """
    Vérifie si l'environnement d'un ordinateur est optimal.
    :param temp: La température de l'environnement, en dégrés celsius.
    :param poussiere: La quantité de poussière dans l'environnement (faible, moyen, élevé).
    :param humidite: Le taux d'humidité de l'environnement, en pourcentage.
    :param afficher_messages: Vrai si la fonction doit afficher des messages, sinon faux.
    :return: None si une des données est invalide, Vrai si l'environnement est optimal et Faux dans le cas opposé.
    """
    poussiere = poussiere.lower()
    if poussiere not in ("faible", "moyen", "élevé"):
        print("Niveau de poussière invalide! Les valeurs valides sont 'faible', 'moyen' et 'élevé'.")
        return None

    alerte : bool = False
    messages: list[str] = []

    # Vérification température
    if temp < 18:
        messages.append("Température trop basse")
        alerte = True
    elif temp > 27:
        messages.append("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        messages.append("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        messages.append("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        messages.append("Trop de poussière")
        alerte = True
    
    if afficher_messages:
        for message in messages:
            print(message)
            
        if not alerte:
            print("Tout est sous contrôle!")
        else:
            print("Environnement non optimal")
    
    # Retour final
    return not alerte


def main():
    nb_ordi : int = int(input("Combien d'ordis doivent être traités? "))
    doit_afficher_messages: bool = "y" == input("Voulez-vous afficher tous les messages à l'écran? ('y' pour oui, n'importe quoi d'autre pour non) ")
    temperatures : list[float] = []
    niveaux_poussiere : list[str] = []
    niveaux_humiditie : list[float] = []
    for i in range(nb_ordi):
        print(f"Ordinateur {i + 1}".center(30, '-'))
        while True: # Input température
            try:
                temp = float(input("Entrez la température (dégres celsius): "))
            except ValueError:  # Gestion d'erreur
                print("Il faut entrer un nombre!")
                continue
            break  # Vérificatilon des conditions supplémentaires

        while True: # Input poussière
            poussiere = input("Entrez le niveau de poussière ('faible', 'moyen', 'élevé'): ").lower()
            if poussiere not in ("faible", "moyen", "élevé"):
                print("Niveau de poussière invalide! Les valeurs valides sont 'faible', 'moyen' et 'élevé'.")
            else:
                break
        while True:
            try:
                humidite = float(input("Entrez l'humidité (pourcentage): "))
            except ValueError:
                print("Il faut entrer un nombre réel")
                continue
            if 0 <= humidite <= 100:
                break
            else:
                print("L'humiditié doit se trouver entre 0% et 100%!")
        temperatures.append(temp)
        niveaux_poussiere.append(poussiere)
        niveaux_humiditie.append(humidite)
    print("*" * 30)
    for i in range(nb_ordi):
        print(f"Ordinateur {i + 1}: ")
        resultat : bool = environnement_optimal(temperatures[i], niveaux_poussiere[i], niveaux_humiditie[i], doit_afficher_messages)
        if not doit_afficher_messages:
            print("Tout est sous contrôle!" if resultat else "Environnement non optimal")
        print("*" * 30)

if __name__ == "__main__":
    main()
