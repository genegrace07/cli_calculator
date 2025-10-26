
class UsersInput:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def user_input(self):
        is_running = True
        while is_running:
            try:
                self.num1 = input('Enter 1st number: ')
                self.num1 = float(self.num1)
                is_running = False
            except ValueError:
                print('Not valid number')
                continue
        while True:
            try:
                self.num2 = input('Enter 2nd number: ')
                self.num2 = float(self.num2)
                return self.num1, self.num2
            except ValueError:
                print('Not valid number')
                continue

class Operators(UsersInput):
    def choose_operator(self):
        operator = input('Choose operators ( +,-,x,/ ): ')
        if operator == '+':
            self.add()
            self.retry()
        elif operator == '-':
            self.minus()
            self.retry()
        elif operator == '*':
            self.multiply()
            self.retry()
        elif operator == '/':
            self.divide()
            self.retry()
        else:
            print('wrong operator')
            self.choose_operator()
    def add(self):
            total = self.num1 + self.num2
            print(f'Total: {total}')
            print()
    def minus(self):
            total = self.num1 - self.num2
            print(f'Total: {total}')
            print()
    def multiply(self):
            total = self.num1 * self.num2
            print(f'Total: {total}')
            print()
    def divide(self):
        try:
            total = self.num1 / self.num2
            print(f'Total: {total}')
            print()
        except ZeroDivisionError:
            print(f'Invalid,{self.num1} Cannot divide by 0')
    def retry(self):
            again = input('Calculate again?y or any key to quit: ').lower().strip()
            if again == 'y':
                self.user_input()
                self.choose_operator()
            else:
                print('Thank you, Goodbye 👋')
                return


user = Operators(0,0)
user.user_input()
user.choose_operator()
