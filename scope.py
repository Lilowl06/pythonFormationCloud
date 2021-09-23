message = "J'aime Python" # variable de portée (scope) globale

def f1() :
    privateMessage = "Message secret" # variable locale
    print(message)

def f2() :
    print(message)
    # print(privateMessage) # c'est impossible car on ne peut pas accèder à une variable locale en dehors de son corps de fonction.

f1()
f2()