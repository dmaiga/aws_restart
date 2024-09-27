# print("python has three numeric types: int,float;and complex ")
# myValue=1
# print(myValue)
# print(type(myValue))
# print( str(myValue) + " is of the data type" + str(type(myValue) ))
# myValue= 3.14
# print(myValue)
# print(type(myValue) )
# print( str(myValue) + " is of the data type" + str(type(myValue) ))
# myValue=5j
# print(myValue)
# print(type(myValue) )
# print( str(myValue) + " is of the data type" + str(type(myValue) ))
# myValue=True
# print(myValue)
# print(type(myValue) )
# print( str(myValue) + " is of the data type" + str(type(myValue) ))
# myValue=False
# print(myValue)
# print(type(myValue) )
# print( str(myValue) + " is of the data type" + str(type(myValue) ))

#           Exercice 1 Présentation du type de données string

myString="This is my string"
print(myString)
print(type(myString))
print( str(myString) + " is of the data type" + str(type(myString)) )

#           Utiliser la concaténation des chaînes

firstString="Water"
secondString="fall"
thridString= firstString + secondString
print(thridString)

#            Utiliser des chaînes d'entrée

name=input("What's your name? ")
print(name)

#           exo4 Formater des chaînes de sortie

color=input("What's your favorite color ? ")
animal= input("What's your favorite animal ? ")
    
print("{}, you like a {} S {}" .format(name,color,animal))
