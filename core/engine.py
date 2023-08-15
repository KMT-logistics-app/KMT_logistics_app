from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output = []
        
        log_user = self._command_factory.create("login, employee")
        output.append(log_user.execute())
        
        for _ in range(40):
            buy_trucks = self._command_factory.create("createtruck")
            output.append(buy_trucks.execute())

        while True:
            input_line = input()
            if input_line.lower() == "end":
                break
            
            command = self._command_factory.create(input_line)
            output.append(command.execute())

        print("\n==========\n".join(output))
