# IBMQ_AWARDS
Project for the IBMQ awards 2019 contest

## Description

Welcome to the **QUANTIC TETRIS!** This is an almost normal Tetris game, but with a small difference that it is based on quantum mechanics properties like  **superposition**, **wave function colapse**, **entanglement** and **mixed states**. If you want to master this game you will need to apply some quantum logic gates like **X**, **Hadamard**, **Z** and **CNOT** to manipulate your state and score a lot of points!

![Image of the game](https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/main_photo.png)

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

## Tutorial

In order to master the Quantic Tetris you will need to learn how to manipulate quantum states! To perform this manipulation you are going to apply the the basic gates used in quantum computing, called **quantum logic gates**. A brief explanation of how these gates works is going to be presented but, first, its necessary to understand what is a quantum state.

### Quantum States
Every stone in the **Quantic Tetris** is a quantum state. Each of the states is composed of two qubits, where
