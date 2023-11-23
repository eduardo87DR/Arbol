class NodoArbol:
    def __init__(self,dato):   ##inicializa la clase
        self.dato = dato 
        self.izq = None #nodo izquierdo vacio
        self.der = None #nodo derecho vacio

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self,dato):
        if self.raiz is None: #Si el arbol esta vacio se crea la raiz 
            self.raiz = NodoArbol(dato)
        else: #Si no, se llama la recursividad para insertar
            self.insertar_recursivo(self.raiz,dato)
#Hacer nodo recursivo
    def insertar_recursivo(self, nodo, nuevo_dato):
        if nuevo_dato < nodo.dato:
            if nodo.izq is None: #Si no hay nodo izquierdo, se inserta
                nodo.izq = NodoArbol(nuevo_dato)
            else: 
                self.insertar_recursivo(nodo.izq, nuevo_dato)
        else:
            if nodo.der is None: #Si no hay nodo derecho, se inserta
                nodo.der = NodoArbol(nuevo_dato)
            else: 
                self.insertar_recursivo(nodo.der, nuevo_dato) 

    #mostrar el arbol de mayor a menor
    def mostrar_arbol(self): 
        self.mostrar_recursivo(self.raiz, 0) #se necesita para los nodos
        #el 0 se envia porque la raiz esta en el nivel 0
    
    def mostrar_recursivo(self,nodo,nivel): #necesita estos parametros para las funciones
        if nodo is not None:
          self.mostrar_recursivo(nodo.der, nivel + 1) #Mostrar recursivamente el lado derecho
          print(" " * nivel + str(nodo.dato)) #Imprimir dato con el nivel
          self.mostrar_recursivo(nodo.izq, nivel + 1) #Mostrar recursivamente el lado izquierdo

    #Busqueda de elementos
    def buscar(self,dato):
        return self.buscar_recursivo(self.raiz,dato)
    
    #Buscar elementos recursivamente en el arbol
    def buscar_recursivo(self,nodo,dato):
        if nodo is None or nodo.dato == dato:
            return nodo 
        if dato < nodo.dato: #Si el dato es menor, se busca en el lado izquierdo
            return self.buscar_recursivo(nodo.izq, dato)
        return self.buscar_recursivo(nodo.der,dato)
    
    #Eliminar nodos
    def eliminar (self,dato):
        self.raiz = self.eliminar_recursivo(self.raiz,dato)
    #Eliminar nodos recursivamente    
    def eliminar_recursivo(self, nodo, dato):
        if nodo is None:
            return nodo 
        if dato < nodo.dato:
            nodo.izq =self.eliminar_recursivo(nodo.izq,dato)
        elif dato >nodo.dato:
            nodo.der = self.eliminar_recursivo(nodo.der, dato)
        else:
            if(nodo.izq is None):
                return nodo.der
            elif nodo.derecha is None:
                return nodo.izq
            nodo.dato =self.encontrar_minimo(nodo.derecha)
            nodo.derecha = self.eliminar_recursivo(nodo.derecha, nodo.dato)
        return nodo
    
    def encontrar_minimo(self, nodo): #encontrar valor minimo del subarbol
        actual = nodo
        while (actual.izq is not None):
            actual = actual.izq
        return actual.dato
    

    #RECORRIDOS DEL ARBOL 
    # Preorden                                                                                                                                                                                             
    def preOrden(self,nodo,resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self.preOrden(nodo.izq,resultado)
            self.preOrden(nodo.der,resultado)
    #Realizar preorden
    def recorrer_preOrden(self):
        resultado = []
        self.preOrden(self.raiz, resultado)
        return resultado
    
    #Inorden
    def inOrden(self, nodo, resultado):
        if nodo is not None:
            self.inOrden(nodo.izq, resultado)
            resultado.append(nodo.dato)
            self.inOrden(nodo.der,resultado)
    #Realizar inorden
    def recorrer_inOrden(self):
        resultado = []
        self.inOrden(self.raiz, resultado)
        return resultado
    
    #PostOrden
    def postOrden(self, nodo, resultado):
        if nodo is not None:
            self.postOrden(nodo.izq, resultado)
            self.postOrden(nodo.der, resultado)
            resultado.append(nodo.dato)

    def recorrer_postOrden(self): #Realizar recorrido postorden
        resultado= []
        self.postOrden(self.raiz, resultado)
        return resultado



#LLAMADO A LA CLASE
arbol = ArbolBinario()
opcion = "si"
while opcion == "si":
    dato_insertar = int(input("ingresa un dato: ")) 
    print("si: Continuar insertando elementos")
    print("no: Terminar la inserción ")
    opcion = input("Ingresa si o no: ")
    arbol.insertar(dato_insertar)

arbol.mostrar_arbol()
dato_buscar = int (input("Que numero quieres buscar?: "))
resultado_busqueda = arbol.buscar(dato_buscar)
if resultado_busqueda:
    print(f"El numero {dato_buscar} fue encontrado en el arbol")
else:
    print(f"El numero {dato_buscar} no se encontro en el arbol")


#Seccion de decision para eliminar
eliminar_opcion = input("Deseas eliminar un nodo del arbol? (si/no): ")
if eliminar_opcion.lower() == "si":
    dato_eliminar = int (input("Que numero quieres eliminar: " ))
    arbol.eliminar(dato_eliminar)
    print("se elimino el número {dato}")
    arbol.mostrar_arbol()

print("Recorrido en inorden: ")
resultado_inOrden = arbol.recorrer_inOrden()
print(resultado_inOrden)

print("Recorrido en preorden: ")
resultado_preOrden = arbol.recorrer_preOrden()
print(resultado_preOrden)

print("Recorrido en postOrden: ")
resultado_postOrden = arbol.recorrer_postOrden()
print(resultado_postOrden)