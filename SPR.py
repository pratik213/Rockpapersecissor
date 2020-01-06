import random
print("Enter your choice")

print("Press 1 to play")
print("Press 2 to Quit")
choice=int(input("Enter your choice  "))
user=str(input("Scissor or Paper or Rock  "))
print("You chosed "+user)
options=['Scissor','Paper','Rock'] 
comp=random.choice(options)
print("Computer chosed "+comp)
while(choice!=2):
           if(user==comp):
               print("Draw")
               break
           elif(user=='Scissor' and comp=='Paper'):
               print("You win")
               break
           elif(user=='Scissor' and comp=='Rock'):
               print("You lose")
               break
           elif(user=='Paper' and comp=='Scissor'):
               print("You lose")
               break
           elif(user=='Paper' and comp=='Rock'):
               print("You win")
               break
           elif(user=='Rock' and comp=='Paper'):
               print("You lose")
               break
           elif(user=='Rock' and comp=='Scissor'):
               print("You win")
               break
           else:
               print("ok")
               break;
print("Thanks for playing")
           

