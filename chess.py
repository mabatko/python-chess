from chessboard import Chessboard
from piece import Piece, Pawn, Rook, Bishop, Queen, Knight, King
from player import Player


CB = Chessboard()


# Whites
WP1 = Pawn("Pawn", "WP1", "White", 0, 1, CB)
WP2 = Pawn("Pawn", "WP2", "White", 1, 1, CB)
WP3 = Pawn("Pawn", "WP3", "White", 2, 1, CB)
WP4 = Pawn("Pawn", "WP4", "White", 3, 1, CB)
WP5 = Pawn("Pawn", "WP5", "White", 4, 1, CB)
WP6 = Pawn("Pawn", "WP6", "White", 5, 1, CB)
WP7 = Pawn("Pawn", "WP7", "White", 6, 1, CB)
WP8 = Pawn("Pawn", "WP8", "White", 7, 1, CB)

WKK = King("King", "WKK", "White", 4, 0, CB)
WQ1 = Queen("Queen", "WQ1", "White", 3, 0, CB)
WR1 = Rook("Rook", "WR1", "White", 0, 0, CB)
WR2 = Rook("Rook", "WR2", "White", 7, 0, CB)
WK1 = Knight("Knight", "WK1", "White", 1, 0, CB)
WK2 = Knight("Knight", "WK2", "White", 6, 0, CB)
WB1 = Bishop("Bishop", "WB1", "White", 2, 0, CB)
WB2 = Bishop("Bishop", "WB2", "White", 5, 0, CB)

CB.addPiece(WP1)
CB.addPiece(WP2)
CB.addPiece(WP3)
CB.addPiece(WP4)
CB.addPiece(WP5)
CB.addPiece(WP6)
CB.addPiece(WP7)
CB.addPiece(WP8)
CB.addPiece(WKK)
CB.addPiece(WQ1)
CB.addPiece(WR1)
CB.addPiece(WR2)
CB.addPiece(WB1)
CB.addPiece(WB2)
CB.addPiece(WK1)
CB.addPiece(WK2)


# Blacks
BP1 = Pawn("Pawn", "BP1", "Black", 0, 6, CB)
BP2 = Pawn("Pawn", "BP2", "Black", 1, 6, CB)
BP3 = Pawn("Pawn", "BP3", "Black", 2, 6, CB)
BP4 = Pawn("Pawn", "BP4", "Black", 3, 6, CB)
BP5 = Pawn("Pawn", "BP5", "Black", 4, 6, CB)
BP6 = Pawn("Pawn", "BP6", "Black", 5, 6, CB)
BP7 = Pawn("Pawn", "BP7", "Black", 6, 6, CB)
BP8 = Pawn("Pawn", "BP8", "Black", 7, 6, CB)

BKK = King("King", "BKK", "Black", 4, 7, CB)
BQ1 = Queen("Queen", "BQ1", "Black", 3, 7, CB)
BR1 = Rook("Rook", "BR1", "Black", 0, 7, CB)
BR2 = Rook("Rook", "BR2", "Black", 7, 7, CB)
BK1 = Knight("Knight", "BK1", "Black", 1, 7, CB)
BK2 = Knight("Knight", "BK2", "Black", 6, 7, CB)
BB1 = Bishop("Bishop", "BB1", "Black", 2, 7, CB)
BB2 = Bishop("Bishop", "BB2", "Black", 5, 7, CB)

CB.addPiece(BP1)
CB.addPiece(BP2)
CB.addPiece(BP3)
CB.addPiece(BP4)
CB.addPiece(BP5)
CB.addPiece(BP6)
CB.addPiece(BP7)
CB.addPiece(BP8)
CB.addPiece(BKK)
CB.addPiece(BQ1)
CB.addPiece(BR1)
CB.addPiece(BR2)
CB.addPiece(BB1)
CB.addPiece(BB2)
CB.addPiece(BK1)
CB.addPiece(BK2)

# black player
black = Player(CB, "Black")


CB.printBoard()

turns = 0

while True:
  if turns % 2 == 0:
    print("White's turn")

    while True:
      pieceToMove = input("Which piece to move?:")
      if CB.isPieceActive(pieceToMove):
        break
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
    turns += 1

  CB.printBoard()
  if CB.isGameFinished():
    print("Game finished after {} turns".format(turns))
    break































