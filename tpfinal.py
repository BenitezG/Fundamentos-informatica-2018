import re


class Elemento:
    def __init__(self, prot, neut, val, sim):
        self.prot = prot
        self.neut = neut
        self.val = val
        self.sim = sim

    def cantProtones(self):
        return self.prot

    def cantNeutrones(self):
        return self.neut

    def cantElectrones(self):
        return self.prot

    def numeroAtomico(self):
        return self.prot

    def pesoAtomico(self):
        return self.prot + self.neut

    def valencia(self):
        return self.val

    def simbolo(self):
        return self.sim


class TablaPeriodica:
    def __init__(self):
        self.listaelementos = []

    def agregarElemento(self, elemento):
        if len(self.listaelementos) == 0:
            self.listaelementos.append(elemento)
        elif len(self.listaelementos) > 0 and elemento.simbolo() not in [self.listaelementos[i].simbolo() for i in range(len(self.listaelementos))]:
            self.listaelementos.append(elemento)
        else:
            print("El elemento ya está en la tabla")

    def elementos(self):
        return self.listaelementos

    def elementoS(self, simbolo):
        for i in range(len(self.listaelementos)):
            if simbolo == self.listaelementos[i].simbolo():
                return self.listaelementos[i]

    def elementoN(self, numero):
        for i in range(len(self.listaelementos)):
            if numero == self.listaelementos[i].cantProtones():
                return self.listaelementos[i]


class Compuesto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.compuesto = {}
        self.enlaces = []

    def nombreCompuesto(self):
        return self.nombre

    def elementosSegunNombre(self):
        return [self.nombreCompuesto()[0], self.nombreCompuesto()[1]]

    def mostrarCompuesto(self):
        return self.compuesto

    def mostrarEnlaces(self):
        return self.enlaces

    def agregarAtomo(self, elemento, atomo):
        self.compuesto[atomo] = elemento

    def agregarAtomos(self, elemento, atomo):
        if type(atomo) == list:
            for i in range(len(atomo)):
                self.compuesto[atomo[i]] = elemento
        elif type(atomo) == int:
            for i in range(1, atomo + 1):
                self.compuesto[elemento.simbolo() + str(i)] = elemento

    def enlazar(self, atomo1, atomo2):
        self.enlaces.append((atomo1, atomo2))

    def enlazarConVarios(self, atomo1, atomo2):
        for i in range(len(atomo2)):
            self.enlaces.append((atomo1, atomo2[i]))

    def enlacesOK(self):
        elemlist = list(self.mostrarCompuesto().keys())
        enlaceslist = self.mostrarEnlaces()
        for i in range(len(enlaceslist)):
            if enlaceslist[i][0] not in elemlist or enlaceslist[i][1] not in elemlist:
                return "Hay al menos un enlace mal hecho\nRevisar los enlaces"

        for i in elemlist:
            if self.cantEnlacesAtomo(i) > self.mostrarCompuesto()[i].valencia():
                return print("Hay átomos con más enlaces que los permitidos\nRevisar los enlaces")

        return "Los enlaces están bien"

    def atomosConEnlacesSobrantes(self):
        masenlaces = []
        elemlist = list(self.mostrarCompuesto().keys())
        for i in elemlist:
            if self.cantEnlacesAtomo(i) > self.mostrarCompuesto()[i].valencia():
                masenlaces.append(i)
        return masenlaces

    def atomosConEnlacesDisponibles(self):
        masenlaces = []
        elemlist = list(self.mostrarCompuesto().keys())
        for i in elemlist:
            if self.cantEnlacesAtomo(i) < self.mostrarCompuesto()[i].valencia():
                masenlaces.append(i)
        return masenlaces

    def cantAtomos(self):
        return len(self.compuesto)

    def atomosDe(self, elemento):
        return sorted(
            [key for key, value in self.compuesto.items() if elemento == value])

    def incluyeAtomo(self, atomo):
        return atomo in self.compuesto.keys()

    def incluyeElemento(self, elemento):
        return elemento in self.compuesto.values()

    def elementosPresentes(self):
        return list(set(self.compuesto.values()))

    def cantElemento(self, elemento):
        keylist = []
        itemlist = list(self.compuesto.items())
        for item in itemlist:
            if item[1] == elemento:
                keylist.append(item[0])
        return len(keylist)

    def cantEnlaces(self):
        return len(self.enlaces)

    def cantEnlacesAtomo(self, atomo):
        numenlaces = 0
        for i in range(len(self.enlaces)):
            if atomo in self.enlaces[i]:
                numenlaces += 1
        return numenlaces

    def masaMolar(self):
        listaelem = list(self.compuesto.values())
        return sum([listaelem[i].pesoAtomico() for i in range(len(listaelem))])

    def proporcionSobreMasa(self, elemento):
        return elemento.pesoAtomico() / self.masaMolar()

    def conQuienesEstaEnlazado(self, nombre):
        listaenlaces = []
        for i in range(len(self.enlaces)):
            if nombre in self.enlaces[i]:
                if nombre == self.enlaces[i][0]:
                    listaenlaces.append(self.enlaces[i][1])
                else:
                    listaenlaces.append(self.enlaces[i][0])
        return listaenlaces

    def estanEnlazado(self, elem1, elem2):
        return (elem1, elem2) in self.enlaces or (elem2, elem1) in self.enlaces


