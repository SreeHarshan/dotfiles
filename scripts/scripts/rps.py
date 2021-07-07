import random
class Brain:

    def __init__(self,weight):
        self.history = []
        self.relation = [
            #Enemy previously put
            [#Enemy previous result
                [1000,1000,1000],#My current put
                [1000,1000,1000],
                [1000,1000,1000]
            ],
            [
                [1000, 1000, 1000],
                [1000, 1000, 1000],
                [1000, 1000, 1000]
            ],
            [
                [1000, 1000, 1000],
                [1000, 1000, 1000],
                [1000, 1000, 1000]
            ]


        ]
        self.name = ['rock','paper','scissor']
        self.weight = weight
        self.loses = 0

    def reset(self):
        self.relation = [
            # Enemy previously put
            [  # Enemy previous result
                [1000, 1000, 1000],  # My current put
                [1000, 1000, 1000],
                [1000, 1000, 1000]
            ],
            [
                [1000, 1000, 1000],
                [1000, 1000, 1000],
                [1000, 1000, 1000]
            ],
            [
                [1000, 1000, 1000],
                [1000, 1000, 1000],
                [1000, 1000, 1000]
            ]

        ]


def win(c1,c2):
    if c1 == 0:  #Rock
        if c2 == 0:#rock
            return 0
        elif c2 == 1:#Paper
            return -1
        else:#Scissor
            return 1
    elif c1 == 1:  #paper
        if c2 == 0:#rock
            return 1
        elif c2 == 1:#Paper
            return 0
        else:#Scissor
            return -1
    elif c1 == 2:  #Scissor
        if c2 == 0:#rock
            return -1
        elif c2 == 1:#Paper
            return 1
        else:#Scissor
            return 0

