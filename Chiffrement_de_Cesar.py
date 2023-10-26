def chiffrement():
    textClair = input("Entrer votre text : ")
    decalage = int(input("Entrer la Décalage : "))
    textChiffrer = ""

    for lettre in textClair:
        if lettre.isalpha():
            if lettre.isupper():
                lettre = chr(((ord(lettre) - 65 - decalage) % 26) + 65)
            else:
                lettre = chr(((ord(lettre) - 97 - decalage) % 26) + 97)

        textChiffrer += lettre

    return textChiffrer


# def déchiffrement():


print("Chiffrement de César")

print(chiffrement())
