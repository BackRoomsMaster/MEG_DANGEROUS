import random
import time

def loading_animation(duration=1, message="Caricamento"):
    for _ in range(3):
        for char in ["|", "/", "-", "\\"]:
            print(f"\r{message} {char}", end="", flush=True)
            time.sleep(duration / 12)
    print("\r" + " " * (len(message) + 2), end="", flush=True)
    print("\r", end="", flush=True)

class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = self.generate_description()
        self.exits = {}
        self.items = []
        self.visited = False
        self.unstable = random.random() < 0.1
        self.hiding_spots = random.randint(0, 2)

    def generate_description(self):
        descriptions = [
            "Un corridoio sporco e maleodorante con piastrelle rotte e cavi pendenti.",
            "Una stanza angusta con pareti coperte di sostanze viscide e nauseabonde.",
            "Un passaggio stretto che svolta bruscamente, illuminato da luci tremolanti.",
            "Un'area che ricorda un ospedale abbandonato, con attrezzature mediche arrugginite.",
            "Un tunnel che sembra un condotto fognario, con tubi sporgenti dalle pareti.",
            "Una sezione buia del labirinto, dove l'oscurità è quasi palpabile."
        ]
        return random.choice(descriptions)

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = []
        self.health = 100
        self.is_hidden = False
        self.moves = 0
        self.items_collected = 0
        self.escapes = 0

class Sentinel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.last_known_player_pos = None

    def move_towards(self, player, rooms):
        if self.last_known_player_pos:
            target_x, target_y = self.last_known_player_pos
        else:
            target_x, target_y = player.x, player.y

        dx = target_x - self.x
        dy = target_y - self.y

        if abs(dx) > abs(dy):
            direction = "est" if dx > 0 else "ovest"
        else:
            direction = "nord" if dy > 0 else "sud"

        new_x, new_y = self.x, self.y
        if direction == "nord" and (self.x, self.y + 1) in rooms:
            new_y += 1
        elif direction == "sud" and (self.x, self.y - 1) in rooms:
            new_y -= 1
        elif direction == "est" and (self.x + 1, self.y) in rooms:
            new_x += 1
        elif direction == "ovest" and (self.x - 1, self.y) in rooms:
            new_x -= 1

        if (new_x, new_y) in rooms:
            self.x, self.y = new_x, new_y

        if self.x == target_x and self.y == target_y:
            self.last_known_player_pos = None

def create_rooms(size=7):
    rooms = {}
    for _ in range(size * size):
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        if (x, y) not in rooms:
            rooms[(x, y)] = Room(x, y)

    for (x, y), room in rooms.items():
        for dx, dy, direction in [(0, 1, "nord"), (0, -1, "sud"), (1, 0, "est"), (-1, 0, "ovest")]:
            if (x + dx, y + dy) in rooms:
                room.add_exit(direction, rooms[(x + dx, y + dy)])

    items = ["torcia", "benda", "acqua", "mappa sbiadita", "cristallo di Firesalt", "adrenalina", "coltello arrugginito"]
    for item in items:
        random_room = random.choice(list(rooms.values()))
        random_room.add_item(item)

    return rooms

def print_map(rooms, player, sentinel):
    loading_animation(message="Generazione mappa")
    min_x = min(room.x for room in rooms.values())
    max_x = max(room.x for room in rooms.values())
    min_y = min(room.y for room in rooms.values())
    max_y = max(room.y for room in rooms.values())

    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if (x, y) in rooms:
                if x == player.x and y == player.y:
                    print("P", end=" ")
                elif x == sentinel.x and y == sentinel.y:
                    print("S", end=" ")
                elif rooms[(x, y)].visited:
                    print("X", end=" ")
                else:
                    print("?", end=" ")
            else:
                print(" ", end=" ")
        print()

def attempt_escape(player, sentinel, rooms):
    print("La Sentinella ti ha raggiunto! Devi fuggire!")
    loading_animation(message="Tentativo di fuga")
    escape_chance = random.random()
    
    if "adrenalina" in player.inventory:
        print("Usi l'adrenalina per aumentare le tue possibilità di fuga!")
        escape_chance += 0.2
        player.inventory.remove("adrenalina")

    if escape_chance > 0.7:
        print("Sei riuscito a sfuggire alla Sentinella!")
        available_rooms = list(rooms[(player.x, player.y)].exits.values())
        if available_rooms:
            new_room = random.choice(available_rooms)
            player.x, player.y = new_room.x, new_room.y
            print("Ti sei spostato in una nuova stanza.")
        player.escapes += 1
        return True
    else:
        print("Non sei riuscito a fuggire. La Sentinella ti ha colpito!")
        player.health -= 50
        if player.health <= 0:
            return False
        print(f"Hai subito danni gravi. Salute rimanente: {player.health}")
        return True

def game_over_screen(player, turns):
    print("\n" + "=" * 40)
    print("GAME OVER")
    print("=" * 40)
    print(f"Hai resistito per {turns} turni nel Livello 611.")
    print(f"Movimenti effettuati: {player.moves}")
    print(f"Oggetti raccolti: {player.items_collected}")
    print(f"Fughe riuscite dalla Sentinella: {player.escapes}")
    print("=" * 40)

