score = 0
rr = ("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣠⠤⠶⠶⠤⠴⢤⠶⠤⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡞⠉⠁⣴⡆⣸⣿⣿⣿⣿⠛⣷⣌⡻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠘⠿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣮⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⣀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⢈⣽⣿⣿⠟⠛⠛⠉⠛⠉⠁⠀⠀⠀⠘⢻⣿⣧⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢥⣼⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⢘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⣀⣀⣀⣠⣄⠀⠀⢠⣤⣄⣀⠀⣿⡿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⢿⣿⡇⠀⠻⣿⣭⣽⢹⣇⠀⠘⣿⣶⣮⠟⢹⣇⢛⡁⠀-- Never gonna give you up⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣘⣿⡇⠀⠚⠉⠀⠂⠈⣙⠀⠀⠈⠀⠀⠀⣘⣻⠿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡺⣧⠈⢷⡄⠀⠀⠀⠀⢠⣶⣤⠀⢠⡄⢀⡄⢸⣿⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣽⣶⣾⣄⡀⠀⠀⠀⢘⣇⣉⣀⡀⠃⠘⣶⢫⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠈⣿⣇⠀⠀⠀⢿⡿⡶⢿⣟⣠⣤⣏⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢹⡽⠆⠀⠀⢀⡽⠷⢶⣶⠶⣯⣯⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⢸⣷⠀⠀⠀⠀⢀⣠⢿⣿⡀⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣾⣿⣿⢸⣿⠀⠀⠀⠀⠈⠁⣸⡏⡷⣏⢻⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣿⣿⣿⣿⣿⣿⡆⠻⣆⢠⠂⣠⣀⣰⣟⣻⣯⣸⠈⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠙⢧⡀⠀⠀⠸⣯⣿⣿⣽⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀
⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣄⠈⢻⣄⠀⠀⢩⣟⡈⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠀⠀⠈⠓⠶⠿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣦⡔⠶⠶⢦⣤⣤⠀⠀⣤⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢰⣼⠿⠿⣿⣿⣿⣿⠛⠛⠒⠶⠶⠶⢤⣠⣬⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⡞⣿⠉⠈⠀⠛⠻⢿⣿⣟⠛⠓⠒⠶⠶⢾⣧⣶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢹⣇⢻⣿⣿⣿⣿⣿⣿⣿⣿⠇⢾⠃⠙⠓⠒⠰⣴⣶⣾⣿⣿⠛⠛⠛⠒⠒⢻⠠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣸⠀⠀⠀⣤⠀⠈⢻⣿⣿⣿⡛⠛⠛⠛⠒⠚⠶⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠁⠀⠈⠀⢬⣤⣶⣿⣿⣿⣿⣟⠉⠛⠛⠛⣿⡾⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
q1 = ("You are in the final round of a gameshow. There are 3 doors to choose, but only one wiil get you to the new 'Flying Tesla'")
print(q1)
print("1 : Door 1")
print("2 : Door 2")
print("3 : Door 3")
ans = int(input("Which door would you choose to open? "))
if ans == 1:
        print("\n")
        print("The host now opens a different door. But, it is empty inside.")
        print("====================\n")
        yolo = input("Would you like to switch or keep your current door? (S/K) ")
        if yolo == 's':
                print("CONGRATULATIONS! YOU WON THE CAR!!")
                print("====================\n")
                yn = input("Now, do you like to check what is in the remaining door? ")
                if yn == "y":
                        print(rr)
                else:
                        print("====================\n")
                        print("Oh well, you just won the car. So why care anyway huh :D")
        else:
                print(rr)
                
elif ans == 3:
        print("\n")
        print("The host now opens a different door. But, it is empty inside.")
        print("====================\n")
        bru = input("Would you like to switch or keep your current door? (s/k) ")
        if bru == 's':
                print("CONGRATULATIONS! YOU WON THE CAR!!")
                print("====================\n")
                hehe = input("Now, do you like to check what is in the remaining door? (y/n) ")
                if hehe == 'y':
                        print(rr)
                else:
                        print("====================\n")
                        print("Oh well, you just won the car. So why care anyway huh :D")
        else:
                print(rr)
else:
        print("====================\n")
        print("CONGRATULATIONS! YOU WON THE CAR!!")
        print("\n")
        uhu = input("Now, shall we check what is in the remaining door? (y/n) ")
        if uhu == 'y':
                print(rr)
        else:
                print("====================\n")
                print("That's fine too. You won anyway, friend :D")
