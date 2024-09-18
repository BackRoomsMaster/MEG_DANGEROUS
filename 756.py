import random
import time
import sys

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class Level756:
    def __init__(self):
        self.islands = ["Isola Centrale", "Isola Orientale", "Isola Settentrionale", "Isola Occidentale", 
                        "Isola Meridionale", "Isola Nord-Est", "Isola Nord-Ovest", "Isola Sud-Est"]
        self.current_island = "Isola Centrale"
        self.piano_melody = "Una melodia di pianoforte distorta e ripetitiva risuona nell'aria."
        self.fog = "Una fitta nebbia avvolge il vuoto sotto le isole fluttuanti."
        self.cow_annoyance = 0
        self.exit_clues = 0
        self.bridges_crossed = 0
        self.escape_attempts = 0
        self.first_description = True

    def describe_environment(self):
        if self.first_description:
            print_slow("\nLivello 756 - Le Isole Fluttuanti")
            self.first_description = False
        print_slow(f"\nTi trovi sull'{self.current_island}")
        print_slow(self.fog)
        print_slow(self.piano_melody)
        print_slow("Sparse querce punteggiano le pianure erbose dell'isola.")
        self.cow_appears()

    def cow_appears(self):
        cow_actions = [
            "La mucca ti fissa intensamente, quasi leggendoti nel pensiero.",
            "La mucca ti segue, cercando di attirare la tua attenzione.",
            "La mucca si mette tra te e il ponte, bloccando il passaggio.",
            "La mucca inizia a fare una danza assurda intorno a te.",
            "La mucca tira fuori un cartello con scritto 'Ehi tu! Sì, proprio tu!'",
            "La mucca indossa improvvisamente un paio di occhiali da sole.",
            "La mucca inizia a mimare le tue azioni in modo esagerato.",
            "La mucca tira fuori una radio e inizia a suonare una canzone dance.",
            "La mucca si traveste da detective e finge di investigare su di te.",
            "La mucca fa apparire un cappello da mago e inizia a fare trucchi.",
            "La mucca tira fuori una lavagna e inizia a spiegare la teoria delle stringhe.",
            "La mucca indossa un costume da supereroe e finge di volare.",
            "La mucca inizia a jonglare con delle mele che appaiono dal nulla.",
            "La mucca tira fuori un megafono e inizia a commentare ogni tua mossa.",
            "La mucca si mette a fare yoga, invitandoti a unirti a lei.",
            "La mucca tira fuori una macchina fotografica e inizia a farti un servizio fotografico.",
            "La mucca indossa un basco e inizia a dipingere un ritratto astratto di te.",
            "La mucca tira fuori un libro e inizia a leggere 'Il Manuale di Sopravvivenza alle Backrooms'.",
            "La mucca inizia a fare una dimostrazione di come si munge... se stessa.",
            "La mucca tira fuori un telescopio e finge di osservare galassie lontane.",
            "La mucca indossa un cappello da chef e inizia a preparare un 'risotto al latte' immaginario.",
            "La mucca tira fuori una chitarra e inizia a suonare 'La Mucca Nel Labirinto Blues'.",
            "La mucca si mette a fare moonwalk, scivolando sull'erba come se fosse ghiaccio.",
            "La mucca tira fuori un mappamondo e inizia a pianificare la sua prossima vacanza.",
            "La mucca indossa un costume da mimo e inizia a mimare di essere intrappolata in una scatola."
        ]
        print_slow("\n" + cow_actions[min(self.cow_annoyance, len(cow_actions) - 1)])
        self.cow_annoyance += 1

    def move_to_island(self):
        if random.random() < 0.3:  # 30% di possibilità che il ponte sia instabile
            print_slow("\nIl ponte oscilla pericolosamente! Devi tornare indietro.")
            self.cow_mocks_failure()
            return
        destination = random.choice([island for island in self.islands if island != self.current_island])
        print_slow(f"\nAttraversi un ponte di corda oscillante verso {destination}.")
        self.current_island = destination
        self.bridges_crossed += 1
        if self.bridges_crossed % 3 == 0:
            self.find_clue()

    def find_clue(self):
        clues = [
            "Noti un simbolo strano inciso su una quercia.",
            "Trovi un pezzo di carta con degli appunti criptici.",
            "Una pietra luminosa attira la tua attenzione.",
            "Senti un sussurro nel vento che sembra indicare una direzione.",
            "Vedi un arcobaleno che punta verso una direzione specifica.",
            "Trovi una bussola che punta sempre verso la mucca, non verso il nord.",
            "Noti che le nuvole formano una freccia nel cielo.",
            "Un fiore raro cresce solo in un punto preciso dell'isola."
        ]
        print_slow("\n" + random.choice(clues))
        self.exit_clues += 1

    def contemplate(self):
        thoughts = [
            "Ti chiedi se la mucca sia la chiave per uscire da questo livello.",
            "La melodia del pianoforte sembra cambiare leggermente... o è solo la tua immaginazione?",
            "Osservi le isole e noti che formano un pattern... ma quale?",
            "Ti domandi se ci sia un significato nascosto in questo luogo surreale.",
            "Pensi che forse dovresti abbracciare l'assurdità di questa situazione.",
            "Ti chiedi se la mucca sia reale o solo una proiezione della tua mente.",
            "Rifletti sul concetto di realtà in un mondo di isole fluttuanti e mucche parlanti.",
            "Mediti sulla possibilità che tutto questo sia solo un elaborato sogno."
        ]
        print_slow("\n" + random.choice(thoughts))

    def interact_with_cow(self):
        cow_interactions = [
            "La mucca ti offre un secchio di latte. Da dove l'ha preso?",
            "La mucca tira fuori una mappa, ma è solo un disegno di altre mucche.",
            "La mucca inizia a recitare Shakespeare. In latino.",
            "La mucca ti sfida a una gara di fissaggio. Vince lei.",
            "La mucca fa apparire un ombrello e inizia a cantare 'Singin' in the Rain'.",
            "La mucca tira fuori un tablet e ti mostra un PowerPoint sulla storia delle Backrooms.",
            "La mucca indossa un cappello da laureato e inizia una lezione sulla fisica quantistica.",
            "La mucca fa apparire un tavolo da poker e ti invita a giocare... con le carte del Tarocchi.",
            "La mucca tira fuori un microfono e inizia uno stand-up comedy sulle difficoltà di essere una mucca nelle Backrooms.",
            "La mucca indossa un costume da astronauta e simula una passeggiata spaziale.",
            "La mucca fa apparire un pianoforte e suona una versione jazz della melodia di sottofondo.",
            "La mucca tira fuori una macchina del tempo in miniatura e ti mostra 'il futuro' (è pieno di mucche).",
            "La mucca indossa un grembiule e inizia a dipingere il paesaggio... aggiungendo più mucche ovunque.",
            "La mucca fa apparire un palcoscenico e mette in scena un one-cow-show intitolato 'Muggiti e Follia'.",
            "La mucca tira fuori un proiettore e inizia una presentazione su 'Come Uscire dal Livello 756 in 100 Semplici Passi' (tutti i passi coinvolgono mucche)."
        ]
        print_slow("\n" + random.choice(cow_interactions))
        if random.random() < 0.2:  # 20% di possibilità di trovare un indizio
            self.find_clue()

    def cow_mocks_failure(self):
        mockeries = [
            "La mucca ride e dice: 'Hai provato a girare la maniglia?'",
            "La mucca sospira: 'Un altro che pensa di poter uscire così facilmente...'",
            "La mucca applaude sarcasticamente: 'Bravo, ci sei quasi! ...No, non è vero.'",
            "La mucca tira fuori un trofeo con scritto 'Miglior Tentativo Fallito dell'Anno'.",
            "La mucca fa il gesto del pollice verso e muggisce delusa.",
            "La mucca tira fuori un cartello con scritto 'Uscita' e una freccia che punta verso il basso nel vuoto.",
            "La mucca indossa un cappello da giudice e dichiara: 'La corte sentenzia: tentativo respinto!'",
            "La mucca fa apparire un tabellone segnapunti: 'Mucca: 1000, Umano: 0'",
            "La mucca tira fuori un megafono: 'Attenzione, abbiamo un altro caso di fuga fallita!'",
            "La mucca indossa occhiali da sole e dice: 'Wow, non ho mai visto nessuno fallire con tanto stile!'",
            "La mucca fa apparire una porta finta, la apre, e dietro c'è solo un muro con scritto 'Ci hai creduto?'",
            "La mucca tira fuori un blocco note: 'Devo aggiungere questo alla mia collezione di Epic Fail'",
            "La mucca indossa un berretto da allenatore: 'Forse dovresti allenarti di più nelle fughe!'",
            f"La mucca fa apparire un'insegna luminosa: 'Uscita Fallita n. {self.escape_attempts}'",
            "La mucca tira fuori una medaglia: 'Premio per la Persistenza nel Fallimento'",
            "La mucca indossa un camice da dottore: 'Mi spiace, la sua fuga non ce l'ha fatta'",
            "La mucca fa apparire un grande libro: 'Lasciatemi aggiungere questo alla Storia dei Tentativi Falliti'",
            "La mucca tira fuori una macchina del tempo giocattolo: 'Vuoi tornare indietro e riprovarci?'",
            "La mucca indossa un costume da mago: 'Per il mio prossimo trucco, farò scomparire le tue speranze di fuga!'",
            "La mucca fa apparire un microfono da karaoke e canta: 'Un altro fallimento, un altro giorno in paradiso!'"
        ]
        print_slow("\n" + random.choice(mockeries))
        self.escape_attempts += 1

    def try_exit(self):
        if self.exit_clues >= 5 and self.cow_annoyance >= 7:
            print_slow("\nLa mucca sospira, poi sorride. 'Hai capito il gioco,' dice.")
            print_slow("Un portale si apre sotto i tuoi piedi. Stai uscendo dal Livello 756!")
            return True
        else:
            print_slow("\nSenti che ti manca ancora qualcosa per uscire...")
            self.cow_mocks_failure()
            return False

    def explore(self):
        while True:
            self.describe_environment()
            action = input("\nCosa vuoi fare? (muovi/contempla/mucca/esci): ").lower()
            if action == "muovi":
                self.move_to_island()
            elif action == "contempla":
                self.contemplate()
            elif action == "mucca":
                self.interact_with_cow()
            elif action == "esci":
                if self.try_exit():
                    break
            else:
                print_slow("Azione non valida. La mucca alza un sopracciglio giudicante.")

if __name__ == "__main__":
    print_slow("Benvenuto nel Livello 756 delle Backrooms - Le Isole Fluttuanti")
    print_slow("Trova la via d'uscita... se ci riesci!")
    level = Level756()
    level.explore()
