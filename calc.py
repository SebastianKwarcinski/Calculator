
class calc:

    def dodaj(x,y):
        return x+y
    def odejmij(x,y):
        return x-y
    def mnozenie(x,y):
        return x*y
    def dziel(x,y):
        return x/y
c=calc

l1 = int(input())
l2 = int(input())
print("Dodawanie: ",c.dodaj(l1,l2))
print("Odejmowanie: ",c.odejmij(l1,l2))
print("Mnożenie: ",c.mnozenie(l1,l2))
print("Dzielenie: ",c.dziel(l1,l2))
