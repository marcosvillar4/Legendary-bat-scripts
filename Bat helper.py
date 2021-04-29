import os
from pathlib import Path  # Import de dependencias


print("What is the name of the game?")
game = input()
print("Input the game id (Use the installed games script)")
gameid = input()
p = Path(game + ".bat")
p.write_text(

    "title Launching "
    + game
    + " \recho Launching "
    + game
    + " \rlegendary launch "
    + gameid
)

os.system("pause")
