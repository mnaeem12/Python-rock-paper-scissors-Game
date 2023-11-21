import random
options =('rock','paper','scissor')
#player1= random.choice(options)
#player2= input('Enter your choice:').lower()
#print('computer cose :',player1)
#print ('you choose :',player2)
while True:
    player1= random.choice(options)
    while(True):
        try:
            player2= input('Enter your choice:').lower()
            if(player2=="rock" or player2=="scissor" or player2=="paper"):
                break
            else:
                y/0    
        except:       
            print('Enter one of three words:', options)     
    
    print('\ncomputer choose :',player1)
    if(player1== player2):
        print ('tie')
    elif(player1=="rock") and (player2=="paper"):
        print ('you Win')
    elif(player1=='rock' and player2=='scissor'):
       print('you Loose')
    elif(player1=='paper' and player2=='rock'):
       print ('you loose')
    elif(player1=='paper' and player2=='scissor'):
       print ('you win')
    elif(player1=='scissor' and player2=='rock'):
       print ('you Win')
    elif(player1=='scissor' and player2=='paper'):
        print ('you Loose')
    while True:    
        try:   
            d= input('you need continue y/n:').lower()   
            if (d=="y" or d=="n"):
                break
            else:
                y/0
        except:
            print ('please enter y or n')
    if(d=="n") :
        break
    elif(d=="y"):
        pass