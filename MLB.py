import random
import string


class Team_Stats:
    def __init__(self, St):
        St += ".txt"
        self.file = open(St, "r")

    def Roster(self):

        Team = []

        A = self.file

        for line in A:
            line = line.split("\t")
            Team.append(line)

        return Team


class Player:
    def __init__(self, P):
        self.P = P

    def Stats(self):
        P = self.P

        if P[1] in ["SP", "RP", "CL"]:

            player = {"Rk": P[0], "Pos": P[1], "Name": P[2], "Age": P[3], "W": P[4], "L": P[5], "W-L%": P[6], "ERA": P[7], "G": P[8], "GS": P[9], "GF": P[10], "CG": P[11], "SHO": P[12], "SV": P[13], "IP": P[14], "H": P[15], "R": P[16], "ER": P[17], "HR": P[18], "BB": P[19], "IBB": P[20], "SO": P[21], "HBP": P[22], "BK": P[23], "WP": P[24], "BF": P[25], "ERA+": P[26], "FIP": P[27], "WHIP": P[28], "H9": P[29], "HR9": P[30], "BB9": P[31], "SO9": P[32], "SO/W": P[33]}
        else:
            # print(P[1])
            player = {"Rk": P[0], "Pos": P[1], "Name": P[2], "Age": P[3], "G": P[4], "PA": P[5], "AB": P[6], "R": P[7], "H": P[8], "2B": P[9], "3B": P[10], "HR": P[11], "RBI": P[12], "SB": P[13], "CS": P[14], "BB": P[15], "SO": P[16], "BA": P[17], "OBP": P[18], "SLG": P[19], "OPS": P[20], "OPS+": P[21], "TB": P[22], "GDP": P[23], "HBP": P[24], "SH": P[25], "SF": P[26], "IBB": P[27]}

        for stat in player:
            try:
                if '.' in player[stat]:
                    player[stat] = float(player[stat])
                else:
                    player[stat] = int(player[stat])
            except ValueError:
                pass

        if player['Name'][-1] not in string.ascii_letters:
            player['Name'] = player['Name'][:-1]

        return player


class Team:
    def __init__(self, team_name):
        Roster = Team_Stats(team_name).Roster()

        Player_1 = Player(Roster[3]).Stats()
        Player_2 = Player(Roster[4]).Stats()
        Player_3 = Player(Roster[5]).Stats()
        Player_4 = Player(Roster[6]).Stats()
        Player_5 = Player(Roster[7]).Stats()
        Player_6 = Player(Roster[8]).Stats()
        Player_7 = Player(Roster[9]).Stats()
        Player_8 = Player(Roster[10]).Stats()
        Player_9 = Player(Roster[11]).Stats()
        Player_10 = Player(Roster[12]).Stats()
        Player_11 = Player(Roster[13]).Stats()
        Player_12 = Player(Roster[14]).Stats()
        Player_13 = Player(Roster[15]).Stats()
        Player_14 = Player(Roster[16]).Stats()
        Player_15 = Player(Roster[17]).Stats()

        Player_16 = Player(Roster[21]).Stats()
        Player_17 = Player(Roster[22]).Stats()
        Player_18 = Player(Roster[23]).Stats()
        Player_19 = Player(Roster[24]).Stats()
        Player_20 = Player(Roster[25]).Stats()
        Player_21 = Player(Roster[26]).Stats()
        Player_22 = Player(Roster[27]).Stats()
        Player_23 = Player(Roster[28]).Stats()
        Player_24 = Player(Roster[29]).Stats()
        Player_25 = Player(Roster[30]).Stats()
        Player_26 = Player(Roster[31]).Stats()
        Player_27 = Player(Roster[32]).Stats()
        Player_28 = Player(Roster[33]).Stats()
        Player_29 = Player(Roster[34]).Stats()
        Player_30 = Player(Roster[35]).Stats()

        self.B = [Player_1, Player_2, Player_3, Player_4, Player_5, Player_6, Player_7, Player_8, Player_9, Player_10, Player_11, Player_12, Player_13, Player_14, Player_15]

        self.P = [Player_16, Player_17, Player_18, Player_19, Player_20, Player_21, Player_22, Player_23, Player_24, Player_25, Player_26, Player_27, Player_26, Player_27, Player_28, Player_29, Player_30]

        self.R = {"B": self.B, "P": self.P}

    def Roster(self):
        return self.R


