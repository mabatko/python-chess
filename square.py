class Square():

  def __init__(self, color, xPosition, yPosition):
    self.color = color
    self.xPosition = xPosition
    self.yPosition = yPosition
    self.pieceOn = " - "


  def printSquare(self):
    if self.color == "White":
      return "░░"+self.pieceOn+"░░"
    else:
      return "▓▓"+self.pieceOn+"▓▓"
