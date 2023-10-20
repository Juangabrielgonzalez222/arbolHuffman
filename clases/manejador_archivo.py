class ManejadorArchivo:
  __lectura=False
  __contenido=None
  def __init_(self):
    self.__lectura=False
  def setLectura(self,v):
    self.__lectura=v
  def getLectura(self):
    return self.__lectura
  def getContenido(self):
    return self.__contenido
  def leerArchivo(self):
    system.file.load( ["txt"],self.recorrerArchivos)
    return self.__lectura
  def recorrerArchivos(self,file_list):
    self.__lectura=True
    for file in file_list:
      self.__contenido=file.content