from models.package import Package

class Customer:
    
# can:
# - send a package
# - request package info
# - receive a package
# - leave feedback

# has:
# - first Name
# - last name
# - email
# - packages

    def __init__(self, first_name, last_name, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.packages: list[Package] = []



    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if len(value) < 2 or len(value) > 15:
            raise ValueError('First name should be between 2 and 15 symbols')
        if not value.isalpha():
            raise ValueError('First name contains invalid symbols! Try writing your name correctly :)')

        self._first_name = value


    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if len(value) < 2 or len(value) > 15:
            raise ValueError('Last name should be between 2 and 15 symbols')
        if not value.isalpha():
            raise ValueError('Last name contains invalid symbols! Try writing your name correctly :)')

        self._last_name = value


    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError('Invalid email address!')
        
        self._email = value
    

    def __str__(self) -> str:
        new_line = '\n'
        packages = [str(pack) for pack in self.packages]
        return f'Customer: {self.first_name} {self.last_name}\
            {new_line}Email address: {self.email}\
            {new_line}Packages: {len(self.packages)}\
            {new_line}{new_line.join(packages)}'
    