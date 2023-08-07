
class Cities:
    SYDNEY = 'Sydney'
    MELBOURNE = 'Melbourne'
    ADELAIDE = 'Adelaide'
    ALICE_SPRINGS = 'Alice Springs'
    BRISBANE = 'Brisbane'
    DARWIN = 'Darwin'
    PERTH = 'Perth'

    cities = [SYDNEY, MELBOURNE, ADELAIDE, ALICE_SPRINGS, BRISBANE, DARWIN, PERTH]
    DISTANCES = {
            SYDNEY: [],
            MELBOURNE: [],
            ADELAIDE: [], 
            ALICE_SPRINGS: [], 
            BRISBANE: [], 
            DARWIN: [], 
            PERTH: []
            }


    dst = [
        [0, 877, 1376, 2762, 909, 3935, 4016],
        [877, 0, 725, 2255, 1765, 3752, 3509],
        [1376, 725, 0, 1530, 1927, 3027, 2785],
        [2762, 2255, 1530, 0, 2993, 1497, 2481],
        [909, 1765, 1927, 2993, 0, 3426, 4311],
        [3935, 3752, 3027, 1497, 3426, 0, 4025],
        [4016, 3509, 2785, 2481, 4311, 4025, 0]
        ]

    for city in range(len(cities)):
        for lst in dst[city:]:
            for dist in range(len(lst)):
                if not lst[dist] == 0:
                    DISTANCES[cities[city]].append([cities[dist], dst[dst.index(lst)][dist]])
            break
    
    










# # info about the cities and the distances between them
# def distances():

#     cities = ['Sydney', 'Melbourne', 'Adelaide', 'Alice Springs', 'Brisbane', 'Darwin','Perth']

#     distances = {
#         'Sydney': [],
#         'Melbourne': [],
#         'Adelaide': [], 
#         'Alice Springs': [], 
#         'Brisbane': [], 
#         'Darwin': [], 
#         'Perth': []
#         }

#     dst = [
#         [0, 877, 1376, 2762, 909, 3935, 4016],
#         [877, 0, 725, 2255, 1765, 3752, 3509],
#         [1376, 725, 0, 1530, 1927, 3027, 2785],
#         [2762, 2255, 1530, 0, 2993, 1497, 2481],
#         [909, 1765, 1927, 2993, 0, 3426, 4311],
#         [3935, 3752, 3027, 1497, 3426, 0, 4025],
#         [4016, 3509, 2785, 2481, 4311, 4025, 0]
#     ]

#     for city in range(len(cities)):
#         for lst in dst[city:]:
#             for dist in range(len(lst)):
#                 if not lst[dist] == 0:
#                     distances[cities[city]].append([cities[dist], str(dst[dst.index(lst)][dist])])
#             break
    
#     return distances


# def calculate_distance(lst):
#     total = 0
#     for city in lst[:-1]:
#         for current, next_city in distances().items():
#             if current == city:
#                 city_idx = lst.index(city)
#                 for i in range(len(next_city)):
#                     if lst[city_idx+1] == next_city[i][0]:
#                         total += int(next_city[i][1])
#                         break
#                 break
            
#     return total

# route = ['Alice Springs', 'Adelaide', 'Melbourne', 'Sydney', 'Brisbane']

# result = calculate_distance(route)

# print(result)