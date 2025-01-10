class Account:
    accounts = []  # Tüm hesapları saklayan static bir liste

    def __init__(self, account_number, owner, balance=0.0):
        self.__account_number = account_number  # Hesap numarası
        self.__owner = owner  # Hesap sahibinin adı
        self.__balance = balance  # Hesap bakiyesi
        Account.accounts.append(self)  # Yeni hesabı listeye ekle

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            Bank.track_transaction(f"{self.__owner} hesabına {amount} TL yatırıldı.")
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.__balance} TL")
        else:
            print("Yatırılacak miktar sıfırdan büyük olmalıdır.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Yetersiz bakiye.")
        elif amount <= 0:
            print("Çekilecek miktar sıfırdan büyük olmalıdır.")
        else:
            self.__balance -= amount
            Bank.track_transaction(f"{self.__owner} hesabından {amount} TL çekildi.")
            print(f"{amount} TL çekildi. Kalan bakiye: {self.__balance} TL")

    def view_balance(self):
        print(f"Hesap Sahibi: {self.__owner}, Hesap Numarası: {self.__account_number}, Bakiye: {self.__balance} TL")

    def get_account_number(self):
        return self.__account_number

    def get_owner(self):
        return self.__owner


class Bank:
    transaction_history = []  # Tüm hesap işlemlerini izleyen static bir liste

    @staticmethod
    def display_bank_info():
        print("Banka Bilgileri:")
        print("Banka Adı: Python Bankası")
        print("Müşteri Hizmetleri: 123-456-7890")

    @staticmethod
    def track_transaction(description):
        Bank.transaction_history.append(description)

    @staticmethod
    def display_transaction_history():
        print("İşlem Geçmişi:")
        for transaction in Bank.transaction_history:
            print(transaction)

    @staticmethod
    def find_account(account_number):
        for account in Account.accounts:
            if account.get_account_number() == account_number:
                return account
        return None


def main():
    Bank.display_bank_info()

    while True:
        print("\n1. Hesap Aç")
        print("2. Giriş Yap")
        print("3. Çıkış")
        choice = input("Seçiminizi yapın (1/2/3): ")

        if choice == '1':
            account_number = input("Hesap numarasını girin: ")
            owner = input("Hesap sahibinin adını girin: ")
            initial_balance = float(input("Başlangıç bakiyesini girin: "))
            Account(account_number, owner, initial_balance)
            print("Hesap başarıyla oluşturuldu.")

        elif choice == '2':
            account_number = input("Hesap numarasını girin: ")
            account = Bank.find_account(account_number)

            if account:
                while True:
                    print("\n1. Para Yatır")
                    print("2. Para Çek")
                    print("3. Bakiye Görüntüle")
                    print("4. Çıkış")
                    action = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")

                    if action == '1':
                        amount = float(input("Yatırılacak miktarı girin: "))
                        account.deposit(amount)

                    elif action == '2':
                        amount = float(input("Çekilecek miktarı girin: "))
                        account.withdraw(amount)

                    elif action == '3':
                        account.view_balance()

                    elif action == '4':
                        print("Çıkış yapılıyor...")
                        break

                    else:
                        print("Geçersiz seçim. Lütfen tekrar deneyin.")
            else:
                print("Hesap bulunamadı.")

        elif choice == '3':
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()