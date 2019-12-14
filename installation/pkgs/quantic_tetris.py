#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Very simple tetris implementation
#
# Control keys:
# Down - Drop stone faster
# Left/Right - Move stone
# Up - Rotate Stone clockwise
# Escape - Quit game
# P - Pause game
#
# Have fun!

# Copyright (c) 2010 "Kevin Chabowski"<kevin@kch42.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from random import randrange as rand
import pygame
import copy
from math import *
from qiskit import BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

# The configuration
qubits = 2
config = {
    'cell_size': 25,
    'cols': 7,
    'rows': 16,
    'delay': 2000,
    'maxfps': 30,
    'states': int(pow(qubits,2)),
    'div_cols':1,
    'menu_rows':5
}

colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 120, 0),
    (255, 255, 0),
    (180, 0, 255),
    (0, 220, 220),
    (0, 0, 0)
]

# Define the shapes of the single parts
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]


def rotate_clockwise(shape):
    return [[shape[y][x]
             for y in range(len(shape))]
            for x in range(len(shape[0]) - 1, -1, -1)]


def check_collision(board, shape, offset,self):
    off_x, off_y = offset
    colision_boards = []
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            try:
                if self.is_colapsed:
                    if cell and board[self.meas_colapse][cy + off_y][cx + off_x]:
                        return True, -1
                else:
                    present_states = [i for i, x in enumerate(self.stone_state) if x != 0]
                    for k in present_states:
                        if cell and board[k][cy + off_y][cx + off_x]:
                            colision_boards.append(k)
            except IndexError:
                return True, -2
    if colision_boards:
        return True, colision_boards
    return False, -3


def join_matrixes(mat1, mat2, mat2_off):
    off_x, off_y = mat2_off
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):
            mat1[cy + off_y - 1][cx + off_x] += val
    return mat1

def new_board():
    board = []
    for i in range(config['states']):
        temp = [[0 for x in range(config['cols'])]
                 for y in range(config['rows'])]
        temp += [[1 for x in range(config['cols'])]]
        board += [copy.deepcopy(temp)]
    return board

def new_division():
    division = [[8 for x in range(config['div_cols'])]
             for y in range(config['rows'])]
    return division


