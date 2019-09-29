class Chessboard:

  board = [[] * 8 for i in range(8)]
  pieces = []
  turns = 0
  lastMove = {"pieceName": '', "type": '', "origX": -1, "origY": -1, "futureX": -1, "futureY": -1}
  

  x_axis = ['   0   ','   1   ','   2   ','   3   ','   4   ','   5   ','   6   ','   7   ']

  def __init__(self):
    from square import Square
    for i in range(8):
      for j in range(8):
        if (i+j)%2:
          self.board[i].append(Square("White", i, j))
        else:
          self.board[i].append(Square("Black", i, j))


  def printBoard(self):
    for i in range(8):
      if not i % 2:
        print(' ', '░░░░░░░▓▓▓▓▓▓▓' * 4)
        print(7-i, end=' ')
        for j in range(8):
          print(self.board[7-i][j].printSquare(), end='')
        print('')
        print(' ', '░░░░░░░▓▓▓▓▓▓▓' * 4)
      else:
        print(' ', '▓▓▓▓▓▓▓░░░░░░░' * 4)
        print(7-i, end=' ')
        for j in range(8):
          print(self.board[7-i][j].printSquare(), end='')
        print('')
        print(' ', '▓▓▓▓▓▓▓░░░░░░░' * 4)
    print(' ', ''.join(self.x_axis))


  def createPiece(self, piece):
    self.pieces.append(piece)


  def deactivatePiece(self, x_pos, y_pos):
    piece_name = self.board[y_pos][x_pos].pieceOn
    pieceToDeactivate = self.returnPieceByName(piece_name)
    pieceToDeactivate.isActive = False
    pieceToDeactivate.initialMoveNotDone = False
    print("Piece {} was removed from [{},{}]".format(piece_name,x_pos,y_pos))


  def addPiece(self, piece):
    if piece.isActive:
      self.board[piece.y_position][piece.x_position].pieceOn = piece.name


  def removePiece(self, piece):
    self.board[piece.y_position][piece.x_position].pieceOn = ' - '


  def returnPieceByName(self, piece_name):
    for pieces in self.pieces:
      if pieces.name == piece_name:
        return pieces


  def isPieceActive(self, name):
    pieceNotFound = True
    for pieces in self.pieces:
      if pieces.name == name:
        pieceNotFound = False
        if not pieces.isActive:
            print("Piece {} is not active".format(name))
            return False
    if pieceNotFound:
      print("Piece with name {} doesn't exist".format(name))
      return False
    return True


  def movePiece(self, piece_name, future_x_pos, future_y_pos):
    pieceToMove = self.returnPieceByName(piece_name)
    
    if pieceToMove.isMoveLegal(future_x_pos, future_y_pos, self):
      self.lastMove["pieceName"] = pieceToMove.name
      self.lastMove["type"] = pieceToMove.type
      self.lastMove["origX"] = pieceToMove.x_position
      self.lastMove["origY"] = pieceToMove.y_position
      self.lastMove["futureX"] = future_x_pos
      self.lastMove["futureY"] = future_y_pos
      
      # is this move castling?
      if pieceToMove.type == "King" and abs(pieceToMove.x_position-future_x_pos) == 2:
        if pieceToMove.color == "White":
          if future_x_pos == 6:
            rook = self.returnPieceByName("WR2")
          else:
            rook = self.returnPieceByName("WR1")
        else:
          if future_x_pos == 6:
            rook = self.returnPieceByName("BR2")
          else:
            rook = self.returnPieceByName("BR1")
        self.removePiece(rook)
        if future_x_pos == 6:
          rook.x_position = 5
        else:
          rook.x_position = 3
        rook.initialMoveNotDone = False
        self.addPiece(rook)
        
      self.removePiece(pieceToMove)
      if not self.isFieldEmpty(future_x_pos, future_y_pos):
        self.deactivatePiece(future_x_pos, future_y_pos)
      pieceToMove.x_position = int(future_x_pos)
      pieceToMove.y_position = int(future_y_pos)
      pieceToMove.initialMoveNotDone = False
      self.addPiece(pieceToMove)

      #pawn promotion
      if pieceToMove.type == "Pawn" and ((pieceToMove.color == "White" and pieceToMove.y_position == 7) or (pieceToMove.color == "Black" and pieceToMove.y_position == 0)):
        self.promotion(pieceToMove)
      
      return True
    else:
      print('The move is not legal')
      return False


  def isFieldValid(self, x_position, y_position):
    if x_position < 0 or x_position > 7 or y_position < 0 or y_position > 7:
      return False
    else:
      return True


  def isFieldEmpty(self, x_position, y_position):
    if self.board[y_position][x_position].pieceOn == ' - ':
      return True
    else:
      return False


  def isEnemyOnTheField(self, x_position, y_position, myColor):
    import re

    if myColor == 'White':
      if re.search("^B.*", self.board[y_position][x_position].pieceOn):
        return True
      else:
        return False
    else:
      if re.search("^W.*", self.board[y_position][x_position].pieceOn):
        return True
      else:
        return False


  def canAttack(self, attackersName, victimsName):
    attacker = self.returnPieceByName(attackersName)
    victim = self.returnPieceByName(victimsName)

    victimsPosition = [victim.x_position, victim.y_position]
    attackersReach = attacker.returnValidFields(self)

    if victimsPosition in attackersReach:
      return True
    else:
      return False


  def isFieldSafe(self, xPos, yPos, myColor):
    fieldInQuestion = [xPos, yPos]
    for piece in self.pieces:
      if piece.color != myColor and piece.isActive:
        if piece.type == "Pawn":
          validFields = piece.returnPossibleTargetFields(self)
        else:
          validFields = piece.returnValidFields(self)
        if fieldInQuestion in validFields:
          return False
    return True


  def countPieceByType(self, typeName, color):
    num = 0
    for piece in self.pieces:
      if piece.type == typeName and piece.color == color:
        num += 1
    return num


  def promotion(self, pawnToPromote):
    from piece import Rook, Bishop, Queen, Knight
    print("Pawn {} on [{},{}] is going to be promoted".format(pawnToPromote.name, pawnToPromote.x_position, pawnToPromote.y_position))
    if pawnToPromote.color == "White":
      while True:
        pieceType = input("Choose which type it will become: Queen, Knight, Rook, Bishop: ").upper()
        if pieceType in ["QUEEN", "KNIGHT", "ROOK", "BISHOP"]:
          break
        else:
          print("Incorrect type")
    else:
      pieceType = "QUEEN"
      
    if pieceType == "ROOK":
      numOfPieces = self.countPieceByType("Rook", pawnToPromote.color)
      if pawnToPromote.color == "White":
        piece = Rook("Rook", "WR"+str(numOfPieces+1), pawnToPromote.color, pawnToPromote.x_position, pawnToPromote.y_position, self, False, True)
      else:
        piece = Rook("Rook", "BR"+str(numOfPieces+1), pawnToPromote.color, pawnToPromote.x_position, pawnToPromote.y_position, self, False, True)
        
    if pieceType == "QUEEN":
      numOfPieces = self.countPieceByType("Queen", pawnToPromote.color)
      if pawnToPromote.color == "White":
        piece = Queen("Queen", "WQ"+str(numOfPieces+1), pawnToPromote.color, pawnToPromote.x_position, pawnToPromote.y_position, self, False, True)
      else:
        piece = Queen("Queen", "BQ"+str(numOfPieces+1), pawnToPromote.color, pawnToPromote.x_position, pawnToPromote.y_position, self, False, True)
        
    if pieceType == "BISHOP":
      numOfPieces = self.countPieceByType("Bishop", pawnToPromote.color)
      if pawnToPromote.color == "White":
        piece = Bishop("Bishop", "WB"+str(numOfPieces+1), pawnToPromote.color, pawnToPromote.x_position, pawnToPromote.y_position, self, False, True)
      else:
        piece = Bishop("Bishop", "BB"+str(numOfPieces+1), pawnToPromote.color, pawnToPromote.x_position, pawnToPromote.y_position, self, False, True)

    if pieceType == "KNIGHT":
      numOfPieces = self.countPieceByType("Knight", pawnToPromote.color)
      if pawnToPromote.color == "White":
        piece = Knight("Knight", "WK"+str(numOfPieces+1), pawnToPromote.color, pawnToPromote.x_position, pawnToPromote.y_position, self, False, True)
      else:
        piece = Knight("Knight", "BK"+str(numOfPieces+1), pawnToPromote.color, pawnToPromote.x_position, pawnToPromote.y_position, self, False, True)
        
    self.addPiece(piece)
    pawnToPromote.isActive = False
    

  def isGameFinished(self):
    if not self.isPieceActive('WKK'):
      print("White king is dead. Black won!")
      return True
    if not self.isPieceActive('BKK'):
      print("Black king is dead. White won!")
      return True
    return False
