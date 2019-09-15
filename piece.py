class Piece:

  def __init__(self, type, name, color, x_position, y_position, board, moved, active):
    self.type = type
    self.name = name
    self.color = color
    self.x_position = x_position
    self.y_position = y_position
    board.createPiece(self)
    self.initialMoveNotDone = moved
    self.isActive = active


  def crawlFields(self, board, direction, fieldsList):
    y_index = self.y_position
    x_index = self.x_position
    enemyFound = False
    while True:
      if direction == 'North':
        y_index += 1
      if direction == 'South':
        y_index -= 1
      if direction == 'West':
        x_index -= 1
      if direction == 'East':
        x_index += 1
      if direction == 'NW':
        y_index += 1
        x_index -= 1
      if direction == 'NE':
        y_index += 1
        x_index += 1
      if direction == 'SE':
        y_index -= 1
        x_index += 1
      if direction == 'SW':
        y_index -= 1
        x_index -= 1
      p = [x_index, y_index]
      if board.isFieldValid(x_index, y_index):
        if board.isFieldEmpty(x_index, y_index):
          fieldsList.append(p)
        else:
          if board.isEnemyOnTheField(x_index, y_index, self.color):
            fieldsList.append(p)
            if not enemyFound:
              enemyFound = True
            else:
              break
          else:
            break
      else:
        break


  def returnJSON(self):
    import json
    data = {"type": self.type, "name": self.name, "color": self.color, "x_position": self.x_position, "y_position": self.y_position, "isActive": self.isActive, "initialMoveNotDone": self.initialMoveNotDone}
    return data



class Pawn(Piece):

  value = 1

  def returnValidFields(self, board):
    validFields = []

    if self.color == 'White':
      upDown = 1
    else:
      upDown = -1

    p = [self.x_position-1, self.y_position+1*upDown]
    if board.isFieldValid(p[0], p[1]) and board.isEnemyOnTheField(p[0], p[1], self.color):
      validFields.append(p)

    px = [self.x_position, self.y_position+1*upDown]
    if board.isFieldValid(px[0], px[1]) and board.isFieldEmpty(px[0], px[1]):
      validFields.append(px)


    p = [self.x_position+1, self.y_position+1*upDown]
    if board.isFieldValid(p[0], p[1]) and board.isEnemyOnTheField(p[0], p[1], self.color):
      validFields.append(p)

    if self.initialMoveNotDone:
      p = [self.x_position, self.y_position+2*upDown]
      if board.isFieldValid(p[0], p[1]) and board.isFieldEmpty(px[0], px[1]) and board.isFieldEmpty(p[0], p[1]):
        validFields.append(p)

    #print(validFields)

    return validFields
  

  def returnPossibleTargetFields(self, board):
    targetFields = []

    if self.color == 'White':
      upDown = 1
    else:
      upDown = -1    

    p = [self.x_position-1, self.y_position+1*upDown]
    if board.isFieldValid(p[0], p[1]):
      targetFields.append(p)

    p = [self.x_position+1, self.y_position+1*upDown]
    if board.isFieldValid(p[0], p[1]):
      targetFields.append(p)

    return targetFields
  

  def isMoveLegal(self, future_x_pos, future_y_pos, board):
    futurePosition = [future_x_pos, future_y_pos]

    validFields = self.returnValidFields(board)

    if futurePosition in validFields:
      return True
    else:
      return False



class Rook(Piece):

  value = 4

  def returnValidFields(self, board):
    validFields = []

    # going North
    self.crawlFields(board, 'North', validFields)
    # going South
    self.crawlFields(board, 'South', validFields)
    # going West
    self.crawlFields(board, 'West', validFields)
    # going East
    self.crawlFields(board, 'East', validFields)

    #print(validFields)
    return validFields


  def isMoveLegal(self, future_x_pos, future_y_pos, board):
    futurePosition = [future_x_pos, future_y_pos]

    validFields = self.returnValidFields(board)    

    if futurePosition in validFields:
      return True
    else:
      return False



