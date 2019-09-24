# Unit converter

print("Hey! Herzlich willkommen zum Einheiten-Umrechner. Ein Programm, das Kilometer in Meilen umrechnet.")

print("Bitte gib als erstes eine Kilometerangabe ein.")

Kilometer = int(input("Meine Kilometerangabe: "))

conversion_factor = 0.62137119

print("Das sind deine Meilen: ")

print (Kilometer * conversion_factor)

print("Möchtest du noch weitere Kilometerangeben umrechnen?")

secret1 = "Ja"

secret2 = "Nein"

while True:
    Antwort = input("Deine Anwort: ")
    if Antwort == secret2:
        print("Schade. Bis zum nächsten Mal.")
        break
    elif Antwort == secret1:
        print("Alles klar. Du kannst jetzt weitere Kilometerangaben umrechnen.")
        Kilometer = int(input("Meine Kilometerangabe: "))
        conversion_factor = 0.62137119
        print("Das sind deine Meilen: ")
        print(Kilometer * conversion_factor)
        break




