<img src="https://drive.google.com/file/d/12IE0Zc20Q7H1o_-ZcXNK4ggxkJnu_TNT/view?usp=sharing" alt="logo" width="300px" style="margin-top: 20px;"/>

# KMT_logistics_app


# Как се работи с приложението:
```
1. Служителят приема пратката и я създава
2. Проверява дали има подходящ маршрут за нея
3. Ако има я добавя към него
4. Ако няма, търси свободен камион чрез find_free_trucks_by_location на база стартовата локация на пратката
5. Ако камионът не е в същия град се изчисляват километрите и времето чрез calculate_distance
6. Създава се маршрут на база получената информация от справките
7. Към маршрута се добавя подходящ камион на база справките по-горе
8. Към маршрута се добавят пратки
9. Ако капацитетът на маршрута в даден момент не позволява да се добавят пратки се създава нов такъв
Налични команди:
- view_truck - показва информация за камион, търсен по ID
- view_route - показва информация за път
- view_pending_packages - показва информация за пратки, които не са добавени към маршрут
- view_package - показва информация за пратка, търсена по ID
- view_locations - показва информация за броя на пратките по локации
- view_location - показва информация за показва броя пратките в локацията и техните дестинации
- find_route - търси/показва информация за маршрут с начална и крайна точка
- find_free_trucks_by_location - търси/показва свободни камиони в определена локация
- crate_truck - създава камион (при стартиране на програмата автоматично се създават 40 камиона)
- create_route - създава маршрут
- create_package - създава пратка
- calculate_distance - изчислява дистанцията и времето за път м/у 2 локации
- assign_truck - добавя камион към ROUTE
- assign_package - добавя пратка към ROUTE

```

# Test case #1 - valid input examples
```
createpackage, Alice Springs, Adelaide, 500, Ivan_Ivanov-ivan@mail.au
createpackage, Adelaide, Sydney, 500.3, Ivan_Ivanov-ivan@mail.au
createroute, alice springs, adelaide, Sydney, 2023/01/08/16/00
createroute, alice springs, adelaide, Sydney, 2024/01/08/16/00
createroute, adelaide, Sydney, Melbourne, 2023/10/08/16/00
createroute, alice springs, sydney, brisbane, perth, adelaide, 2030/01/01/10/20
assigntruck, 1001, 1
assignpackage, 1, 1
findroute, Sydney, Melbourne
viewpackage, 1
viewroute, 2
viewroute, 3
viewtruck, 1011
viewtruck, 1001
end
```

# Test case #2 - valid input examples
```
createpackage, Alice Springs, Adelaide, 500, Ivan_Ivanov-ivan@mail.au 
createpackage, Alice Springs, Adelaide, 300.50, Ivan_Ivanov-ivan@mail.au
createpackage, Adelaide, Sydney, 500.3, Ivan_Ivanov-ivan@mail.au
createpackage, Darwin, Adelaide, 300.50, Petar_Ivanov-pepi@mail.bg
createpackage, Sydney, Adelaide, 200.50, Ivan_Ivanov-ivan@mail.au
createroute, alice springs, adelaide, Sydney, 2024/01/08/16/00
assigntruck, 1011, 1
viewlocation, alice springs
viewlocations
viewpendingpackages
findfreetrucksbylocation, Sydney
calculatedistance, sydney, melbourne
end
```

# Invalid input examples
```
createpackage Alice Springs Adelaide 500 Ivan_Ivanov-ivan@mail.au              -> no commas between the values
createpackage, 500, Alice Springs, Adelaide, Ivan_Ivanov-ivan@mail.au          -> invalid place for package's weight
createpackage, Alice Springs, Adelaide, 500, Ivan_Ivanov-ivanail.au            -> invalid email address - no '@' symbol
createpack, Alice Springs, Adelaide, 500, Ivan_Ivanov-ivan@ail.au              -> invalid command name
createpackage, Alice Springs, Adelaide, 500, I_Ivanov-ivan@ail.au              -> invalid customer first name
createpackage, Alice Springs, Adelaide, 500, Ivan_Ivanov-iv@l.au               -> invalid email - too short


```
createpackage, Alice Springs, Adelaide, 500, Ivan_Ivanov-ivan@mail.au 
createpackage, Alice Springs, Adelaide, 300.50, Ivan_Ivanov-ivan@mail.au
createpackage, Adelaide, Sydney, 500.3, Ivan_Ivanov-ivan@mail.au
createpackage, Darwin, Adelaide, 300.50, Petar_Ivanov-pepi@mail.bg
createpackage, Sydney, Adelaide, 200.50, Ivan_Ivanov-ivan@mail.au
viewpendingpackages
viewlocations
findfreetrucksbylocation, melbourne
createroute, alice springs, adelaide, sydney, darwin, 2023/08/10/18/00
assigntruck, 1030, 1
assignpackage, 1, 1
assignpackage, 2, 1
assignpackage, 3, 1
assignpackage, 1, 1
viewpendingpackages
viewlocations
viewtruck, 1030
viewtruck, 1031
viewroute, 1
viewpackage, 1
assigntruck, 1030, 1
end