import json
import os
from collections import Counter

april = './april.json'
thismonth = []

if(not os.path.exists(april)):
    result = []
    with open('./all.json', 'r') as fp:
        result = json.load(fp)

    # only this month
    thismonth = list(filter(lambda x: x["global_game"]["match_start"] > "2019-04-01T00:00:00Z", result))
    # only standard
    thismonth = list(filter(lambda x: x["global_game"]["game_type"] == 2, thismonth))

    print(f'replays in this month is {len(thismonth)}')

    with open(april, 'w') as fp:
        json.dump(thismonth, fp)
else:
    with open(april, 'r') as fp:
        thismonth = json.load(fp)

cc = map(lambda x: x["global_game"]["ladder_season"], thismonth)
c = Counter(cc)
print(c)

cc = map(lambda x: x["friendly_player"]["hero_class_name"], thismonth)
c = Counter(cc)
print(c)

cc = map(lambda x: 'Won' if x["friendly_player"]["final_state"] == 4 else ('Lose' if x["friendly_player"]["final_state"] == 5 else 'Draw'), thismonth)
c = Counter(cc)
print(c)

print("rank")
cc = map(lambda x: x["friendly_player"]["rank"], thismonth)
c = Counter(cc)
print(c)

print("is first?")
cc = map(lambda x: x["friendly_player"]["is_first"], thismonth)
c = Counter(cc)
print(c)

print("opposing_player")
cc = map(lambda x: x["opposing_player"]["rank"], thismonth)
c = Counter(cc)
print(c)

cc = map(lambda x: x["opposing_player"]["hero_class_name"], thismonth)
c = Counter(cc)
print(c)

print("rank")
cc = map(lambda x: x["friendly_player"]["is_first"], thismonth)
c = Counter(cc)
print(c)


print("For rank 2 and above==")

rank2above = list(filter(lambda x: x["friendly_player"]["rank"] <= 2, thismonth))

print("opposing_player")
cc = map(lambda x: (x["opposing_player"]["hero_class_name"], 'won' if x["friendly_player"]["final_state"] == 4 else 'Lose'), rank2above)
c = Counter(cc)
print(c)

cc = map(lambda x: x["opposing_player"]["hero_class_name"], rank2above)
c = Counter(cc)
print(c)

print("For rogue==")

rogue = list(filter(lambda x: x["opposing_player"]["hero_class_name"] == 'ROGUE', thismonth))

print("opposing_player")
cc = map(lambda x: (x["friendly_player"]["is_first"],'won' if x["friendly_player"]["final_state"] == 4 else 'Lose'), rogue)
c = Counter(cc)
print(c)

print("For rogue above rank2==")

rogue = list(filter(lambda x: x["opposing_player"]["hero_class_name"] == 'ROGUE', rank2above))

print("opposing_player")
cc = map(lambda x: (x["friendly_player"]["is_first"],'won' if x["friendly_player"]["final_state"] == 4 else 'Lose'), rogue)
c = Counter(cc)
print(c)

cc = map(lambda x: (x["opposing_player"]["hero_class_name"], 'won' if x["friendly_player"]["final_state"] == 4 else 'Lose'), rogue)
c = Counter(cc)
print(c)

print("For warrior above rank2==")

warrior = list(filter(lambda x: x["opposing_player"]["hero_class_name"] == 'WARRIOR', rank2above))

print("opposing_player")
cc = map(lambda x: (x["opposing_player"]["hero_class_name"], 'won' if x["friendly_player"]["final_state"] == 4 else 'Lose'), warrior)
c = Counter(cc)
print(c)
