import unittest

class ValidationHelpers_Should(unittest.TestCase):
    
    # Every command passes proper validation of parameters before it is executed.
    # In this class all the validation cases are tested so there is no need to test
    # the validation of parameters for every command explicitly.
    
    def test_validationHelpersModule_workProperly(self):
        pass
    

class AssignPackageCommand_Should(unittest.TestCase):
    def test_assignPackageCommand_initsCorrectly(self):
        # test for correct result with valid params type
        # test for correct error with invalid params type
        # test for correct error if the package is already assigned
        # test for correct result if the package is assigned to the route
        # test for proper error if the route's truck have no capacity
        # test for proper message if there is no truck assigned to the route
        pass


class AssignTruckCommand_Should(unittest.TestCase):
    def test_assignTruckCommand_initsCorrectly(self):
        # test correct result if truck assigned properly
        # test correct result if truck already assigned
        # test correct result if no route found
        # test correct result if truck id incorrect        
        pass


class CalculateDistanceCommand_Should(unittest.TestCase):
    def test_calculateDistanceCommand_initsCorrectly(self):
        # test correct result with valid data passed 
        # only one test case because if the data is invalid it will raise errors before that
        pass

class CreatePackageCommand_Should(unittest.TestCase):
    def test_createPackageCommand_initsCorrectly(self):
        # test correct package object is created with valid data
        # test correct customer instance created with valid customer info
        # test that the package is added to to customer's packages and customer profile is created
        # test correct message for created package is returned
        # test id is incremented
        pass


class CreateRouteCommand_Should(unittest.TestCase):
    def test_createRouteCommand_initsCorrectly(self):
        # test proper message is returned if the route points are less than two
        # test datetime object is created from the data provided
        # test correct route object is cerated with valid data
        # test correct message returned when the route is created
        # test id is incremented
        pass

class CreateTruckCommand_Should(unittest.TestCase):
    def test_createTruckCommand_initsCorrectly(self):
        # test correct object is created with every instance
        # test id is incremented with correct truck specs
        pass


class FindFreeTrucksByLocationCommand_Should(unittest.TestCase):
    def test_findFreeTrucksByLocationCommand_initsCorrectly(self):
        # test correct message if no free trucks are found
        # test correct message if free trucks are found
        pass

class FindRouteCommand_Should(unittest.TestCase):
    def test_findRouteCommand_initsCorrectly(self):
        # test correct string is returned if routes are found
        # test correct string is returned if no routes are found
        pass

class ViewLocationCommand_Should(unittest.TestCase):
    def test_viewLocationCommand_initsCorrectly(self):
        # test return correct information about the searched location
        pass


class ViewLocationsCommand_Should(unittest.TestCase):
    def test_viewLocationsCommand_initsCorrectly(self):
        # test for correct output if the user is a manager
        # test proper error raised if the user is not a manager
        pass

class ViewPackageCommand_Should(unittest.TestCase):
    def test_viewPackageCommand_initsCorrectly(self):
        # test correct message returned when package is found
        # test correct message returned when package is not found
        pass


class ViewPendingPackagesCommand_Should(unittest.TestCase):
    def test_viewPendingPackagesCommand_initsCorrectly(self):
        pass


class ViewRouteCommand_Should(unittest.TestCase):
    def test_viewRouteCommand_initsCorrectly(self):
        pass


class ViewTruckCommand_Should(unittest.TestCase):
    def test_viewTruckCommand_initsCorrectly(self):
        pass
