from datetime import datetime
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
from commands.validation_helpers import (
    create_customer_info, try_parse_float, try_parse_int, 
    validate_params_count, ensure_valid_location_name
    )
from models.customer import Customer
from errors.application_error import ApplicationError

import test_data as td
import unittest

class ValidationHelpers_Should(unittest.TestCase):
    
    '''
    Every command in the application passes proper validation of parameters before it is executed.

    In this class all the validation cases are tested so there is no need to test
    the validation of parameters for every command explicitly.
    '''

    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()

    def test_ensureValidLocationName_withValidLocationName(self):
        # Arrange & Act
        result = ensure_valid_location_name(td.VALID_START_LOCATION)

        # Assert
        self.assertIsInstance(result, str)

    def test_ensureValidLocationName_raisesNameError_whenInvalidLocationName(self):
        # Arrange, Act & Assert
        with self.assertRaises(NameError):
            ensure_valid_location_name(td.INVALID_LOCATION_NAME)
        
    def test_validateParamsCount_withCorrectParamsCount(self):
        # Arrange, Act, Assert
        validate_params_count(['param1', 'param2'], 2)

    def test_validateParamsCount_raisesValueError_withIncorrectParamsCount(self):
        # Arrange, Act, Assert
        with self.assertRaises(ValueError):
            validate_params_count(['param1', 'param2'], 3)

    def test_tryParseFloat_withCorrectValue(self):
        # Arrange & Act
        result = try_parse_float('5')

        # Assert
        self.assertEqual(result, 5.0)

    def test_tryParseFloat_withIncorrectValue(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            try_parse_float('Sydney')
        
    def test_tryParseInt_withCorrectValue(self):
        # Arrange & Act
        result = try_parse_int('5')

        # Assert
        self.assertEqual(result, 5)

    def test_tryParseInt_withIncorrectValue(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            try_parse_int('Sydney')

    def test_createCustomerInfo_withCorrectData(self):
        # Arrange & Act
        result = create_customer_info(td.VALID_CONTACT_INFO)
        
        # Assert
        self.assertEqual(result, ('Ivan', 'Ivanov', 'ivan@mail.au'))

    def test_createCustomerInfo_raisesIndexError_whenDataIncorrectlyFormatted(self):
        # Arrange, Act & Assert
        
        with self.assertRaises(IndexError):
            create_customer_info(td.INVALID_CONTACT_INFO)


class AssignPackageCommand_Should(unittest.TestCase):

    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
        
    def test_assignPackageCommand_initsCorrectly(self):

        # Arrange & Act
        result = CommandFactory.create(self, 'assignpackage, 1, 1')
        
        # Assert
        self.assertIsInstance(result, AssignPackageCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 2)
       
        # test for proper error if the route's truck have no capacity
        # test for proper message if there is no truck assigned to the route

    def test_packageAssignedCorrectly_toRoute(self):
        # Arrange
        self._app_data.create_truck()
        test_package = self._app_data.create_package(
            td.VALID_START_LOCATION, td.VALID_END_LOCATION, td.VALID_WEIGHT, td.VALID_CONTACT_INFO
        )
        test_route = self._app_data.create_route(
            [td.VALID_START_LOCATION, td.VALID_END_LOCATION], datetime(*map(int, td.VALID_DATE.split("/")))
            )
        AssignTruckCommand.execute(CommandFactory.create(
            self, f'assigntruck, {self._app_data._trucks[0].TRUCK_ID}, {self._app_data._routes[0].ROUTE_ID}')
            )
        
        # Act
        result = AssignPackageCommand.execute(CommandFactory.create(self, f'assignpackage, {str(test_package._id)}, {str(test_route._id)}'))
                
        # Assert
        self.assertEqual(result, f"Package {test_package._id} was assigned to route {test_route._id}.")

    def test_assignPackageToRoute_returnsCorrectMessage_ifPackageAlreadyAssigned(self):
        # Arrange
        self._app_data.create_truck()
        test_package = self._app_data.create_package(
            td.VALID_START_LOCATION, td.VALID_END_LOCATION, td.VALID_WEIGHT, td.VALID_CONTACT_INFO
        )
        test_route = self._app_data.create_route(
            [td.VALID_START_LOCATION, td.VALID_END_LOCATION], datetime(*map(int, td.VALID_DATE.split("/")))
            )
        AssignTruckCommand.execute(CommandFactory.create(
            self, f'assigntruck, {self._app_data._trucks[0].TRUCK_ID}, {self._app_data._routes[0].ROUTE_ID}')
            )

        # Act
        AssignPackageCommand.execute(CommandFactory.create(self, f'assignpackage, {str(test_package._id)}, {str(test_route._id)}'))
        result = AssignPackageCommand.execute(CommandFactory.create(self, f'assignpackage, {str(test_package._id)}, {str(test_route._id)}'))

        # Assert
        self.assertEqual(result, f'Package {test_package._id} already assigned.')

class AssignTruckCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()

    def test_assignTruckCommand_initsCorrectly(self):
        # test correct result if truck assigned properly
        # test correct result if truck already assigned
        # test correct result if no route found
        # test correct result if truck id incorrect 
        
        # Arrange & Act
        result = CommandFactory.create(self, 'assigntruck, 1010, 1')
        
        # Assert
        self.assertIsInstance(result, AssignTruckCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 2)


class CalculateDistanceCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_calculateDistanceCommand_initsCorrectly(self):
        # test correct result with valid data passed 
        # only one test case because if the data is invalid it will raise errors before that

        # Arrange & Act
        result = CommandFactory.create(self, 'calculatedistance, sydney, melbourne')
        
        # Assert
        self.assertIsInstance(result, CalculateDistanceCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 2)


class CreatePackageCommand_Should(unittest.TestCase):
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()

    def test_createPackageCommand_initsCorrectly(self):

        # Arrange & Act
        result = CommandFactory.create(self, f'createpackage, {td.VALID_PACKAGE}')
        
        # Assert
        self.assertIsInstance(result, CreatePackageCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 4)

    
    def test_createPackageCommand_returnsCorrectOutput_withValidData(self):
        # Arrange & Act
        cmd_create = CommandFactory.create(self, f'createpackage, {td.VALID_PACKAGE}')
        result = CreatePackageCommand.execute(cmd_create)
        
        # Assert
        self.assertIsInstance(result, str)

    def test_packageId_incrementsCorrectly(self):
        # Arrange & Act
        result1 = ApplicationData.create_package(
            self._app_data, td.VALID_START_LOCATION, td.VALID_END_LOCATION, td.VALID_WEIGHT, td.VALID_CONTACT_INFO
            )
        
        result2 = ApplicationData.create_package(
            self._app_data, td.VALID_START_LOCATION, td.VALID_END_LOCATION, td.VALID_WEIGHT, td.VALID_CONTACT_INFO
            )
        
        # Assert
        self.assertEqual(result1._id, 5)
        self.assertEqual(result2._id, 6)
        
    def test_customerObjectCreated_withValidData(self):
        # Arrange & Act
        result = ApplicationData.create_customer(self._app_data, *create_customer_info(td.VALID_CONTACT_INFO))

        # Assert
        self.assertIsInstance(result, Customer)


    def test_customerProfileCreated_andPackageAdded_toCustomersPackages(self):
        # Arrange & Act
        cmd_create = CommandFactory.create(self, f'createpackage, {td.VALID_PACKAGE}')
        CreatePackageCommand.execute(cmd_create)
        the_customer = self._app_data._customers[0]

        # Assert
        self.assertEqual(len(self._app_data._customers), 1)
        self.assertEqual(len(the_customer._packages), 1)
    

class CreateRouteCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_createRouteCommand_initsCorrectly(self):
        # test proper message is returned if the route points are less than two
        # test datetime object is created from the data provided
        # test correct route object is cerated with valid data
        # test correct message returned when the route is created
        # test id is incremented

        # Arrange & Act
        result = CommandFactory.create(self, f'createroute, {td.VALID_ROUTE}')
        
        # Assert
        self.assertIsInstance(result, CreateRouteCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 3)


class CreateTruckCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_createTruckCommand_initsCorrectly(self):
        # test correct object is created with every instance
        # test id is incremented with correct truck specs

        # Arrange & Act
        result = CommandFactory.create(self, f'createtruck')
        
        # Assert
        self.assertIsInstance(result, CreateTruckCommand)
        self.assertIsInstance(result._app_data, ApplicationData)


class FindFreeTrucksByLocationCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_findFreeTrucksByLocationCommand_initsCorrectly(self):
        # test correct message if no free trucks are found
        # test correct message if free trucks are found
        
        # Arrange & Act
        result = CommandFactory.create(self, f'findfreetrucksbylocation, {td.VALID_START_LOCATION}')
        
        # Assert
        self.assertIsInstance(result, FindFreeTrucksByLocationCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 1)


class FindRouteCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_findRouteCommand_initsCorrectly(self):
        # test correct string is returned if routes are found
        # test correct string is returned if no routes are found
        
        # Arrange & Act
        result = CommandFactory.create(self, f'findroute, {td.VALID_START_LOCATION}, {td.VALID_END_LOCATION}')
        
        # Assert
        self.assertIsInstance(result, FindRouteCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 2)


class ViewLocationCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_viewLocationCommand_initsCorrectly(self):
        # test return correct information about the searched location
        # test retuns correct message or error if the user has/doesn't have right to perform the task
        
        # Arrange & Act
        result = CommandFactory.create(self, f'viewlocation, {td.VALID_START_LOCATION}')
        
        # Assert
        self.assertIsInstance(result, ViewLocationCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 1)


class ViewLocationsCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_viewLocationsCommand_initsCorrectly(self):
        # test for correct output if the user is a manager
        # test proper error raised if the user is not a manager
        
        # Arrange & Act
        result = CommandFactory.create(self, 'viewlocations')
        
        # Assert
        self.assertIsInstance(result, ViewLocationsCommand)
        self.assertIsInstance(result._app_data, ApplicationData)


class ViewPackageCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_viewPackageCommand_initsCorrectly(self):
        # Arrange & Act
        result = CommandFactory.create(self, 'viewpackage, 1')
        
        # Assert
        self.assertIsInstance(result, ViewPackageCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 1)

    def test_viewPackageCommand_returnsCorrectMessage_whenPackageFound(self):
        # Arrange & Act
        cmd_create = CommandFactory.create(self, 'viewpackage, 1')
        result = ViewPackageCommand.execute(cmd_create)
        
        # Assert
        self.assertIsInstance(result, str)

    def test_viewPackageCommand_raisesValueError_whenNoPackageFound(self):
        # Arrange
        cmd_create = CommandFactory.create(self, 'viewpackage, Sydney')
        
        #Act & Assert
        with self.assertRaises(ValueError):
            ViewPackageCommand.execute(cmd_create)
        

class ViewPendingPackagesCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_viewPendingPackagesCommand_initsCorrectly(self):
        # test correct return when there are no packages accepted
        # test correct return when there are accepted packages
        # test correct return/error if the user is not supervisor

        # Arrange & Act
        result = CommandFactory.create(self, 'viewpendingpackages')
        
        # Assert
        self.assertIsInstance(result, ViewPendingPackagesCommand)
        self.assertIsInstance(result._app_data, ApplicationData)


class ViewRouteCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_viewRouteCommand_initsCorrectly(self):
        # test correct return when route found
        # test correct return when no route is found
         
         # Arrange & Act
        result = CommandFactory.create(self, 'viewroute, 1')
        
        # Assert
        self.assertIsInstance(result, ViewRouteCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 1)


class ViewTruckCommand_Should(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act
        self._app_data = ApplicationData()
    
    def test_viewTruckCommand_initsCorrectly(self):
        # test correct return when truck is found
        # test correct return when no truck is found

        # Arrange & Act
        result = CommandFactory.create(self, 'viewtruck, 1001')
        
        # Assert
        self.assertIsInstance(result, ViewTruckCommand)
        self.assertIsInstance(result._app_data, ApplicationData)
        self.assertEqual(len(result._params), 1)
