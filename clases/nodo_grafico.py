class NodoGrafico:
  __texto1=''
  __ancho=0
  __alto=0
  def __init__(self,texto1='',ancho=0,alto=0):
    self.__texto1=texto1
    self.__ancho=ancho
    self.__alto=alto
  def getAlto(self):
    return self.__alto
  def getAncho(self):
    return self.__ancho
  def mostrar(self,x,y):
    screen.fillRoundRect(x,y,self.__ancho,self.__alto,self.__ancho,'rgb(175,190,197)')
    screen.drawRoundRect(x,y,self.__ancho,self.__alto,self.__ancho,'#000')
    screen.drawText(self.__texto1,x,y,6,'#000')