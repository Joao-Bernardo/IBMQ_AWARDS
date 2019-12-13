# Tutorial

In order to master the Quantic Tetris you will need to learn how to manipulate quantum states!
To perform this manipulation you are going to apply the basic gates used in quantum computing, called **quantum logic gates**.
A brief explanation of how these gates works is going to be presented but, first, its necessary to understand what is a quantum state.

## Quantum States
### Basis States
Every stone (the falling objects in tetris) in the **Quantic Tetris** is a quantum state.
Each of the states is composed of two qubits and the four basis states are seen below:

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/basis_states.png" />

In **Quantic Tetris** the screen is divided in four parts, where each of the parts correspond to one of the basis states.
The order of the basis states and the corresponding division in the screen goes from left to right as 00, 01, 10 and 11.
So, for example, if our current state is 00, the stone will fall on the left most screen. Just as ilustrated below:

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/state_00.png" />

### Superpositions

When the stone falls as one of the basis states, it has nothing quantic about it. However, the stones can also fall as a
**superposition** of states, just like the schrodinger cat that is dead and alive simultaneously. 
This means that instead of falling in just one of the divisions, the stone may fall on two or even four of the
divisions simultaneously. For example, in the figure below, the current state is a superposition of 00 and 01 (written as 00 + 01).

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/superposition.png" />

When the state falls as a superposition, for example 00 + 01, it means that it is both 00 **and** 01 at the same time.
However, just like the schrodinger cat turns out to be dead **or** alive after an external observer measure it, our **superposition** is
going to colapse to 00 **or** 01 when it interacts with something, for example, another stone or even the ground.

Finally, one last thing that you need to know about superpositions is that you can manipulate them applying **quantum logic gates**. 
For example, it is possible to transform the superposition described in the figure above from the 00 + 01 state to the basis state 00, just by applying one of our quantum gates.
This is a crucial hability that you need to master in the game since you want total control over which division the stone is going
to be on, so you dont need to handle a random state collapse to one of the basis state when the stone interacts with something.
The exaplanation of how the application of the gates works is going to be presented on the gates section.

### Mixed State

This is a special kind of state, which can be seen below, that looks like a superposition but in fact it is not. This state represents some **lack of information** that, sometimes, we have about a certain quantum system, due, for example, to noise. 
Thinking in terms of our dear schordinger cat, is like the cat was in a superposition of dead and alive simultaneously, but then a small
and annoying fly came and observed it, so that the cat collpased, for example, to the alive state (thanks God !!). In that case, we did not observe it yet, so we are not sure if it is dead or alive, but the quantum superposition doesnt exist anymore. 
What it really means is that we dont know in wich basis state the stone (or the cat) is at and we will only know when the stone interacts with something (in other words, when **we** observe the cat). The key difference from quantum superpositions is the fact
that applying any combination of gates wont change this state and it will always remain with four basis states until it collapse to one of the basis states on one of the divisions on the screen.
So this is definitly the **worst case state**, since you can not control where the stone is going to be.

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/mixed_state.png" />

## Quantum Gates

### Qubit Numbering
As we mentioned in the previous section, each of the four basis states is composed of two qubits. Even though one tetris stone is represented by both qubits, when we apply quantum gates we need to specify exactly on wich qubit the gate is going to act. In our case we have qubit one and qubit two. The first qubit is the left most qubit and second qubit is the one on the right. The indexing for the case where our state is 01 can be seen on the figure below:

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/qubits.png" />

Another example can be seen on the next figure where now we have a superposition state. In this case, when a gate is applied on, for example, qubit one, it will act on the first qubit of both basis states.

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/qubits_superposition.png" />

One important thing to note is that the basis states, for example, |00> can also be written as |0>|0>. This means that, for example, the |01> + |11> superposition can be written as (|0> + |1>)|1>.

### Basic Gates
The basic gates that we have in **Quantic Tetris** are based on some really common gates used in quantum computing. These gates are the **X**, **Z**, **H** and **CNOT**. The first three gates act on only one qubit, while the **CNOT** gate acts on two qubits. These gates can be fully understood by examining how they transforms qubits in the state |0> and in the state |1>. Their action on these states is described below.

#### X gate
This gate acts transforming |0> in |1> and |1> in |0>. It operation is ilustrated in the figure below:

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/gate_x.png" />

#### Z gate
This gate acts transforming |1> in -|1> and doing nothing to |0>. It operation is ilustrated in the figure below:

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/gate_z.png" />

#### H gate
This gate acts transforming |0> in a superposition |0> + |1> and transforming |1> in |0> - |1>. It operation is ilustrated in the figure below:

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/gate_h.png" />

It is important to note that, if this gate is applied to a superposition of, for example, |0> + |1> it transforms this superposition in the |0> state again. Also, if it is applied to |0> - |1> it transforms this superposition back to |1>.

#### CNOT gate
This gate acts on two qubits simultaneously. Basically, it applies a **X** gate on the targer qubit if the control qubit is 1. It operation is ilustrated in the figure below for the case where the control qubit is the first qubit:

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/gate_cnot.png" />

#### Examples
Now that you know what each of the gates do, we can see some examples of state manipulation.

The first example is presented on the next figure and shows how to transform a superposition of two basis states in just one.

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/ex1.png" />

The second example is presented on the next figure and shows how to transform a superposition of four basis states in just one. In this case its necessary to apply the **H** gate in each qubit, where the order doesnt matter.

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/ex2.png" />

Finally, our last example shows a very peculiar state called an entagled state. This state has an interesting story behind it involving the famous scientist Albert Einstein (lets say he didnt like it very much!) and it is a superposition like, for example, |00> + |11>. The curious thing about this superposition is that it cant be separated with one qubit multiplying a superposition of the other qubit, like in the last two examples (i.e. you cant write something like |0>(|0> + |1>). This implies that, to transform this superpostion in one of the basis states, you first need to apply the **CNOT** gate, and after that, you can apply the **H**. This process is ilustred in the figure below (where the *index 1* in the **CNOT** gate is to indicate that the control qubit is the first one) :

<img src="https://github.com/Joao-Bernardo/IBMQ_AWARDS/blob/master/images/ex3.png" />