class Medio:
    def __init__(self):
        self.composicion = {}

    def mostrarMedio(self):
        listaMedio = []
        for i in list(self.composicion.items()):
            listaMedio.append([i[0].nombreCompuesto(), i[1]])
        return listaMedio

    def agregarComponente(self, componente, cantidad):
        if componente in self.composicion:
            self.composicion[componente] = self.composicion[
                                               componente] + cantidad
        else:
            self.composicion[componente] = cantidad
        return self.composicion

    def masaTotal(self):
        masa = 0
        for i in list(self.composicion.items()):
            masa = masa + (i[0].masaMolar() * i[1])
        return masa

    def elementosPresentes(self):
        listaelementos = []
        objs = [elem.elementosPresentes() for elem in
                list(self.composicion.keys())]
        for i in objs:
            for j in i:
                listaelementos.append(j)
        return [elem.simbolo() for elem in (set(listaelementos))]

    def compuestosPresentes(self):
        return [elem.nombreCompuesto() for elem in
                list(self.composicion.keys())]

    def cantMolesElementos(self, elemento):
        numelem = 0
        for i in list(self.composicion.items()):
            numelem = numelem + (i[0].cantElemento(elemento) * i[1])
        return numelem

    def masaDeCompuesto(self, compuesto):
        return compuesto.masaMolar() * self.composicion[compuesto]

    def masaDeElemento(self, elemento):
        return self.cantMolesElementos(elemento) * elemento.pesoAtomico()

    def proporcionElementoSobreMasa(self, elemento):
        return (self.cantMolesElementos(
            elemento) * elemento.pesoAtomico()) / self.masaTotal()

    def proporcionCompuestoSobreMasa(self, compuesto):
        return (compuesto.masaMolar() * self.composicion[
            compuesto]) / self.masaTotal()

    def escalar(self, numero):
        keyslist = list(self.composicion.keys())
        for key in keyslist:
            self.composicion[key] *= numero

    def incorporarMedio(self, otroMedio):
        for i in otroMedio.composicion.keys():
            self.composicion[i] = self.composicion[i] + otroMedio.composicion[i]
        return self.composicion

    def masMedio(self, otroMedio):
        nuevomedio = Medio()
        for i in otroMedio.composicion.keys():
            nuevomedio.composicion[i] = self.composicion[i] + otroMedio.composicion[i]
        return nuevomedio


class DescripcionMedio:
    def __init__(self, medio):
        self.descripcionmedio = medio

    def descMed(self):
        return self.descripcionmedio

    def apareceCompuesto(self, comp):
        a = comp.nombreCompuesto()
        return re.search(a, self.descMed()) is not None

    def molesCompuesto(self, comp):
        a = comp.nombreCompuesto()
        if re.search(a, self.descMed()) is not None:
            return len(re.findall(a, self.descMed()))
        else:
            return 0

    def quienesAparecen(self, listaDeCompuestos):
        listaaparecen = []
        for i in listaDeCompuestos:
            if i.nombreCompuesto() in self.descMed():
                listaaparecen.append(i.nombreCompuesto())
        return listaaparecen

    def agregarAMedio(self, medio, compuesto):
        a = compuesto.nombreCompuesto()
        if re.search(a, self.descMed()) is not None:
            medio.agregarComponente(compuesto, len(re.findall(a, self.descMed())))


# Datos para hacer los Test

# Datos para hacer el test de la clase TablaPeriodica

oxigeno = Elemento(8, 8, 2, "O")
nitrogeno = Elemento(7, 7, 3, "N")
hidrogeno = Elemento(1, 0, 1, "H")
carbono = Elemento(6, 6, 4, "C")

tablaP = TablaPeriodica()

tablaP.agregarElemento(oxigeno)
tablaP.agregarElemento(hidrogeno)
tablaP.agregarElemento(nitrogeno)
tablaP.agregarElemento(carbono)

# Datos para hacer el test de la clase Compuesto

nh3 = Compuesto("NH3")
nh3.agregarAtomo(tablaP.elementoS("N"), "N1")
nh3.agregarAtomo(tablaP.elementoS("H"), "H2")
nh3.agregarAtomo(tablaP.elementoS("H"), "H3")
nh3.agregarAtomo(tablaP.elementoS("H"), "H4")
nh3.enlazar("N1", "H2")
nh3.enlazar("N1", "H3")
nh3.enlazar("N1", "H4")

# Datos para hacer el test de la clase Medio

agua = Compuesto("H2O")
agua.agregarAtomo(tablaP.elementoS("O"), "O1")
agua.agregarAtomo(tablaP.elementoS("H"), "H2")
agua.agregarAtomo(tablaP.elementoS("H"), "H3")
agua.enlazar("O1", "H2")
agua.enlazar("O1", "H3")

metano = Compuesto("CH4")
metano.agregarAtomo(tablaP.elementoS("C"), "C1")
metano.agregarAtomo(tablaP.elementoS("H"), "H2")
metano.agregarAtomo(tablaP.elementoS("H"), "H3")
metano.agregarAtomo(tablaP.elementoS("H"), "H4")
metano.agregarAtomo(tablaP.elementoS("H"), "H5")
metano.enlazar("C1", "H2")
metano.enlazar("C1", "H3")
metano.enlazar("C1", "H4")
metano.enlazar("C1", "H5")

co2 = Compuesto("CO2")
co2.agregarAtomo(tablaP.elementoS("C"), "C1")
co2.agregarAtomo(tablaP.elementoS("O"), "O2")
co2.agregarAtomo(tablaP.elementoS("O"), "O3")
co2.enlazar("C1", "O2")
co2.enlazar("C1", "O2")
co2.enlazar("C1", "O3")
co2.enlazar("C1", "O3")

# Datos para hacer el test de la clase DescripcionMedio
medioRaro = Medio()
