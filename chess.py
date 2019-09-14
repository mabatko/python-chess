import os
import re
from chessboard import Chessboard
from player import Player
from loader import Loader


CB = Chessboard()

LD = Loader(CB)

if os.path.exists("save.json"):
  LD.loadGame()
else:
  LD.newGame()

# black player
black = Player(CB, "Black")


CB.printBoard()


while True:
  if CB.turns % 2 == 0:
    print("White's turn")

    while True:
      pieceToMove = input("Which piece to move?:")
      if CB.isPieceActive(pieceToMove):
        if re.search("^W.*", pieceToMove):
          break
        else:
          print("Can't move black's piece!")
    while True:
      futureXPosition = int(input("Future X position:"))
      if futureXPosition < 0 or futureXPosition > 7:
        print("Invalid X position")
      else:
        break
    while True:
      futureYPosition = int(input("Future Y position:"))
      if futureYPosition < 0 or futureYPosition > 7:
        print("Invalid Y position")
      else:
        break

  else:
    print("Black's turn:")
    blacksTurn = black.doMove()
    pieceToMove = blacksTurn[0]
    futureXPosition = blacksTurn[1]
    futureYPosition = blacksTurn[2]
    print("{} goes to [{},{}]".format(pieceToMove,futureXPosition,futureYPosition))

  
  if CB.movePiece(pieceToMove, futureXPosition, futureYPosition):
    CB.turns += 1

  CB.printBoard()

  LD.saveGame()
  
  if CB.isGameFinished():
    print("Game finished after {} turns".format(CB.turns))
    LD.removeSave()
    break