def main():
    rooms = create_rooms()
    start_room = random.choice(list(rooms.values()))
    player = Player(start_room.x, start_room.y)
    sentinel = Sentinel(start_room.x, start_room.y)

    while (sentinel.x, sentinel.y) == (player.x, player.y):
        sentinel_room = random.choice(list(rooms.values()))
        sentinel.x, sentinel.y = sentinel_room.x, sentinel_room.y

    print("Benvenuto nel Livello 611 delle Backrooms: Il Labirinto!")
    print("Ti trovi in un intricato labirinto di corridoi sporchi e pericolosi.")
    print("La Sentinella, un essere mostruoso e letale, ti sta dando la caccia.")
    print("Trova un'uscita prima che sia troppo tardi.")
    print("Puoi muoverti usando i comandi: nord, sud, est, ovest")
    print("Altri comandi: guarda, prendi, inventario, mappa, nascondi, usa, esci")

    turns = 0
    while True:
        turns += 1
        current_room = rooms[(player.x, player.y)]
        current_room.visited = True

        print("\n" + current_room.description)
        
        if (player.x, player.y) == (sentinel.x, sentinel.y) and not player.is_hidden:
            if not attempt_escape(player, sentinel, rooms):
                print("La Sentinella ti ha ucciso.")
                game_over_screen(player, turns)
                break

        if current_room.unstable:
            print("Questa zona sembra instabile. Potresti provare a noclippare per uscire.")

        if current_room.hiding_spots > 0:
            print(f"Ci sono {current_room.hiding_spots} nascondigli in questa stanza.")

        command = input("> ").lower()

        if command == "esci":
            print("Hai deciso di arrenderti al Labirinto. Grazie per aver giocato!")
            game_over_screen(player, turns)
            break
        elif command in ["nord", "sud", "est", "ovest"]:
            if player.is_hidden:
                print("Devi uscire dal nascondiglio prima di muoverti.")
            elif command in current_room.exits:
                loading_animation(message="Spostamento")
                new_room = current_room.exits[command]
                player.x, player.y = new_room.x, new_room.y
                print("Ti muovi verso", command, "attraverso il corridoio insidioso.")
                player.is_hidden = False
                player.moves += 1
            else:
                print("Non puoi andare in quella direzione. Il passaggio è bloccato.")
        elif command == "guarda":
            loading_animation(message="Osservando")
            if current_room.items:
                print(f"Tra i detriti e lo sporco, vedi: {', '.join(current_room.items)}")
            else:
                print("Non vedi nulla di utile, solo sporcizia e detriti.")
        elif command == "prendi":
            if current_room.items:
                loading_animation(message="Raccogliendo")
                item = current_room.items.pop()
                player.inventory.append(item)
                print(f"Hai raccolto: {item}")
                player.items_collected += 1
            else:
                print("Non c'è nulla di utile da prendere qui.")
        elif command == "inventario":
            loading_animation(message="Controllo inventario")
            if player.inventory:
                print(f"Nel tuo zaino hai: {', '.join(player.inventory)}")
            else:
                print("Il tuo zaino è vuoto.")
        elif command == "mappa":
            print_map(rooms, player, sentinel)
        elif command == "nascondi":
            if current_room.hiding_spots > 0 and not player.is_hidden:
                loading_animation(message="Nascondendosi")
                player.is_hidden = True
                print("Ti sei nascosto. La Sentinella non può vederti.")
            elif player.is_hidden:
                loading_animation(message="Uscendo dal nascondiglio")
                player.is_hidden = False
                print("Sei uscito dal nascondiglio.")
            else:
                print("Non ci sono nascondigli in questa stanza.")
        elif command.startswith("usa "):
            item = command[4:]
            if item in player.inventory:
                loading_animation(message=f"Usando {item}")
                if item == "torcia":
                    print("Hai acceso la torcia. Ora puoi vedere meglio.")
                elif item == "benda":
                    player.health = min(100, player.health + 20)
                    print(f"Hai usato la benda. Salute: {player.health}")
                    player.inventory.remove("benda")
                elif item == "acqua":
                    print("Hai bevuto l'acqua. Ti senti un po' meglio.")
                    player.inventory.remove("acqua")
                elif item == "cristallo di Firesalt":
                    print("Hai usato il cristallo di Firesalt. Un'esplosione ha temporaneamente stordito la Sentinella!")
                    sentinel.last_known_player_pos = None
                    player.inventory.remove("cristallo di Firesalt")
                else:
                    print("Non puoi usare questo oggetto ora.")
            else:
                print("Non hai questo oggetto nel tuo inventario.")
        elif command == "noclip" and current_room.unstable:
            loading_animation(message="Tentativo di noclip")
            print("Sei riuscito a noclippare fuori dal Livello 611! Hai vinto!")
            game_over_screen(player, turns)
            break
        else:
            print("Non capisco questo comando.")

        # Movimento della Sentinella
        if not player.is_hidden and random.random() < 0.8:  # 80% chance of updating last known position
            sentinel.last_known_player_pos = (player.x, player.y)
        sentinel.move_towards(player, rooms)
        
        # Avviso di prossimità della Sentinella
        distance = abs(sentinel.x - player.x) + abs(sentinel.y - player.y)
        if distance <= 2 and not player.is_hidden:
            print("Senti il rumore metallico dei passi della Sentinella. È vicina!")

        if turns % 5 == 0 and player.health < 100:
            player.health = min(100, player.health + 5)
            print(f"Ti sei riposato un po'. Salute: {player.health}")

if __name__ == "__main__":
    main()
