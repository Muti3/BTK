import random

# 1. Abstract Player Class
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.choice = None
    
    @abstractmethod
    def make_choice(self):
        pass

    def get_choice(self):
        return self.choice

    def set_choice(self, choice):
        self.choice = choice

# 2. ComputerPlayer Abstract Class (inherits from Player)
class ComputerPlayer(Player):
    def __init__(self, name="Computer"):
        super().__init__(name)

# 3. HumanPlayer Class (inherits from Player)
class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_choice(self):
        # Kullanıcıdan hamle almak
        while True:
            print(f"{self.name}, lütfen taş (1), kağıt (2) veya makas (3) seçin:")
            try:
                choice = int(input())
                if choice in [1, 2, 3]:
                    self.set_choice(choice)
                    break
                else:
                    print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")

# 4. RandomComputerPlayer Class (inherits from ComputerPlayer)
class RandomComputerPlayer(ComputerPlayer):
    def make_choice(self):
        # Bilgisayarın rastgele bir seçim yapması
        self.set_choice(random.choice([1, 2, 3]))

# 5. Helper Functions
def determine_winner(player_choice, computer_choice):
    # Taş (1), Kağıt (2), Makas (3)
    if player_choice == computer_choice:
        return "Beraberlik!"
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

def choice_to_string(choice):
    if choice == 1:
        return "Taş"
    elif choice == 2:
        return "Kağıt"
    elif choice == 3:
        return "Makas"

# 6. Main Game Function
def play_game():
    # Kullanıcı adı ve oyun başlatma
    player_name = input("Lütfen isminizi girin: ")
    player = HumanPlayer(player_name)
    computer = RandomComputerPlayer()
    
    player_score = 0
    computer_score = 0
    history = []

    while True:
        # Her tur için oyuncuların seçim yapması
        player.make_choice()
        computer.make_choice()

        print(f"\n{player.name}'ın seçimi: {choice_to_string(player.get_choice())}")
        print(f"Bilgisayarın seçimi: {choice_to_string(computer.get_choice())}")

        # Sonuçları belirle
        result = determine_winner(player.get_choice(), computer.get_choice())
        print(f"Sonuç: {result}")
        
        if result == "Kazandınız!":
            player_score += 1
        elif result == "Kaybettiniz!":
            computer_score += 1

        # Skorları ekrana yazdır
        print(f"\nPuan Durumu: {player.name} - {player_score}, Bilgisayar - {computer_score}")

        # Hamle geçmişini kaydet
        history.append((player.name, choice_to_string(player.get_choice()), "vs", "Bilgisayar", choice_to_string(computer.get_choice()), result))
        
        # Geçmişi gösterme seçeneği
        show_history = input("\nHamle geçmişini görmek ister misiniz? (e/h): ")
        if show_history.lower() == "e":
            print("\n--- Hamle Geçmişi ---")
            for entry in history:
                print(f"{entry[0]} {entry[1]} {entry[2]} {entry[3]} {entry[4]} - {entry[5]}")
        
        # Devam etme veya çıkma seçeneği
        play_again = input("\nBir tur daha oynamak ister misiniz? (e/h): ")
        if play_again.lower() != 'e':
            print("\nOyun bitti!")
            print(f"\nToplam Puanlar: {player.name} - {player_score}, Bilgisayar - {computer_score}")
            break

# 7. Oyun Başlatma
if __name__ == "__main__":
    play_game()
