class Chessboard:

  board = [[' - '] * 8 for i in range(8)]
  pieces = []
  turns = 0

  x_axis = [' 0 ',' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ']

  def __init__(self):
    pass


  def printBoard(self):
    for i in range(8):
      print(' ', ['   '] * 8)
      print(7-i, self.board[7-i])
      print(' ', ['   '] * 8)
    print(' ', self.x_axis)


  def createPiece(self, piece):
    self.pieces.append(piece)


  def deactivatePiece(self, x_pos, y_pos):
    piece_name = self.board[y_pos][x_pos]
    pieceToDeactivate = self.returnPieceByName(piece_name)
    pieceToDeactivate.isActive = False
    print("Piece {} was removed from [{},{}]".format(piece_name,x_pos,y_pos))


  def addPiece(self, piece):
    self.board[piece.y_position][piece.x_position] = piece.name


  def removePiece(self, piece):
    self.board[piece.y_position][piece.x_position] = ' - '


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
      self.removePiece(pieceToMove)
      if not self.isFieldEmpty(future_x_pos, future_y_pos):
        self.deactivatePiece(future_x_pos, future_y_pos)
      pieceToMove.x_position = int(future_x_pos)
      pieceToMove.y_position = int(future_y_pos)
      pieceToMove.initialMoveNotDone = False
      self.addPiece(pieceToMove)
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
    if self.board[y_position][x_position] == ' - ':
      return True
    else:
      return False


  def isEnemyOnTheField(self, x_position, y_position, myColor):
    import re

    if myColor == 'White':
      if re.search("^B.*", self.board[y_position][x_position]):
        return True
      else:
        return False
    else:
      if re.search("^W.*", self.board[y_position][x_position]):
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


  def isGameFinished(self):
    if not self.isPieceActive('WKK'):
      print("White king is dead. Black won!")
      return True
    if not self.isPieceActive('BKK'):
      print("Black king is dead. White won!")
      return True
    return False