class Bishop(Piece):

  value = 3

  def returnValidFields(self, board):
    validFields = []

    # going NW
    self.crawlFields(board, 'NW', validFields)
    # going NE
    self.crawlFields(board, 'NE', validFields)
    # going SE
    self.crawlFields(board, 'SE', validFields)
    # going SW
    self.crawlFields(board, 'SW', validFields)

    #print(validFields)
    return validFields


  def isMoveLegal(self, future_x_pos, future_y_pos, board):
    futurePosition = [future_x_pos, future_y_pos]

    validFields = self.returnValidFields(board)

    if futurePosition in validFields:
      return True
    else:
      return False



class Queen(Piece):

  value = 5

  def returnValidFields(self, board):
    validFields = []

    # going North
    self.crawlFields(board, 'North', validFields)
    # going South
    self.crawlFields(board, 'South', validFields)
    # going West
    self.crawlFields(board, 'West', validFields)
    # going East
    self.crawlFields(board, 'East', validFields)
    # going NW
    self.crawlFields(board, 'NW', validFields)
    # going NE
    self.crawlFields(board, 'NE', validFields)
    # going SE
    self.crawlFields(board, 'SE', validFields)
    # going SW
    self.crawlFields(board, 'SW', validFields)

    #print(validFields)
    return validFields


  def isMoveLegal(self, future_x_pos, future_y_pos, board):
    futurePosition = [future_x_pos, future_y_pos]

    validFields = self.returnValidFields(board)

    if futurePosition in validFields:
      return True
    else:
      return False



class Knight(Piece):

  value = 2

  def returnValidFields(self, board):
    validFields = []

    p = [self.x_position+1, self.y_position+2]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position+2, self.y_position+1]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position+2, self.y_position-1]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position+1, self.y_position-2]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position-1, self.y_position-2]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position-2, self.y_position-1]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position-2, self.y_position+1]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position-1, self.y_position+2]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    #print(validFields)
    return validFields


  def isMoveLegal(self, future_x_pos, future_y_pos, board):
    futurePosition = [future_x_pos, future_y_pos]

    validFields = self.returnValidFields(board)

    if futurePosition in validFields:
      return True
    else:
      return False



class King(Piece):

  value = 6

  def returnValidFields(self, board):
    validFields = []

    p = [self.x_position, self.y_position+1]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position+1, self.y_position+1]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position+1, self.y_position]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position+1, self.y_position-1]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position, self.y_position-1]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position-1, self.y_position-1]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position-1, self.y_position]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    p = [self.x_position-1, self.y_position+1]
    if board.isFieldValid(p[0], p[1]) and (board.isEnemyOnTheField(p[0], p[1], self.color) or board.isFieldEmpty(p[0], p[1])):
      validFields.append(p)

    #castling
    if self.initialMoveNotDone:
      if self.color == 'White':
        QR1 = board.returnPieceByName("WR1")
        KR2 = board.returnPieceByName("WR2")
      else:
        QR1 = board.returnPieceByName("BR1")
        KR2 = board.returnPieceByName("BR2")
        
      # kingside
      p = [self.x_position+2, self.y_position]
      if board.isFieldValid(p[0], p[1]) and self.initialMoveNotDone and KR2.initialMoveNotDone and board.isFieldEmpty(p[0]-1,p[1]) and board.isFieldEmpty(p[0],p[1]):
        if board.isFieldSafe(self.x_position, self.y_position, self.color) and board.isFieldSafe(p[0]-1, p[1], self.color) and board.isFieldSafe(p[0], p[1], self.color):
          validFields.append(p)

      # queenside
      p = [self.x_position-2, self.y_position]
      if board.isFieldValid(p[0], p[1]) and self.initialMoveNotDone and QR1.initialMoveNotDone and board.isFieldEmpty(p[0]+1,p[1]) and board.isFieldEmpty(p[0],p[1]) and board.isFieldEmpty(p[0]-1,p[1]):
        if board.isFieldSafe(self.x_position, self.y_position, self.color) and board.isFieldSafe(p[0]+1, p[1], self.color) and board.isFieldSafe(p[0], p[1], self.color):
          validFields.append(p)

    #print(validFields)
    return validFields


  def isMoveLegal(self, future_x_pos, future_y_pos, board):
    futurePosition = [future_x_pos, future_y_pos]

    if not board.isFieldSafe(future_x_pos, future_y_pos, self.color):
      print("Can't move to chessmate!")
      return False

    validFields = self.returnValidFields(board)

    if futurePosition in validFields:
      return True
    else:
      return False

