
import numpy as np
from Forbidden_Moves import cal_features
import copy
import math
EPS=0.5
def flip_coin(board):
    explore=EPS/math.log(len(board.states)+0.01)
    gen=np.random.random()
    if gen<explore:
        return 1
    return 0

class QPlayer:
    # method: qlearn
    def __init__(self,board,alpha=0.1,gamma=0.9):
        self.alpha = alpha
        self.gamma = gamma # future reward discount factor
        self.Q=np.zeros(board.width * board.height)
        #执黑
        #feature1-7
        self.contblack2=np.zeros(board.width * board.height)
        self.contblack3=np.zeros(board.width * board.height)
        self.contblack4=np.zeros(board.width * board.height)
        self.contblack5=np.zeros(board.width * board.height)
        self.contwhite3=np.zeros(board.width * board.height)
        self.contwhite4=np.zeros(board.width * board.height)
        self.contwhite5=np.zeros(board.width * board.height)
        self.weights=[5, 10, 20, 15, 30]
        #             b2  b3  b4  w3  w4
        # self.weights=[0.5, 1, 2, 5, 1.5, 3, 5]
        #             b2  b3  b4 b5  w3 w4 w5
        self.player=None
    def update_qval(self,board,sensible_moves):
        # print(board.states)
        thisplayerState=[]
        otherplayerState=[]
        for k in board.states:
            if board.states[k]==self.player:
                thisplayerState.append(k)
            else:
                otherplayerState.append(k)
        cal_features(self,board,sensible_moves,thisplayerState,otherplayerState)
        # print(len(np.where(self.contwhite3)[0]))
        for move in range(board.width * board.height):
            if move in sensible_moves:
                if self.contblack5[move]==1:
                    self.Q[move]=500
                elif self.contwhite5[move]==1:
                    self.Q[move]=500
                else:
                    features=self.weights[0] * self.contblack2[move]+\
                            self.weights[1] * self.contblack3[move]+\
                            self.weights[2] * self.contblack4[move]+\
                            self.weights[3] * self.contwhite3[move]+\
                            self.weights[4] * self.contwhite4[move]
                    self.Q[move]=features
            else:
                self.Q[move]=-100000
            if move in board.save_forbidden:
                self.Q[move]=-100000
    def update_weights(self,move,prevQ):
        maxQ=max(self.Q)
        upd = 0.01 + self.gamma*maxQ - prevQ
        coef=self.alpha*upd
        self.weights[0]+=coef*self.contblack2[move]
        self.weights[1]+=coef*self.contblack3[move]
        self.weights[2]+=coef*self.contblack4[move]
        self.weights[3]+=coef*self.contwhite3[move]
        self.weights[4]+=coef*self.contwhite4[move]
        
    def set_player_ind(self, p):
        self.player = p

    def get_action(self,board):
        # print('get Q action')
        sensible_moves=np.copy(board.availables)
        for m in sensible_moves:
            if m in board.save_forbidden:
                np.delete(sensible_moves,np.where(sensible_moves==m)[0])
        iters=250
        for t in range(iters):
            self.update_qval(board,sensible_moves)
            if flip_coin(board)==1:
                move=np.random.choice(sensible_moves)
            else:
                maxQ=max(self.Q)
                best_choices=np.where(self.Q==maxQ)[0]
                
                for m in best_choices:
                    if m in board.save_forbidden:
                        # np.delete(best_choices,m)
                        np.delete(best_choices,np.where(best_choices==m)[0])
                move=np.random.choice(best_choices)
            tmpBoard=copy.deepcopy(board)
            tmpBoard.do_move(move)
            otherm=np.copy(board.availables)
            for m in otherm:
                if m in board.save_forbidden:
                    # otherm.remove(m)
                    np.delete(otherm,np.where(otherm==m)[0])

            randmove=np.random.choice(otherm)
            prevQ=self.Q[move]
            self.update_qval(board,sensible_moves)
            self.update_weights(move,prevQ)

        return move
    def __str__(self):
        return "Pure RL Player"

