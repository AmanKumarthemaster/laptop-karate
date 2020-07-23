import time
print('Welcome to the most powerful scenario maker for your games, AurScenarioMaker!')

scenar = input("Now tell me what type of game are you making? 1 for adventure 2 for life simulation 3 for mystery:")


if int(scenar) == 1:
    name = input("Um... A adventure game? OK! But, first of all tell me your name:")
    print("Oh! So your name is",name+"? Hello",name+". My name is David.")
    
    
elif int(scenar) == 2:
    name = input("Oh! A simulation? OK! But, first of all tell me your name:")
    print("Oh! So your name is",name+"? Hello",name+". My name is David.")
    
elif int(scenar) == 3:
    name = input("Got that! OK! But, first of all tell me your name:")
    print("Oh! So your name is",name+"? Hello",name+". My name is David.")
else:
    print("I am not sure I can help with that.Exiting.....")
    time.sleep(3)
    exit()
