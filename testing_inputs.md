## Test case #1 - valid input examples
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

## Test case #1 - expected output
```
Truck Scania with ID 1001 was created.
==========
Truck Scania with ID 1002 was created.
==========
Truck Scania with ID 1003 was created.
==========
Truck Scania with ID 1004 was created.
==========
Truck Scania with ID 1005 was created.
==========
Truck Scania with ID 1006 was created.
==========
Truck Scania with ID 1007 was created.
==========
Truck Scania with ID 1008 was created.
==========
Truck Scania with ID 1009 was created.
==========
Truck Scania with ID 1010 was created.
==========
Truck Man with ID 1011 was created.
==========
Truck Man with ID 1012 was created.
==========
Truck Man with ID 1013 was created.
==========
Truck Man with ID 1014 was created.
==========
Truck Man with ID 1015 was created.
==========
Truck Man with ID 1016 was created.
==========
Truck Man with ID 1017 was created.
==========
Truck Man with ID 1018 was created.
==========
Truck Man with ID 1019 was created.
==========
Truck Man with ID 1020 was created.
==========
Truck Man with ID 1021 was created.
==========
Truck Man with ID 1022 was created.
==========
Truck Man with ID 1023 was created.
==========
Truck Man with ID 1024 was created.
==========
Truck Man with ID 1025 was created.
==========
Truck Actross with ID 1026 was created.
==========
Truck Actross with ID 1027 was created.
==========
Truck Actross with ID 1028 was created.
==========
Truck Actross with ID 1029 was created.
==========
Truck Actross with ID 1030 was created.
==========
Truck Actross with ID 1031 was created.
==========
Truck Actross with ID 1032 was created.
==========
Truck Actross with ID 1033 was created.
==========
Truck Actross with ID 1034 was created.
==========
Truck Actross with ID 1035 was created.
==========
Truck Actross with ID 1036 was created.
==========
Truck Actross with ID 1037 was created.
==========
Truck Actross with ID 1038 was created.
==========
Truck Actross with ID 1039 was created.
==========
Truck Actross with ID 1040 was created.
==========
Package from Ivan Ivanov was accepted.
==========
Package from Ivan Ivanov was accepted.
==========
Delivery route 1 was created.
==========
Delivery route 2 was created.
==========
Delivery route 3 was created.
==========
Delivery route 4 was created.
==========
Truck 1001 assigned to route 1
==========
Package 1 was assigned to route 1.
==========
Found 1 routes:
Route ID: 3
  Status: pending
  Total distance: 2253km
  Route details: Adelaide -> Sydney -> Melbourne
  Packages: 0 with total weight 0kgs
  Truck assigned:
None
==========
Package: #1
  Expected delivery time: 2023-01-10 01:24:08.275862.
  Details:   Weight 500.0kgs
  Accepted in Alice springs: 2023/08/14, 21:04
  Status: delivered
  Customer: Ivan Ivanov - ivan@mail.au
***Customer Ivan Ivanov's feedback:
  "Thank you very much! You are the best logistics company :)"
==========
Route ID: 2
  Status: pending
  Total distance: 2906km
  Route details: Alice springs -> Adelaide -> Sydney
  Packages: 0 with total weight 0kgs
  Truck assigned:
None
==========
Route ID: 3
  Status: pending
  Total distance: 2253km
  Route details: Adelaide -> Sydney -> Melbourne
  Packages: 0 with total weight 0kgs
  Truck assigned:
None
==========
Truck ID: 1011.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
==========
Truck ID: 1001.
  Location: Sydney.
  Brand: Scania.
  Capacity: 41500.0kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 2023-01-08 16:00:00
From 2023-01-10 01:24:08.275862 to 9999-12-31 23:59:59.999999
```

