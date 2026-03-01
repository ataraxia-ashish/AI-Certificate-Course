while True:
    print("Menu for Sports equipment : ")
    print("1. Football")
    print("2. Cricket ")
    print("3. Chess ")
    print("4. Tennis ")
    print("5. Hockey")
    print("6. Exit")
    choice = int(input("Select Sports : "))
    if choice == 6:
        print("Exiting program : ")
    elif choice > 6:
        print("Invalid choice !! ")
    else :
        match choice: 
        case 1 :
        print("Here are the Football equipments Menu : ")
    print("1. Football ball $ 10  ")
    print("2. Shoes $ 5")
    print("3. Socks $ 2")
    print("4. Wrist band  $ 3")
    print("5. Exit")
    choice_football = input("Enter equipment you want to purchase : ")
    if choice_football == 5:
        print("Exiting program : ")
    elif choice_football > 5:
        print("Invalid choice !! ")
    else :
        match choice_football: 
        case 1 :
        print("The football ball purchased has been confirmed")
        case 2 :
        print("The shoes purchased has been confirmed")
        case 3 :
        print("The Socks purchased has been confirmed")
        case 4 :
        print("The Wrist band purchased has been confirmed")
        

        case 2 :
        print("Here are the Cricket equipments : ")
        print("1. Cricket ball $ 10  ")
    print("2. Cricket bat $ 50")
    print("3. Elbow guard $ 5")
    print("4. Pads  $ 7")
    print("5. Exit")
    choice_cricket = input("Enter equipment you want to purchase : ")
    if choice_cricket == 5:
        print("Exiting program : ")
    elif choice_cricket > 5:
        print("Invalid choice !! ")
    else :
        match choice_cricket: 
        case 1 :
        print("The cricket ball purchased has been confirmed")
        case 2 :
        print("The cricket bat purchased has been confirmed")
        case 3 :
        print("The elbow guard purchased has been confirmed")
        case 4 :
        print("The pads purchased has been confirmed")

        case 3 :
        print("Here are the Chess equipments : ")
        print("1. Chess board $ 10  ")
    print("2. Extra queen piece $ 2")
    print("3. Extra pieces $ 1")
    print("4. Board brush  $ 3")
    print("5. Exit")
    choice_chess = input("Enter equipment you want to purchase : ")
    if choice_chess == 5:
        print("Exiting program : ")
    elif choice_chess > 5:
        print("Invalid choice !! ")
    else :
        match choice_chess: 
        case 1 :
        print("The chess board purchased has been confirmed")
        case 2 :
        print("The extra queen purchased has been confirmed")
        case 3 :
        print("The extra other pieces purchased has been confirmed")
        case 4 :
        print("The board brush purchased has been confirmed")


        case 4 :
        print("Here are the Tennis equipments : ")
        print("1. Tennis racket $ 10  ")
    print("2. Tennis ball $ 2")
    print("3. Tennis net $ 1")
    print("4. wrist band  $ 3")
    print("5. Exit")
    choice_tennis = input("Enter equipment you want to purchase : ")
    if choice_tennis == 5:
        print("Exiting program : ")
    elif choice_tennis > 5:
        print("Invalid choice !! ")
    else :
        match choice_tennis: 
        case 1 :
        print("The Tennis racket purchased has been confirmed")
        case 2 :
        print("The tennis ball purchased has been confirmed")
        case 3 :
        print("The Tennis net purchased has been confirmed")
        case 4 :
        print("The wrist band purchased has been confirmed")
        
        case 5 :
        print("Here are the Hockey equipments : ")
        print("1. Hockey stick $ 10  ")
    print("2. Puck $ 2")
    print("3. Gloves $ 1")
    print("4. Helmet  $ 3")
    print("5. Exit")
    choice_hockey = input("Enter equipment you want to purchase : ")
    if choice_hockey == 5:
        print("Exiting program : ")
    elif choice_hockey > 5:
        print("Invalid choice !! ")
    else :
        match choice_hockey: 
        case 1 :
        print("The Hockey stick purchased has been confirmed")
        case 2 :
        print("The puck purchased has been confirmed")
        case 3 :
        print("The Gloves purchased has been confirmed")
        case 4 :
        print("The Helmet purchased has been confirmed")
