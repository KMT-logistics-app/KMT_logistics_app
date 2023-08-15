from core.application_data import ApplicationData as ad
from core.command_factory import CommandFactory
from models.constants.roles import Roles


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output = []

        for _ in range(40):  # при всяко стартиране на програмата трябва да купим всичките 40 камиона
            buy_trucks = self._command_factory.create("createtruck")
            output.append(buy_trucks.execute())
        
        ad.logged_in_user = Roles.EMPLOYEE

        while True:
            input_line = input()
            if input_line.lower() == "end":
                break
            
            command = self._command_factory.create(input_line)
            output.append(command.execute())

        print("\n==========\n".join(output))
