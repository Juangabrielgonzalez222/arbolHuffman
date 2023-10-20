class NodoHuffman:
    __frecuencia=0
    __valor=""
    __izq=None
    __der=None
    __nodoGrafico=None
    def __init__(self,frecuencia=0,valor=""):
        self.__frecuencia=frecuencia
        self.__valor=valor
        self.__izq=None
        self.__der=None
        self.__nodoGrafico=None
    def getFrecuencia(self):
        return self.__frecuencia
    def getValor(self):
        return self.__valor
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der
    def setFrecuencia(self,frecuencia):
        self.__frecuencia=frecuencia
    def setValor(self,valor):
        self.__valor=valor
    def setIzq(self,izq):
        self.__izq=izq
    def setDer(self,der):
        self.__der=der
    def crearNodoGrafico(self,tamaño):
      self.__nodoGrafico=NodoGrafico(self.__valor,tamaño,tamaño)
    def mostrar(self,x,y):
      self.__nodoGrafico.mostrar(x,y)
    def getNodoGAlto(self):
      return self.__nodoGrafico.getAlto()
    def getNodoGAncho(self):
      return self.__nodoGrafico.getAncho()
class Arbol:
    __cab=None
    def __init__(self):
        self.__cab=None
    def getCabeza(self):
        return self.__cab
    def insertarRecursivo(self,nodoNuevo,nodo):
        if nodoNuevo.getFrecuencia() != nodo.getFrecuencia():
            if nodoNuevo.getFrecuencia() < nodo.getFrecencia():
                if nodo.getIzq():
                    self.insertarRecursivo(nodoNuevo,nodo.getIzq())
                else:
                    nodo.setIzq(nodoNuevo)
            else:
                if nodo.getDer():
                    self.insertarRecursivo(nodoNuevo,nodo.getDer())
                else:
                    nodo.setDer(nodoNuevo)
        else:
            print('El dato ya se encuentra en el arbol.')
    def insertar(self,nodo):
        if self.__cab==None:
            self.__cab=nodo
        else:
            self.insertarRecursivo(nodo,self.__cab)
    def preOrden(self,ancho,alto):
        if self.__cab:
          self.preOrdenRecursivo(self.__cab,0,(alto/2))
    def preOrdenRecursivo(self,nodo,x,y):
        if nodo is not None:
          alto=nodo.getNodoGAlto()
          if nodo==self.__cab:
            y-=alto/2+8
          if nodo.getIzq():
            screen.drawLine(x,y,x-alto,y-alto)
            screen.drawLine(x,y,x+alto,y-alto)
          nodo.mostrar(x,y)
          y-=alto
          self.preOrdenRecursivo(nodo.getIzq(),x-alto,y)
          self.preOrdenRecursivo(nodo.getDer(),x+alto,y)
    def crearNodosGraficos(self):
      self.crearNodosGraficosR(self.__cab,6*len(self.__cab.getValor()))
    def crearNodosGraficosR(self,nodo,tamaño):
      if nodo is not None:
          nodo.crearNodoGrafico(tamaño)
          self.crearNodosGraficosR(nodo.getIzq(),tamaño)
          self.crearNodosGraficosR(nodo.getDer(),tamaño)
    def buscar(self,dato):
        res=self.buscarRecursivo(dato,self.__cab)
        return res
    def buscarRecursivo(self,dato,nodo):
        if nodo and nodo.getIzq():
            if nodo.getIzq().getValor().find(dato)!=-1:
                return '0'+self.buscarRecursivo(dato,nodo.getIzq())
            elif nodo.getDer().getValor().find(dato)!=-1:
                return '1'+self.buscarRecursivo(dato,nodo.getDer())
            else:
                return ''
        else:
            return ''
    def buscarDecodificar(self,dato):
      res=self.buscarDRecursivo(dato,self.__cab)
      return res
    def buscarDRecursivo(self,dato,nodo,res=''):
      if len(dato)>0:
        if nodo.getIzq():
          numero=dato[0]
          if len(dato)>1:
            dato2=''
            for i in range(1,len(dato)):
              dato2+=dato[i]
            dato=dato2
          else:
            dato=''
          if numero=='0':
            return self.buscarDRecursivo(dato,nodo.getIzq(),res)
          else:
            
            return self.buscarDRecursivo(dato,nodo.getDer(),res)
        else:
          res+=nodo.getValor()
          return self.buscarDRecursivo(dato,self.__cab,res)
      else:
        res+=nodo.getValor()
        return res
    def altura(self):
        return self.alturaRecursivo(self.__cab)
    def alturaRecursivo(self,nodo):
        if nodo ==None:
            return 0
        alturaIzq=self.alturaRecursivo(nodo.getIzq())
        alturaDer=self.alturaRecursivo(nodo.getDer())

        alturaActual=0
        if alturaIzq>alturaDer:
            alturaActual=alturaIzq
        else:
            alturaActual=alturaDer
        return alturaActual+1
    def procesarCadena(self,cadena):
      nuevaCadena=''
      cadena.replace(' ','')
      if cadena.find('0')!=-1 or cadena.find('1')!=-1:
        nuevaCadena=self.buscarDecodificar(cadena)
      else:
        for i in range(len(cadena)):
          nuevaCadena+=self.buscar(cadena[i])
      return nuevaCadena