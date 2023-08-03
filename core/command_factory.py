from commands.assign_package import AssignPackageCommand
from commands.assign_truck import AssignTruckCommand
from commands.create_package import CreatePackageCommand
from commands.create_route import CreateRouteCommand
from commands.find_route import FindRouteCommand
from commands.view_package import ViewPackageCommand
from commands.view_route import ViewRouteCommand
from commands.view_truck import ViewTruckCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()


        if cmd.lower() == "assignpackage":
            return AssignPackageCommand(params, self._app_data)
        if cmd.lower() == "assigntruck":
            return AssignTruckCommand(params, self._app_data)
        if cmd.lower() == "createpackage":
            return CreatePackageCommand(params, self._app_data)
        if cmd.lower() == "createroute":
            return CreateRouteCommand(params, self._app_data)
        if cmd.lower() == "findroute":
            return FindRouteCommand(params, self._app_data)
        if cmd.lower() == "viewpackage":
            return ViewPackageCommand(params, self._app_data)
        if cmd.lower() == "viewroute":
            return ViewRouteCommand(params, self._app_data)
        if cmd.lower() == "viewtruck":
            return ViewTruckCommand(params, self._app_data)
        

        raise ValueError(f'Invalid command: {cmd}')