'''
print("Hello world!")
print(2+3)
a = 2
b = 3
print(a+b)
# print(a+"+"+b+"="+a+b)
print("Hello"+" "+"World!")
print(a,"+",b,"=",a+b)
print(a,"+",b,"=",a+b,sep="")
print(a,"+",b,"=",a+b,sep=" valami ")
s = "pipacs"
print(a,"+",b,"=",a+b,sep=s)

# nev = input()

# print("Kérem a neved:")
# print("Kérem a neved: ",end="")
# nev = input()

nev = input("Kérem a neved: ")

print("Szia "+nev+"!")
kor = input("Kérem az életkorod: ")
# print(65-kor)
print(type(kor))
egesz = 12
tizedes = 3.5
print(type(egesz))
print(type(tizedes))
# egesz = True      !!!!!!!!! NE
# print(type(egesz))

egesz = egesz / tizedes     # !!!!!!!!! NE
print(type(egesz))

logikaiIgaz = True
logikaiHamis = False

valami = 1,2,3
print(valami)

print(kor*2)
print(int(kor)*2)

egesz = int( input("Kérek egy egész számot: "))
tizedes = float( input("Kérek egy tizedes törtet: "))

valami = 1,2,4
print(type(valami))

tupleM = (1,2,4,1)
print(type(tupleM))

lista = [1,2,4,1]
print(type(lista))

halmaz = {1,2,4,1}
print(type(halmaz))


print(valami)
valami.clear()
print(valami)

print(tupleM, lista, halmaz,sep="\n")

lista.sort()
print(lista)

for elem in lista:
    print(elem,end=", ")
    elem = elem + 1
    elem += 1
    print(elem)
print(elem)
'''
for i in range(10):
    print(i,end=", ")
print()

for i in range(10,20,2):
    print(i,end=", ")
