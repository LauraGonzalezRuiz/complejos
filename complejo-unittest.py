#!/usr/bin/env python3

import unittest

class Complejo(object):
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def sumar(self, otro):
        result = Complejo(self.real + otro.real,
                            self.imag + otro.imag)
        return result

    def restar(self, otro):
        result = Complejo(self.real - otro.real,
                            self.imag - otro.imag)
        return result

    def multiplicar(self, otro):
        result = Compeljo(self.real*otro.real - self.imag*otro.imag, self.real*otro.imag + otro.real*self.imag)

        return result

    def dividir(self, otro):
        numerador = Compeljo(self.real*otro.real + self.imag*otro.imag, - self.real*otro.imag + otro.real*self.imag)
        denominador = Complejo(otro.real**2 + otro.imag**2)
        reuslt = numerador / denominador

        return result

    def igual(self, otro):
        return self.real == otro.real and self.imag == otro.imag 


class TestComplejo(unittest.TestCase):

    def test_sumar(self):

        c1 = Complejo(1,2)
        c2 = Complejo(3,4)

        suma = c1.sumar(c2)

        self.assertEqual(suma.real, 4)
        self.assertEqual(suma.imag, 6)

    def test_restar(self):

        c1 = Complejo(6,1)
        c2 = Complejo(8,4)

        restar = c1.restar(c2)

        self.assertEqual(restar.real, -2)
        self.assertEqual(restar.imag, -3)

    def test_multiplicar(self):
        
        c1 = Complejo(5,1)
        c2 = Complejo(8,6)

        multiplicacion = c1.multiplicar(c2)

        self.assertEqual(multiplicar.real, 34)
        self.assertEqual(multiplicar.imag, 38)

    def test_dividir(self):
        
        c1 = Complejo(1,2)
        c2 = Complejo(3,4)

        division = c1.dividir(c2)

        self.assertEqual(multiplicar.real, 11/(-7))
        self.assertEqual(multiplicar.imag, 2/(-7))

if __name__ == "__main__":
    unittest.main()


