#from getpass import getpass as input

print("Battle of the Legends - Rock , Paper , Scissor")
print()
print("Welcome everyone to the great fight!")
print("On the right is the champion of years 'PLAYER 1'.")
print("When we look to the left side, we see a new but determined name. 'PLAYER 2'!!!")
print()

round = 0
p1 = 0
p2 = 0


print()
print("And we have received the match results, dear sports fans.!")
print()

while True :
  if round == 5 :
    print("Total Score" , p1 , " - " , p2)
    print ("Game over guys! Come on, go home. Good Night")
    exit()
  else :
    round +=1
    print()
    print("Round " , round , " :")
    print()
    player1 = input("Player 1 : R ,P ,S ?  ").upper()
    print()
    player2 = input("Player 2 : R ,P ,S ?  ").upper()

    if player1 not in ["R","P","S"] or player2 not in ["R","P","S"] :
      print("Match cancellation cheat detected")
      break  # Döngüyü tamamen sonlandırır
      
    if player1 == "R" :
      if player2 == "R" :
        print("😲 🗿 - 🗿 😲")
        continue
      elif player2 == "P" :
        print("🤯 🗿 - 🧻 😎")
        p2 += 1
        continue
      elif player2 == "S" :
        print("🥳 🗿 - ✂️ 😱")
        p1 += 1
        continue

    

    if player1 == "P" :
      if player2 == "R" :
        print("🤪 🧻 - 🗿 🤬")
        p1 += 1
        continue
      elif player2 == "P" :
        print("😒 🧻 - 🧻 😒")
        continue
      elif player2 == "S" :
        print("😭 🧻 - ✂️ 🤩")
        p2 += 1
        continue

    if player1 == "S" :
      if player2 == "R" :
        print("🥺 ✂️ - 🗿 😂")
        p2 += 1
        continue
      elif player2 == "P" :
        print("💪😁 ✂️ - 🧻 🤕")
        p1 += 1
        continue
      elif player2 == "S" :
        print("😅 ✂️ - ✂️ 😅")
        continue
