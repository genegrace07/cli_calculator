
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
        while True:
            operator = input('Choose operators ( +,-,x,/ ): ')
            if operator == '+':
                total = self.num1 + self.num2
                print(f'Total: {total}')
                print()
                self.retry()
                self.user_input()
            elif operator not in (' +,-,x,/ '):
                print('wrong operator')
                continue
    def add(self):
        pass
    def minus(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass
    def retry(self):
        while True:
            if input('Calculate again?y or any key to quit: ') == 'y'.lower().strip():
                break
            else:
                print('Thank you, Goodbye 👋')
                break


user = UsersInput(2,3)
user.user_input()
op = Operators(2,3)
op.choose_operator()

'''
functions
loops
conditionals
oop( classes, inheritance )
modules & packages ( import,virtualenv, pip, requirements.txt )

'''