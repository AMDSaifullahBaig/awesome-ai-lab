# GRU — Gated Recurrent Unit

## What is GRU?

**GRU (Gated Recurrent Unit)** is a type of Recurrent Neural Network (RNN) designed to handle sequential data while maintaining useful information from previous time steps.

Unlike LSTM, GRU has **one hidden state** and does not have a separate cell state.

### Analogy

Think of GRU as a **smart editor** reading a story sentence by sentence.

* **Reset gate** → decides how much of the old information should be considered when creating new information.
* **Update gate** → decides how much old information to keep and how much new information to add.
* **Hidden state** → the current summary of everything important seen so far.

---

## GRU Architecture

At each time step:

```text
Current Input (xₜ)
       +
Previous Hidden State (hₜ₋₁)
       ↓
 ┌───────────────┐
 │   Reset Gate  │
 │  Update Gate  │
 │   Candidate   │
 └───────────────┘
       ↓
 New Hidden State (hₜ)
```

## Mathematics

### Update Gate

Controls how much new information replaces the previous hidden state.

$$
z_t = \sigma(W_z[x_t,h_{t-1}] + b_z)
$$

### Reset Gate

Controls how much previous information is used when creating the candidate state.

$$
r_t = \sigma(W_r[x_t,h_{t-1}] + b_r)
$$

### Candidate Hidden State

Creates possible new information.

$$
\tilde{h}_t =
\tanh(W_h[x_t,r_t \odot h_{t-1}] + b_h)
$$

### New Hidden State

Combines old and new information.

$$
h_t =
(1-z_t)\odot h_{t-1}
+
z_t\odot\tilde{h}_t
$$

Where:

* $\sigma$ = sigmoid
* $\tanh$ = hyperbolic tangent
* $\odot$ = element-wise multiplication
* $x_t$ = current input
* $h_{t-1}$ = previous hidden state
* $h_t$ = new hidden state

---

## GRU vs LSTM

| Feature                | GRU            | LSTM           |
| ---------------------- | -------------- | -------------- |
| Hidden state           | ✓              | ✓              |
| Separate cell state    | ✗              | ✓              |
| Main gates             | 2              | 3              |
| Parameters             | Fewer          | More           |
| Training               | Usually faster | Usually slower |
| Memory mechanism       | Simpler        | More explicit  |
| Long-term dependencies | ✓              | ✓              |

### When to use GRU?

Use GRU when you want:

* Good sequence modelling with a simpler architecture
* Faster training
* Fewer parameters
* A smaller model
* A good alternative to LSTM

### Advantages

* Fewer parameters than LSTM
* Faster training and inference
* Simpler architecture
* Can capture long-term dependencies
* Often performs similarly to LSTM

### Disadvantages

* Less explicit memory control than LSTM
* Performance can depend heavily on the dataset
* For some complex long-term dependencies, LSTM may work better

## In One Line

> **GRU = a simpler gated RNN that uses reset and update gates to control what information to forget, keep, and add.**
