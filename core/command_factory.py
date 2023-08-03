from commands.assign_package import AssignPackageCommand
from commands.assign_truck import AssignTruckCommand
from commands.create_package import CreatePackageCommand
from commands.create_delivery_route import CreateRouteCommand
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
            # "assignpackage 501 to truck 1011"
            return AssignPackageCommand(params, self._app_data)
        if cmd.lower() == "assigntruck":
            # "assign truck 1011 to route 102"
            return AssignTruckCommand(params, self._app_data)
        if cmd.lower() == "createpackage":
            # "createpackage Sofia Varna 500kg Ivan_Ivanov"
            return CreatePackageCommand(params, self._app_data)
        if cmd.lower() == "createroute":
            # "createroute Sofia Varna"
            return CreateRouteCommand(params, self._app_data)
        if cmd.lower() == "findroute":
            return FindRouteCommand(params, self._app_data)
            # "findroute Sofia Varna"
        if cmd.lower() == "viewpackage":
            return ViewPackageCommand(params, self._app_data)
            # "viewpackage 501"
        if cmd.lower() == "viewroute":
            return ViewRouteCommand(params, self._app_data)
            # "viewroute 5"
        if cmd.lower() == "viewtruck":
            # "viewtruck 1011"
            return ViewTruckCommand(params, self._app_data)

        raise ValueError(f"Invalid command: {cmd}")
