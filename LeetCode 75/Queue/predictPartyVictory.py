def predictPartyVictory(senate):
    senate = list(senate)

    while len(senate) > 1:
        if not senate[1] == senate[0]:
            senate.pop(1)
            senate.append(senate[0])
            senate.pop(0)
        else:
            senate.append(senate[0])
            senate.pop(0)

        votes = "".join(senate)
        if votes.count("D") == len(senate) or votes.count("R") == len(senate):
            break

    return "Radiant" if senate[0] == "R" else "Dire"

print(predictPartyVictory("D"))