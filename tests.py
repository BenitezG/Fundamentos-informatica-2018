import unittest
import tpfinal as tp


# Tests para el trabajo final

# Test para "Elementos"

class ElementoTest(unittest.TestCase):
    def test_basicos(self):
        hidrogeno = tp.Elemento(1, 0, 1, "H")
        oxigeno = tp.Elemento(8, 8, 2, "O")
        self.assertEqual(8, oxigeno.cantProtones())
        self.assertEqual(8, oxigeno.cantNeutrones())
        self.assertEqual(8, oxigeno.cantElectrones())
        self.assertEqual(8, oxigeno.numeroAtomico())
        self.assertEqual(16, oxigeno.pesoAtomico())
        self.assertEqual(2, oxigeno.valencia())
        self.assertEqual('O', oxigeno.simbolo())
        self.assertEqual(1, hidrogeno.cantProtones())
        self.assertEqual(0, hidrogeno.cantNeutrones())
        self.assertEqual(1, hidrogeno.cantElectrones())
        self.assertEqual(1, hidrogeno.numeroAtomico())
        self.assertEqual(1, hidrogeno.pesoAtomico())
        self.assertEqual(1, hidrogeno.valencia())
        self.assertEqual('H', hidrogeno.simbolo())


# Test para "TablaPeriodica"

class TablaPeriodicaTest(unittest.TestCase):
    def test_basicos(self):
        self.assertEqual(4, len(tp.tablaP.elementos()))
        self.assertEqual(6, tp.tablaP.elementoS('C').numeroAtomico())
        self.assertEqual(14, tp.tablaP.elementoN(7).pesoAtomico())


# Test para "Compuestos"

class CompuestoTest(unittest.TestCase):
    def test_basicos(self):
        nh3 = tp.Compuesto('NH3')
        nh3.agregarAtomo(tp.tablaP.elementoS("N"), "N1")
        nh3.agregarAtomo(tp.tablaP.elementoS("H"), "H2")
        nh3.agregarAtomo(tp.tablaP.elementoS("H"), "H3")
        nh3.agregarAtomo(tp.tablaP.elementoS("H"), "H4")
        nh3.enlazar("N1", "H2")
        nh3.enlazar("N1", "H3")
        nh3.enlazar("N1", "H4")
        self.assertEqual(4, nh3.cantAtomos())
        self.assertEqual(True, nh3.incluyeAtomo("N1"))
        self.assertEqual(False, nh3.incluyeAtomo("N4"))
        self.assertEqual(3, nh3.cantEnlaces())
        self.assertEqual(17, nh3.masaMolar())


# Test para "Medio"

class MedioTest(unittest.TestCase):
    def test_basicos(self):
        medioRaro = tp.Medio()
        medioRaro.agregarComponente(tp.agua, 100)
        medioRaro.agregarComponente(tp.nh3, 6)
        medioRaro.agregarComponente(tp.metano, 20)
        medioRaro.agregarComponente(tp.co2, 14)
        medioRaro.agregarComponente(tp.nh3, 15)
        self.assertEqual(3093, medioRaro.masaTotal())
        self.assertCountEqual(["CO2", "H2O", "NH3", "CH4"], medioRaro.compuestosPresentes())
        self.assertEqual(1800, medioRaro.masaDeCompuesto(tp.agua))


# Test para "DescripcionMedio"

class DescripcionMedioTest(unittest.TestCase):
    def test_basicos(self):
        miDescripcion = tp.DescripcionMedio("[H2O][CO2][H2O][CH4]")
        tp.medioRaro.agregarComponente(tp.agua, 100)
        tp.medioRaro.agregarComponente(tp.nh3, 6)
        tp.medioRaro.agregarComponente(tp.metano, 20)
        tp.medioRaro.agregarComponente(tp.co2, 14)
        miDescripcion.agregarAMedio(tp.medioRaro, tp.agua)
        self.assertEqual(True, miDescripcion.apareceCompuesto(tp.agua))
        self.assertEqual(False, miDescripcion.apareceCompuesto(tp.nh3))
        self.assertEqual(2, miDescripcion.molesCompuesto(tp.agua))
        self.assertEqual(0, miDescripcion.molesCompuesto(tp.nh3))
        self.assertEqual(102, tp.medioRaro.composicion[tp.agua])
