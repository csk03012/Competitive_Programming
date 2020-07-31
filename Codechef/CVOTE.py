n, m = map(int, input().split())

countries = []
mix = dict()
players = []
for i in range(n):
    player, desh = input().split()
    if desh not in countries:
        countries.append(desh)
        mix[player] = desh
        players.append(player)
    else:
        mix[player] = desh
        players.append(player)
countries = {ele: 0 for ele in sorted(countries)}
players = {ele: 0 for ele in sorted(players)}

for i in range(m):
    player = input()
    players[player] += 1
    countries[mix[player]] += 1

max_players = max(players.values())
max_countries = max(countries.values())

print(list(countries.keys())[list(countries.values()).index(max_countries)])
print(list(players.keys())[list(players.values()).index(max_players)])

