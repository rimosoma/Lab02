class Dictionary:
    def __init__(self, filename="dictionary.txt"):
        self.filename = filename
        self.righe = []
        try:
            # Apri il file in modalità lettura
            with open(self.filename, "r", encoding="utf-8") as file:
                self.righe = file.readlines()  # Leggi tutte le righe
        except FileNotFoundError:
            print(f"Errore: File '{self.filename}' non trovato. Verrà creato un nuovo file.")
            # Se il file non esiste, crea una lista vuota
            self.righe = []
        except Exception as e:
            print(f"Errore inatteso: {str(e)}")
    def addWordTrad(self, aliena, italiana):
        """
        Aggiunge una traduzione (italiana) a una parola aliena esistente.
        Se la parola aliena non esiste, non fa nulla.
        """
        for i, riga in enumerate(self.righe):
            tupla = riga.strip().split()  # Rimuove spazi e newline, poi divide
            if tupla and tupla[0] == aliena:  # Controlla se la prima parola è "aliena"
                self.righe[i] = riga.strip() + " " + italiana + "\n"  # Aggiunge la traduzione
                break
    def addWord(self, aliena, italiane):
        """
        Aggiunge una nuova parola aliena con la sua traduzione italiana.
        Se la parola aliena esiste già, non fa nulla.
        """
        # Verifica se la parola aliena esiste già
        for riga in self.righe:
            tupla = riga.strip().split()
            if tupla and tupla[0] == aliena:
                print(f"La parola '{aliena}' esiste già.")
                return
        # Aggiunge la nuova parola e traduzione
        self.righe.append(f"{aliena} {italiane}\n")
    def save(self):
        """
        Salva le modifiche nel file.
        """
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.writelines(self.righe)  # Scrivi tutte le righe nel file
            print(f"File '{self.filename}' salvato con successo.")
        except Exception as e:
            print(f"Errore durante il salvataggio del file: {str(e)}")





def translate(self):
    pass

def translateWordWildCard(self):
    pass