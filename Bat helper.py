import os
print ("What is the name of the game?")
game = input()
print ("Input the game id (Use the installed games script)")
gameid = input()
print ("Paste the following code in a txt document and change its extension to .bat")
print ("title Launching " + game)
print ("echo Launching " + game)
print ("legendary launch " + gameid)
os.system("pause")
