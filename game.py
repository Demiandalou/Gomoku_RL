# -*- coding: utf-8 -*-
"""
@author: Junxiao Song
"""

from __future__ import print_function
import numpy as np
from Forbidden_Moves import forbidden_move

# def double_three(self,curPlayer,noncurPlayer,x,y):
# save_forbidden=

class Board(object):
    """board for the game"""

    def __init__(self, **kwargs):
        self.width = int(kwargs.get('width', 8))
        self.height = int(kwargs.get('height', 8))
        # board states stored as a dict,
        # key: move as location on the board,
        # value: player as pieces type
        self.states = {}
        # need how many pieces in a row to win
        self.n_in_row = int(kwargs.get('n_in_row', 5))
        self.players = [1, 2]  # player1 and player2
        self.forbidden=[]
        self.save_forbidden=[]
    def init_board(self, start_player=0):
        if self.width < self.n_in_row or self.height < self.n_in_row:
            raise Exception('board width and height can not be '
                            'less than {}'.format(self.n_in_row))
        self.current_player = self.players[start_player]  # start player
        # keep available moves in a list
        self.availables = list(range(self.width * self.height))
        self.states = {}
        self.last_move = -1

    def move_to_location(self, move):
        """
        3*3 board's moves like:
        6 7 8
        3 4 5
        0 1 2
        and move 5's location is (1,2)
        """
        h = move // self.width
        w = move % self.width
        return [h, w]

    def location_to_move(self, location):
        if len(location) != 2:
            return -1
        h = location[0]
        w = location[1]
        move = h * self.width + w
        if move not in range(self.width * self.height):
            return -1
        return move

    def current_state(self):
        """return the board state from the perspective of the current player.
        state shape: 4*width*height
        """

        square_state = np.zeros((4, self.width, self.height))
        if self.states:
            moves, players = np.array(list(zip(*self.states.items())))
            move_curr = moves[players == self.current_player]
            move_oppo = moves[players != self.current_player]
            square_state[0][move_curr // self.width,
                            move_curr % self.height] = 1.0
            square_state[1][move_oppo // self.width,
                            move_oppo % self.height] = 1.0
            # indicate the last move location
            square_state[2][self.last_move // self.width,
                            self.last_move % self.height] = 1.0
        if len(self.states) % 2 == 0:
            square_state[3][:, :] = 1.0  # indicate the colour to play

        # square_state[:, ::-1, :][0][0] indicate position of non-current player
        # square_state[:, ::-1, :][1][0] indicate position of current player
        # square_state[:, ::-1, :][2][0] indicate position of last move (belong to cur player)
        # print(square_state[:, ::-1, :])
        return square_state[:, ::-1, :]

    def do_move(self, move):
        self.states[move] = self.current_player
        self.availables.remove(move)
        self.current_player = (
            self.players[0] if self.current_player == self.players[1]
            else self.players[1]
        )
        self.last_move = move
        # for m in self.availables:
        #     x = 7-(m // self.width)
        #     y = m % self.width
        #     # print(x,y)
        #     Feature_states=self.current_state()
        #     # print(Feature_states)
        #     noncurPlayerState=Feature_states[1]
        #     curPlayerState=Feature_states[0]
        #     isforbidden=forbidden_move(curPlayerState,noncurPlayerState,x,y,self.width)
        #     if isforbidden==1:
        #         print('here')
        #         self.forbidden.append(m)
        #         # list(sensible_moves).remove(m)
        
    def has_a_winner(self):
        width = self.width
        height = self.height
        states = self.states
        n = self.n_in_row

        # # ############# forbidden move ################
        # # # self.current_player
        # # # square_state[:, ::-1, :][0] indicate position of non-current player
        # # # square_state[:, ::-1, :][1] indicate position of current player
        # # # square_state[:, ::-1, :][2] indicate position of last move (belong to cur player)
        # # # print(square_state[:, ::-1, :])
        
        # # # print('judging forbidden moves')
        # Feature_states=self.current_state()
        # curPlayerState=Feature_states[1]
        # noncurPlayerState=Feature_states[0]
        # lastMove=Feature_states[2]
        # a=np.where(lastMove==1)
        # if len(a[0])!=0:
        #     x,y=a[0][0],a[1][0]
        # else:
        #     x,y=0,0
        #     # print('has a winner',x,y)
        #     # exit()
        # # if self.current_player==2:
        # modi_curPlayer=np.copy(curPlayerState)
        # modi_curPlayer[x][y]=0
        # isforbidden=forbidden_move(modi_curPlayer,noncurPlayerState,x,y,self.width)
        # # print(isforbidden)
        # # if isforbidden==1:
        # #     return True,1

        moved = list(set(range(width * height)) - set(self.availables))
        if len(moved) < self.n_in_row *2-1:
            return False, -1
        for m in moved:
            h = m // width
            w = m % width
            try:
                player = states[m]
            except:
                continue
            if (w in range(width - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n))) == 1):
                return True, player
            if (h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * width, width))) == 1):
                return True, player
            if (w in range(width - n + 1) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width + 1), width + 1))) == 1):
                return True, player
            if (w in range(n - 1, width) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width - 1), width - 1))) == 1):
                return True, player
        return False, -1

    def game_end(self):
        """Check whether the game is ended or not"""
        win, winner = self.has_a_winner()
        # print('In game_end',win,winner)
        if win:
            return True, winner
        elif not len(self.availables):
            return True, -1
        return False, -1

    def get_current_player(self):
        return self.current_player