class Game:
    def __init__(self, team_nameA, team_nameB):
        self.Team_A = Team(team_nameA).Roster()
        self.Team_B = Team(team_nameB).Roster()

        self.B_A = self.Team_A['B']
        self.B_B = self.Team_B['B']
        self.P_A = self.Team_A['P']
        self.P_B = self.Team_B['P']

    def Out(self):
        R = random.randrange(100)
        Dict = {"FB": 20, "LO": 20, "PO": 20, "SO": 20, "GB": 20}

        tracker = 0
        for out in Dict:
            tracker += Dict[out]
            # print("{} : {}  {}".format(out, tracker, R)) # Test
            if R < tracker:
                return out

    def Base_Advance(self, H, Bases):

        Dict = {"1B": 1, "2B": 2, "3B": 3, "HR": 4}

        cheak = True
        cheak2 = True
        cheak3 = True

        B = [0, 0, 0]
        B_i = [0, 0, 0]

        if H in ["BB", "IBB", "HBP", 'B', '']:
            for i in range(len(Bases[:-1])):
                if Bases[i] == 1:
                    B[0] += 1
                    B_i[0] = i
                elif Bases[i] == 2:
                    B[1] += 1
                    B_i[1] = i
                elif Bases[i] == 3:
                    B[2] += 1
                    B_i[2] = i

            if B[0] == 1 and B[1] == 1 and B[2] == 1:
                Bases[-1] += 1

            elif B[0] == 1 and B[1] == 1:
                Bases[B_i[0]] += 1
                Bases[B_i[1]] += 1
                for i in range(len(Bases[:-1])):
                    if Bases[i] == 0:
                        Bases[i] += 1

            elif B[0] == 1:
                Bases[B_i[0]] += 1
                for i in range(len(Bases[:-1])):
                    if Bases[i] == 0 and cheak2:
                        Bases[i] += 1
                        cheak2 = False

            elif B[0] == 0:
                for i in range(len(Bases[:-1])):
                    if Bases[i] == 0 and cheak3:
                        Bases[i] += 1
                        cheak3 = False

        elif H in ["Out"]:
            pass

        else:

            for i in range(len(Bases[:-1])):
                if Bases[i] > 0:
                    Bases[i] += Dict[H]
                if Bases[i] > 3:
                    Bases[i] = 0
                    Bases[-1] += 1
                if Bases[i] == 0 and cheak:
                    Bases[i] += Dict[H]
                    if Bases[i] > 3:
                        Bases[i] = 0
                        Bases[-1] += 1
                    cheak = False

        return Bases

    def Placement(self, H):

        Chance = {"1B": [20, 10, 70], "2B": [40, 40, 20], "3B": [28, 70, 2], "HR": [0, 100, 0]}
        P = {'1': 'LD', '2': 'FB', '3': 'GB'}

        Dict = {"FB": 20, "LO": 20, "PO": 20, "SO": 20, "GB": 20}

        R = random.randrange(100)
        if H == "Out":
            tracker = 0
            for out in Dict:
                tracker += Dict[out]
                # print("{} : {}  {}".format(out, tracker, R)) # Test
                if R < tracker:
                    return out

        if H in ['BB', 'IBB', 'HBP']:
            return '-'

        else:
            count = 0
            Tracker = 0
            for i in Chance[H]:
                count += 1
                Tracker += i
                # print("{} : {}  {}".format(P[str(count)], Tracker, R))    TEST
                if R < Tracker:
                    return P[str(count)]

    def On_Base(self, B):
        Tracker = 0
        T_B = int(B['H'] + B['BB'] + B['HBP'] + B['IBB'])
        B1 = B['H'] - B['3B'] - B['2B'] - B['HR']
        Base = {"1B": B1, "2B": B['2B'], "3B": B['3B'],
                "BB": B['BB'], "IBB": B['IBB'], "HR": B['HR'], 'HBP': B['HBP']}

        R = random.randrange(T_B)

        for i in Base:
            Tracker += Base[i]
            # print("{} : {}  {}".format(i, Tracker, R))  # TEST
            if R <= Tracker:
                Hit = i
                return Hit

    def At_Bat(self, B, P, Bases):
        B_OBP = B["OBP"]
        P_OBP = (P["H"] + P["BB"] + P['HBP'] + 8) / P["BF"]

        F_OBP = B_OBP - (.333 - P_OBP)

        # A = B['Name'].split(" ")
        # C = P['Name'].split(" ")

        # A = A[0][0] + A[1][0]
        # C = C[0][0] + C[1][0]

        # print("B: {} P: {} OBP: {} OOBP: {:.2f} AOBP: {:.2f}".format(A, C, B_OBP, P_OBP, F_OBP))

        IP_or_O = int(F_OBP * 1000)

        R = random.randrange(1000)

        if R < IP_or_O:
            Hit = self.On_Base(B)

        else:
            Hit = "Out"

        Bases = self.Base_Advance(Hit, Bases)
        Placement = self.Placement(Hit)

        return {'Hit': Hit, 'Placement': Placement, 'Bases': Bases}

    def game(self, B, P):

        team_A = self.Team_A
        team_B = self.Team_B

        Bases_A = [0, 0, 0, 0]
        Bases_B = [0, 0, 0, 0]

        lineup_A = 0
        lineup_B = 0

        for Inning in range(1, 10):
            print("--------------------------------------------------------------")
            print("INNING {}".format(Inning))
            print("--------------------------------------------------------------")

            Bases_A[0] = 0
            Bases_A[1] = 0
            Bases_A[2] = 0

            Bases_B[0] = 0
            Bases_B[1] = 0
            Bases_B[2] = 0

            for i in range(2):
                out = 0
                if i == 0:
                    Batter = team_A['B']
                    Pitcher = team_B['P'][0]
                    lineup = lineup_A
                    Bases = Bases_A

                elif i == 1:
                    print("--------------------------------------------------------------")
                    Batter = team_B['B']
                    Pitcher = team_A['P'][0]
                    lineup = lineup_B
                    Bases = Bases_B

                while out < 3:
                    AB = self.At_Bat(Batter[lineup], Pitcher, Bases)
                    lineup += 1
                    H = AB['Hit']
                    P = AB['Placement']
                    B = AB['Bases']
                    N = Batter[lineup]['Name']
                    print("{}\t{}\t{}\t{}\t{}".format(N, H, P, B, B[-1]))
                    Bases = B
                    if H == "Out":
                        out += 1

        print("--------------------------------------------------------------\n")
        twins_score = Bases_A[3]
        yanks_score = Bases_B[3]
        if(twins_score > yanks_score):
          print("Twins win {} to {}".format(twins_score, yanks_score))
        elif(twins_score == yanks_score):
          print("Twins win {} to {}".format(twins_score + 1, yanks_score))
        else:
          print("Yankees win {} to {}".format(yanks_score, twins_score))
        return

        # game = False
        # if cheak == 0:
        #     print("--------------------------------------------------------------")
        #     print("INNING {}".format(Inning))
        #     print("--------------------------------------------------------------")
        #     cheak = 1
        # elif cheak == 1:
        #     print("--------------------------------------------------------------")
        #     cheak = 0
        # out = 0
        # while out < 3 and Inning <= 9:
        #     AB = self.At_Bat(B, P)
        #     Index = AB.find("\t") + 4
        #     Bases = self.Base_Advance(AB[Index:], Bases)
        #     print("{}\t{}".format(AB, Bases))
        #     if AB[-3:] == "Out":
        #         out += 1

        return

    def GET(self):
        return {'A': self.Team_A, 'B': self.Team_B}


Twins_vs_Yankees_09 = Game("Twins_09", "Yankees_09")

Batter = Twins_vs_Yankees_09.GET()['A']['B'][2]
Pitcher = Twins_vs_Yankees_09.GET()['B']['P'][5]

Twins_vs_Yankees_09.game(Batter, Pitcher)

# O = 0
# IP = 0

# for i in range(10000):

#     A = Twins_vs_Yankees_09.At_Bat(Batter, Pitcher)
#     if A[-3:] == "Out":
#         O += 1
#     else:
#         IP += 1

# Avg = IP / (O + IP)
# print("O: {}, IP: {}, Avg: {}".format(O, IP, Avg))


# print(Twins_vs_Yankees_09.On_Base(Batter))
# print(Twins_vs_Yankees_09.Placement("2B"))
# print(Twins_vs_Yankees_09.Base_Advance("BB", [1, 2, 3, 0]))
# print(Twins_vs_Yankees_09.Out())
