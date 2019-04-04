class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def __getattr__(self, item):
        print("No such attribute")
        return 0

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __str__(self):
        return "First - %s, Last - %s, Pay - %s" % (self.first, self.last, self.pay)

    # def __repr__(self):
    #     pass

class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang



dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(dev_1)
dev_1.pay = 90
dev_1.apply_raise()
print(dev_1.pay)

# print(dev_1.email)
# print(dev_2.prog_lang)
# print(dev_1.fullname)