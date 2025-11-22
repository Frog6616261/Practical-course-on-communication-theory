# Homework

1.  Show that\
    $$\hat{X}(\omega) = -i \cdot \operatorname{sgn}(\omega) X(\omega).$$

2.  Prove the properties of the Hilbert transform:

    (a) If (x(t) = x(-t)), then\
        $$\hat{x}(t) = -\hat{x}(-t).$$\
    (b) If (x(t) = -x(-t)), then\
        $$\hat{x}(t) = \hat{x}(-t).$$\
    (c) $$\hat{\hat{x}}(t) = -x(t).$$\
    (d) $$\int_{-\infty}^{\infty} x^{2}(t)\, dt = \int_{-\infty}^{\infty} \hat{x}^{2}(t)\, dt.$$\
    (e) $$\int_{-\infty}^{\infty} x(t)\hat{x}(t)\, dt = 0.$$

3.  Compute the Hilbert transform of the functions (x(t)):

    (a) (x(t) = `\text{const}`{=tex};)\
    (b) (x(t) = `\sin`{=tex}(`\omega `{=tex}t);)\
    (c) (x(t) = `\cos`{=tex}(`\omega `{=tex}t);)\
    (d) $$x(t) = \frac{1}{1 + t^{2}}.$$

4.  The figure below shows four waveforms (s_i(t)), defining a certain
    signal space.

    (a) Determine the dimension of the given signal space and obtain a
        set of basis functions.\
    (b) Use the basis functions to represent the four signal waveforms
        as vectors (s_1, s_2, s_3, s_4.)\
    (c) Determine the minimum distance between any pair of vectors.

5.  Let\
    $$Z(t) = X(t) + jY(t)$$\
    be a complex random process, where (X(t)) and (Y(t)) are real,
    independent, zero-mean, jointly stationary Gaussian random
    processes. Their power spectral densities are known:

    $$
    S_X(f) = S_Y(f) =
    \begin{cases}
    N_0, & |f| \le W, \\
    0, & \text{otherwise}.
    \end{cases}
    $$

    (a) Find (E\[Z(t)\]) and (R_Z(t+`\tau`{=tex}, t)), and show that
        (Z(t)) is stationary.\
    (b) Find the power spectral density of the process (Z(t)).\
    (c) Assume that (`\varphi`{=tex}\_1(t), `\varphi`{=tex}\_2(t),
        `\ldots`{=tex}, `\varphi`{=tex}\_n(t)) are orthonormal and all
        (`\varphi`{=tex}\_j(t)) are band-limited to (\[-W, W\]). Define
        random variables (Z_j) as projections of (Z(t)) onto
        (`\varphi`{=tex}\_j(t)):

    $$
    Z_j = \int_{-\infty}^{\infty} Z(t)\varphi_j^*(t)\, dt, \quad j = 1,2,\ldots,n.
    $$

    Determine (E\[Z_j\]) and (E\[Z_j Z_k\^\*\]), and show that (Z_j) are
    i.i.d. zero-mean Gaussian random variables. Find their variance.

    (d) Define

    $$
    \tilde{Z}(t) = Z(t) - \sum_{j=1}^n Z_j \varphi_j(t)
    $$

    as the error of approximating (Z(t)) by a linear combination of
    (`\varphi`{=tex}\_j(t)). Show that

    $$
    E[\tilde{Z}(t) Z_k^*] = 0
    $$

    for all (k = 1, 2, `\ldots`{=tex}, n).

6.  Write a Python class implementing:

    (a) computation of a bandpass signal (x(t)) from a given low-pass
        signal (x_l(t));\
    (b) computation of the analytic signal from a given bandpass signal
        (x(t));\
    (c) computation of the low-pass signal (x_l(t)) from a given
        bandpass signal (x(t));\
    (d) computation of the envelope of a bandpass signal from a given
        low-pass signal (x_l(t)).

    Demonstrate the results of the code using the spectrum
    (X_l(`\omega`{=tex})) from problem **4.1-1**.
