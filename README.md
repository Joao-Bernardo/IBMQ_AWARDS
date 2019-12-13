# IBMQ_AWARDS
Project for the IBMQ awards 2019 contest. Watch the video below!

https://www.youtube.com/watch?v=VuZNc3Ej0ME&t

## Description

Welcome to the **QUANTIC TETRIS!** This is an almost normal Tetris game, but with a small difference that it is based on quantum mechanics properties like  **superposition**, **wave function colapse**, **entanglement** and **mixed states**. If you want to master this game you will need to apply some quantum logic gates like **X**, **Hadamard**, **Z** and **CNOT** to manipulate your state and score a lot of points!

![Image of the game](https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/quantic_tetris_gif.gif)

## Controls
### Movement
left arrow - move the stone to the left

right arrow - move the stone to the right

down arrow - make the stone fall faster

up arrow - rotate the stone 

### Logic Gate Application
enter - apply toggled gate

q - toggle **H** gate

w - toggle **X** gate

e - toggle **Z** gate

r - toggle **CNOT** gate

1 - toggle **qubit 1** as the one in wich the gate will be applied (if the gate is CNOT, it chooses **qubit 1** as the control)

2 - toggle **qubit 2** as the one in wich the gate will be applied (if the gate is CNOT, it chooses **qubit 2** as the control)

### Others

p - pause

esc - quit

## Tutorial
https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/Tutorial.md

## Game Engine
The game engine is based on the application of gates generated by the set S={CNOT,Hadamard,P} that is not an universal set for quantum computing. This set has the property that it can only generate equally weighted superpositions, always with a number of basis states that are a power of 2. This means that in our case we will always have superpositions with two or four basis states. 

The choice for this set is due to the simplified states generated by it and to the fact that the gates that we want to be present in our game can all be generated by this set. This implies that the user experience is simpler, and it makes the learning process easier for users that are non familiar with quantum computing.
