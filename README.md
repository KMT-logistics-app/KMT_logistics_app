<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg)" alt="logo" width="300px" style="margin-top: 20px;"/>

# KMT_logistics_app

## Description:
The application will be used by employees of a large Australian company aiming to expand its activities to the freight industry. The app will be used to manage the delivery of packages between hubs in major Australian cities. An employee of the company is able to record the details of a delivery package, create or search for suitable delivery routes, and inspect the current state of delivery packages, transport vehicles and delivery routes.

## What is the work flow:

1. Employee accepts the package from a customer and creates it in the application.
2. He/She check if there is a suitable route for it.
3. If there is a route, the employee adds the package to the route.
4. If there's not, he/she search for the nearest free truck.
5. If the truck is not at the same city, the employee calculates the kilometers and the time for relocation of the truck.
6. Тhe route is created based on the information gathered above.
7. The employee assigns the truck and packages to the route.
8. To the routes can be assigned many packages but only one truck.
9. The capacity for the packages in the route is based on the truck load capacity. If the employye tries to assign package which weight is bigger than the capacity left, new route has to be created.

## Available commands:
- view_truck - shows information about a truck, searched by ID
- view_route - shows information about a route, searched by ID
- view_pending_packages - can be performed only by manager, shows information about packages in the hubs which are not assigned to any route
- view_package - shows information aboute package, searched by ID
- view_locations - shows information about the number of packages in the locations(assigned and accepted), searched by ID
- view_location - shows information about the packages in the current city for the current destinations
- find_route - search/shows for a route which starts or goes through a specific location and ends at specific location
- find_free_trucks_by_location - search/shows free trucks at a specific location
- crate_truck - creates truck (when the program is started, it automatically performs this command)
- create_route - creates route based on at least two locations(starting and ending) and exact time for starting
- create_package - creates package based on start and end locations, weight and contact_info
- calculate_distance - calculates the distance and time for travel between two locations
- assign_truck - assigns truck to ROUTE
- assign_package - assigns package to ROUTE
- login_user - logs a user
- logout_user - logs out a user

# Models
## Truck
#### Properties:
- id - unique identifier
- brand - specific model
- status - dynamic state for a specific moment / starts with "free"
- routes - routes which will be or are already done by the truck
- capacity - the max sum of packages weight which could be loaded
- range - the max length of a route which the truck could be added to
- location - a dynamic property that indicates where the truck is at a given time
- free_intervals - shows the free intervals in which the truck can be used based on the routes which it's assigned to
#### Methods:
- create_id(self) - creates unique ID
- validate_brand(self, current_id) - defines the brand based on the ID
- validate_capacity(self) - defines the capacity based on the brand
- validate_range(self) - defines the range based on the brand
- str(self) - displays information about the truck based on it's ID, location, brand, capacity, range, status, availability

## Package
#### Properties:
- id - unique identifier
- start_location - the location where the package is accepted and will be picked up for delivery
- end_location - the hub in which it has to be delivered
- contact_info - customer from class customer(first and last names + email)
- route - the routhe to which it is assigned / None, if it's not assigned yet
- status - dynamic state for a specific moment / starts with "Accepted"
- accepted_time - the specific moment at which it was created
- estimated_arrival_time - the exact time when the route in which the package is assigned to finishes / starts with None until it's assigned to route
- delivery_time_needed - needed time for traveling between the start and end locations
- weight - float number of it's weight
#### Methods:
- create_id(self) - creates unique ID
- time_needed(self) - calculates the required travel time
- package_details(self) - shows information about the package based on it's weight, accepted time, start location, status and contact_info
- str(self) - displays information for ID, expected delivery time and the details

## Route
#### Properties:
- id - unique identifier
- route_points - start, mid(if contained) and end locations
- departure_time - exact time for starting
- distance - the total distance to be covered
- truck - the truck which will transport the shipments
- packages - list of packages which will be shipped
- status - dynamic property which indicates whether the route has started or finished / status is "pending" until the start time
#### Methods:
- assign_package(self, package) - assigns package(changes package status and estimated delivery time)
- assign_truck(self, truck) - assigns truck
- calculate_estimated_time(self) - calculates the estimated arrival time at the final destination based on the route points
- create_id(self) - creates unique ID
- packages_weight(self) - returns the total weight of all assigned packages
- truck_capacity(self) - returns the remaining capacity of the assigned truck
- total_distance(self) - calculates the total sum of the distances between the route stops
- str(self) - displays information for ID, status, total distance, route points, packages, assigned truck

## Customer
#### Properties:
- first_name - first name of the customer
- last_name - last name of the customer
- email - email of the customer
- packages - list of customer's packages
#### Methods:
- add_package(self, package) - adds package to costomer's packages list