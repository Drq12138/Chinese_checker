import random, re, datetime


class Agent(object):
    def __init__(self, game):
        self.game = game

    def getAction(self, state):
        raise Exception("Not implemented yet")


class RandomAgent(Agent):
    def getAction(self, state):
        legal_actions = self.game.actions(state)
        self.action = random.choice(legal_actions)


class SimpleGreedyAgent(Agent):
    # a one-step-lookahead greedy agent that returns action with max vertical advance
    def getAction(self, state):
        legal_actions = self.game.actions(state)

        self.action = random.choice(legal_actions)

        player = self.game.player(state)
        if player == 1:
            max_vertical_advance_one_step = max([action[0][0] - action[1][0] for action in legal_actions])
            max_actions = [action for action in legal_actions if
                           action[0][0] - action[1][0] == max_vertical_advance_one_step]
        else:
            max_vertical_advance_one_step = max([action[1][0] - action[0][0] for action in legal_actions])
            max_actions = [action for action in legal_actions if
                           action[1][0] - action[0][0] == max_vertical_advance_one_step]
        self.action = random.choice(max_actions)


class TeamNameMinimaxAgent(Agent):
    def getAction(self, state):
        legal_actions = self.game.actions(state)
        self.action = random.choice(legal_actions)

        player = self.game.player(state)
        ### START CODE HERE ###
        self.scoreList = []
        self.minMax(state, 2, -1000, 1000)
        a = self.scoreList.index(max(self.scoreList))
        self.action = legal_actions[a]


    def minMax(self, state, depth, alpha, beta):
        if depth == 0:
            return self.heuristic(state)
        
        if self.game.player(state) == 1:
            for i in self.game.actions(state):
                score = self.minMax(self.game.succ(state, i), depth-1, alpha, beta)
                if depth == 2:
                    self.scoreList.append(score)
                if score > alpha:
                    alpha = score
                    if alpha >= beta:
                        return beta
            return alpha
        else:
            for i in self.game.actions(state):
                score = self.minMax(self.game.succ(state, i), depth-1, alpha, beta)
                if score <beta:
                    beta = score
                    if alpha >= beta:
                        return alpha
            return beta

    def heuristic(self, state):
        total = 0
        
        for i in state[1].board_status.keys():
            if state[1].board_status[i] == 1:
                total += 20-i[0]
                if abs(i[1]-(min(20-i[0], i[0])+1)/2)<2:
                    total+=1
                else:
                    total-=2
                if i[0]<5:
                    total+=3
            elif state[1].board_status[i] == 2:
                total+=20-i[0]
                if i[0]<5:
                    total-=1
        return total










        ### END CODE HERE ###



