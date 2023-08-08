# from models.truck import Truck
from models.constants.cities import Cities
from datetime import datetime, timedelta
# from models.package import Package
# from models.truck import Truck


class Route:
    ROUTE_ID = 0

    def __init__(self, *args) -> None:
        self._id = self.create_id()
        self.route_points = args[:-1]
        self._distance = self.calculate_distance(self.route_points)
        # self.trucks: list[Truck] = []  # разкоментирано от Трифон
        self.departure_time = args[-1]
        # self._packages = list[Package]  # добавено от Трифон


    def packages_weight(self):  # добавено от Трифон
        weight_sum = 0
        for package in self._packages:
            weight_sum += package.weight
        return weight_sum


    def trucks_capacity(self):  # добавено от Трифон
        all_trucks_capacity = 0
        for truck in self.trucks:
            all_trucks_capacity += truck.capacity
        result = all_trucks_capacity - self.packages_weight()
        if result > 0:
            return result
        else:
            return 0


    def assign_package(self, pack):  # добавено от Трифон
        self._packages.append(pack)

    # def assign_truck(self, truck: Truck):  # разкоментирано от Трифон
    #     self.trucks.append(truck)

    @property
    def departure_time(self):
        return self._departure_time


    @departure_time.setter # да се оправят входните параметри
    def departure_time(self, value):
        if not isinstance(value, datetime):
            raise TypeError
        self._departure_time = value


    @property
    def route_id(self):
        return self._id

    @property
    def distance(self):
        return self._distance

    def calculate_distance(self, lst):
        total = 0

        for city in lst[:-1]:
            for current, next_city in Cities.DISTANCES.items():
                if current == city:
                    city_idx = lst.index(city)
                    for i in range(len(next_city)):
                        if lst[city_idx + 1] == next_city[i][0]:
                            total += next_city[i][1]
                            break
                    break

        return total

    # не е довършено, но започва да става ясно какво трябва да се направи. Много добре се разбира като се дебъгне с примерния инпут
    def calculate_estimated_time(self, lst):
        eta = self.departure_time
        print(self.departure_time)
        for city in lst[:-1]:
            for current, next_city in Cities.DISTANCES.items():
                if current == city:
                    city_idx = lst.index(city)
                    for i in range(len(next_city)):
                        if lst[city_idx + 1] == next_city[i][0]:
                            eta += timedelta(hours=next_city[i][1] / 87)
                            print(
                                f'Next stop: {lst[city_idx+1]} {eta.strftime("%Y-%m-%d  %H:%M")}, travel time: {next_city[i][1] / 87:.2f} hours'
                            )
                            break
                    break

        return eta

    def create_id(self):
        Route.ROUTE_ID += 1
        return Route.ROUTE_ID

    def __str__(self) -> str:
        new_line = "\n"
        return f'Route ID: {self._id}\
        {new_line}Total distance: {self._distance}km\
        {new_line}Route details: {" -> ".join(self.route_points)}'


# този клас Route трябва да генерира уникално ID и да включва час тръгване и час пристигане

# трябва да има метод assign_truck(truck)

# трябва да има __str__ имплементация

# route = ["Alice Springs", "Adelaide", "Melbourne", "Sydney", "Brisbane"]
# new_route = Route(route)

# print(str(new_route))
# hours = new_route.calculate_estimated_time(route)
