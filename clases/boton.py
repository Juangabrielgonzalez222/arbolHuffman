class Boton:
  __x=0
  __y=0
  __ancho=0
  __alto=0
  __texto=''
  def __init__(self,x=0,y=0,ancho=20,alto=60,texto=''):
    self.__x=x
    self.__y=y
    self.__ancho=ancho
    self.__alto=alto
    self.__texto=texto
  def getX(self):
    return self.__x
  def getY(self):
    return self.__y
  def getTexto(self):
    return self.__texto
  def getAncho(self):
    return self.__ancho
  def getAlto(self):
    return self.__alto
  def setTexto(self,t):
    self.__texto=t
  def getBotonSeleccionado(self,posX,posY):
    res=None
    sup=self.__y+self.__alto/2
    inf=self.__y-self.__alto/2
    der=self.__x-self.__ancho/2
    izq=self.__x+self.__ancho/2
    if posY<sup and posY>inf and posX<izq and posX>der:
      res=True
    return res
  def mostrarTexto(self):
    screen.drawText(self.__texto,self.__x,self.__y,6,'#000')
  def draw(self):
    screen.drawRect(self.__x,self.__y,self.__ancho,self.__alto,'#000')
    self.mostrarTexto()