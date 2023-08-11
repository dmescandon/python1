#imprimir letra a letra
lista ="gato"
for letra in lista:
    print (letra)



#imprimir nombre completo con espacios
lista_nombre = "Diana Marcela Escandon Barbosa"
print(lista_nombre)
for letra_nombre in lista_nombre:
    print(letra_nombre)


    #pedirle al usuario que escriba una frase e imprimir el numero de palabras que ingreso el usuario 
    #input
    #contador de palabras (split: cadena de texto las divide en espacios)
    frase_inicial= "split se encarga de dividir texto por espacios"
    palabra_div= frase_inicial.split()
    print(palabra_div)

    Frase= input("escriba una frase:")
    print(Frase)
    palabra_divfrase=Frase.split()
    print(palabra_divfrase)
