import re


def dfs(bp, maxspend, cache, time, bots, amt):
    global recurs_count
    #if time == 0:
    #    print(bots)
    #    return amt[3]
    recurs_count += 1
    
    key = tuple([time, *bots, *amt])
    if key in cache:
        return cache[key]
    
    maxval = amt[3] + bots[3] * time
    
    for btype, recipe in enumerate(bp):
        if btype != 3 and bots[btype] >= maxspend[btype]:
            continue
    
        wait = 0
        for ramt, rtype in recipe:
            if bots[rtype] == 0:
                break
            wait = max(wait, -(-(ramt - amt[rtype]) // bots[rtype]))
        else:
            remtime = time - wait - 1
            if remtime <= 0:
                continue
            bots_ = bots[:]
            amt_ = [x + y * (wait + 1) for x, y in zip(amt, bots)]
            for ramt, rtype in recipe:
                amt_[rtype] -= ramt
            bots_[btype] += 1
            #print(bots_, wait)
            for i in range(3):
                amt_[i] = min(amt_[i], maxspend[i] * remtime)
            maxval = max(maxval, dfs(bp, maxspend, cache, remtime, bots_, amt_))
    
    cache[key] = maxval
    return maxval

total = 0
total_a = []

for i, line in enumerate(open(0)):
    bp = []
    maxspend = [0, 0, 0]
    for section in line.split(": ")[1].split(". "):
        recipe = []
        for x, y in re.findall(r"(\d+) (\w+)", section):
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            recipe.append((x, y))
            maxspend[y] = max(maxspend[y], x)
        bp.append(recipe)
    recurs_count = 0
    v = dfs(bp, maxspend, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])
    total_a.append(v) #print(recurs_count)
    total += (i + 1) * v

print(total)
print(total_a)
