class Employee:
    """Moddule for Class Employee"""
    
    raise_amt = 0.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email_me(self):
        return f'{self.first}.{self.last}@emial.com'

    @property
    def fullname(self):
        return f'{self.first}.{self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
