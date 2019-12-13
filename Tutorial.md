# Tutorial

In order to master the Quantic Tetris you will need to learn how to manipulate quantum states!
To perform this manipulation you are going to apply the basic gates used in quantum computing, called **quantum logic gates**.
A brief explanation of how these gates works is going to be presented but, first, its necessary to understand what is a quantum state.

## Quantum States
### Basis States
Every stone in the **Quantic Tetris** is a quantum state.
Each of the states is composed of two qubits and the four basis states are seen below:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />

In **Quantic Tetris** the screen is divided in four parts, where each of the parts correspond to one of the basis states. 
So, for example, if our current state is 00, the stone will fall on the left most screen. Just as ilustrated below:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />

The order of the basis states and the corresponding division in the screen goes from left to right as 00, 01, 10 and 11.

### Superpositions

When the stone falls as one of the basis states, it has nothing quantic about it. However, the stones can also fall as a
**superposition** of states, just like the schrodinger cat that is death and alive simultaneously. 
This means that instead of falling in just one of the divisions, the stone may fall on two or even four of the
divisions simultaneously. For example, in the figure below, the current state is a superposition of 00 and 01.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />

When the state falls as a superposition, for example 00 and 01, it means that it is both 00 **and** 01 at the same time.
However, just like the schrodinger cat turns out to be dead **or** alive after an external observer measure it, our **superposition** is
going to colapse to 00 **or** 01 when it interacts with something, for example, another stone or even the ground.

Finally, one last thing that you need to know about superpositions is that you can manipulate it applying **quantum logic gates**. 
For example, if you apply the gate **H** on the second qubit of our previous superposition, it transforms 00 and 01 to 00.
The exaplanation of this is going to be presented on the gates section.

### Mixed State

This is a special kind of state, that can be seen below, that looks like a superposition but in fact it is not. This state represents some **lack of information**
that we sometimes have about quantum system due, for example, to noise. What it really means is that we dont know in wich basis state
the stone is and we will only know when the stone interacts with something. But the key difference from quantum superpositions is the fact
that applying any combination of gates wont change the state and it will always remain with four basis states until it collapse.
So this is definitly the **worst case state**, since you cant control where the stone is going to be.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />





