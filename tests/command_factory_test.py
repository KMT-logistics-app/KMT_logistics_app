from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from commands.assign_package import AssignPackageCommand
from commands.assign_truck import AssignTruckCommand
from commands.calculate_distance import CalculateDistanceCommand
from commands.create_package import CreatePackageCommand
from commands.create_route import CreateRouteCommand
from commands.create_truck import CreateTruckCommand
from commands.find_free_trucks_by_location import FindFreeTrucksByLocationCommand
from commands.find_route import FindRouteCommand
from commands.view_location import ViewLocationCommand
from commands.view_locations import ViewLocationsCommand
from commands.view_package import ViewPackageCommand
from commands.view_pending_packages import ViewPendingPackagesCommand
from commands.view_route import ViewRouteCommand
from commands.view_truck import ViewTruckCommand
import unittest


class CommandFactory_Should(unittest.TestCase):
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
        self._command_factory = CommandFactory(self._app_data)

    def test_commandCreate_inputLine(self):
        # Arrange
        commands = {
            "assignpackage, 1, 1": AssignPackageCommand,
            "assigntruck, 1011, 1": AssignTruckCommand,
            "calculatedistance, sydney, melbourne": CalculateDistanceCommand,
            "createpackage, Darwin, Adelaide, 300.50, Petar_Ivanov-pepi@mail.bg": CreatePackageCommand,
            "createroute, alice springs, adelaide, Sydney, 2024/01/08/16/00": CreateRouteCommand,
            "createtruck": CreateTruckCommand,
            "findfreetrucksbylocation, Sydney": FindFreeTrucksByLocationCommand,
            "findroute, Sydney, Melbourne": FindRouteCommand,
            "viewlocation, Sydney": ViewLocationCommand,
            "viewlocations": ViewLocationsCommand,
            "viewpackage, 1": ViewPackageCommand,
            "viewpendingpackages": ViewPendingPackagesCommand,
            "viewroute, 1": ViewRouteCommand,
            "viewtruck, 1011": ViewTruckCommand,
        }

        # Act & Assert
        for cmd, command_class in commands.items():
            input_line = cmd.lower()
            command_instance = self._command_factory.create(input_line)
            self.assertIsInstance(command_instance, command_class)
            self.assertIsInstance(command_instance._app_data, ApplicationData)

    def test_invalid_command(self):
        with self.assertRaises(ValueError):
            self._command_factory.create('routecreate')

    def test_params_correct_extraction(self):
        # Arrange & Act
        input_line = 'calculatedistance, param1, param2'
        command_instance = self._command_factory.create(input_line)
        # Assert
        self.assertEqual(['param1', 'param2'], command_instance._params)