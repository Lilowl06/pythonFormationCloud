# focntion : unité de code contenant une ou plusieurs instructions pouvant être appelée autant de fois que souhaité.
# utilsation pour des traitements répétitif
# micro-organisme d'entrée-sortie

def separator(charactere, times):
    row = ""
    for n in range(times) :
        row += charactere
    print(row)
# ca ne renvoie rien et normal car la fooction est défini mais pas utilisée !

'''
for n in range(5):
    separator()
'''

'''
separator("*",30)
separator("-",40)
separator("_",50)
'''

def hello() :
    #print("Hello !")
    return "Ciao tutti"

result = hello()
print(result)

def square(n):
    return n*n

# print(square(5))

numbers = [6,4,40,10,8,15]
for n in numbers :
    if n <= 10 :
        print(square(n))
