from pprint import pprint

'''
Time:        53     71     78     80
Distance:   275   1181   1215   


Race Length: 7 seconds
Time Held, Time Traveled, Distance Traveled
0          7              0
1          6              6
2          5              10
3          4              12
4          3              12
5          2              10
6          1              6
7          0              0

Distance Travelled = Time Held * Time Traveled
Time Traveled = Race Length - Time Held

Distance Travelled = Time Held * (Race Length - Time Held)
'''
with open("Inputs/day6.txt", 'r') as f:
    lines = f.read().split("\n")
    times = lines[0].split()
    times.pop(0)
    distances = lines[1].split()
    distances.pop(0)

    counters = [0] * len(times)
    for i in range(len(times)):
        raceLength = int(times[i])
        for j in range(1, int(times[i])-1):
            timeHeld = j
            timeTraveled = raceLength - timeHeld
            distanceTraveled = timeHeld * timeTraveled
            record = distances[i]
            if (distanceTraveled > int(record)):
                counters[i]+=1
    score = 1
    for i in range(len(counters)):
        score*=counters[i]
    print(score)

with open("Inputs/day6.txt", 'r') as f:
    lines = f.read().split("\n")
    times = lines[0].split()
    times.pop(0)
    times=int(''.join(times))
    distances = lines[1].split()
    distances.pop(0)
    distances=int(''.join(distances))
    pprint(times)
    pprint(distances)

    counter=0
    max=0
    print("YO" + str(times-1))
    for i in range(1, times-1):
        timeHeld = i
        timeTraveled = times - timeHeld
        distanceTraveled = timeHeld * timeTraveled
        record = distances
        if (distanceTraveled > int(record)):
            counter+=1
    print(counter)