def max(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return l.index(max)

def Fight(b1,b2,c,keep):

    points = 0
    b1_prev_result = random.randint(0, 2)
    b1_prev_put = random.randint(0, 2)
    b2_prev_result = random.randint(0, 2)
    b2_prev_put = random.randint(0, 2)

    for i in range(c):

        b1put = max(b1.relation[b2_prev_put][b2_prev_result])

        b2put = max(b2.relation[b1_prev_put][b1_prev_result])

        w = win(b1put,b2put)

        #Brain to not put these in this circumstance
        if w == -1:#B1 lost,B2 won
            b1.relation[b2_prev_put][b2_prev_result][b1put] -= b1.weight * 2
            points += 1
        elif w == 0:#Draw
            b1.relation[b2_prev_put][b2_prev_result][b1put] -= b1.weight
            b2.relation[b1_prev_put][b1_prev_result][b2put] -= b2.weight
        else:#B1 won,B2 lost
            points -= 1
            b2.relation[b1_prev_put][b1_prev_result][b2put] -= b2.weight

        #Brain to put these next in this circumstance
        b2counter_to_put = b2put + 1
        if b2counter_to_put == 3:
            b2counter_to_put = 0
        b1.relation[b2_prev_put][b2_prev_result][b2counter_to_put] += b1.weight

        b1counter_to_put = b1put + 1
        if b1counter_to_put == 3:
            b1counter_to_put = 0
        b2.relation[b1_prev_put][b1_prev_result][b1counter_to_put] += b2.weight

        #Update previous result and puts
        b1_prev_result = w + 1
        b1_prev_put = b1put
        b2_prev_result = (-w) + 1
        b2_prev_put = b2put

    if keep:
        b1.reset()
        b2.reset()
    if points < 0:#b1 lost
        return b1
    else:#b1 won or draw
        return b2

def DetailedFight(b1,b2,c):

    points = 0
    b1_prev_result = random.randint(0,2)
    b1_prev_put = random.randint(0,2)
    b2_prev_result = random.randint(0,2)
    b2_prev_put = random.randint(0,2)

    for i in range(c):
        b1max = 0.000000000001
        for i in b1.relation[b2_prev_put][b2_prev_result]:
            if i > b1max:
                b1max = i

        b1put = b1.relation[b2_prev_put][b2_prev_result].index(b1max)

        b2max = 0
        for i in b2.relation[b1_prev_put][b1_prev_result]:
            if i > b2max:
                b2max = i
        b2put = b2.relation[b1_prev_put][b1_prev_result].index(b2max)

        print("Bot1:",b1.name[b1put])
        print("Bot2:", b1.name[b2put])

        w = win(b1put,b2put)

        #Brain to not put these in this circumstance
        if w == -1:#B1 lost,B2 won
            b1.relation[b2_prev_put][b2_prev_result][b1put] -= b1.weight * 2
            points += 1
            print("B2 won")
        elif w == 0:#Draw
            b1.relation[b2_prev_put][b2_prev_result][b1put] -= b1.weight
            b2.relation[b1_prev_put][b1_prev_result][b2put] -= b2.weight
            print("Draw")
        else:#B1 won,B2 lost
            points -= 1
            b2.relation[b1_prev_put][b1_prev_result][b2put] -= b2.weight
            print("B1 won")

        #Brain to put these next in this circumstance
        b2counter_to_put = b2put + 1
        if b2counter_to_put == 3:
            b2counter_to_put = 0
        b1.relation[b2_prev_put][b2_prev_result][b2counter_to_put] += b1.weight

        b1counter_to_put = b1put + 1
        if b1counter_to_put == 3:
            b1counter_to_put = 0
        b2.relation[b1_prev_put][b1_prev_result][b1counter_to_put] += b2.weight

        #Update previous result and puts
        b1_prev_result = w + 1
        b1_prev_put = b1put
        b2_prev_result = (-w) + 1
        b2_prev_put = b2put

        input()

    b1.reset()
    b2.reset()

    if points < 0:#b1 lost
        print("B2 won")
    else:#b1 won or draw
        print("B1 won")

def PlayerFight(c,b1):

    points = 0
    b2_prev_result = random.randint(0, 2)
    b2_prev_put = random.randint(0, 2)

    for i in range(c):
        b1max = b1.relation[b2_prev_put][b2_prev_result][0]
        for i in b1.relation[b2_prev_put][b2_prev_result]:
            if i > b1max:
                b1max = i

        b1put = b1.relation[b2_prev_put][b2_prev_result].index(b1max)

        b2put = int(input("Rock,Paper,Scissor:"))-1

        print("Player:", b1.name[b2put])
        print("Bot:",b1.name[b1put])

        w = win(b1put, b2put)

        # Brain to not put these in this circumstance
        if w == -1:  # B1 lost,B2 won
            b1.relation[b2_prev_put][b2_prev_result][b1put] -= b1.weight * 2
            points += 1
            print("Won")
        elif w == 0:  # Draw
            b1.relation[b2_prev_put][b2_prev_result][b1put] -= b1.weight
            print("Draw")

        else:  # B1 won,B2 lost
            points -= 1
            print("Lost")


        # Brain to put these next in this circumstance
        b2counter_to_put = b2put + 1
        if b2counter_to_put == 3:
            b2counter_to_put = 0
        b1.relation[b2_prev_put][b2_prev_result][b2counter_to_put] += b1.weight

        # Update previous result and puts
        b2_prev_result = (-w) + 1
        b2_prev_put = b2put

    b1.reset()
    print("You scored",points,"points")
    print("Bot scored", -points, "points")

Brains = []

b = Brain(1.5866666666666667)
b.relation = [[[1000.0, 1000.0, 1001.5866666666667], [998.4133333333335, 996.8266666666668, 998.4133333333335], [1000.0, 1000.0, 1003.1733333333334]], [[1000.0000000000001, 998.4133333333334, 1001.5866666666667], [1000.0000000000001, 1001.5866666666667, 1004.7600000000001], [998.4133333333334, 1003.1733333333335, 1000.0]], [[1000.0, 1000.0, 1001.5866666666667], [1001.5866666666667, 996.8266666666668, 1000.0], [1000.0, 1003.1733333333334, 1001.5866666666667]]]
Brains.append(b)

b = Brain(0.12571428571428572)
b.relation = [[[999.9999999999999, 999.8742857142856, 1000.1257142857143], [999.8742857142855, 999.8742857142854, 1000.2514285714283], [999.9999999999999, 1000.2514285714284, 1000.0]], [[999.8742857142856, 999.8742857142856, 1000.1257142857141], [999.8742857142857, 999.9999999999998, 999.8742857142855], [1000.1257142857141, 999.9999999999999, 1000.2514285714284]], [[999.8742857142856, 999.8742857142855, 999.8742857142856], [999.8742857142856, 999.8742857142856, 999.8742857142855], [1000.2514285714284, 1000.2514285714283, 1000.1257142857143]]]
Brains.append(b)

b = Brain(1.0766666666666667)
b.relation = [[[1001.0766666666668, 1000.0000000000002, 1000.0000000000001], [1001.0766666666669, 1002.1533333333335, 1000.0000000000002], [1001.0766666666667, 1002.1533333333336, 1002.1533333333334]], [[998.9233333333336, 1005.3833333333336, 1000.0000000000002], [1000.0000000000002, 1001.0766666666667, 1001.0766666666667], [1000.0000000000002, 1002.1533333333338, 1002.1533333333336]], [[998.9233333333335, 998.9233333333335, 1002.1533333333336], [1001.0766666666667, 1002.1533333333336, 998.9233333333335], [1000.0000000000002, 1000.0000000000003, 1000.0000000000002]]]
Brains.append(b)

b = Brain(4.867142857142857)
b.relation =[[[1004.8671428571429, 1004.8671428571429, 1009.7342857142858], [1004.8671428571429, 995.1328571428571, 1000.0], [1014.6014285714286, 1014.6014285714286, 1019.4685714285715]], [[1009.7342857142858, 1004.8671428571429, 1000.0], [995.1328571428571, 1000.0, 995.1328571428571], [1000.0, 1009.7342857142858, 1009.7342857142858]], [[1000.0, 1000.0, 1000.0], [1004.8671428571429, 1004.8671428571429, 1014.6014285714286], [1004.8671428571429, 1009.7342857142858, 1014.6014285714286]]]
Brains.append(b)

b = Brain(9.118)
b.relation =[[[990.8820000000004, 990.8820000000005, 1000.0000000000006], [1000.0000000000002, 1000.0000000000003, 1009.1180000000005], [1000.0000000000002, 1027.354, 990.8820000000002]], [[990.8820000000001, 1018.236, 1018.2360000000001], [990.8820000000002, 1000.0000000000001, 1027.3540000000003], [1000.0000000000002, 1009.1180000000002, 1009.1180000000003]], [[990.882, 981.7640000000002, 1000.0000000000001], [1000.0000000000001, 1000.0000000000001, 1018.2360000000001], [1000.0000000000007, 990.8820000000003, 1009.1180000000004]]]

#Fight(Brains[-1],b,5,True)
#DetailedFight(Brains[-1],b,5)
PlayerFight(10000,b)
#PlayerFight(10,Brains[0])
#PlayerFight(10,Brains[-1])

