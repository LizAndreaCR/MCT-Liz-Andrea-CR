print("Hi")
print("Welcome To Nerve")
input()
print("This Is A Game Of Truth Or Dare Without The Truth")
###########################################
input()
####por aqui va un while True
#aqui va la primera decicion 
decision =input("Are you a WATCHER or a PLAYER? ")
#decision = 'player'#
#decision = 'watcher'#
if decision == 'player':
  print("Welcome To PLAYER Mode")
  name=input('Enter your username @')
  print("Once You're In Theres No Way Back")
  print("If you're a snitcher or you happen to say anything that happens in this game to the police then you're death")
  
###########################################
  
  print("You youre a player ")
  print("You have a time limit for each challenge, the time depends on the challenge that touches you")
  print("Here's Your First Dare:")
  print("You have a limited time")
  print("Kiss A Stranger") 
  
  #.               #.             #. 
  decision2 = input("ACCEPT or DECLINE = ")
  #decision2 = 'accept'#
#decision2 = 'decline'#
  if decision2 == 'accept':
    print("Your time start's now!")
    video = input("Did you record your video? ")
    if video== 'yes':
      print("Wait Until The Next Dare")
    elif video == 'no':
      print("GAME OVER")
      #aqui iria un break#
###########################################
      
  elif decision2 == 'decline':
    print("GAME OVER")
    #aqui iria un break#
###########################################
#aqui es la deciscion de watcher
    
elif decision == 'watcher':
  print("Welcome To WATCHER mode")
  name2=input('Enter your username @')
  
  print("Once You're In Theres No Way Back")
  print("If you're a snitcher or you happen to say anything that happens in this game to the police then you're death")
  
###########################################
  
print("What do you wanna do first? ")
decision3 =input("- Propose Challenges For The Players -   - Watch Players -")
 
#decision3 = 'Propose challenges '#
#decision3 = 'Watch players'#
if decision3== '- Propose Challenges For The Players -':
      print("Write any challenge you want players to do")

elif decision3 == '- Watch Players -':
  print("In this part you can only see the challenges that the players do, and you can comment on their videos")
  #                #                  # 
  
if decision4 == 'another': 
    print("Do you want to comment on the video?")
    comment= input("Do you want to comment on the video? ")
    if comment== 'yes':
      print("Down here is a space for you to comment")
    elif comment == 'no':
      print("Ok, now you can see the challenges without interruptions")
      
###########################################

