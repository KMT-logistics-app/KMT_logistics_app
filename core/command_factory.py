from commands.assign_package import AssignPackageCommand
from commands.assign_truck import AssignTruckCommand
from commands.create_package import CreatePackageCommand
from commands.create_route import CreateRouteCommand
from commands.find_route import FindRouteCommand
from commands.view_package import ViewPackageCommand
from commands.view_route import ViewRouteCommand
from commands.view_truck import ViewTruckCommand
from commands.create_route import CreateRouteCommand
from commands.create_truck import CreateTruckCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "assignpackage":
            # "assignpackage 1 to route 1"
            return AssignPackageCommand(params, self._app_data)
        if cmd.lower() == "createtruck":
            # "createtruck"
            return CreateTruckCommand(self._app_data)
        if cmd.lower() == "assigntruck":
            # "assign truck 1011 to route 102"
            return AssignTruckCommand(params, self._app_data)
        if cmd.lower() == "createpackage":
            # "createpackage Alice_Springs Adelaide 500kg Ivan_Ivanov ivan@mail.au"
            return CreatePackageCommand(params, self._app_data)
        if cmd.lower() == "createroute":
            # "createroute Sydney Melbourne 2023/08/08/16/00"
            return CreateRouteCommand(params, self._app_data)
        if cmd.lower() == "findroute":
            return FindRouteCommand(params, self._app_data)
            # "findroute Sydney Melbourne"
        if cmd.lower() == "viewpackage":
            return ViewPackageCommand(params, self._app_data)
            # "viewpackage 1"
        if cmd.lower() == "viewroute":
            return ViewRouteCommand(params, self._app_data)
            # "viewroute 7"
        if cmd.lower() == "viewtruck":
            # "viewtruck 1011"
            return ViewTruckCommand(params, self._app_data)

        raise ValueError(f"Invalid command: {cmd}")