## Test case #2 - valid input examples
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
## Test case #2 - expected output
```
Truck Scania with ID 1001 was created.
==========
Truck Scania with ID 1002 was created.
==========
Truck Scania with ID 1003 was created.
==========
Truck Scania with ID 1004 was created.
==========
Truck Scania with ID 1005 was created.
==========
Truck Scania with ID 1006 was created.
==========
Truck Scania with ID 1007 was created.
==========
Truck Scania with ID 1008 was created.
==========
Truck Scania with ID 1009 was created.
==========
Truck Scania with ID 1010 was created.
==========
Truck Man with ID 1011 was created.
==========
Truck Man with ID 1012 was created.
==========
Truck Man with ID 1013 was created.
==========
Truck Man with ID 1014 was created.
==========
Truck Man with ID 1015 was created.
==========
Truck Man with ID 1016 was created.
==========
Truck Man with ID 1017 was created.
==========
Truck Man with ID 1018 was created.
==========
Truck Man with ID 1019 was created.
==========
Truck Man with ID 1020 was created.
==========
Truck Man with ID 1021 was created.
==========
Truck Man with ID 1022 was created.
==========
Truck Man with ID 1023 was created.
==========
Truck Man with ID 1024 was created.
==========
Truck Man with ID 1025 was created.
==========
Truck Actross with ID 1026 was created.
==========
Truck Actross with ID 1027 was created.
==========
Truck Actross with ID 1028 was created.
==========
Truck Actross with ID 1029 was created.
==========
Truck Actross with ID 1030 was created.
==========
Truck Actross with ID 1031 was created.
==========
Truck Actross with ID 1032 was created.
==========
Truck Actross with ID 1033 was created.
==========
Truck Actross with ID 1034 was created.
==========
Truck Actross with ID 1035 was created.
==========
Truck Actross with ID 1036 was created.
==========
Truck Actross with ID 1037 was created.
==========
Truck Actross with ID 1038 was created.
==========
Truck Actross with ID 1039 was created.
==========
Truck Actross with ID 1040 was created.
==========
Package from Ivan Ivanov was accepted.
==========
Package from Ivan Ivanov was accepted.
==========
Package from Ivan Ivanov was accepted.
==========
Package from Petar Ivanov was accepted.
==========
Package from Ivan Ivanov was accepted.
==========
Delivery route 1 was created.
==========
Truck 1011 assigned to route 1
==========
You don't have permission
==========
Sydney has packages with total weight 200.5kg.
Melbourne has packages with total weight 0kg.
Adelaide has packages with total weight 500.3kg.
Alice springs has packages with total weight 800.5kg.
Brisbane has packages with total weight 0kg.
Darwin has packages with total weight 300.5kg.
Perth has packages with total weight 0kg.
==========
Total packages waiting to be assigned: 5.
 - Alice springs: 2 package/s
 - Adelaide: 1 package/s
 - Darwin: 1 package/s
 - Sydney: 1 package/s
==========
Truck ID: 1001.
  Location: Sydney.
  Brand: Scania.
  Capacity: 42000kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1002.
  Location: Sydney.
  Brand: Scania.
  Capacity: 42000kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1003.
  Location: Sydney.
  Brand: Scania.
  Capacity: 42000kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1004.
  Location: Sydney.
  Brand: Scania.
  Capacity: 42000kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1005.
  Location: Sydney.
  Brand: Scania.
  Capacity: 42000kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1006.
  Location: Sydney.
  Brand: Scania.
  Capacity: 42000kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1007.
  Location: Sydney.
  Brand: Scania.
  Capacity: 42000kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1008.
  Location: Sydney.
  Brand: Scania.
  Capacity: 42000kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1009.
  Location: Sydney.
  Brand: Scania.
  Capacity: 42000kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1010.
  Location: Sydney.
  Brand: Scania.
  Capacity: 42000kg.
  Range: 8000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1011.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 2024-01-08 16:00:00
From 2024-01-10 01:24:08.275862 to 9999-12-31 23:59:59.999999
Truck ID: 1012.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1013.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1014.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1015.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1016.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1017.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1018.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1019.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1020.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1021.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1022.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1023.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1024.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1025.
  Location: Sydney.
  Brand: Man.
  Capacity: 37000kg.
  Range: 10000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1026.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1027.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1028.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1029.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1030.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1031.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1032.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1033.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1034.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1035.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1036.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1037.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1038.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1039.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
Truck ID: 1040.
  Location: Sydney.
  Brand: Actross.
  Capacity: 26000kg.
  Range: 13000km.
  Status: free.
  Availability:
From 0001-01-01 00:00:00 to 9999-12-31 23:59:59.999999
==========
Sydney - Melbourne -> 877km; approx. travel time: 10hours and 4 minutes.
```

## Invalid input examples
```
createpackage Alice Springs Adelaide 500 Ivan_Ivanov-ivan@mail.au              -> no commas between the values
createpackage, 500, Alice Springs, Adelaide, Ivan_Ivanov-ivan@mail.au          -> invalid place for package's weight
createpackage, Alice Springs, Adelaide, 500, Ivan_Ivanov-ivanail.au            -> invalid email address - no '@' symbol
createpack, Alice Springs, Adelaide, 500, Ivan_Ivanov-ivan@ail.au              -> invalid command name
createpackage, Alice Springs, Adelaide, 500, I_Ivanov-ivan@ail.au              -> invalid customer first name
createpackage, Alice Springs, Adelaide, 500, Ivan_Ivanov-iv@l.au               -> invalid email - too short


```
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
```