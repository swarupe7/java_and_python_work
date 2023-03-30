import random
print("Hi lets start our game...")
print("Game Rules:","*"*10)
print("There would be Three Game Denomination")
print('->rock')
print('->paper')
print('->scissor')
print('-->Use * To Quit')
print('If the Object Chosen by  Player dominates Object Chosen by Computer a point goes to Player')
print('If the Object Chosen by Computer dominates Object Chosen by Player a point goes to Computer')
print('If both enter the Same Choice There Scores would remain pretty same(Draw!)')
print('If the Player Quit in middle of game the Computer would win')
print('if you doesnt enter a valid input it might waste a round')
print('There would be five Rounds in this Game')
print('Ok lets begin the Game',"*"*5)
u_s=0
c_s=0
options=['rock','paper','scissor']
uop=options+['*']
for i in range(5):
      pval=input("enter your Denomination:")
      cval=random.choice(options)
      kk='computer choice is '+cval
      if pval not in uop:
         print('please enter a valid input ')
         continue
      if pval=="*":
           print('Computer Wins')
           c_s=999
           u_s=0
           break
      if pval==cval:
           print('Its a Draw Round')
           #print(kk)
           continue
      if pval=='rock':
            if cval=='paper':
                  c_s+=1
                  print('Computer wins this round')
                  print(kk)
            if cval=='scissor':
                  u_s+=1
                  print('player wins this round')
                  print(kk)
      if pval=='paper':
            if cval=='rock':
                  u_s+=1
                  print('player wins this round')
                  print(kk)
            if cval=='scissor':
                  c_s+=1
                  print('computer wins this round')
                  print(kk)
      if pval=="scissor":
            if cval=='rock':
                  c_s+=1
                  print('computer wins this round')
                  print(kk)
            if cval=="paper":
                  u_s+=1
                  print('player wins this round')
                  print(kk)

if(u_s>c_s):
     print('Player wins the whole Game')
if(c_s>u_s):
      print('Computer wins the whole Game')
if(c_s==u_s):
      print('The match is a Tie')

print('Thanks for playing this Game')

      