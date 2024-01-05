from art import logo
import random

def blackjack():
    print(logo)
    # Înlocuiește flag-ul cu o variabilă care să controleze continuarea jocului
    playing = True
    while playing:
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        carti_player = []
        carti_computer = []

        # Alegerea primelor două cărți pentru jucător și computer
        for _ in range(2):
            carti_player.append(random.choice(cards))
            carti_computer.append(random.choice(cards))

        # Funcția pentru calcularea scorului total
        def calculeaza_scor(carti):
            # Tratează asul ca 1 dacă depășește 21
            if sum(carti) > 21 and 11 in carti:
                carti.remove(11)
                carti.append(1)
            return sum(carti)

        while True:
            print(f"Cartile tale: {carti_player}, scor: {calculeaza_scor(carti_player)}")
            print(f"Cartea computerului: [{carti_computer[0]}]")

            # Întrebare pentru extragerea unei noi cărți sau oprire
            vrea_hit = input("Vrei să mai extragi o carte? y/n: ")
            if vrea_hit == 'y':
                carti_player.append(random.choice(cards))
                # Verificare pentru scorul jucătorului
                if calculeaza_scor(carti_player) > 21:
                    print("Ai depășit 21! Ai pierdut.")
                    break
            else:
                # Computerul extrage cărți până când scorul său este cel puțin 17
                while calculeaza_scor(carti_computer) < 17:
                    carti_computer.append(random.choice(cards))

                # Determinarea rezultatului jocului
                scor_jucator = calculeaza_scor(carti_player)
                scor_computer = calculeaza_scor(carti_computer)

                print(f"Cartile tale: {carti_player}, scor: {scor_jucator}")
                print(f"Cartile computerului: {carti_computer}, scor: {scor_computer}")

                if scor_jucator > 21:
                    print("Ai depășit 21! Ai pierdut.")
                elif scor_computer > 21:
                    print("Computerul a depășit 21! Ai câștigat.")
                elif scor_jucator > scor_computer:
                    print("Ai câștigat!")
                elif scor_jucator == scor_computer:
                    print("Este egalitate!")
                else:
                    print("Ai pierdut.")
                # Oprim jocul
                playing = False
                break

blackjack()
