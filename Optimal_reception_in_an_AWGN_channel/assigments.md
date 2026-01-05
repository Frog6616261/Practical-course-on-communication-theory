
# Communication Systems — Problems

## 1. Ternary Communication System

A ternary communication system transmits one of three equiprobable signals:  
$s(t)$, $0$, or $-s(t)$ every $T$ seconds.

The received signal is given by:
- $r_1(t) = s(t) + z(t)$,
- $r_1(t) = z(t)$, or
- $r_1(t) = -s(t) + z(t)$,

where $z(t)$ is white Gaussian noise with  
$\mathbb{E}[z(t)] = 0$ and autocorrelation function  
$R_z(\tau) = \mathbb{E}[z(t) z^*(\tau)] = 2N_0 \delta(t - \tau)$.

The optimal receiver computes the correlation metric

$$
U = \Re \left\{ \int_0^T r_1(t) s^*(t)\, dt \right\}
$$

and compares $U$ with thresholds $A$ and $-A$:

- If $U > A$, decide that $s(t)$ was transmitted.
- If $U < -A$, decide that $-s(t)$ was transmitted.
- If $-A < U < A$, decide that $0$ was transmitted.

**Tasks:**
- Determine the three conditional error probabilities:
  - $P_e$ given that $s(t)$ was transmitted;
  - $P_e$ given that $-s(t)$ was transmitted;
  - $P_e$ given that $0$ was transmitted.
- Determine the average probability of error $P_e$ as a function of the threshold $A$, assuming the three symbols are a priori equiprobable.
- Determine the value of $A$ that minimizes $P_e$.

---

## 2. Binary Communication System with Non-Gaussian Noise

In a binary communication system, two equiprobable messages are used:
$$
\mathbf{s}_1 = (1, 1), \quad \mathbf{s}_2 = (-1, -1).
$$

The received signal is
$$
\mathbf{r} = \mathbf{s} + \mathbf{n},
$$
where $\mathbf{n} = (n_1, n_2)$.

It is assumed that $n_1$ and $n_2$ are independent random variables, each with probability density function
$$
f(n) = \frac{1}{2} e^{-|n|}.
$$

**Task:**
- Determine and sketch the decision regions $D_1$ and $D_2$ for this communication system.

---

## 3. Spectral Efficiency of Modulation Schemes

Assume that information must be transmitted at a rate of $R$ bit/s.  
Determine the required bandwidth for each of the following six communication systems and rank them in order of increasing spectral efficiency, starting from the most efficient and ending with the least efficient.

- Orthogonal binary frequency-shift keying (BFSK).
- 8-ary phase-shift keying (8PSK).
- Quadrature phase-shift keying (QPSK).
- 64-point quadrature amplitude modulation (64-QAM).
- Binary phase-shift keying (BPSK).
- Orthogonal 16-ary frequency-shift keying (16-FSK).

---

## 4. Matched Filter and Correlator Analysis

Consider the signal
$$
s(t) =
\begin{cases}
\dfrac{A}{T}\, t \cos(2\pi f_c t), & 0 \le t \le T, \\
0, & \text{otherwise}.
\end{cases}
$$

**Tasks:**
- Determine the impulse response of the matched filter for this signal.
- Determine the matched-filter output at time $t = T$.
- Assume that the signal $s(t)$ is applied to a correlator that computes the correlation of the input signal with itself. Determine the correlator output at time $t = T$. Compare this result with the result obtained in the previous item.

---

## 5. Optimal BPSK Receiver Simulation

Implement an optimal receiver for binary phase-shift keying (BPSK) as a Python class and analyze its noise immunity using Monte Carlo simulation.

**Tasks:**
- Estimate the bit error rate (BER) as a function of the signal-to-noise ratio (SNR).
- Compare the simulated BER curve $\text{BER} = f(\text{SNR})$ with the corresponding theoretical expression.
