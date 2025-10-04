# Assigments

## 1.  
Using the Gram–Schmidt orthogonalization process, orthonormalize the following systems of vectors, using the standard definition of the inner product for vectors:

- a) $v_1=(1,3,-2),\; v_2=(3,7,-2)$;  
- b) $v_1=(1,3,1),\; v_2=(5,1,3),\; v_3=(1,6,-8)$;  
- c) $v_1=(1,2,3),\; v_2=(2,1,1),\; v_3=(6,-7,-2)$.  


---

## 2.  
Let $p_0(x)=1, p_1(x)=x-1, p_2(x)=x^2-x+1$ — polynomials of the real variable $(x)$. Using the Gram–Schmidt orthogonalization method, construct polynomials orthonormal with respect to the inner product in $(L^2[-0.5, 0.5])$.


---

## 3.  
Show that if on an interval:  
- the function $f(x)$ is $k$-times differentiable;  
- $f^{(k)}(x)$ is continuous;  

then the coefficients of its Fourier series $\widehat f_n$ (where $n$ is the index) satisfy
$\widehat f_n=o\!\bigl(n^{-k}\bigr)$


---

## 4.  
Compute the discrete Fourier transform (DFT) of the triangular pulse $\wedge(x)$ from exercise 1.2.2 for some “reasonable” sampling frequency $f_s$. Plot the discrete and the continuous spectra on the same axes.

The triangular pulse \(\wedge(x)\) can be defined as:

$
\wedge(x) =
\begin{cases} 
1 - \frac{2}{\omega}|x|, & |x| \le \frac{\omega}{2}, \\[2mm]
0, & |x| > \frac{\omega}{2},
\end{cases}
$

where $\omega > 0$ is the half-width of the triangle (half of the base).


---

## 5.  
Consider the sinusoidal pulse $s(x)$ defined by
$[
s(x)=\begin{cases}
\sin\!\bigl(\tfrac{\pi x}{l}\bigr), & x\in[0,l],\\[4pt]
0, & \text{otherwise.}
\end{cases}
]$

Compute analytically the continuous and the discrete Fourier transforms of this sinusoidal pulse. Plot the results on the same axes in dB and compare them.


