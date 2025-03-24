def tulosta_lista():
    lista = ["Apple", "Samsung", "LG", "Sony", "Huawei", "Nokia", "OnePlus", "Motorola"]
    for i in lista:
        print(i)

def ykkonen():
    print("Ykkönen")

def kakkonen():
    print("Kakkonen")

def kolmonen():
    print("Kolmonen")
def ope_vili(arvo):
    for i in range(arvo):
        print("Vili on paras opettaja!")
tulosta_lista()
ykkonen()
kakkonen()
kolmonen()
kakkonen()
ykkonen()
arvo =int(input("> Kuinka hyvä opettaja Vili on (1 - 10)? "))
ope_vili(arvo)