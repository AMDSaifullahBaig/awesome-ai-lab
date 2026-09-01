# LSTM Gates and Equations

At each time step, an LSTM receives three pieces of information:

* Current input: $x_t$
* Previous hidden state: $h_{t-1}$
* Previous cell state: $c_{t-1}$

The LSTM uses gates to decide what information to forget, store, and expose.

---

## 1. Forget Gate

The forget gate decides how much information from the previous cell state should be retained.

$$
f_t = \sigma(W_f[h_{t-1}, x_t] + b_f)
$$

The sigmoid function produces values between 0 and 1.

* A value close to **0** means: forget this information.
* A value close to **1** means: keep this information.

---

## 2. Input Gate

The input gate decides how much new information should be stored.

$$
i_t = \sigma(W_i[h_{t-1}, x_t] + b_i)
$$

The LSTM also creates a candidate cell state containing possible new information.

$$
\tilde{c}_t = \tanh(W_c[h_{t-1}, x_t] + b_c)
$$

The input gate controls how much of this candidate information should be added to the memory.

---

## 3. Cell State Update

The cell state is updated using both the useful old memory and the useful new information.

$$
c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t
$$

Where $\odot$ represents **element-wise multiplication**.

The process can be understood as:

```text
Previous Memory
       ↓
Forget unnecessary information
       +
Add useful new information
       ↓
Updated Cell State
```

---

## 4. Output Gate

The output gate decides which information from the updated cell state should become the new hidden state.

$$
o_t = \sigma(W_o[h_{t-1}, x_t] + b_o)
$$

The new hidden state is calculated as:

$$
h_t = o_t \odot \tanh(c_t)
$$

The hidden state represents the information that the LSTM exposes at the current time step.

---

## Complete LSTM Flow

```text
Previous Hidden State (hₜ₋₁)
Previous Cell State   (cₜ₋₁)
Current Input         (xₜ)
            │
            ▼
       Forget Gate
            │
            ▼
        Input Gate
            │
            ▼
      Update Cell State
            │
            ▼
       Output Gate
            │
            ▼
New Hidden State (hₜ)
New Cell State   (cₜ)
```

## Important Symbols

| Symbol    | Meaning                                |
| --------- | -------------------------------------- |
| $x_t$     | Current input                          |
| $h_{t-1}$ | Previous hidden state                  |
| $h_t$     | New hidden state                       |
| $c_{t-1}$ | Previous cell state                    |
| $c_t$     | New cell state                         |
| $\sigma$  | Sigmoid activation function            |
| $\tanh$   | Hyperbolic tangent activation function |
| $\odot$   | Element-wise multiplication            |
| $W$       | Learnable weights                      |
| $b$       | Learnable biases                       |

## Key Idea

A basic RNN mainly carries information using its hidden state. An LSTM introduces a separate **cell state**, allowing it to control what information should be retained or forgotten across a sequence.
