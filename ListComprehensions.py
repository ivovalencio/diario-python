#lista = [1,2,3,4,5]

#try:
 #   quadrados=[item**2 for item in lista if True]
#except Exception as e:
 #   print(e)
#else:
 #   print(quadrados)

#lista = [2,4,6,8]

#cubos = [item**3 for item in lista ]
#print(f"O resultado de cada item da lista elevado ao cubo é {cubos}")


#lista = [3,6,9,12]
#vezes3=[item*3 for item in lista]
#print(f" O Triplo de cada número da lista é:{vezes3}")


#cubo=[]
#print(f"Uma lista de todos os números ao cubo é {cubo}")
#for numero in lista:
 #   cubo.append(numero**3)
  #  print(cubo)

lista = [1,2,3,4,5,6,7,8,9,10]
cubo=[numero**3 for numero in lista]
print(f" O Triplo de cada número da lista é:{cubo}")

pares=[numero for numero in lista if numero%2==0]
print(f"Os números pares são: {pares}")
impares=[numero for numero in lista if numero%2!=0]
print(f"Os números ímpares são: {impares}")

