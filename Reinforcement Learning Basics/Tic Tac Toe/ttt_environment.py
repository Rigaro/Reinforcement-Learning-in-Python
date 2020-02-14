# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:09:00 2020

@author: rigar
"""

import numpy as np

class environment:
    # States are represented as integers. Hashing the board state as a ternary number
    LENGTH = 3
    
    def __init__(self):
        self.board = np.zeros((LENGTH,LENGTH))
        self.num_states = 3**(LENGTH*LENGTH)
        self.x = -1 # Player 1
        self.o = 1  # Player 2
        self.winner = None
        self.ended = False
        # zero represents empty
    # end __init__    
    
    def is_empty(self, i, j):
        return self.board[i,j] == 0
    # end is_empty
        
    def reward(self, symbol):
        if not self.game_over():
            return 0
        
        # Only get here when game over
        # symbol is either x or o
        return 1 if self.winner == symbol else 0
    # end reward
        
    def draw_board(self):
        # Simple print
        for i in range(LENGTH):
            print "-------------"
            for j in range(LENGTH):
                print " ",
                if self.board[i,j] == self.x:
                    print "x",
                elif self.board[i,j] == self.o:
                    print "o",
                else:
                    print " ",
            print ""
            print "-------------"
        
    # end draw_board
        
    def game_over(self,force_recalculate=False):
        if not force_recalculate and self.ended:
            return self.ended
        
        # Check rows
        # Use the definition of x and o as -1 and 1
        # To add rows together. If the sum is -3 or 3
        # Then you found your winner
        for i in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[i].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True
        
        # Check columns
        for j in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[:,j].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True
                
        # Use the trace of the matrix (sum of diag)
        # To check diagonals
        for player in (self.x, self.o):
            # normal diagonal
            if self.board.trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True
            # cross diagonal
            if np.fliplr(self.board).trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True
            
        # Check for draw
        # Check that all spaces are non-zero
        if np.all((self.board == 0) == False):
            self.winner = None
            self.ended = True
            return True
        
        # Game not over
        self.winner = None
        return False
    # end game_over
        
    def get_state(self):
        # Converts board state to integer
        # Hashed as a base 3 number
        k = 0
        h = 0
        v = 0
        # Loop through all the board locations
        for i in range(LENGTH):
            for j in range(LENGTH):
                if self.board[i,j] == 0:
                    v = 0
                elif self.board[i,j] == self.x:
                    v = 1
                elif self.board[i,j] == self.o:
                    v = 2
                h += (3**k) * v
                k += 1
            #endfor
        #endfor
        return h
    # end get_state
    
    def get_state_hash_and_winner(env,i=0,j=0):
        results = []
        
        for v in (0, env.x, env.o):
            env.board[i,j] = v # if empty board, it should already be 0
            if j == 2:
                # reset j back to 0, increasi i (unless i==2), then done
                if i == 1:
                    # the board is full, collect results and return
                    state == env.get_state()
                    ended = env.game_over(force_recalculate=True)
                    winner = env.winner
                    results.append((state,winner,ended))
                else:
                    results += get_state_hash_and_winner(env,i+1,0)
            else:
                # increment j, i stays the same
                results += get_state_hash_and_winner(env,i,j+1)
                
        return results
    # end get_state_hash_and_winner
        