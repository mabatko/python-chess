class Player:

  myPieces = []
  oponentsPieces = []

  def __init__(self, chessboard, color):
    self.cb = chessboard
    self.color = color
    

  def updatePieces(self):
    self.myPieces = []
    self.oponentsPieces = []
    for pieces in self.cb.pieces:
      if pieces.color == self.color and pieces.isActive:
        self.myPieces.append(pieces)
      if pieces.color != self.color and pieces.isActive:
        self.oponentsPieces.append(pieces)
        

  def returnRandomPieceName(self):
    import random

    randomIndex = random.randint(0, len(self.myPieces)-1)
    return self.myPieces[randomIndex].name
  

  def randomValidMove(self, piece_name):
    import random
    move = ["NNN", -1, -1]
    
    piece = self.cb.returnPieceByName(piece_name)
    validFields = piece.returnValidFields(self.cb)

    if len(validFields) == 0:
      return move
    
    randomIndex = random.randint(0,len(validFields)-1)
    move[0] = piece.name
    move[1] = validFields[randomIndex][0]
    move[2] = validFields[randomIndex][1]
    return move


  def attackIfPossible(self, pieceName):
    piece = self.cb.returnPieceByName(pieceName)

    validFields = piece.returnValidFields(self.cb)
    for field in validFields:
      if self.cb.isEnemyOnTheField(field[0], field[1], piece.color):
        return [pieceName, field[0], field[1]]
    return self.randomValidMove(pieceName)


  def doMove(self):
    self.updatePieces()

    # check if King is endangered
    if self.color == "Black":
      king = self.cb.returnPieceByName("BKK")
    else:
      king = self.cb.returnPieceByName("WKK")
      
    if not self.cb.isFieldSafe(king.x_position, king.y_position, king.color):
      print("king has to move")
    
    bestAttackPossible = self.bestAttackPossible()
    if bestAttackPossible[0] == 'NNN':
      while True:
        pieceName = self.returnRandomPieceName()
        #print(pieceName)
        bestAttackPossible = self.randomValidMove(pieceName)
        if bestAttackPossible[0] != 'NNN':
          break
        #else:
          #print("No valid moves for {}".format(pieceName))
    return bestAttackPossible


  def bestAttackPossible(self):
    bestAttackerSoFar = 'NNN'
    bestVictimSoFarX = -1
    bestVictimSoFarY = -1
    bestVictimsValue = -1

    for attacker in self.myPieces:
      for victim in self.oponentsPieces:
        if self.cb.canAttack(attacker.name, victim.name):
          if victim.value > bestVictimsValue:
            bestAttackerSoFar = attacker.name
            bestVictimSoFarX = victim.x_position
            bestVictimSoFarY = victim.y_position
            bestVictimsValue = victim.value
    return [bestAttackerSoFar, bestVictimSoFarX, bestVictimSoFarY]


