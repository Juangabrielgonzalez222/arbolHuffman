class Nodo:
    __item=None
    __sig=None
    def __init__(self):
        self.__item=None
        self.__sig=None
    def getItem(self):
        return self.__item.getCabeza().getFrecuencia()
    def getArbol(self):
        return self.__item
    def getSiguiente(self):
        return self.__sig
    def cargarItem(self,x):
        self.__item=x
    def cargarSiguiente(self,x):
        self.__sig=x

class ListaEnlazada:
    __cab=None
    __cant=0
    def __init__(self):
        self.__cab=None
        self.__cant=0
    def vacia(self):
        return self.__cant==0
    def primero(self):
        x=None
        if not self.vacia():
            x=self.__cab.getItem()
        return x
    def ultimo(self):
        x=None
        if not self.vacia():
            aux=self.__cab
            while aux.getSiguiente()!=None:
                aux=aux.getSiguiente()
            x=aux.getItem()
        return x
    def siguiente(self,p):
        if not self.vacia() and p>0 and p<self.__cant:
            p+=1
        else:
            p=None
        return p
    def anterior(self,p):
        if not self.vacia() and p>1 and p<=self.__cant:
            p-=1
        else:
            p=None
        return p
    def insertar(self,x):
        nodo=Nodo()
        nodo.cargarItem(x)
        if self.vacia():
            self.__cab=nodo
        elif self.__cab.getItem()>nodo.getItem():
            nodo.cargarSiguiente(self.__cab)
            self.__cab=nodo
        else:
            aux=self.__cab
            while aux.getSiguiente()!=None and  nodo.getItem()> aux.getSiguiente().getItem():
                aux=aux.getSiguiente()
            nodo.cargarSiguiente(aux.getSiguiente())
            aux.cargarSiguiente(nodo)
        self.__cant+=1
    def suprimir(self,x):
        res = None
        if not self.vacia():
            if self.__cab.getItem()==x:
                res=self.__cab
                self.__cab=self.__cab.getSiguiente()    
            else:
                aux=self.__cab
                while aux.getSiguiente()!=None and aux.getSiguiente().getItem()!=x:
                    aux=aux.getSiguiente()
                if aux.getSiguiente()!=None:
                    res=aux.getSiguiente()
                    aux.cargarSiguiente(aux.getSiguiente().getSiguiente())
            self.__cant-=1
        return res
    def buscar(self,x):
        aux=self.__cab
        p=1
        while aux!=None and aux.getItem()!=x:
            p+=1
            aux=aux.getSiguiente()
        if aux==None:
            p=None
        return p
    def recuperar(self,p):
        res=None
        aux=self.__cab
        if p>0 and p<=self.__cant:
            while p>1:
                aux=aux.getSiguiente()
                p-=1
            if p==1:
                res=aux.getItem()
        return res
    def recorrer(self):
        aux=self.__cab
        while aux!=None:
            print(aux.getItem(),aux.getArbol().getCabeza().getValor())
            aux=aux.getSiguiente()