class Game(object):
    """game server"""

    def __init__(self, board, **kwargs):
        self.board = board

    def graphic(self, board, player1, player2):
        """Draw the board and show game info"""
        width = board.width
        height = board.height

        print("Player", player1, "with X".rjust(3))
        print("Player", player2, "with O".rjust(3))
        print("Forbidden move", "with N".rjust(3))
        print()
        for x in range(width):
            print("{0:8}".format(x), end='')
        print('\r\n')
        for i in range(height - 1, -1, -1):
            print("{0:4d}".format(i), end='')
            for j in range(width):
                loc = i * width + j
                p = board.states.get(loc, -1)
                if p == player1:
                    # print(p,player1)
                    print('X'.center(8), end='')
                elif p == player2:
                    print('O'.center(8), end='')
                elif loc in self.board.forbidden:
                    print('N'.center(8), end='')
                else:
                    print('_'.center(8), end='')
            print('\r\n\r\n')

    # Human play: game.start_play(human, mcts_player, start_player=1, is_shown=1)
    # Train: self.game.start_play(current_mcts_player,
                                    #   pure_mcts_player,
                                    #   start_player=i % 2,
                                    #   is_shown=0)
    def start_play(self, player1, player2, start_player=0, is_shown=1):
        """start a game between two players"""
        if start_player not in (0, 1):
            raise Exception('start_player should be either 0 (player1 first) '
                            'or 1 (player2 first)')
        self.board.init_board(start_player)
        p1, p2 = self.board.players
        player1.set_player_ind(p1)
        player2.set_player_ind(p2)
        players = {p1: player1, p2: player2}
        if is_shown:
            self.graphic(self.board, player1.player, player2.player)
        cnt=0
        while True:
            current_player = self.board.get_current_player()
            player_in_turn = players[current_player]
            move = player_in_turn.get_action(self.board)
            # print(move)
            # loc=self.board.move_to_location(move)
            # print(self.board.location_to_move(loc))
            # print(self.board.location_to_move([3,4]))
            
            # if current_player==2:
            #     cnt+=1
            # if cnt==1 and current_player==2:
            #     move=self.board.location_to_move([3,4])
            # if cnt==2 and current_player==2:
            #     move=self.board.location_to_move([2,5])
            # if cnt==3 and current_player==2:
            #     move=self.board.location_to_move([5,4])
            # if cnt==4 and current_player==2:
            #     move=self.board.location_to_move([6,5])
            # if cnt==5 and current_player==2:
            #     move=self.board.location_to_move([3,2])
            # if cnt==6 and current_player==2:
            #     move=self.board.location_to_move([5,2])
            # # if cnt==4 and current_player==2:
            # #     move=self.board.location_to_move([6,1])
            # # if cnt==5 and current_player==2:
            # #     move=self.board.location_to_move([1,6])
            # # if cnt==5 and current_player==2:
            # #     move=self.board.location_to_move([4,3])

            self.board.do_move(move)
            # print(move)
            
            sensible_moves=np.copy(self.board.availables)
            # print('board.current_player',board.current_player)# should==2:
            if current_player==2:
                # self.board.save_forbidden=[]
                for m in sensible_moves:
                    x = 7-(m // self.board.width)
                    y = m % self.board.width
                    # print(x,y)
                    Feature_states=self.board.current_state()
                    # print(Feature_states)
                    curPlayerState=Feature_states[1]
                    noncurPlayerState=Feature_states[0]
                    isforbidden=forbidden_move(curPlayerState,noncurPlayerState,x,y,self.board.width)
                    if isforbidden==1:
                        # print('here')
                        self.board.forbidden.append(m)
                        self.board.save_forbidden.append(m)
                    if (m in self.board.save_forbidden) and isforbidden==0:
                        self.board.save_forbidden.remove(m)
            if is_shown:
                self.graphic(self.board, player1.player, player2.player)
            # print('playing')
            # print("current player:",current_player)
            # curState=self.board.current_state()
            # if cnt==5 and current_player==2:
            #     print(curState)
            #     print(self.board.has_a_winner())
            # lastMove=curState[2]
            # a=np.where(lastMove==1)
            # print(len(a))
            # print('playing',a[0][0],a[1][0])
            self.board.forbidden=[]
            end, winner = self.board.game_end()
            # print(end,winner,is_shown)

            if end:
                if is_shown:
                    if winner != -1:
                        print("Game end. Winner is", players[winner])
                    else:
                        print("Game end. Tie")
                return winner

    def start_self_play(self, player, is_shown=0, temp=1e-3):
        """ start a self-play game using a MCTS player, reuse the search tree,
        and store the self-play data: (state, mcts_probs, z) for training
        """
        self.board.init_board()
        p1, p2 = self.board.players
        states, mcts_probs, current_players = [], [], []
        while True:
            move, move_probs = player.get_action(self.board,
                                                 temp=temp,
                                                 return_prob=1)
            # store the data
            states.append(self.board.current_state())
            mcts_probs.append(move_probs)
            current_players.append(self.board.current_player)
            # perform a move
            self.board.do_move(move)
            if is_shown:
                self.graphic(self.board, p1, p2)
            end, winner = self.board.game_end()
            if end:
                # winner from the perspective of the current player of each state
                winners_z = np.zeros(len(current_players))
                if winner != -1:
                    winners_z[np.array(current_players) == winner] = 1.0
                    winners_z[np.array(current_players) != winner] = -1.0
                # reset MCTS root node
                player.reset_player()
                if is_shown:
                    if winner != -1:
                        print("Game end. Winner is player:", winner)
                    else:
                        print("Game end. Tie")
                return winner, zip(states, mcts_probs, winners_z)
