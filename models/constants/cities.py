
class Cities:
    SYDNEY = 'Sydney'
    MELBOURNE = 'Melbourne'
    ADELAIDE = 'Adelaide'
    ALICE_SPRINGS = 'Alice springs'
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
