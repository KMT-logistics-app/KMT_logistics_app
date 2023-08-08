from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output = []
        for _ in range(40): # при всяко стартиране на програмата трябва да купим всичките 40 камиона
            buy_trucks = self._command_factory.create('createtruck')
            output.append(buy_trucks.execute())
        while True:
            input_line = input()
            if input_line.lower() == 'end':
                break

            command = self._command_factory.create(input_line)
            output.append(command.execute())

        print('\n'.join(output))
