from collections import deque

def predictPartyVictory(senate):
    r = deque()
    d = deque()

    for i in range(len(senate)):
        el = senate[i]
        if el == "R":
            r.append(i)
        else:
            d.append(i)
    
    while len(r) > 0 and len(d) > 0:
        rCur = r.popleft()
        dCur = d.popleft()

        if rCur < dCur:
            r.append(rCur + len(senate))
        else:
            d.append(dCur + len(senate))

    return "Radiant" if r else "Dire"

print(predictPartyVictory("DDRRR"))

# DDRRR
# DRR