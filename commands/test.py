towns = {
    "SYDNEY": [15, 20, 30],
    "MELBOURNE": [2],
    "ADELAIDE": [3],
    "ALICE_SPRINGS": [4],
    "BRISBANE": [5],
    "DARWIN": [6],
    "PERTH": [],
}

output = []

for key, value in towns.items():
    output.append(f"{key} has packs with weight {sum(value)}kg.")

print("\n".join(output))
