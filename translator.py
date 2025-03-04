from dictionary import Dictionary

class Translator:
    def __init__(self):
        self.elenco_coppie = {}
        self.dizionario = Dictionary()  # Usa la classe Dictionary

    def printMenu(self):
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        try:
            with open(dict, "r",encoding="utf-8") as file:
                for line in file:
                    if not line or line.startswith("#"):
                        continue
                    coppia = line.strip().split()
                    if len(coppia) > 2:
                        #gestisci multiple def
                        aliena = coppia[0]
                        italiane = coppia[1:]
                        self.elenco_coppie[aliena] = italiane
                    aliena = coppia[0]
                    italiana = coppia[1]
                    self.elenco_coppie[aliena] = italiana
        except FileNotFoundError:
            print(f"Errore: File '{dict}' non trovato")
        except Exception as e:
            print(f"Errore inatteso: {str(e)}")

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        aliena = entry[0].lower()
        italiane = entry[1]
        if aliena not in self.elenco_coppie:
            print("La parola non era memorizzata ed è stata memorizzata con le sue traduzioni")
            self.elenco_coppie[aliena] = italiane
            self.dizionario.addWord(aliena, " ".join(italiane))
        else:
            if self.elenco_coppie[aliena] != italiane:
                print("La parola aliena era gia salvata ma procedo ad aggiornare le traduzioni da lei aggiunte")
                print(f"traduzioni precedenti della parola {aliena}: {self.elenco_coppie[aliena]}")
                for italiana in italiane:
                    if  italiana not in self.elenco_coppie[aliena]:
                        self.elenco_coppie[aliena].append(italiana)
                        self.dizionario.addWordTrad(aliena, italiana)

                print(f"traduzioni aggiornate per la parola{aliena}: {self.elenco_coppie[aliena]}")

            if self.elenco_coppie[aliena] == italiane:
                print("La parola era gia salvata con queste traduzioni")
        self.dizionario.save()

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.lower()
        if query in self.elenco_coppie:
            print(print(f"Traduzioni di '{query}': {', '.join(self.elenco_coppie[query])}"))
        else:
            print("parola aliena non trovata")
    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        query = query.lower()
        if "?" not in query:
            print("Formato wildcard non valido. Usa '?' come carattere jolly.")
            return

        parti = query.split("?")
        if len(parti) != 2:
            print("Formato wildcard non valido. Usa un solo '?'.")
            return

        risultato = []
        for aliena in self.elenco_coppie:
            if aliena.startswith(parti[0]) and aliena.endswith(parti[1]):
                risultato.append([aliena, self.elenco_coppie[aliena]])
        if risultato:
            print("Parole trovate:")
            for parola, traduzioni in risultato:
                print(f"{parola}: {', '.join(traduzioni)}")
        else:
            print("Nessuna parola trovata con il pattern specificato.")
