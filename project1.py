start = input("This is a text adeventure, first up you need to choose the weapon: dagger, sword or short club. Choose wisely\n")

if start.lower() == "dagger" or start.lower() == "short club":
    choice2 = input("You waited until the guard open their door for a meal and then knocked them out with their weapon.\nYou see a crossroad, choose either you prefer going right or left.\n")

    try:
        if choice2.lower() == "right":
            print("You ran into some guards and failed their mission.")

        else:
            choice3 = input("There are 5 doors labeled 1-5\nPick one you want to walk through.\n")

            try:
                if int(choice3) != 4:
                    choice4 = input("You have to choose either going down or up the stairs.\n")

                    try:
                        if choice4.lower() == "down":
                            print("You failed the mission.")

                        else:
                            choice5 = input("There are two guards waiting for them on the right corridor. You can either fight the guards or run left.\n")
                            try:
                                if choice5.lower() == "fight":
                                    print("You managed to take down the guards using your wits and abilities and escaped the dungeon. \nCongratulation!!")
                                else:
                                    print("You ran into 5 more guards and was promptly put back into their cell, failing the mission.")

                            except:
                                pass    
                    except:
                        pass
                else:
                    print("You walked straight into the guards' living quarters and was promptly put back in the dungeon.")

            except:
                pass
    except:
        pass

elif start.lower() == "sword":
    print("The guard saw the sword when he walked in because it was so big and called in reinforcements, and the user's escape failed.")