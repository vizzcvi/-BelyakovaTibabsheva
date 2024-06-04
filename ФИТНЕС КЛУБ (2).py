class Member:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        self.trainings = []
        self.payments = []

    def add_training(self, training):
        self.trainings.append(training)

    def make_payment(self, amount):
        self.payments.append(amount)

    def get_total_payments(self):
        return sum(self.payments)

class Training:
    def __init__(self, date, type):
        self.date = date
        self.type = type

class Payment:
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date

# Функция для добавления нового члена
def add_member():
    name = input("Введите имя участника: ")
    membership_type = input("Введите тип членства: ")
    return Member(name, membership_type)

# Функция для записи на тренировку
def record_training(member):
    date = input("Введите дату тренировки: ")
    type = input("Введите тип тренировки: ")
    member.add_training(Training(date, type))

# Функция для совершения платежа
def make_payment(member):
    amount = float(input("Введите сумму платежа: "))
    member.make_payment(Payment(amount, "today"))

# Основная функция программы
def main():
    members = []
    while True:
        print("\n1. Добавить нового участника")
        print("2. Записаться на тренировку")
        print("3. Совершить платеж")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            member = add_member()
            members.append(member)
        elif choice == '2':
            name = input("Введите имя участника: ")
            for member in members:
                if member.name == name:
                    record_training(member)
                    break
        elif choice == '3':
            name = input("Введите имя участника: ")
            for member in members:
                if member.name == name:
                    make_payment(member)
                    break
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
