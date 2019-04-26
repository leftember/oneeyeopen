import json
result = []
index = 0
while(True):
    try:
        with open(f'./r{index}.json', 'r') as fp:
            r = json.load(fp)
            result.extend(r)
        index = index + 1
    except IOError:
        pass
        break

with open('./all.json', 'w') as fp:
    json.dump(result, fp)
