from commands.assign_package import AssignPackageCommand
from commands.assign_truck import AssignTruckCommand
from commands.calculate_distance import CalculateDistanceCommand
from commands.create_package import CreatePackageCommand
from commands.create_route import CreateRouteCommand
from commands.find_route import FindRouteCommand
from commands.view_package import ViewPackageCommand
from commands.view_pending_packages import ViewPendingPackagesCommand
from commands.view_route import ViewRouteCommand
from commands.view_truck import ViewTruckCommand
from commands.create_route import CreateRouteCommand
from commands.create_truck import CreateTruckCommand
from commands.view_locations import ViewLocationsCommand
from commands.view_location import ViewLocationCommand
from commands.find_free_trucks_by_location import FindFreeTrucksByLocationCommand
from commands.login_user import LoginUserCommand
from commands.logout_user import LogoutUserCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split(", ")

        if cmd.lower() == "assignpackage":
            return AssignPackageCommand(params, self._app_data)
        if cmd.lower() == "viewlocations":
            return ViewLocationsCommand(self._app_data)
        if cmd.lower() == "viewlocation":
            return ViewLocationCommand(params, self._app_data)
        if cmd.lower() == "createtruck":
            return CreateTruckCommand(self._app_data)
        if cmd.lower() == "calculatedistance":
            return CalculateDistanceCommand(params, self._app_data)
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
        if cmd.lower() == "viewpendingpackages":
            return ViewPendingPackagesCommand(self._app_data)
        if cmd.lower() == "findfreetrucksbylocation":
            return FindFreeTrucksByLocationCommand(params, self._app_data)
        if cmd.lower() == "login":
            return LoginUserCommand(params, self._app_data)
        if cmd.lower() == "logout":
            return LogoutUserCommand(self._app_data)

        raise ValueError(f"Invalid command: {cmd}")