class TetrisApp(object):
    def __init__(self):
        pygame.init()
        self.quit = False
        pygame.key.set_repeat(250, 25)
        if config['cell_size'] > 17:
            font_size = config['cell_size']
        else:
            font_size = int(3*config['cell_size']/4)
        self.font = pygame.font.SysFont('comicsansms', font_size)
        self.width = config['cell_size']*((config['states']*(config['cols'] + config['div_cols']))-config['div_cols'])
        self.height = config['cell_size'] * (config['rows'] + config['menu_rows'])
        pygame.display.set_caption('Quantic Tetris')
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.event.set_blocked(pygame.MOUSEMOTION)  # We do not need
        # mouse movement
        # events, so we
        # block them.
        self.init_game()

    def new_stone(self):
        self.stone = tetris_shapes[rand(len(tetris_shapes))]
        self.stone_x = int(config['cols'] / 2 - len(self.stone[0]) / 2)
        self.stone_y = 0
        self.is_colapsed = False
        self.meas_colapse = -1
        self.stone_state = []
        self.stone_state = self.generate_state()
        if self.stone_state.count(0) == (config['states']-1):
            self.is_colapsed = True
            present_states = [i for i, x in enumerate(self.stone_state) if x != 0]
            self.meas_colapse = present_states[0]

        if check_collision(self.board,
                           self.stone,
                           (self.stone_x, self.stone_y),self)[0]:
            self.gameover = True
            
    def remove_row(self,board, row):
        self.points = self.points + 100
        if config['delay'] > 150:
            config['delay'] = int(config['delay']*0.9)
            pygame.time.set_timer(pygame.USEREVENT + 1, config['delay'])
        del board[row]
        return [[0 for i in range(config['cols'])]] + board

    def generate_state(self):
        while 1:
            state = []
            count_ones = 0
            count_neg = 0
            if rand(int(config['states']+1)) < config['states']:
                for i in range(config['states']):
                    if rand(2):
                        if (rand(2)):
                            state.append(1)
                        else:
                            state.append(-1)
                            count_neg = count_neg+1
                        count_ones = count_ones+1
                    else:
                        state.append(0)          
                if count_ones != 0 and count_ones != 3:
                    self.mixed_state = False
                    break
            else:
                for i in range(config['states']):
                    state.append(1)
                count_ones = config['states']
                self.mixed_state = True
                break
                
        state = [(i/sqrt(count_ones)) for i in state]
        return state

    def colapse_stone_state(self):
        stone_state = []
        for i in range(config['states']):
            if i == self.meas_colapse:
                stone_state.append(1)
            else:
                stone_state.append(0)
        return stone_state

    def colapse_index(self):
        pygame.mixer.music.load('pkgs/colapse.mp3')
        pygame.mixer.music.play()
        present_states = [i for i, x in enumerate(self.stone_state) if x != 0]
        colapsed_to = present_states[rand(len(present_states))]
        return colapsed_to

    def init_game(self):
        self.board = new_board()
        self.new_stone()
        self.division = new_division()
        self.qubit_gate = 1
        self.gate = 'X'
        self.points = 0
        self.application_result = 0 # 0 means it was not applied recently, 1 means Success, 2 means Not Allowed

    def center_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image = pygame.font.Font(
                pygame.font.get_default_font(), 12).render(
                line, False, (255, 255, 255), (0, 0, 0))

            msgim_center_x, msgim_center_y = msg_image.get_size()
            msgim_center_x //= 2
            msgim_center_y //= 2

            self.screen.blit(msg_image, (
                self.width // 2 - msgim_center_x,
                self.height // 2 - msgim_center_y + i * 22))

    def draw_matrix(self, matrix, offset,neg=False):
        off_x, off_y = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(
                        self.screen,
                        colors[val],
                        pygame.Rect(
                            (off_x + x) *
                            config['cell_size'],
                            (off_y + y + config['menu_rows']) *
                            config['cell_size'],
                            config['cell_size'],
                            config['cell_size']), 0)
                    if neg:
                        pygame.draw.rect(
                            self.screen,
                            colors[0],
                            pygame.Rect(
                                (off_x + x) *
                                config['cell_size'] + 3*config['cell_size']/8,
                                (off_y + y + config['menu_rows']) *
                                config['cell_size'] + 3*config['cell_size']/8,
                                config['cell_size']/4,
                                config['cell_size']/4), 0)
    
    def draw_menu(self):
        pygame.draw.rect(
                            self.screen,
                            colors[0],
                            pygame.Rect(
                                0,
                                0,
                                self.width,
                                config['cell_size']*config['menu_rows']), 0)
        
        points_text = self.font.render('Points: ' + str(self.points), True, (255,255,255))
        state_string = self.state_to_string()
        state_text = self.font.render('Current State: ' + state_string, True, (255,255,255))
        gate_string = self.gate_to_string()
        gate_text = self.font.render('Gate: ' + gate_string, True, (255,255,255))
        
        self.screen.blit(points_text,(10,5))
        self.screen.blit(state_text,(10,10 + points_text.get_height()))
        self.screen.blit(gate_text, (10,15 + points_text.get_height() + state_text.get_height()))
        
    def gate_to_string(self):
        gate_result = ''
        if self.application_result == 1:
            gate_result = ' Applied!'
        elif self.application_result == 2:
            gate_result = ' Not Allowed!'
        if self.qubit_gate == 1:
            return self.gate + chr(8321) + gate_result
        else:
            return self.gate + chr(8322) + gate_result
            
        
        
    def state_to_string(self):
        base_states_str = ['|00>','|01>', '|10>','|11>']
        present_states = [i for i, x in enumerate(self.stone_state) if x != 0]
        state_str = ''
        for i in present_states:
            if self.stone_state[i] > 0:
                signal = '+'
            else:
                signal = '-'
            state_str = state_str + ' ' + signal + ' ' + base_states_str[i]
        if self.mixed_state:
            state_str = 'I/2 (Mixed State)' 
        return state_str
        
        
    def move(self, delta_x):
        if not self.gameover and not self.paused:
            new_x = self.stone_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > config['cols'] - len(self.stone[0]):
                new_x = config['cols'] - len(self.stone[0])
            if not check_collision(self.board,
                                   self.stone,
                                   (new_x, self.stone_y),self)[0]:
                self.stone_x = new_x

    def exit(self):
        self.center_msg("Exiting...")
        self.quit = True
        pygame.display.update()
        del self.font
        pygame.quit()

    def drop(self):
        if not self.gameover and not self.paused:
            self.application_result = 0
            self.stone_y += 1
            result, colisions = check_collision(self.board,
                               self.stone,
                               (self.stone_x, self.stone_y),self)
            if result and not self.is_colapsed:
                self.is_colapsed = True
                self.meas_colapse = self.colapse_index()
                self.stone_state = self.colapse_stone_state()
                if self.meas_colapse in colisions:
                    self.board[self.meas_colapse] = join_matrixes(
                        self.board[self.meas_colapse],
                        self.stone,
                        (self.stone_x, self.stone_y))
                    while True:
                        for i, row in enumerate(self.board[self.meas_colapse][:-1]):
                            if 0 not in row:
                                self.board[self.meas_colapse] = self.remove_row(
                                    self.board[self.meas_colapse], i)
                                break
                        else:
                            break
                    self.new_stone()
            elif result and self.is_colapsed:
                self.board[self.meas_colapse] = join_matrixes(
                    self.board[self.meas_colapse],
                    self.stone,
                    (self.stone_x, self.stone_y))
                while True:
                    for i, row in enumerate(self.board[self.meas_colapse][:-1]):
                        if 0 not in row:
                            self.board[self.meas_colapse] = self.remove_row(
                                self.board[self.meas_colapse], i)
                            break
                    else:
                        break
                self.new_stone()

    def rotate_stone(self):
        pygame.mixer.music.load('pkgs/moving.mp3')
        pygame.mixer.music.play()
        if not self.gameover and not self.paused:
            new_stone = rotate_clockwise(self.stone)
            if not check_collision(self.board,
                                   new_stone,
                                   (self.stone_x, self.stone_y),self)[0]:
                self.stone = new_stone

    def toggle_pause(self):
        self.paused = not self.paused

    def start_game(self):
        if self.gameover:
            self.init_game()
            self.gameover = False

    def toggle_qubit(self,q):
        pygame.mixer.music.load('pkgs/gate_toggle.mp3')
        pygame.mixer.music.play()
        self.qubit_gate = q%2

    def toggle_gate(self,gate):
        pygame.mixer.music.load('pkgs/gate_toggle.mp3')
        pygame.mixer.music.play()
        self.gate = gate

    def assign_state(self, qc_state):
            current_state = self.stone_state
            current_meas = self.meas_colapse
            current_iscolapsed = self.is_colapsed
            
            self.stone_state = list(qc_state)
            present_states = [i for i, x in enumerate(self.stone_state) if x != 0]
            if len(present_states) == 1:
                self.meas_colapse = present_states[0]
                self.is_colapsed = True
            else:
                self.meas_colapse = -1
                self.is_colapsed = False
            result, colisions = check_collision(self.board, self.stone,(self.stone_x, self.stone_y),self)
            if result:
                self.stone_state = current_state
                self.meas_colapse = current_meas
                self.is_colapsed = current_iscolapsed
                return 2
            else:
                return 1
            
    def apply_gate(self):
        pygame.mixer.music.load('pkgs/gate.mp3')
        pygame.mixer.music.play()
        if not self.mixed_state and not self.gameover and not self.paused and not check_collision(self.board,self.stone,(self.stone_x, self.stone_y), self)[0]:
            q = QuantumRegister(qubits)
            qc = QuantumCircuit(q)
            qc.initialize(self.stone_state, [q[0], q[1]])
            backend = BasicAer.get_backend('statevector_simulator')
            if self.gate == 'H':
                qc.h(self.qubit_gate)
            if self.gate =='X':
                qc.x(self.qubit_gate)
            if self.gate =='Z':
                qc.z(self.qubit_gate)
            if self.gate =='CNOT':
                qc.cx(self.qubit_gate,(self.qubit_gate+1)%2)
            job = execute(qc, backend)
            qc_state = job.result().get_statevector(qc)
            self.application_result = self.assign_state(qc_state)

    def run(self):
        key_actions = {
            'ESCAPE': self.exit,
            'LEFT': lambda: self.move(-1),
            'RIGHT': lambda: self.move(+1),
            'DOWN': self.drop,
            'UP': self.rotate_stone,
            'p': self.toggle_pause,
            'SPACE': self.start_game,
            '1': lambda: self.toggle_qubit(1),
            '2': lambda: self.toggle_qubit(2),
            'q': lambda: self.toggle_gate('H'),
            'w': lambda: self.toggle_gate('X'),
            'e': lambda: self.toggle_gate('Z'),
            'r': lambda: self.toggle_gate('CNOT'),
            'RETURN': lambda: self.apply_gate()
        }

        self.gameover = False
        self.paused = False

        pygame.time.set_timer(pygame.USEREVENT + 1, config['delay'])
        dont_burn_my_cpu = pygame.time.Clock()
        while not self.quit:
            self.screen.fill((255, 255, 255))
            self.draw_menu()
            if self.gameover:
                self.center_msg("""Game Over!
Press space to continue""")
            else:
                if self.paused:
                    self.center_msg("Paused")
                else:
                    for k in range(config['states']):
                        state_offset = (k*(config['cols']+config['div_cols']),0)
                        self.draw_matrix(self.board[k], state_offset)
                        if self.is_colapsed and (self.meas_colapse == k):
                            self.draw_matrix(self.stone,
                                         (self.stone_x + state_offset[0],
                                          self.stone_y))
                        elif not self.is_colapsed:
                            present_states = [i for i, x in enumerate(self.stone_state) if x != 0]
                            if k in present_states:
                                if self.stone_state[k] < 0:
                                    neg = True
                                else:
                                    neg = False
                                self.draw_matrix(self.stone,
                                             (self.stone_x + state_offset[0],
                                              self.stone_y),neg)
                        if k > 0:
                            self.draw_matrix(self.division, (k*(config['cols']) + (k-1)*config['div_cols'],0))

            pygame.display.update() 
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT + 1:
                    self.drop()
                elif event.type == pygame.QUIT:
                    self.exit()
                elif event.type == pygame.KEYDOWN:
                    for key in key_actions:
                        if event.key == eval("pygame.K_"
                                             + key):
                            key_actions[key]()

            dont_burn_my_cpu.tick(config['maxfps'])


def main():
    App = TetrisApp()
    App.run()
			
if __name__ == '__main__':
	main()


# In[ ]:




