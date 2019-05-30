import random
PlayerName=input("What is your name?")
print("Welcome to Clash Of Gladiators, "+PlayerName+"! You're a gladiator being put into fight today!")
def start():
    print("Note: The Clashes are in a storyline, so if you pick one further on, you will have everything from the list")
    print("that you have in the storyline! Now, choose! VVV")
    BattleChoice=input("What Battle would you like to fight? (please type the number of the battle of your choice(1-5, or Local)")
    def LocalBattle():
        class Character:
            def __init__(self, name, health):
                self.health=health
                self.name=name
        class Attack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-5), (damage+5))
                self.critical_damage=critical_damage
        while True:
            print("Welcome to Local Battle! This is a mode where you fight someone on one computer!")
            yesno=input("Do you want to play?(You can type no if you have no friends!)")
            if yesno.lower()=="yes":
                print("Lets get started!")
                health=True
                break
            elif yesno.lower()=="no":
                print("Okay! See ya!")
                start()
                break
            else:
                print("Sorry, I didn't understand you!")
                print("Type yes or no:")
        while True:
            player1name=input("Player 1! Please enter your name!")
            player2name=input("Player 2! Plaese enter your name!")
            if player1name==player2name:
                print("Please type different names!")
            elif player1name!=player2name:
                break
        
        while health:
            try:
                player1health=int(input(player1name+", please type your desired health!"))
                player2health=int(input(player2name+", please type your desired health!"))
                if player1health<=0 or player2health<=0:
                    print("You can't have a health of 0 or less than 0 or you would be dead!")
                else:
                    health=False
                    Stats=True
            except:
                print("Please type a number!")
        player1=Character(player1name, player1health)
        player2=Character(player2name, player2health)
        Attacks=["Sword Slash", "Jump Jab", "Fireball", "Lightningbolt", "Weaken", "Blinding Light", "Heal"]
        HealCount1=0
        HealCount2=0
        Blind1=False
        Blind2=False
        unconscious1=False
        unconscious2=False
        unconsciousturncount1=0
        unconsciousturncount2=0
        weaken1=0
        weaken2=0
        Stats=True
        while Stats:
            try:
                swordslashdamage1=int(input(player1.name+", how much damage would you like SwordSlash to do?"))
                swordslashdamage2=int(input(player2.name+", how much damage would you like SwordSlash to do?"))
                jumpjabdamage1=int(input(player1.name+", how much damage would you like JumpJab to do?"))
                jumpjabdamage2=int(input(player2.name+", how much damage would you like JumpJab to do?"))
                fireballdamage1=int(input(player1.name+", how much damage would you like Fireball to do?"))
                fireballdamage2=int(input(player2.name+", how much damage would you like Fireball to do?"))
                lightningboltturns=int(input("Please decide how many turns you want the lightningbolt to knock players out for:"))
                weakenweaken=int(input("Please decide how much damage you want like Weaken to get rid of:"))
                weakendamage1=int(input(player1.name+", how much damage would you like Weaken to do?"))
                weakendamage2=int(input(player2.name+", how much damage would you like Weaken to do?"))
                blindinglightdamage1=int(input(player1.name+", how much damage would you like Blinding Light to do?"))
                blindinglightdamage2=int(input(player2.name+", how much damage would you like Blinding Light to do?"))
                healdamage1=int(input(player1.name+", how much damage would you like Heal to heal?"))
                healdamage2=int(input(player2.name+", how much damage would you like Heal to heal?"))
                criticalchoice=int(input("How much more damage should the critical hits do?"))
                damageforattackslist=[swordslashdamage1, swordslashdamage2, jumpjabdamage1, jumpjabdamage2, fireballdamage1, fireballdamage2, lightningboltturns, weakenweaken, weakendamage1, weakendamage2, blindinglightdamage1, blindinglightdamage2, healdamage1, healdamage2, criticalchoice]
                for x in damageforattackslist:
                    if x<0:
                        Go=False
                        break
                    elif x>0:
                        Go=True
                        SwordSlash1=Attack("swordslash", swordslashdamage1, (swordslashdamage1+criticalchoice))
                        SwordSlash2=Attack("swordslash", swordslashdamage2, (swordslashdamage2+criticalchoice))
                        JumpJab1=Attack("jumpjab", jumpjabdamage1, (jumpjabdamage1+criticalchoice))
                        JumpJab2=Attack("jumpjab", jumpjabdamage2, (jumpjabdamage2+criticalchoice))
                        Fireball1=Attack("fireball", fireballdamage1, (fireballdamage1+criticalchoice))
                        Fireball2=Attack("fireball", fireballdamage2, (fireballdamage2+criticalchoice))
                        Lightningbolt=Attack("lightningbolt", 0, 0)
                        Weaken1=Attack("weaken", weakendamage1, (weakendamage1+criticalchoice))
                        Weaken2=Attack("weaken", weakendamage2, (weakendamage2+criticalchoice))
                        BlindingLight1=Attack("blindinglight", blindinglightdamage1, (blindinglightdamage1+criticalchoice))
                        BlindingLight2=Attack("blindinglight", blindinglightdamage2, (blindinglightdamage2+criticalchoice))
                        Heal1=Attack("heal", healdamage1, (healdamage1+criticalchoice))
                        Heal2=Attack("heal", healdamage2, (healdamage2+criticalchoice))
                if Go==True:
                    run=True
                    Stats=False
                    print("That's all the stats set, now it's time to BATTLE!")
                    break
                elif Go==False:
                    print("Please do not use negatives. It will cause problems!")
            except:
                print("Please type numbers!")
        print("Local Battle! "+player1.name+" Vs. "+player2.name+"!")
        while run:
            if not unconscious1:                                                                     #Player1 Attacks HERE
                if not Blind1:
                    print("It's "+player1.name+"'s turn!")
                    move=input("Here are your attacks:"+str(Attacks)+" Please choose one!").lower()
                    if move=="swordslash" or move=="sword slash":
                        print(player1.name+" used Sword Slash!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance<4:
                            player2.health-=(SwordSlash1.damage-weaken2)
                            print(player1.name+"'s sword met its destination! "+player2.name+"'s health is now "+str(player2.health)+"!")
                        elif hit_chance>7 and not unconscious2:
                            print(player2.name+" dodged your attack at the last second. Better luck next time!")
                            print(player2.name+"'s health is at "+str(player2.health)+"!")
                        else:
                            player2.health-=(SwordSlash1.critical_damage-weaken2)
                            print("WOW! A critical hit! "+player2.name+"'s health is now at"+str(player2.health)+"!")
                    elif move=="jumpjab" or move=="jump jab":
                        print(player1.name+" used Jump Jab!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance<4:
                            player2.health-=(JumpJab1.damage-weaken2)
                            print(player1.name+"'s sword met its destination! "+player2.name+"'s health is now "+str(player2.health)+"!")
                        elif hit_chance>8 and not unconscious2:
                            print(player2.name+" dodged your attack at the last second. Better luck next time!")
                            print(player2.name+"'s health is at "+str(player2.health)+"!")
                        else:
                            player2.health-=(JumpJab1.critical_damage-weaken2)
                            print("WOW! A critical hit! "+player2.name+"'s health is now "+str(player2.health)+"!")
                    elif move=="fireball" or move=="fire ball":
                        print(player1.name+" used Fireball!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance<6:
                            player2.health-=(Fireball1.damage-weaken2)          
                            print(player1.name+"'s Fireball hit "+player2.name+"! "+player2.name+"'s health is at "+str(player2.health)+"!")
                        elif hit_chance>=6 and hit_chance<8 and not unconscious2:
                            print(player2.name+" was to fast!")
                        else:
                            player2.health-=(Fireball1.critical_damage-weaken2)
                            print("Critical hit! Good job! "+player2.name+"'s health is now "+str(player2.health)+"!")
                    elif move=="lightningbolt" or move=="lightning bolt":
                        chance=random.randint(1, 10)
                        if unconscious2==False:
                            print(player1.name+" used Lightningbolt!")
                            print("Lightningbolt knocks out the opponent for 2 turns, but doesn't do any damage.")
                            if chance>5:
                                print("The lightningbolt hit! "+player2.name+"'s health is at "+str(player2.health)+"!")
                                unconscious2=True
                            else:
                                print("Oh no, the lightningbolt missed! "+player2.name+"'s health is at "+str(player2.health)+"!")
                        else:
                            print("You are not alowed to use this move if the enemy is still unconscious.")
                    elif move=="weaken":
                        print(player1.name+" used Weaken!")
                        print("Weaken weakens the opponents attacks.")
                        chance=random.randint(1,10)
                        if chance<3:
                            print("Uh oh! The Weaken didn't work! "+player2.name+"'s health is at "+str(player2.health)+"!")
                        else:
                            weaken1=weakenweaken
                            chance=random.randint(1,10)
                            if chance<7:
                                player2.health-=(Weaken1.damage-weaken2)
                                print("The Weaken also did damage! "+player2.name+"'s health is now at "+str(player2.health)+"!")
                            else:
                                player2.health-=(Weaken1.critical_damage-weaken2)
                                print("The Weaken also did critical damage! "+player2.name+"'s health is at "+str(player2.health)+"!")
                    elif move=="blindinglight" or move=="blinding light":
                        chance=random.randint(1,10)
                        print(player1.name+" used Blinding Light!")
                        print("Blinding Light makes your opponent very blind and have a 10% chance of hitting you.")
                        Blind2=True
                        if chance<4:
                            player2.health-=(BlindingLight1.damage-weaken2)
                            print("The Blinding Light also did damage! "+player2.name+"'s health is now "+str(player2.health)+".")
                        elif chance>=4 and chance<8:
                            player2.health-=(BlindingLight1.damage-weaken2)
                            print("The Blinding Light also did critical damage! "+player2.name+"'s health is now "+str(player2.health)+".")
                        else:
                            print("The Blinding Light didn't do any damage!")
                    elif move=="heal":
                        if HealCount1<3:
                            chance=random.randint(1,10)
                            print(player1.name+" used Heal!")
                            print("Note: You can only heal 3 times in each Battle regardless of wheather the heal works or not.")
                            HealCount1+=1
                            if chance<5:
                                player1.health+=(Heal1.damage-weaken2)
                                print("The Heal worked! "+player1.name+"'s health is now at "+str(player1.health)+"!")
                            elif chance>=5 and chance<8:
                                player1.health+=(Heal1.critical_damage-weaken2)
                                print("The Heal worked extra well! "+player1.name+"'s health is now at "+str(player1.health)+"!")
                            else:
                                print("The Heal didn't work at all! "+player1.name+"'s health is at "+str(player1.health)+"!")
                        else:
                            print("You can't use heal more than 3 times. You turn has been skipped.")
                    else:
                        print("That is not a valid attack choice. Skipping your turn.")
                elif Blind1:
                    print("It's "+player1.name+"'s turn!")
                    print(player1.name+" is blind!")
                    move=input("Here are your attacks:"+str(Attacks)+" Please choose one!").lower()
                    if move=="swordslash" or move=="sword slash":
                        print(player1.name+" used Sword Slash!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance==4:
                            player2.health-=(SwordSlash1.damage-weaken2)
                            print(player1.name+"'s sword met its destination! "+player2.name+"'s health is now "+str(player2.health)+"!")
                        else:
                            print("What a miss!")
                    elif move=="jumpjab" or move=="jump jab":
                        print(player1.name+" used Jump Jab!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance==7:
                            player2.health-=(JumpJab1.damage-weaken2)
                            print(player1.name+"'s sword met its destination! "+player2.name+"'s health is now "+str(player2.health)+"!")
                        else:
                            print("Blindness caused a miss! Such a shame!")
                    elif move=="fireball" or move=="fire ball":
                        print(player1.name+" used Fireball!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance==6:
                            player2.health-=(Fireball1.damage-weaken2)          
                            print(player1.name+"'s Fireball hit "+player2.name+"! "+player2.name+"'s health is at "+str(player2.health)+"!")
                        else:
                            print("Miss!")
                    elif move=="lightningbolt" or move=="lightning bolt":
                        chance=random.randint(1, 10)
                        if unconscious2==False:
                            print(player1.name+" used Lightningbolt!")
                            print("Lightningbolt knocks out the opponent for 2 turns, but doesn't do any damage.")
                            if chance==5:
                                print("The lightningbolt hit! "+player2.name+"'s health is at "+str(player2.health)+"!")
                                unconscious2=True
                            else:
                                print("Oh no, the lightningbolt missed! "+player2.name+"'s health is at "+str(player2.health)+"!")
                        else:
                            print("You are not alowed to use this move if the enemy is still unconscious.")
                    elif move=="weaken":
                        print(player1.name+" used Weaken!")
                        print("Weaken weakens the opponents attacks.")
                        chance=random.randint(1,10)
                        Weaken1=weakenweaken
                        if chance==3:
                            player2.health-=(Weaken1.damage-weaken2)
                            print("The Weaken also did damage! "+player2.name+"'s health is now at "+str(player2.health)+"!")
                        else:
                            print("The Weaken didn't do any additional damage!")
                    elif move=="blindinglight" or move=="blinding light":
                        chance=random.randint(1,10)
                        print(player1.name+" used Blinding Light!")
                        print("Blinding Light makes your opponent very blind and have a 10% chance of hitting you.")
                        Blind2=True
                        if chance==4:
                            player2.health-=(BlindingLight1.damage-weaken2)
                            print("The Blinding Light also did damage! "+player2.name+"'s health is now "+str(player2.health)+".")
                        else:
                            print("The Blinding Light didn't do any damage!")
                    elif move=="heal":
                        if HealCount1<3:
                            chance=random.randint(1,10)
                            print(player1.name+" used Heal!")
                            print("Note: You can only heal 3 times in each Battle regardless of wheather the heal works or not.")
                            HealCount1+=1
                            if chance==7:
                                player1.health+=(Heal1.damage-weaken2)
                                print("The Heal worked! "+player1.name+"'s health is now at "+str(player1.health)+"!")
                            else:
                                print("The Heal didn't work at all! "+player1.name+"'s health is at "+str(player1.health)+"!")
                        else:
                            print("You can't use heal more than 3 times. You turn has been skipped.")
                    else:
                        print("That is not a valid attack choice. Skipping your turn.")
            else:
                unconsciousturncount1+=1
                if unconsciousturncount1==lightningboltturns:
                    unconsciousturncount1=0
                    unconscious1=False
                    print(player1.name+" will wake up after the next turn!")
                else:
                    print(player1.name+" is unconscious!")
            weaken2=0
            Blind1=False
            if player2.health<=0:
                print(player1.name+" has won!")
                yesno=input("Rematch?")
                if yesno=="yes":
                    print("Here we go!")
                elif yesno=="no":
                    print("Okay!")
                    break
                else:
                    print("I didn't understand you! To the menu we go!")
                    break
            elif player1.health<=0:
                print(player2.name+" has won!")
                yesno=input("Rematch?")
                if yesno=="yes":
                    print("Here we go!")
                elif yesno=="no":
                    print("Okay!")
                    break
                else:
                    print("I didn't understand you! To the menu we go!")
                    break
            if not unconscious2:                                                                     #Player2 Attacks HERE
                if not Blind2:
                    print("It's "+player2.name+"'s turn!")
                    move=input("Here are your attacks:"+str(Attacks)+" Please choose one!").lower()
                    if move=="swordslash" or move=="sword slash":
                        print(player2.name+" used Sword Slash!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance<4:
                            player1.health-=(SwordSlash2.damage-weaken1)
                            print(player2.name+"'s sword met its destination! "+player1.name+"'s health is now "+str(player1.health)+"!")
                        elif hit_chance>7 and not unconscious1:
                            print(player1.name+" dodged your attack at the last second. Better luck next time!")
                            print(player1.name+"'s health is at "+str(player1.health)+"!")
                        else:
                            player1.health-=(SwordSlash2.critical_damage-weaken1)
                            print("WOW! A critical hit! "+player1.name+"'s health is now at"+str(player1.health)+"!")
                    elif move=="jumpjab" or move=="jump jab":
                        print(player2.name+" used Jump Jab!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance<4:
                            player1.health-=(JumpJab2.damage-weaken1)
                            print(player2.name+"'s sword met its destination! "+player1.name+"'s health is now "+str(player1.health)+"!")
                        elif hit_chance>8 and not unconscious1:
                            print(player1.name+" dodged your attack at the last second. Better luck next time!")
                            print(player1.name+"'s health is at "+str(player1.health)+"!")
                        else:
                            player1.health-=(JumpJab2.critical_damage-weaken1)
                            print("WOW! A critical hit! "+player1.name+"'s health is now "+str(player1.health)+"!")
                    elif move=="fireball" or move=="fire ball":
                        print(player2.name+" used Fireball!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance<6:
                            player1.health-=(Fireball2.damage-weaken1)          
                            print(player2.name+"'s Fireball hit "+player1.name+"! "+player1.name+"'s health is at "+str(player1.health)+"!")
                        elif hit_chance>=6 and hit_chance<8 and not unconscious1:
                            print(player1.name+" was to fast!")
                        else:
                            player1.health-=(Fireball2.critical_damage-weaken1)
                            print("Critical hit! Good job! "+player1.name+"'s health is now "+str(player1.health)+"!")
                    elif move=="lightningbolt" or move=="lightning bolt":
                        chance=random.randint(1, 10)
                        if unconscious1==False:         
                            print(player2.name+" used Lightningbolt!")
                            print("Lightningbolt knocks out the opponent for 2 turns, but doesn't do any damage.")
                            if chance>5:
                                print("The lightningbolt hit! "+player1.name+"'s health is at "+str(player1.health)+"!")
                                unconscious1=True
                            else:
                                print("Oh no, the lightningbolt missed! "+player1.name+"'s health is at "+str(player1.health)+"!")
                        else:
                            print("You are not alowed to use this move if the enemy is still unconscious.")
                    elif move=="weaken":
                        print(player2.name+" used Weaken!")
                        print("Weaken weakens the opponents attacks.")
                        chance=random.randint(1,10)
                        if chance<3:
                            print("Uh oh! The Weaken didn't work! "+player1.name+"'s health is at "+str(player1.health)+"!")
                        else:
                            weaken2=weakenweaken
                            chance=random.randint(1,10)
                            if chance<7:
                                player1.health-=(Weaken2.damage-weaken1)
                                print("The Weaken also did damage! "+player1.name+"'s health is now at "+str(player1.health)+"!")
                            else:
                                player1.health-=(Weaken2.critical_damage-weaken1)
                                print("The Weaken also did critical damage! "+player1.name+"'s health is at "+str(player1.health)+"!")
                    elif move=="blindinglight" or move=="blinding light":
                        chance=random.randint(1,10)
                        print(player2.name+" used Blinding Light!")
                        print("Blinding Light makes your opponent very blind and have a 10% chance of hitting you.")
                        Blind1=True
                        if chance<4:
                            player1.health-=(BlindingLight2.damage-weaken1)
                            print("The Blinding Light also did damage! "+player1.name+"'s health is now "+str(player1.health)+".")
                        elif chance>=4 and chance<8:
                            player1.health-=(BlindingLight2.damage-weaken1)
                            print("The Blinding Light also did critical damage! "+player1.name+"'s health is now "+str(player1.health)+".")
                        else:
                            print("The Blinding Light didn't do any damage!")
                    elif move=="heal":
                        if HealCount2<3:
                            chance=random.randint(1,10)
                            print(player2.name+" used Heal!")
                            print("Note: You can only heal 3 times in each Battle regardless of wheather the heal works or not.")
                            HealCount2+=1
                            if chance<5:
                                player2.health+=(Heal2.damage-weaken1)
                                print("The Heal worked! "+player2.name+"'s health is now at "+str(player2.health)+"!")
                            elif chance>=5 and chance<8:
                                player2.health+=(Heal2.critical_damage-weaken1)
                                print("The Heal worked extra well! "+player2.name+"'s health is now at "+str(player2.health)+"!")
                            else:
                                print("The Heal didn't work at all! "+player2.name+"'s health is at "+str(player2.health)+"!")
                        else:
                            print("You can't use heal more than 3 times. You turn has been skipped.")
                    else:
                        print("That is not a valid attack choice. Skipping your turn.")
                elif Blind2:
                    print("It's "+player2.name+"'s turn!")
                    print(player2.name+" is blind!")
                    move=input("Here are your attacks:"+str(Attacks)+" Please choose one!").lower()
                    if move=="swordslash" or move=="sword slash":
                        print(player2.name+" used Sword Slash!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance==4:
                            player1.health-=(SwordSlash2.damage-weaken1)
                            print(player2.name+"'s sword met its destination! "+player1.name+"'s health is now "+str(player1.health)+"!")
                        else:
                            print("What a miss!")
                    elif move=="jumpjab" or move=="jump jab":
                        print(player2.name+" used Jump Jab!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance==7:
                            player1.health-=(JumpJab2.damage-weaken1)
                            print(player2.name+"'s sword met its destination! "+player1.name+"'s health is now "+str(player1.health)+"!")
                        else:
                            print("Blindness caused a miss! Such a shame!")
                    elif move=="fireball" or move=="fire ball":
                        print(player2.name+" used Fireball!")
                        hit_chance=random.randint(1, 10)
                        if hit_chance==6:
                            player1.health-=(Fireball2.damage-weaken1)          
                            print(player2.name+"'s Fireball hit "+player1.name+"! "+player1.name+"'s health is at "+str(player1.health)+"!")
                        else:
                            print("Miss!")
                    elif move=="lightningbolt" or move=="lightning bolt":
                        chance=random.randint(1, 10)
                        if unconscious1==False:
                            print(player2.name+" used Lightningbolt!")
                            print("Lightningbolt knocks out the opponent for 2 turns, but doesn't do any damage.")
                            if chance==5:
                                print("The lightningbolt hit! "+player1.name+"'s health is at "+str(player1.health)+"!")
                                unconscious1=True
                            else:
                                print("Oh no, the lightningbolt missed! "+player1.name+"'s health is at "+str(player1.health)+"!")
                        else:
                            print("You are not alowed to use this move if the enemy is still unconscious.")
                    elif move=="weaken":
                        print(player2.name+" used Weaken!")
                        print("Weaken weakens the opponents attacks.")
                        chance=random.randint(1,10)
                        if chance==3:
                            player1.health-=(Weaken2.damage-weaken1)
                            print("The Weaken also did damage! "+player1.name+"'s health is now at "+str(player1.health)+"!")
                        else:
                            print("The Weaken didn't do any additional damage!")
                    elif move=="blindinglight" or move=="blinding light":
                        chance=random.randint(1,10)
                        print(player2.name+" used Blinding Light!")
                        print("Blinding Light makes your opponent very blind and have a 10% chance of hitting you.")
                        Blind1=True
                        if chance==4:
                            player1.health-=(BlindingLight2.damage-weaken1)
                            print("The Blinding Light also did damage! "+player1.name+"'s health is now "+str(player1.health)+".")
                        else:
                            print("The Blinding Light didn't do any damage!")
                    elif move=="heal":
                        if HealCount2<3:
                            chance=random.randint(1,10)
                            print(player2.name+" used Heal!")
                            print("Note: You can only heal 3 times in each Battle regardless of wheather the heal works or not.")
                            HealCount2+=1
                            if chance==7:
                                player2.health+=(Heal2.damage-weaken1)
                                print("The Heal worked! "+player2.name+"'s health is now at "+str(player2.health)+"!")
                            else:
                                print("The Heal didn't work at all! "+player2.name+"'s health is at "+str(player2.health)+"!")
                        else:
                            print("You can't use heal more than 3 times. You turn has been skipped.")
                    else:
                        print("That is not a valid attack choice. Skipping your turn.")
            else:
                unconsciousturncount2+=1
                if unconsciousturncount2==lightningboltturns:
                    unconsciousturncount2=0
                    unconscious2=False
                    print(player2.name+" will wake up after the next turn!")
                else:
                    print(player2.name+" is unconscious!")
            Blind2=False
            weaken1=0
            if player2.health<=0:
                print(player1.name+" has won!")
                yesno=input("Rematch?")
                if yesno=="yes":
                    print("Here we go!")
                elif yesno=="no":
                    print("Okay!")
                    break
                else:
                    print("I didn't understand you! To the menu we go!")
                    break
            elif player1.health<=0:
                print(player2.name+" has won!")
                yesno=input("Rematch?")
                if yesno=="yes":
                    print("Here we go!")
                elif yesno=="no":
                    print("Okay!")
                    break
                else:
                    print("I didn't understand you! To the menu we go!")
                    break
    def Battle1():
        class Character:
            def __init__(self, name, health):
                self.health=health
                self.name=name
        class Attack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-5), (damage+5))
                self.critical_damage=critical_damage
        class EnemyAttack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-5),(damage+5))
                self.critical_damage=critical_damage
        Attacks=["Sword Slash", "Jump Jab"]
        SwordSlash=Attack("swordslash", 10, 23)
        JumpJab=Attack("jumpjab", 15, 24)
        player=Character(PlayerName, 50)
        Enemy1=Character("Swordsman", 50)
        Stab=EnemyAttack("stab", 12, 21)
        Uppercut=EnemyAttack("uppercut", 20, 22)
        print("Battle 1! Welcome "+player.name+" to the battle! He will be fighting "+Enemy1.name+"!")
        print("You have "+str(player.health)+" health. The Swordsman has "+str(Enemy1.health)+" health.")
        Battle1=True
        while Battle1:
            move=input("Here are your attacks:"+str(Attacks)+" Please choose one!").lower()
            if move=="swordslash" or move=="sword slash":
                print("You used Sword Slash!")
                hit_chance=random.randint(0, 10)
                if hit_chance<4:
                    Enemy1.health-=SwordSlash.damage
                    print("Your sword met its destination! The "+Enemy1.name+"'s health is now "+str(Enemy1.health)+"!")
                elif hit_chance>7:
                    print("The "+Enemy1.name+" dodged your attack at the last second. Better luck next time!")
                    print("The "+Enemy1.name+"'s health is at "+str(Enemy1.health)+"!")
                else:
                    Enemy1.health-=SwordSlash.critical_damage
                    print("WOW! A critical hit! The "+Enemy1.name+"'s health is now "+str(Enemy1.health)+"!")
            elif move=="jumpjab" or move=="jump jab":
                print("You used Jump Jab!")
                hit_chance=random.randint(0, 10)
                if hit_chance<4:
                    Enemy1.health-=JumpJab.damage
                    print("Your sword met its destination! The "+Enemy1.name+"'s health is now "+str(Enemy1.health)+"!")
                elif hit_chance>8:
                    print("The "+Enemy1.name+" dodged your attack at the last second. Better luck next time!")
                    print("The "+Enemy1.name+"'s health is at "+str(Enemy1.health)+"!")
                else:
                    Enemy1.health-=JumpJab.critical_damage
                    print("WOW! A critical hit! The "+Enemy1.name+"'s health is now "+str(Enemy1.health)+"!")
            else:
                print("That is not a valid attack choice. Skipping your turn.")
            if player.health<=0:
                print("You died! Restarting the game...")
                start()
                break
            elif Enemy1.health<=0:
                print("You defeated the "+Enemy1.name+"! Good job! Getting Battle 2 ready...")
                Battle2()
                break
            enemychance=random.randint(0, 10)
            if enemychance<4:
                print("The "+Enemy1.name+" used Uppercut!")
                enemy_critical_chance=random.randint(0, 10)
                if enemy_critical_chance<5:
                    player.health-=Uppercut.damage
                    print("The uppercut hit you. Your health is now "+str(player.health)+".")
                elif enemy_critical_chance>=5 and enemy_critical_chance<9:
                    print("Wow! You dodged the uppercut! Good job! Your health is at "+str(player.health)+".")
                else:
                    player.health-=Uppercut.critical_damage
                    print("Oooh! That uppercut hit you hard! Your health is now "+str(player.health)+".")
            else:
                print("The "+Enemy1.name+" used Stab!")
                enemy_critical_chance=random.randint(0, 10)
                if enemy_critical_chance<5:
                    player.health-=Stab.damage
                    print("The "+Enemy1.name+" stabbed you. Your health is at "+str(player.health)+".")
                elif enemy_critical_chance>=5 and enemy_critical_chance<8:
                    print("Nice dodging skills you have there! Your health is at "+str(player.health)+".")
                else:
                    player.health-=Stab.critical_damage
                    print("Are you okay there? That stab was critical! Your health is at "+str(player.health)+".")
            if player.health<=0:
                print("You died! Restarting the game...")
                start()
                break
            elif Enemy1.health<=0:
                print("You defeated the "+Enemy1.name+"! Good job! Getting Battle 2 ready...")
                Battle2()
                break
    def Battle2():                                                                                                 #Battle 2!!!!
        class Character:
            def __init__(self, name, health):
                self.health=health
                self.name=name
        class Attack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-3), (damage+7))
                self.critical_damage=critical_damage
        class EnemyAttack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-4),(damage+6))
                self.critical_damage=critical_damage
        Attacks=["Sword Slash", "Jump Jab", "Fireball"]
        SwordSlash=Attack("swordslash", 20, 23)
        JumpJab=Attack("jumpjab", 25, 24)
        Fireball=Attack("fireball", 30, 22)
        player=Character(PlayerName, 110)
        Enemy2=Character("Witchlock", 100)
        PoisonCount=0
        PoisonSwitch=False
        PoisonTurnCount=0
        Poison=EnemyAttack("poison", 10, 0)
        Heal=EnemyAttack("heal", 20, 27)
        Harmful=EnemyAttack("harmful", 25, 32)
        print("Battle 2! Welcome "+player.name+" to the battle! He will be fighting "+Enemy2.name+"!")
        print("You have "+str(player.health)+" health. The "+Enemy2.name+" has "+str(Enemy2.health)+" health.")
        print("You spent days training for this battle. You even learned how to shoot a fireball! You are ready.")
        print("Your attack damage has even increased!")
        Battle2=True
        while Battle2:
            move=input("Here are your attacks:"+str(Attacks)+" Please choose one!").lower()
            if move=="swordslash" or move=="sword slash":
                print("You used Sword Slash!")
                hit_chance=random.randint(0, 10)
                if hit_chance<4:
                    Enemy2.health-=SwordSlash.damage
                    print("Your sword met its destination! The "+Enemy2.name+"'s health is now "+str(Enemy2.health)+"!")
                elif hit_chance>7:
                    print("The "+Enemy2.name+" dodged your attack at the last second. Better luck next time!")
                    print("The "+Enemy2.name+"'s health is at "+str(Enemy2.health)+"!")
                else:
                    Enemy2.health-=SwordSlash.critical_damage
                    print("WOW! A critical hit! The "+Enemy2.name+"'s health is now "+str(Enemy2.health)+"!")
            elif move=="jumpjab" or move=="jump jab":
                print("You used Jump Jab!")
                hit_chance=random.randint(0, 10)
                if hit_chance<4:
                    Enemy2.health-=JumpJab.damage
                    print("Your sword met its destination! The "+Enemy2.name+"'s health is now "+str(Enemy2.health)+"!")
                elif hit_chance>8:
                    print("The "+Enemy2.name+" dodged your attack at the last second. Better luck next time!")
                    print("The "+Enemy2.name+"'s health is at "+str(Enemy2.health)+"!")
                else:
                    Enemy2.health-=JumpJab.critical_damage
                    print("WOW! A critical hit! The "+Enemy2.name+"'s health is now "+str(Enemy2.health)+"!")
            elif move=="fireball" or move=="fire ball":
                print("You used Fireball!")
                hit_chance=random.randint(0, 10)
                if hit_chance<6:
                    Enemy2.health-=Fireball.damage
                    print("Your Fireball hit the "+Enemy2.name+"! The "+Enemy2.name+" health is at "+str(Enemy2.health)+"!")
                elif hit_chance>=6 and hit_chance<8:
                    print("The "+Enemy2.name+" was to fast!")
                else:
                    Enemy2.health-=Fireball.critical_damage
                    print("Critical hit! Good job! The "+Enemy2.name+"'s health is now "+str(Enemy2.health)+"!")
            else:
                print("That is not a valid attack choice. Skipping your turn.")
            if player.health<=0:
                print("You died! Restarting the game...")
                start()
                break
            elif Enemy2.health<=0:
                print("You defeated the "+Enemy2.name+"! Good job! Getting Battle 3 ready...")
                Battle3()
                break
            enemy_critical_chance=random.randint(0, 10)
            if PoisonSwitch and PoisonTurnCount<4:
                player.health-=Poison.damage
                PoisonTurnCount+=1
                print("You are still being poisoned. Your health is now "+str(player.health)+".")
                if PoisonTurnCount==3:
                    PoisonSwitch=False
                    PoisonTurnCount=0
            if enemy_critical_chance<3 and PoisonCount<3 and PoisonSwitch==False:
                PoisonCount+=1
                PoisonSwitch=True
                player.health-=Poison.damage
                print("The "+Enemy2.name+" used poison!")
                print("Poison decreases your health every turn for 3 turns! Your health is now "+str(player.health)+".")
            elif enemy_critical_chance>=3 and enemy_critical_chance<6:
                print("The "+Enemy2.name+" used Heal!")
                hit_chance=random.randint(0, 10)
                if hit_chance<4:
                    Enemy.health+=Heal.damage
                    print("The Heal worked fine! The "+Enemy2.name+"'s health is now "+str(Enemy2.health)+"!")
                elif hit_chance>=4 and hit_chance<7:
                    Enemy.health+=Heal.critical_damage
                    print("The Heal worked awesomely! The "+Enemy2.name+"'s health is now "+str(Enemy2.health)+"!")
                else:
                    print("The Heal didn't work at ALL! The "+Enemy2.name+"'s health is "+str(Enemy2.health)+"!")
            else:
                print("The "+Enemy2.name+" used Harmful!")
                enemy_critical_chance=random.randint(0, 10)
                if enemy_critical_chance<5:
                    player.health-=Harmful.damage
                    print("The Harmful Potion hit you! Your health is now at "+str(player.health)+"!")
                elif enemy_critical_chance>=5 and enemy_critical_chance<8:
                    print("You stepped out of the way of the Harmful Potion! Your health is at "+str(player.health)+".")
                else:
                    player.health-=Harmful.critical_damage
                    print("That Harmful Potion hit you right in the head! Your health is at "+str(player.health)+".")
            if player.health<=0:
                print("You died! Restarting the game...")
                start()
                break
            elif Enemy2.health<=0:
                print("You defeated the "+Enemy2.name+"! Good job! Getting Battle 3 ready...")
                Battle3()
                break
    def Battle3():                                                                                                 #Battle 2!!!!
        class Character:
            def __init__(self, name, health):
                self.health=health
                self.name=name
        class Attack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-2), (damage+8))
                self.critical_damage=critical_damage
        class EnemyAttack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-3),(damage+7))
                self.critical_damage=critical_damage
        Attacks=["Sword Slash", "Jump Jab", "Fireball", "Lightningbolt", "Weaken"]
        SwordSlash=Attack("swordslash", 40, 50)
        JumpJab=Attack("jumpjab", 43, 53)
        Fireball=Attack("fireball", 50, 60)
        Lightningbolt=Attack("lightningbolt", 0, 0)
        Weaken=Attack("weaken", 20, 30)
        unconcious=False
        unconciousturncount=0
        weaken=0
        player=Character(PlayerName, 180)
        Enemy=Character("Fire Dragon", 210)
        Firebreath=Attack("firebreath", 55, 65)
        MeteorShower=EnemyAttack("meteorshower", 8, 0)
        VolcanoEruption=Attack("volcano", 70, 90)
        VolcanoBoiling=False
        VolcanoTurnTimer=0
        Firefist=Attack("firefist", 60, 80)
        print("Battle 3! Welcome "+player.name+" to the battle! He will be fighting "+Enemy.name+"!")
        print("You have "+str(player.health)+" health. The "+Enemy.name+" has "+str(Enemy.health)+" health.")
        print("You trained and trained and trained, and now you are sure that you can survive the "+Enemy.name+".")
        Battle3=True
        while Battle3:
            move=input("Here are your attacks:"+str(Attacks)+" Please choose one!").lower()
            if move=="swordslash" or move=="sword slash":
                print("You used Sword Slash!")
                hit_chance=random.randint(0, 10)
                if hit_chance<4:
                    Enemy.health-=SwordSlash.damage
                    print("Your sword met its destination! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                elif hit_chance>7:
                    print("The "+Enemy.name+" dodged your attack at the last second. Better luck next time!")
                    print("The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                else:
                    Enemy.health-=SwordSlash.critical_damage
                    print("WOW! A critical hit! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
            elif move=="jumpjab" or move=="jump jab":
                print("You used Jump Jab!")
                hit_chance=random.randint(0, 10)
                if hit_chance<4:
                    Enemy.health-=JumpJab.damage
                    print("Your sword met its destination! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                elif hit_chance>8:
                    print("The "+Enemy.name+" dodged your attack at the last second. Better luck next time!")
                    print("The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                else:
                    Enemy.health-=JumpJab.critical_damage
                    print("WOW! A critical hit! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
            elif move=="fireball" or move=="fire ball":
                print("You used Fireball!")
                hit_chance=random.randint(0, 10)
                if hit_chance<6:
                    Enemy.health-=Fireball.damage
                    print("Your Fireball hit the "+Enemy.name+"! The "+Enemy.name+" health is at "+str(Enemy.health)+"!")
                elif hit_chance>=6 and hit_chance<8:
                    print("The "+Enemy.name+" was to fast!")
                else:
                    Enemy.health-=Fireball.critical_damage
                    print("Critical hit! Good job! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
            elif move=="lightningbolt" or move=="lightning bolt":
                chance=random.randint(0, 10)
                if unconcious==False:
                    print("You used Lightningbolt!")
                    print("Lightningbolt knocks out the opponent for 2 turns, but doesn't do any damage.")
                    if chance>6:
                        print("The lightningbolt hit! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                        unconcious=True
                    else:
                        print("Oh no, the lightningbolt missed! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                else:
                    print("You are not alowed to use this move if the enemy is still unconcious.")
            elif move=="weaken":
                print("You used Weaken!")
                print("Weaken weakens the opponents attacks for this turn by 15 damage.")
                chance=random.randint(0,10)
                if chance<3:
                    print("Uh oh! The Weaken didn't work! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                else:
                    weaken=15
                    chance=random.randint(0,10)
                    if chance<7:
                        Enemy.health-=Weaken.damage
                        print("The Weaken also did damage! The "+Enemy.name+"'s health is now at "+str(Enemy.health)+"!")
                    else:
                        Enemy.health-=Weaken.critical_damage
                        print("The Weaken also did critical damage! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
            else:
                print("That is not a valid attack choice. Skipping your turn.")
            if player.health<=0:
                print("You died! Restarting the game...")
                start()
                break
            elif Enemy.health<=0:
                print("You defeated the "+Enemy.name+"! Good job! Getting Battle 4 ready...")
                once=True
                Battle4()
                break
            if not unconcious:
                choose_attack=random.randint(1,8)                           #Enemy Attacks start here
                if choose_attack==1 or choose_attack==2:
                    print("The "+Enemy.name+" used Firebreath!")
                    chance=random.randint(0,10)
                    if chance<6:
                        player.health-=(Firebreath.damage-weaken)
                        print("The Firebreath hit you in the chest! Your health is now at "+str(player.health)+"!")
                    elif chance>=6 and chance<8:
                        player.health-=(Firebreath.critical_damage-weaken)
                        print("The Firebreath hit you in the face! Your health is now at "+str(player.health)+"!")
                    else:
                        print("You dodged the Firebreath! Your health is at "+str(player.health)+".")
                elif choose_attack==3 or choose_attack==4:
                    print("The "+Enemy.name+" chose MeteorShower!")
                    chance=random.randint(0,10)
                    Damage=chance*MeteorShower.damage
                    player.health-=(Damage-weaken)
                    print("You got hit by "+str(chance)+" meteors out of 10! Your health is now at "+str(player.health)+"!")
                elif choose_attack==5 or choose_attack==6 and VolcanoBoiling==False:
                    print("The "+Enemy.name+" chose Volcano Eruption!")
                    VolcanoChance=random.randint(1,2)
                    if VolcanoChance==1:
                        VolcanoBoiling=True
                        VolcanoCritical=True
                        print("The Volcano will erupt in three turns! The lava is EXTRA HOT!")
                    if VolcanoChance==2:
                        VolcanoBoiling=True
                        VolcanoCritical=False
                        print("The Volcano will erupt in three turns!")
                else:
                    print("The "+Enemy.name+" used Firefist!")
                    chance=random.randint(1,3)
                    if chance==1:
                        player.health-=(Firefist.damage-weaken)
                        print("The Firefist hit you in the arm! Your health is now at "+str(player.health)+"!")
                    elif chance==2:
                        player.health-=(Firefist.critical_damage-weaken)
                        print("The Firefist hit you in the gut! Your health is now at "+str(player.health)+"!")
                    else:
                        print("You dodged the Firefist! Your health is at "+str(player.health)+"!")
            else:
                unconciousturncount+=1
                if unconciousturncount==2:
                    unconciousturncount=0
                    unconcious=False
                    print("The "+Enemy.name+" will wake up after your next turn!")
                else:
                    print("The "+Enemy.name+" is unconcious!")
            if VolcanoBoiling:
                VolcanoTurnTimer+=1
                if VolcanoTurnTimer==4:
                    VolcanoTurnTimer=0
                    VolcanoBoiling=False
                    VolcanoChance=random.randint(1,2)
                    if VolcanoChance==1:
                        if VolcanoCritical:
                            player.health-=(VolcanoEruption.critical_damage-weaken)
                            print("The volano erupted, soaking you in extra hot lava! Your health is now "+str(player.health)+"!")
                        elif not VolcanoCritical:
                            player.health-=(VolcanoEruption.damage-weaken)
                            print("The volano erupted, soaking you in lava! Your health is now "+str(player.health)+"!")
                    elif VolcanoChance==2:
                        print("You managed to find cover right before the lava from the volcano soaked everything! Your health is at "+str(player.health)+"!")
                else:
                    print("The lava in the volcano is still rising.")
            weaken=0
            if player.health<=0:
                print("You died! Restarting the game...")
                start()
                break
            elif Enemy.health<=0:
                print("You defeated the "+Enemy.name+"! Good job! Getting Battle 4 ready...")
                Battle4()
                break
    def Battle4():                                                                                              #Battle 2!!!!
        class Character:
            def __init__(self, name, health):
                self.health=health
                self.name=name
        class Attack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-1), (damage+9))
                self.critical_damage=critical_damage
        class EnemyAttack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-2),(damage+8))
                self.critical_damage=critical_damage
        Attacks=["Sword Slash", "Jump Jab", "Fireball", "Lightningbolt", "Weaken", "Blinding Light"]
        SwordSlash=Attack("swordslash",60, 70)
        JumpJab=Attack("jumpjab", 65, 75)
        Fireball=Attack("fireball", 70, 80)
        Lightningbolt=Attack("lightningbolt", 0, 0)
        Weaken=Attack("weaken", 40, 50)
        BlindingLight=Attack("blindinglight", 60, 70)
        Blind=False
        unconcious=False
        unconciousturncount=0
        weaken=0
        player=Character(PlayerName, 400)
        Enemy=Character("Lava Beast", 550)
        HotLava=Attack("hotlava", 67, 80)
        LavaRock=Attack("lavarock", 112, 0)
        LavaFlood=Attack("lavaflood", 30, 0)
        Bomb=Attack("bomb", 100, 120)
        LavaFlooding=False
        print("Battle 4! Welcome "+player.name+" to the battle! He will be fighting "+Enemy.name+"!")
        print("You have "+str(player.health)+" health. The "+Enemy.name+" has "+str(Enemy.health)+" health.")
        print("After months of all-nighters in the training room, you are finally sure you can beat this monster.")
        Battle4=True
        while Battle4:
            move=input("Here are your attacks:"+str(Attacks)+" Please choose one!").lower()
            if move=="swordslash" or move=="sword slash":
                print("You used Sword Slash!")
                hit_chance=random.randint(1, 10)
                if hit_chance<4:
                    Enemy.health-=SwordSlash.damage
                    print("Your sword met its destination! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                elif hit_chance>7 and not unconcious:
                    print("The "+Enemy.name+" dodged your attack at the last second. Better luck next time!")
                    print("The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                else:
                    Enemy.health-=SwordSlash.critical_damage
                    print("WOW! A critical hit! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
            elif move=="jumpjab" or move=="jump jab":
                print("You used Jump Jab!")
                hit_chance=random.randint(1, 10)
                if hit_chance<4:
                    Enemy.health-=JumpJab.damage
                    print("Your sword met its destination! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                elif hit_chance>8 and not unconcious:
                    print("The "+Enemy.name+" dodged your attack at the last second. Better luck next time!")
                    print("The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                else:
                    Enemy.health-=JumpJab.critical_damage
                    print("WOW! A critical hit! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
            elif move=="fireball" or move=="fire ball":
                print("You used Fireball!")
                hit_chance=random.randint(1, 10)
                if hit_chance<6:
                    Enemy.health-=Fireball.damage
                    print("Your Fireball hit the "+Enemy.name+"! The "+Enemy.name+" health is at "+str(Enemy.health)+"!")
                elif hit_chance>=6 and hit_chance<8 and not unconcious:
                    print("The "+Enemy.name+" was to fast!")
                else:
                    Enemy.health-=Fireball.critical_damage
                    print("Critical hit! Good job! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
            elif move=="lightningbolt" or move=="lightning bolt":
                chance=random.randint(1, 10)
                if unconcious==False:
                    print("You used Lightningbolt!")
                    print("Lightningbolt knocks out the opponent for 2 turns, but doesn't do any damage.")
                    if chance>5:
                        print("The lightningbolt hit! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                        unconcious=True
                    else:
                        print("Oh no, the lightningbolt missed! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                else:
                    print("You are not alowed to use this move if the enemy is still unconcious.")
            elif move=="weaken":
                print("You used Weaken!")
                print("Weaken weakens the opponents attacks for this turn by 35 damage.")
                chance=random.randint(1,10)
                if chance<3:
                    print("Uh oh! The Weaken didn't work! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                else:
                    weaken=35
                    chance=random.randint(1,10)
                    if chance<7:
                        Enemy.health-=Weaken.damage
                        print("The Weaken also did damage! The "+Enemy.name+"'s health is now at "+str(Enemy.health)+"!")
                    else:
                        Enemy.health-=Weaken.critical_damage
                        print("The Weaken also did critical damage! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
            elif move=="blindinglight" or move=="blinding light":
                chance=random.randint(1,10)
                print("You used Blinding Light!")
                print("Blinding Light makes your opponent very blind and have a 10% chance of hitting you.")
                Blind=True
                if chance<4:
                    Enemy.health-=BlindingLight.damage
                    print("The Blinding Light also did damage! The "+Enemy.name+"'s health is now "+str(Enemy.health)+".")
                elif chance>=4 and chance<8:
                    Enemy.health-=BlindingLight.damage
                    print("The Blinding Light also did critical damage! The "+Enemy.name+"'s health is now "+str(Enemy.health)+".")
                else:
                    print("The Blinding Light didn't do any damage!")
            else:
                print("That is not a valid attack choice. Skipping your turn.")
            if player.health<=0:
                print("You died! Restarting the game...")
                start()
                break
            elif player.health<=0 and Enemy.health<=0:
                print("Tie game! You have both died!")
                start()
                break
            elif Enemy.health<=0:
                print("You defeated the "+Enemy.name+"! Good job! Getting Battle edcjkn ready...")
                print("I see you have beat the creation I had made many years ago...")
                print("Nobody has EVER beat it...")
                print("What was that? Who am I? Well, WHO I am isn't relevent. It's whether you think you're ready to fight me or not...")
                while True:
                    case=input("Yes, or no.").lower()
                    if case=="yes":
                        print("...")
                        print("...")
                        print("Beat my friend Rocky and I will tell you the code.")
                        break
                    elif case=="no":
                        print("The voice went away.")
                        break
                    else:
                        print("I didn't understand you.")
                Battle5()
                break
            if not unconcious:
                choose_attack=random.randint(1,4)                                            #Enemy Attacks start here
                if not Blind:
                    if choose_attack==1:
                        print("The "+Enemy.name+" chose Hot Lava!")
                        chance=random.randint(1,3)
                        if chance==1:
                            player.health-=(HotLava.damage-weaken)
                            print("The Hot Lava landed on your foot! Your health is now at "+str(player.health)+"!")
                        elif chance==2:
                            player.health-=(HotLava.critical_damage-weaken)
                            print("The Hot Lava landed on your face! Your health is now at "+str(player.health)+"!")
                        else:
                            print("Good job dodging that Hot Lava! Your health is at "+str(player.health)+"!")
                    elif choose_attack==2:
                        print("The "+Enemy.name+" used Lava Rock!")
                        while True:
                            guess=input("Guess a number between 1 and 3!")
                            ran=random.randint(1,3)
                            try:
                                if int(guess)==ran:
                                    print("WOW! You sure are lucky! That Lava Rock completly missed you!")
                                    break
                                else:
                                    player.health-=(LavaRock.damage-weaken)
                                    print("Wrong. The number was "+str(ran)+"! Your health is now at "+str(player.health)+"!")
                                    break
                            except:
                                print("That isn't a number! Try again!")
                    elif choose_attack==3 and not LavaFlooding:
                        print("The "+Enemy.name+" used Lava Flood!")
                        print("Lava Flood floods the whole arena with lava and does "+str(LavaFlood.damage)+" damage every round to you for the rest of the game!")
                        print("Note: Weaken doesn't weaken the lava!")
                        LavaWeaken=0
                        LavaFlooding=True
                    elif choose_attack==4:
                        print("The "+Enemy.name+" used bomb!")
                        chance=random.randint(1,10)
                        if chance<4:
                            dm=(Bomb.damage-weaken)
                            player.health-=dm
                            Enemy.health-=dm
                            print("The Bomb did "+str(dm)+"to both you and the "+Enemy.name+"! Your health is now "+str(player.health)+".")
                            print("The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                        elif chance>=4 and chance<6:
                            dm=(Bomb.critical_damage-weaken)
                            player.health-=dm
                            Enemy.health-=dm
                            print("The Bomb did "+str(dm)+"to both you and the "+Enemy.name+"! Your health is now "+str(player.health)+".")
                            print("The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                        else:
                            print("The Bomb malfunctioned!")
                elif Blind:
                    print("The Enemy is still blind!")
                    if choose_attack==1:
                        print("The "+Enemy.name+" chose Hot Lava!")
                        chance=random.randint(1,10)
                        if chance==6:
                            player.health-=(HotLava.damage-weaken)
                            print("The Hot Lava landed on your foot! Your health is now at "+str(player.health)+"!")
                        else:
                            print("The "+Enemy.name+" is so blind, it missed!")
                    elif choose_attack==2:
                        print("The "+Enemy.name+" used Lava Rock!")
                        while True:
                            guess=input("Guess a number between 1 and 10!")
                            ran=random.randint(1,10)
                            try:
                                if int(guess)!=ran:
                                    print("WOW! You sure are lucky that you didn't guess the right number! That Lava Rock completly missed you!")
                                    break
                                else:
                                    player.health-=(LavaRock.damage-weaken)
                                    print("How did you guess the right number?! That Lava Rock hit you! Your health is now at "+str(player.health)+"!")
                                    break
                            except:
                                print("That isn't a number! Try again!")
                    elif choose_attack==3 and not LavaFlooding:
                        print("The "+Enemy.name+" used LavaFlood while it was blind!")
                        print("It didn't know how hot the Lava was when it spewed out!")
                        print("The lava does 15 damage because the "+Enemy.name+" was blind when it spewed out the lava,")
                        print("So the lava is cooler than normal!")
                        LavaFlooding=True
                        LavaWeaken=15
                    elif choose_attack==4:
                        print("The "+Enemy.name+" used Bomb!")
                        chance=random.randint(1,10)
                        if chance==3:
                            dm=(Bomb.damage-weaken)
                            player.health-dm
                            Enemy.health-=dm
                            print("The Bomb did "+str(dm)+"to both you and the "+Enemy.name+"! Your health is now "+str(player.health)+".")
                            print("The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                        else:
                            print("The bomb missed!")
            else:
                unconciousturncount+=1
                if unconciousturncount==2:
                    unconciousturncount=0
                    unconcious=False
                    print("The "+Enemy.name+" will wake up after your next turn!")
                else:
                    print("The "+Enemy.name+" is unconscious!")
            if LavaFlooding:
                player.health-=(LavaFlood.damage-LavaWeaken)
                print("The lava is still there. Your health is now "+str(player.health)+"!")
            weaken=0
            Blind=False
            if player.health<=0:
                print("You died! Restarting the game...")
                start()
                break
            elif player.health<=0 and Enemy.health<=0:
                print("Tie game! You have both died!")
                start()
                break
            elif Enemy.health<=0:
                print("You defeated the "+Enemy.name+"! Good job! Getting Battle edcjkn ready...")
                print("I see you have beat the creation I had made many years ago...")
                print("Nobody has EVER beat it...")
                print("What was that? Who am I? Well, WHO I am isn't relevent. It's whether you think you're ready to fight me or not...")
                while True:
                    case=input("Yes, or no.").lower()
                    if case=="yes":
                        print("...")
                        print("...")
                        print("Beat my friend Rocky and I will tell you the code.")
                        break
                    elif case=="no":
                        print("The voice went away.")
                        break
                    else:
                        print("I didn't understand you.")
                Battle5()
                break
    def Battle5():
        class Character:
            def __init__(self, name, health):
                self.health=health
                self.name=name
        class Attack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-0), (damage+10))
                self.critical_damage=critical_damage
        class EnemyAttack:
            def __init__(self, name, damage, critical_damage):
                self.name=name
                self.damage=random.randint((damage-1),(damage+9))
                self.critical_damage=critical_damage
        Attacks=["Sword Slash", "Jump Jab", "Fireball", "Lightningbolt", "Weaken", "Blinding Light", "Heal"]
        SwordSlash=Attack("swordslash", 80, 90)
        JumpJab=Attack("jumpjab", 90, 100)
        Fireball=Attack("fireball", 110, 120)
        Lightningbolt=Attack("lightningbolt", 0, 0)
        Weaken=Attack("weaken", 60, 70)
        BlindingLight=Attack("blindinglight", 70, 80)
        Heal=Attack("heal", 100, 120)
        HealCount=0
        Blind=False
        unconscious=False
        unconsciousturncount=0
        weaken=0
        player=Character(PlayerName, 750)
        Enemy=Character("Rocky", 800)
        RockSlam=Attack("rockslam", 120, 140)
        Earthquake=Attack("earthquake", 80, 95)
        EarthquakeOn=False
        RockPunch=Attack("rockpunch", 90, 0)
        playerunconsciousturncount=0
        player_unconscious=False
        Boulder=Attack("boulder", 100, 110)
        print("Battle 5! Welcome "+player.name+" to the battle! He will be fighting "+Enemy.name+"!")
        print("You have "+str(player.health)+" health. The "+Enemy.name+" has "+str(Enemy.health)+" health.")
        print("You trained again. You did lots of all-nighters. You are ready.")
        Battle5=True
        while Battle5:
            if not player_unconscious:
                move=input("Here are your attacks:"+str(Attacks)+" Please choose one!").lower()
                if move=="swordslash" or move=="sword slash":
                    print("You used Sword Slash!")
                    hit_chance=random.randint(1, 10)
                    if hit_chance<4:
                        Enemy.health-=SwordSlash.damage
                        print("Your sword met its destination! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                    elif hit_chance>7 and not unconscious:
                        print("The "+Enemy.name+" dodged your attack at the last second. Better luck next time!")
                        print("The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                    else:
                        Enemy.health-=SwordSlash.critical_damage
                        print("WOW! A critical hit! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                elif move=="jumpjab" or move=="jump jab":
                    print("You used Jump Jab!")
                    hit_chance=random.randint(1, 10)
                    if hit_chance<4:
                        Enemy.health-=JumpJab.damage
                        print("Your sword met its destination! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                    elif hit_chance>8 and not unconscious:
                        print("The "+Enemy.name+" dodged your attack at the last second. Better luck next time!")
                        print("The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                    else:
                        Enemy.health-=JumpJab.critical_damage
                        print("WOW! A critical hit! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                elif move=="fireball" or move=="fire ball":
                    print("You used Fireball!")
                    hit_chance=random.randint(1, 10)
                    if hit_chance<6:
                        Enemy.health-=Fireball.damage
                        print("Your Fireball hit the "+Enemy.name+"! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                    elif hit_chance>=6 and hit_chance<8 and not unconscious:
                        print("The "+Enemy.name+" was to fast!")
                    else:
                        Enemy.health-=Fireball.critical_damage
                        print("Critical hit! Good job! The "+Enemy.name+"'s health is now "+str(Enemy.health)+"!")
                elif move=="lightningbolt" or move=="lightning bolt":
                    chance=random.randint(1, 10)
                    if unconscious==False:
                        print("You used Lightningbolt!")
                        print("Lightningbolt knocks out the opponent for 2 turns, but doesn't do any damage.")
                        if chance>5:
                            print("The lightningbolt hit! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                            unconscious=True
                        else:
                            print("Oh no, the lightningbolt missed! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                    else:
                        print("You are not alowed to use this move if the enemy is still unconscious.")
                elif move=="weaken":
                    print("You used Weaken!")
                    print("Weaken weakens the opponents attacks for this turn by 35 damage.")
                    chance=random.randint(1,10)
                    if chance<3:
                        print("Uh oh! The Weaken didn't work! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                    else:
                        weaken=35
                        chance=random.randint(1,10)
                        if chance<7:
                            Enemy.health-=Weaken.damage
                            print("The Weaken also did damage! The "+Enemy.name+"'s health is now at "+str(Enemy.health)+"!")
                        else:
                            Enemy.health-=Weaken.critical_damage
                            print("The Weaken also did critical damage! The "+Enemy.name+"'s health is at "+str(Enemy.health)+"!")
                elif move=="blindinglight" or move=="blinding light":
                    chance=random.randint(1,10)
                    print("You used Blinding Light!")
                    print("Blinding Light makes your opponent very blind and have a 10% chance of hitting you.")
                    Blind=True
                    if chance<4:
                        Enemy.health-=BlindingLight.damage
                        print("The Blinding Light also did damage! The "+Enemy.name+"'s health is now "+str(Enemy.health)+".")
                    elif chance>=4 and chance<8:
                        Enemy.health-=BlindingLight.damage
                        print("The Blinding Light also did critical damage! The "+Enemy.name+"'s health is now "+str(Enemy.health)+".")
                    else:
                        print("The Blinding Light didn't do any damage!")
                elif move=="heal":
                    if HealCount<3:
                        chance=random.randint(1,10)
                        print("You used Heal!")
                        print("Note: You can only heal 3 times in each Battle regardless of wheather the heal works or not.")
                        HealCount+=1
                        if chance<5:
                            player.health+=Heal.damage
                            print("The Heal worked! Your health is now at "+str(player.health)+"!")
                        elif chance>=5 and chance<8:
                            player.health+=Heal.critical_damage
                            print("The Heal worked extra well! Your health is now at "+str(Enemy.health)+"!")
                        else:
                            print("The Heal didn't work at all! Your health is at "+str(Enemy.health)+"!")
                    else:
                        print("You can't use heal more than 3 times. You turn has been skipped.")
                else:
                    print("That is not a valid attack choice. Skipping your turn.")
            if player.health<=0:
                print("You died! Restarting the game...")
                start()
                break
            elif player.health<=0 and Enemy.health<=0:
                print("Tie game! You have both died!")
                start()
                break
            elif Enemy.health<=0:
                print("You defeated the "+Enemy.name+"! Good job! Getting Battle 6 ready...")
                print("Again, you have defeated my freind Rocky. You are ready to fight me, arn't you?")
                print("Well, I-")
                print("...")
                print("...")
                print("You are ready. The code is 666.")
                Battle6()
                break
            if not unconscious:
                choose_attack=random.randint(1,4)                                            #Enemy Attacks start here
                if not Blind:
                    if choose_attack==1:
                        print("The "+Enemy.name+" chose Rock Slam!")
                        chance=random.randint(1,3)
                        if chance==1:
                            player.health-=(RockSlam.damage-weaken)
                            print("The Rock Slam landed directly! Your health is now at "+str(player.health)+"!")
                        elif chance==2 and not player_unconscious:
                            print("The Rock Slam flew over your shoulder! Your health is at "+str(player.health)+"!")
                        else:
                            player.health-=(RockSlam.critical_damage-weaken)
                            print("The Rock Slam landed directly on your face! Your health is now at "+str(player.health)+"!")
                    elif choose_attack==2 and not EarthquakeOn:
                       print("The "+Enemy.name+" used Earthquake!")
                       print("Every round you have a chance of getting hit by falling rocks!")
                       EarthquakeOn=True
                    elif choose_attack==3 and not player_unconscious:
                        print("The "+Enemy.name+" used Rock Punch!")
                        chance=random.randint(1,10)
                        if chance<5:
                            player.health-=(RockPunch.damage-weaken)
                            print("The Rock Punch met its destination! Your health is now "+str(player.health)+"!")
                            print("You are now knocked out!")
                            player_unconscious=True
                        elif chance>=5 and chance<9:
                            player.health-=(RockPunch.critical_damage-weaken)
                            print("The Rock Punch landed on your face! Your health is now "+str(player.health)+"!")
                            print("You are now knocked out!")
                            player_unconscious=True
                        else:
                            print("The Rock Punch missed!")
                    else:
                        print("The "+Enemy.name+" chose Boulder!")
                        chance=random.randint(1,3)
                        if chance==1:
                            player.health-=(Boulder.damage-weaken)
                            print("The Boulder knocked you over! Your health is now at "+str(player.health)+"!")
                        elif chance==2:
                            print("The Boulder flew high above you! Your health is at "+str(player.health)+"!")
                        else:
                            player.health-=(Boulder.critical_damage-weaken)
                            print("The boulder gained speed and hit you hard! Your health is now at "+str(player.health)+"!")
                elif Blind:
                    print("The Enemy is still blind!")
                    if choose_attack==1:
                        print("The "+Enemy.name+" chose Hot Lava!")
                        chance=random.randint(1,10)
                        if chance==2:
                            player.health-=(RockSlam.damage-weaken)
                            print("The Rock Slam landed on your foot! Your health is now at "+str(player.health)+"!")
                        else:
                            print("The Rock Slam missed!")
                    elif choose_attack==2 and not EarthquakeOn:
                       print("The "+Enemy.name+" used Earthquake!")
                       print("Every round you have a chance of getting hit by falling rocks!")
                       print("Note: The Blindness doesn't effect the Earthquake!")
                       EarthquakeOn=True
                    elif choose_attack==3:
                        print("The "+Enemy.name+" used Rock Punch while it was blind!")
                        chance=(1,10)
                        if chance==9:
                            player.health-=(RockPunch.damage-weaken)
                            print("The Rock Punch still hit you! Your health is now at"+str(player.health)+"!")
                            print("You are now unconscious!")
                            player_unconscious=True
                        else:
                            print("It missed!")
                    elif choose_attack==4:
                        print("The "+Enemy.name+" used Boulder!")
                        chance=random.randint(1,10)
                        if chance==9:
                            print("The Boulder knocked you down! Your health is now at "+str(player.health)+"!")
                        else:
                            print("The Boulder missed completely!")
            else:
                unconsciousturncount+=1
                if unconsciousturncount==2:
                    unconsciousturncount=0
                    unconscious=False
                    print("The "+Enemy.name+" will wake up after your next turn!")
                else:
                    print("The "+Enemy.name+" is unconscious!")
            if player_unconscious:
                playerunconsciousturncount+=1
                if playerunconsciousturncount==2:
                    print("You have woken up!")
                    player_unconscious=False
                    playerunconsciousturncount=0
                else:
                    print("You will wake up in one turn!")
            if EarthquakeOn:
                chance=random.randint(1,3)
                if chance==1:
                    player.health-=(Earthquake.damage-weaken)
                    print("A medium sized rock fell on you! Your health is now at "+str(player.health)+"!")
                elif chance==2:
                    player.health-=(Earthquake.critical_damage-weaken)
                    print("A large rock fell on you! Your health is now at "+str(player.health)+".")
                else:
                    print("No rocks landed on you.")
            weaken=0
            Blind=False
            if player.health<=0:
                print("You died! Restarting the game...")
                start()
                break
            elif player.health<=0 and Enemy.health<=0:
                print("Tie game! You have both died!")
                print("Try again.")
                start()
                break
            elif Enemy.health<=0:
                print("You defeated the "+Enemy.name+"! Good job! Getting Battle 6 ready...")
                print("Again, you have defeated my freind Rocky. You are ready to fight me, arn't you?")
                print("Well, I-")
                print("...")
                print("...")
                print("You are ready. The code is 666.")
                Battle6()
                break
    def Battle6():
        print("Battle 6 isn't ready yet.")
    def Battle666():
        print("I have to set up my arena first! Shoo! Begone you foul creature!")
    if BattleChoice=="1" or BattleChoice.lower()=="battle 1":
        print("You chose Battle 1!")
        Battle1()
    elif BattleChoice=="2" or BattleChoice.lower()=="battle 2":
        print("You chose Battle 2!")
        Battle2()
    elif BattleChoice=="3" or BattleChoice.lower()=="battle 3":
        print("You chose Battle 3!")
        Battle3()
    elif BattleChoice=="4" or BattleChoice.lower()=="battle 4":
        print("You chose Battle 4!")
        Battle4()
    elif BattleChoice=="5" or BattleChoice.lower()=="battle 5":
        print("You chose Battle 5!")
        Battle5()
    elif BattleChoice=="6" or BattleChoice.lower()=="battle 6":
        print("You chose Battle 6!")
        Battle6()
    elif BattleChoice.lower()=="local":
        print("You have selected Local Battle!")
        LocalBattle()
    elif BattleChoice=="666":
        sure=input("Are you sure you want to do this?").lower()
        if sure=="yes":
            print("I'll probably never see you again.")
            Battle666()
        elif sure=="no":
            print("Didn't think so.")
            start()
    else:
        print("Sorry, that isn't a valid choice. Please type 1, 2, 3, 4, 5, or local!.")
        start()
start()
print("Yes, I know, the game isn't done yet. I'm still working on it!")
print("Thanks for playing!")
