class Loader():

  def __init__(self, chessboard):
    self.cb = chessboard


  def newGame(self):
    from piece import Piece, Pawn, Rook, Bishop, Queen, Knight, King
    # Whites
    WP1 = Pawn("Pawn", "WP1", "White", 0, 1, self.cb, True, True)
    WP2 = Pawn("Pawn", "WP2", "White", 1, 1, self.cb, True, True)
    WP3 = Pawn("Pawn", "WP3", "White", 2, 1, self.cb, True, True)
    WP4 = Pawn("Pawn", "WP4", "White", 3, 1, self.cb, True, True)
    WP5 = Pawn("Pawn", "WP5", "White", 4, 1, self.cb, True, True)
    WP6 = Pawn("Pawn", "WP6", "White", 5, 1, self.cb, True, True)
    WP7 = Pawn("Pawn", "WP7", "White", 6, 1, self.cb, True, True)
    WP8 = Pawn("Pawn", "WP8", "White", 7, 1, self.cb, True, True)

    WKK = King("King", "WKK", "White", 4, 0, self.cb, True, True)
    WQ1 = Queen("Queen", "WQ1", "White", 3, 0, self.cb, True, True)
    WR1 = Rook("Rook", "WR1", "White", 0, 0, self.cb, True, True)
    WR2 = Rook("Rook", "WR2", "White", 7, 0, self.cb, True, True)
    WK1 = Knight("Knight", "WK1", "White", 1, 0, self.cb, True, True)
    WK2 = Knight("Knight", "WK2", "White", 6, 0, self.cb, True, True)
    WB1 = Bishop("Bishop", "WB1", "White", 2, 0, self.cb, True, True)
    WB2 = Bishop("Bishop", "WB2", "White", 5, 0, self.cb, True, True)

    self.cb.addPiece(WP1)
    self.cb.addPiece(WP2)
    self.cb.addPiece(WP3)
    self.cb.addPiece(WP4)
    self.cb.addPiece(WP5)
    self.cb.addPiece(WP6)
    self.cb.addPiece(WP7)
    self.cb.addPiece(WP8)
    self.cb.addPiece(WKK)
    self.cb.addPiece(WQ1)
    self.cb.addPiece(WR1)
    self.cb.addPiece(WR2)
    self.cb.addPiece(WB1)
    self.cb.addPiece(WB2)
    self.cb.addPiece(WK1)
    self.cb.addPiece(WK2)

    # Blacks
    BP1 = Pawn("Pawn", "BP1", "Black", 0, 6, self.cb, True, True)
    BP2 = Pawn("Pawn", "BP2", "Black", 1, 6, self.cb, True, True)
    BP3 = Pawn("Pawn", "BP3", "Black", 2, 6, self.cb, True, True)
    BP4 = Pawn("Pawn", "BP4", "Black", 3, 6, self.cb, True, True)
    BP5 = Pawn("Pawn", "BP5", "Black", 4, 6, self.cb, True, True)
    BP6 = Pawn("Pawn", "BP6", "Black", 5, 6, self.cb, True, True)
    BP7 = Pawn("Pawn", "BP7", "Black", 6, 6, self.cb, True, True)
    BP8 = Pawn("Pawn", "BP8", "Black", 7, 6, self.cb, True, True)

    BKK = King("King", "BKK", "Black", 4, 7, self.cb, True, True)
    BQ1 = Queen("Queen", "BQ1", "Black", 3, 7, self.cb, True, True)
    BR1 = Rook("Rook", "BR1", "Black", 0, 7, self.cb, True, True)
    BR2 = Rook("Rook", "BR2", "Black", 7, 7, self.cb, True, True)
    BK1 = Knight("Knight", "BK1", "Black", 1, 7, self.cb, True, True)
    BK2 = Knight("Knight", "BK2", "Black", 6, 7, self.cb, True, True)
    BB1 = Bishop("Bishop", "BB1", "Black", 2, 7, self.cb, True, True)
    BB2 = Bishop("Bishop", "BB2", "Black", 5, 7, self.cb, True, True)

    self.cb.addPiece(BP1)
    self.cb.addPiece(BP2)
    self.cb.addPiece(BP3)
    self.cb.addPiece(BP4)
    self.cb.addPiece(BP5)
    self.cb.addPiece(BP6)
    self.cb.addPiece(BP7)
    self.cb.addPiece(BP8)
    self.cb.addPiece(BKK)
    self.cb.addPiece(BQ1)
    self.cb.addPiece(BR1)
    self.cb.addPiece(BR2)
    self.cb.addPiece(BB1)
    self.cb.addPiece(BB2)
    self.cb.addPiece(BK1)
    self.cb.addPiece(BK2)
    

  def loadGame(self):
    import json
    from piece import Piece, Pawn, Rook, Bishop, Queen, Knight, King
    
    with open("save.json", "r") as saveFile:
      data = json.load(saveFile)
      for key in data:
        if key == "turns":
          self.cb.turns = data[key]
        else:
          if data[key]["type"] == "Pawn":
            piece = Pawn(data[key]["type"], data[key]["name"], data[key]["color"], data[key]["x_position"], data[key]["y_position"], self.cb, data[key]["initialMoveNotDone"], data[key]["isActive"])
          if data[key]["type"] == "Rook":
            piece = Rook(data[key]["type"], data[key]["name"], data[key]["color"], data[key]["x_position"], data[key]["y_position"], self.cb, data[key]["initialMoveNotDone"], data[key]["isActive"])
          if data[key]["type"] == "Knight":
            piece = Knight(data[key]["type"], data[key]["name"], data[key]["color"], data[key]["x_position"], data[key]["y_position"], self.cb, data[key]["initialMoveNotDone"], data[key]["isActive"])
          if data[key]["type"] == "Bishop":
            piece = Bishop(data[key]["type"], data[key]["name"], data[key]["color"], data[key]["x_position"], data[key]["y_position"], self.cb, data[key]["initialMoveNotDone"], data[key]["isActive"])
          if data[key]["type"] == "Queen":
            piece = Queen(data[key]["type"], data[key]["name"], data[key]["color"], data[key]["x_position"], data[key]["y_position"], self.cb, data[key]["initialMoveNotDone"], data[key]["isActive"])
          if data[key]["type"] == "King":
            piece = King(data[key]["type"], data[key]["name"], data[key]["color"], data[key]["x_position"], data[key]["y_position"], self.cb, data[key]["initialMoveNotDone"], data[key]["isActive"])
            
          self.cb.addPiece(piece)


  def saveGame(self):
    import json
    data = {"turns": self.cb.turns}
    for piece in self.cb.pieces:
      data[piece.name] = piece.returnJSON()
    with open("save.json", "w") as saveFile:
      json.dump(data, saveFile)
      

  def removeSave(self):
    import os
    if os.path.exists("save.json"):
      os.remove("save.json")
