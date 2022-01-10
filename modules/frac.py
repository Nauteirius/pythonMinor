class Frac:
    """Klasa reprezentująca ułamek."""



    def __init__(self, x=0, y=1):

        #dodac wlasciwosci czyszczoce sprawdzajace. #Done.
        if y == 0:
            try:
                raise ValueError #Czy zabezpieczenie zostało poprawnie wprowadzone?
            except ValueError:
                print("Can't divide by 0")
        else:
            self.x = x//Frac.nwd(x,y)
            self.y = y//Frac.nwd(x,y)

    @staticmethod
    def nwd(x,y): 
        if((x % y)==0):
            return y
        else:
            return Frac.nwd(y,(x%y))
        

        
         
    
    def normalize(self, other):
        if isinstance(other, int): 
            other = Frac(other)
        elif isinstance(other, float):
            a,b = other.as_integer_ratio()
            other = Frac(a,b)
        return other 
   
    def __str__(self):          # zwraca "x/y" lub "x" dla y=1
        if (self.y == 1):
            return str(self.x)
        else:
            return (str(self.x) + "/" + str(self.y))

    def __repr__(self):         # zwraca "Frac(x, y)"
        return "Frac(" + str(self.x) + ", " + str(self.y) + ")"

    #def __cmp__(self, other): pass  # cmp(frac1, frac2)    # Py2

    def __eq__(self, other):     # Py2.7 i Py3
        other=self.normalize(other)
        if ((self.x / self.y) == (other.x / other.y)):
            return True
        else:
            return False

    __req__ = __eq__

    def __ne__(self, other): 
        other=self.normalize(other)
        if ((self.x / self.y) == (other.x / other.y)): 
            return False
        else:
            return True

    __rne__ = __ne__

    def __lt__(self, other): 
        other=self.normalize(other)
        if ((self.x / self.y) < (other.x / other.y)):
            return True
        else:
            return False

    #def __rlt__(self, other):
    #    other=self.normalize(other)
    #    return not self.__lt__(other) #TypeError: '<' not supported between instances of 'float' and 'Frac' - dlaczego?

    def __le__(self, other): 
        other=self.normalize(other)
        if ((self.x / self.y) <= (other.x / other.y)):
            return True
        else:
            return False

    def __gt__(self, other): 
        other=self.normalize(other)
        if ((self.x / self.y) > (other.x / other.y)):
            return True
        else:
            return False

    def __ge__(self, other): 
        other=self.normalize(other)
        if ((self.x / self.y) >= (other.x / other.y)):
            return True
        else:
            return False

    def __add__(self, other):   # frac1+frac2, frac+int
        #other.normalize() nie jestem pewien dlaczego taki zapis nie dziala
        other=self.normalize(other)
        return Frac((self.x*other.y + other.x*self.y),self.y*other.y)

        #konstruktor realizuje  wlasciwosci czyszczoce sprawdzajace
        #rsub other.normalise()

    __radd__ = __add__              # int+frac


    def __sub__(self, other):  # frac1 - frac2
        other=self.normalize(other)
        return Frac((self.x*other.y - other.x*self.y),self.y*other.y)


    def __rsub__(self, other):
        other=self.normalize(other)
        return Frac((other.x*self.y - self.x*other.y),self.y*other.y)

    def __mul__(self, other):   # frac1 * frac2
        other=self.normalize(other)
        return Frac(self.x*other.x,self.y*other.y)

    __rmul__ = __mul__ 

    def __div__(self, other): pass  # frac1 / frac2, Py2

    def __truediv__(self, other):   # frac1 / frac2, Py3
        other=self.normalize(other)
        return Frac(self.x*other.y,self.y*other.x)

    def __rtruediv__(self, other):
        other=self.normalize(other)
        return Frac(other.x*self.y,other.y*self.x)

    def __floordiv__(self, other):   # frac1 // frac2, opcjonalnie
    #a/b // c/d = a*d//c*b
        other=self.normalize(other)
        return Frac(self.x*other.y // other.x*self.y)

    def __rfloordiv__(self, other):
        other=self.normalize(other)
        return Frac(other.x*self.y // self.x*other.y)

    def __mod__(self, other):   # frac1 % frac2, opcjonalnie
    #(a//b) *b + (a%b) = a
    # a%b = a - (a//b) * b
        other=self.normalize(other)
        return self - ((self//other) * other)

    def __rmod__(self, other):
        other=self.normalize(other)
        return other - ((other//self) * self)
    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):        # float(frac)
        return float(self)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase): 
    def setUp(self):
        self.u1 = Frac(4,7)
        self.u2 = Frac(5,9)

    def testPrint(self):
        self.assertEqual(str(self.u1),"4/7")
        self.assertEqual(repr(self.u2),"Frac(5, 9)")
    def test_cmp(self):
        self.assertTrue((Frac(5,7)==Frac(15,21)))
        self.assertFalse((Frac(5,7)==Frac(16,21)))
        self.assertTrue((Frac(5,2)==2.5))
        self.assertTrue((3.5==Frac(7,2)))
        self.assertTrue((Frac(5,7)!=Frac(16,21)))
        self.assertFalse((Frac(5,7)!=Frac(15,21)))
        self.assertFalse((3.5!=Frac(7,2))) #
        self.assertFalse((Frac(5,4)!=1.25)) 
        self.assertTrue(Frac(4,7)<Frac(6,9))
        self.assertFalse(Frac(4,7)<Frac(5,9))
        self.assertTrue(0.3<Frac(6,9))
        self.assertTrue(Frac(4,7)<1.25)
        self.assertFalse(1.0<Frac(6,9))
        self.assertTrue(1.0>Frac(6,9))
        self.assertFalse(0.0>Frac(6,9))
        self.assertTrue(Frac(6,9)>0.5)
        self.assertFalse(1.0>Frac(12,7))
        self.assertTrue(Frac(4,7)<=Frac(6,9))
        self.assertFalse(Frac(4,7)<=Frac(5,9))
        self.assertTrue(Frac(6,9)<=Frac(18,27))
        self.assertTrue(Frac(6,9)>=Frac(18,27))
        self.assertTrue(2>=Frac(18,27))
        self.assertTrue(Frac(6,9)>=0.5)
        self.assertFalse(0.25>=Frac(18,27))
        self.assertFalse(Frac(18,27)>=2.25)
        

    def test_add(self):
        self.assertEqual(Frac(4,7)+Frac(1,4),Frac(23,28))
        self.assertEqual(Frac(2,4)+Frac(1,4),Frac(3,4)) 
        self.assertEqual(Frac(2,4)+1,1.5)
        self.assertEqual(1.5+Frac(2,4),2)
    def test_sub(self):
        self.assertEqual(Frac(4,7)-Frac(1,4),Frac(9,28))
        self.assertEqual(Frac(3,4)-Frac(1,4),Frac(1,2))
        self.assertEqual(Frac(3,4)-Frac(1,4),Frac(2,4))

        self.assertEqual(Frac(4,7)-1,Frac(-3,7))
        self.assertEqual(5-Frac(2,4),4.5)
        

    def test_mul(self):
        self.assertEqual(Frac(5,9)*Frac(2,3),Frac(10,27))
        self.assertEqual(Frac(4,8)*Frac(1,2),Frac(2,8))

        self.assertEqual(Frac(4,8)*2,1)
        self.assertEqual(0.25*Frac(1,2),Frac(1,8))

    def test_truediv(self):
        self.assertEqual(Frac(3,4)/Frac(2/3),Frac(9,8))
        self.assertEqual(Frac(4)/Frac(2),Frac(2))

        self.assertEqual(Frac(4)/3,Frac(4,3))
        self.assertEqual(8/Frac(3/2),Frac(16,3))

    def test_floordiv(self):
        self.assertEqual(Frac(1,2)//2,0)
        self.assertEqual(5//Frac(2,1),2)

    def test_mod(self):
        self.assertEqual(Frac(1,2)%2,0.5)
        self.assertEqual(5%Frac(4,2),1)

    def test_pos(self):
        self.assertEqual(+Frac(2,4),Frac(2,4))
    def test_neg(self):
        self.assertEqual(-Frac(2,4),Frac(-2,4))
    def test_invert(self):
        self.assertEqual(~Frac(1,4),Frac(4))
        print(3.5%Frac(3,7), " -wynik: 3.5%2/3")
        print(Frac(3,7)//Frac(3,19), " -wynik 3/7 floor 3/19")
        print(-1%8, " wazne")

    
if __name__ == "__main__":
    unittest.main()     # wszystkie testy

