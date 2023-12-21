from pprint import pprint

class Card:
    def __init__(self, hand, bet):
        self.hand = hand
        self.jokerHand = hand
        self.bet = bet
        self.handType = ""
        self.handInt = int(hand, 16)
    
    def __str__(self):
        return "Bet: " + str(self.bet) + "\tHand: " + str(self.hand) + "\tHand Type: " + str(self.handType) + "\tHand Int: " + str(self.handInt)
    
    def getHandType(self, part2=False):
        '''
        Hand Types:
        1: High Card
        2: One Pair
        3: Two Pair
        4: Three of a Kind
        5: Full House
        6: Four of a Kind
        7: Five of a Kind
        '''

        if (part2):
            self.hand = self.jokerHand

        # If only one denomination
        if (len(set(self.hand)) == 1):
            self.handType = 7
        # If two denominations, either four of a kind or full house
        elif (len(set(self.hand)) == 2):
            # If four of a kind
            if (self.hand.count(self.hand[0]) == 4 or self.hand.count(self.hand[0]) == 1):
                self.handType = 6
            # Else must be full house
            else:
                self.handType = 5
        # If three denominations, either three of a kind or two pair
        elif (len(set(self.hand)) == 3):
            # If three of a kind
            if (self.hand.count(self.hand[0]) == 3 or self.hand.count(self.hand[1]) == 3 or self.hand.count(self.hand[2]) == 3):
                self.handType = 4
            # Else must be two pair
            else:
                self.handType = 3
        # If four denominations, must be one pair
        elif (len(set(self.hand)) == 4):
            self.handType = 2
        # Else must be high card
        else:
            self.handType = 1

    def filterJokers(self):
        # Get the most frequent denomination by looping through the hand and counting the number of times each denomination appears
        mostFrequent = ""
        mostFrequentCount = 0
        for i in range(len(self.hand)):
            if (self.hand.count(self.hand[i]) > mostFrequentCount and self.hand[i] != "1"):
                mostFrequentCount = self.hand.count(self.hand[i])
                mostFrequent = self.hand[i]
            # Case where there are two denominations that appear the same number of times, we pick the larger number
            if (self.hand.count(self.hand[i]) == mostFrequentCount and self.hand[i] != "1"):
                if (int(self.hand[i], 16) > int(mostFrequent, 16)):
                    mostFrequentCount = self.hand.count(self.hand[i])
                    mostFrequent = self.hand[i]

        # Get the locations of all 1s
        for i in range(len(self.hand)):
            if (self.hand[i] == "1"):
                self.jokerHand = self.jokerHand[:i] + mostFrequent + self.jokerHand[i+1:]

        # Set return to -1
        self.handType = -1
        return


with open("Inputs/day7.txt", 'r') as f:
    lines = f.read().split("\n")
    cards = []
    for line in lines:
        parts = line.split(" ")
        # Replace any T with A, J with B, Q with C, K with D and A with E
        parts[0] = parts[0].replace("A", "E")
        parts[0] = parts[0].replace("K", "D")
        parts[0] = parts[0].replace("Q", "C")
        parts[0] = parts[0].replace("J", "B")
        parts[0] = parts[0].replace("T", "A")
        x = Card(parts[0], parts[1])
        x.getHandType()
        cards.append(x)
    # Sort the cards by hand type, then by largest handInt
    cards.sort(key=lambda x: x.handInt, reverse=False)
    cards.sort(key=lambda x: x.handType, reverse=False)

    total=0
    # For each card, add to total the bet * the card's position in the list, starting at 1
    for i in range(len(cards)):
        total+=int(cards[i].bet)*(i+1)
    
    print(total)


with open("Inputs/day7.txt", 'r') as f:
    lines = f.read().split("\n")
    # Create a list of Card objects
    cards = []
    for line in lines:
        parts = line.split(" ")

        # Replace any T with A, J with B, Q with C, K with D and A with E so can treat hands as hex values
        parts[0] = parts[0].replace("A", "E")
        parts[0] = parts[0].replace("K", "D")
        parts[0] = parts[0].replace("Q", "C")
        parts[0] = parts[0].replace("J", "1")
        parts[0] = parts[0].replace("T", "A")
        x = Card(parts[0], parts[1])
        x.filterJokers()
        if (x.handType == -1):
            x.getHandType(True)
        cards.append(x)
    # Sort the cards by hand type, then by largest handInt
    cards.sort(key=lambda x: x.handInt, reverse=False)
    cards.sort(key=lambda x: x.handType, reverse=False)

    total=0
    # For each card, add to total the bet * the card's position in the list, starting at 1
    for i in range(len(cards)):
        total+=int(cards[i].bet)*(i+1)

    for i in range(len(cards)):
        print(cards[i])
    print(total)
