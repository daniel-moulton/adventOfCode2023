from pprint import pprint

def calcAccepted(rating, workflows, workflow):
    # print("Start of calcAccepted, worklow is ", workflow)
    x = rating['x']
    m = rating['m']
    a = rating['a']
    s = rating['s']

    # print(workflow)

    for key, value in workflow.items():
        # print(key, value)
        if key == 'A':
            return True
        elif key == 'R':
            return False
        elif value is None:
            return calcAccepted(rating, workflows, workflows[key])
        if eval(key):
            if (value=='A'):
                return True
            elif (value == 'R'):
                return False
            else:
                return calcAccepted(rating, workflows, workflows[value])
    return False





with open("Inputs/day19.txt", "r") as file:
    workflows = {}
    line = file.readline()
    total = 0
    while line.strip():
        workflowName, rest = line.strip().split('{')
        rest = rest[:-1]
        rules = rest.split(',')
        ruleDict = {}
        for rule in rules:
            if ':' in rule:
                rule2, destination = rule.strip().split(":")
                ruleDict[rule2.strip()] = destination.strip()
            else:
                ruleDict[rule.strip()] = None
        workflows[workflowName] = ruleDict
        line = file.readline()
        # print(workflows[workflowName])

    ratings = []
    for line in file.readlines():
        if line == '\n':
            break
        else:
            rating = {}
            x,m,a,s = line.strip().split(',')
            s = s[:-1]
            rating['x'] = int(x.strip().split('=')[1])
            rating['m'] = int(m.strip().split('=')[1])
            rating['a'] = int(a.strip().split('=')[1])
            rating['s'] = int(s.strip().split('=')[1])
            ratings.append(rating)
    
    for rating in ratings:
        if (calcAccepted(rating, workflows, workflows["in"])):
            total += rating['x'] + rating['m'] + rating['a'] + rating['s']
    print(total)
