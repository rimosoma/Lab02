import translator as tr
t = tr.Translator()
t.loadDictionary("dictionary.txt")
while True:
    t.printMenu()
    txtIn = input("Scelta: ").strip()

    if not txtIn.isdigit() or int(txtIn) not in [1, 2, 3, 4]:
        print("Input non valido. Inserisci un numero tra 1 e 4.")
        continue

    scelta = int(txtIn)
    # Add input control here!

    if scelta == 1:
        print("inserire parola e traduzione separate da spazio: ")
        txtIn = input().lower().strip()
        parole = txtIn.split()
        if len(parole) < 2:
            print("Input non valido. Inserisci almeno una parola aliena e una traduzione.")
            continue
        aliena = parole[0]
        italiane = parole[1:]
        t.handleAdd([aliena, italiane])

    if scelta == 2:
        print("inserire parola aliena per ottenere la traduzione: ")
        txtIn = input().lower().strip()
        t.handleTranslate(txtIn)
    if scelta == 3:
        print("inserire parola aliena per ottenere le compatibili traduzioni: ")
        txtIn = input().lower().strip()
        t.handleWildCard(txtIn)
    if scelta == 4:
        print("uscita dal programma")
        break