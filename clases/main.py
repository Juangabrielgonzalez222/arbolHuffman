from browser import aio
def init():
  global arbolCodificado,anchoPantalla,altoPantalla,abrirArchivo,leerArchivo,manejadorA,espera,botones,cadenaDeArchivo,textoCadena
  abrirArchivo=False
  asset_manager.loadFont("opensansvariablefont_wdthwght")
  anchoPantalla=screen.width
  altoPantalla=screen.height
  l=ListaEnlazada()
  a1=Arbol()
  nodo=NodoHuffman(15,'A')
  a1.insertar(nodo)
  a2=Arbol()
  nodo=NodoHuffman(6,'B')
  a2.insertar(nodo)
  a3=Arbol()
  nodo=NodoHuffman(7,'C')
  a3.insertar(nodo)
  a4=Arbol()
  nodo=NodoHuffman(12,'D')
  a4.insertar(nodo)
  l.insertar(a1)
  l.insertar(a2)
  l.insertar(a3)
  l.insertar(a4)
  bandera=True
  primero=None
  while bandera:
    primero=l.primero()
    primero=l.suprimir(primero)
    segundo=l.primero()
    segundo=l.suprimir(segundo)
    if primero and segundo:
        nodo=NodoHuffman(segundo.getItem()+primero.getItem(),primero.getArbol().getCabeza().getValor()+segundo.getArbol().getCabeza().getValor())
        nodo.setIzq(primero.getArbol().getCabeza())
        nodo.setDer(segundo.getArbol().getCabeza())
        arbol=Arbol()
        arbol.insertar(nodo)
        l.insertar(arbol)
    else:
        bandera=False
  arbolCodificado=primero.getArbol()
  arbolCodificado.crearNodosGraficos()
  screen.setFont("opensansvariablefont_wdthwght")
  manejadorA=ManejadorArchivo()
  espera=0
  botones=[]
  botones.append(Boton(-anchoPantalla/2+40,-altoPantalla/2+20,60,20,'Leer Archivo'))
  botones.append(Boton(anchoPantalla/2-50,-altoPantalla/2+20,80,20,'Guardar en Archivo'))
  cadenaDeArchivo=''
  textoCadena=''
def update():
  global abrirArchivo,espera,cadenaDeArchivo,textoCadena
  if abrirArchivo:
    if espera>300:
      r=manejadorA.leerArchivo()
      if r:
        abrirArchivo=False
        if manejadorA.getContenido().find('0')==-1 and manejadorA.getContenido().find('1')==-1:
          textoCadena='Cadena codificada: '
        else:
          textoCadena='Cadena decodificada: '
        cadenaDeArchivo=arbolCodificado.procesarCadena(manejadorA.getContenido())
        textoCadena+=cadenaDeArchivo
      espera=0
    else:
      espera+=1
  if touch.release:
      posX=touch.x
      posY=touch.y
      if botones[0].getBotonSeleccionado(posX,posY) and abrirArchivo==False:
        abrirArchivo=True
        manejadorA.setLectura(False)
      elif botones[1].getBotonSeleccionado(posX,posY):
        system.file.save( cadenaDeArchivo,'cadenaCodificada.txt' )
      
def draw():
  screen.clear("rgb(175,190,197)")
  arbolCodificado.preOrden(anchoPantalla,altoPantalla)
  screen.drawText(textoCadena,(-anchoPantalla/2+screen.textWidth(textoCadena, 7)/2)+10,-50,7)
  for boton in botones:
    boton.draw()