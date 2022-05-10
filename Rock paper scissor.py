import random
Computer_choice = random.choice(['Rock','Paper','Sissor'])
choice =int(input("Enter your the number\n1.Rock\n2.Paper\n3.Sissor\n"))
if choice == 1:
    print("You have entered Rock")
    user_choice = 'Rock'
elif choice == 2:
    print("You have entered paper")
    user_choice = 'Paper'
elif choice == 3:
    print("You have entered Sissor")
    user_choice = 'Sissor'

if Computer_choice == user_choice:
    print("TIE \n Computer selected"" " +Computer_choice)
elif Computer_choice== 'Rock' and user_choice== 'Paper':
    print("you won,Computer selected"" " +Computer_choice)
elif Computer_choice == 'Paper' and user_choice== 'Sissor':
    print("you won,Computer selected"" " +Computer_choice)
elif Computer_choice == 'Sissor' and user_choice== 'Rock':
    print("you won,Computer selected"" " +Computer_choice)
else:
    print("you lost :-( computer has selected"" "+str(Computer_choice))