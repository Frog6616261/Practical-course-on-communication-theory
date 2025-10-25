# Probability and Statistics Exercises

## 1. Dice Experiment
A fair die is rolled. If the number of points is even, the experiment ends. If the number of points is odd, the die is rolled a second time, after which the experiment ends.  

**(a)** Describe the sample space of this experiment. How many elements does it contain?  
**(b)** Find the probability that the sum of points (considering a possible second roll) is divisible by six.  
**(c)** Let ξ be the sum and η be the product of the points rolled (considering a possible second roll). Find the probability distributions of the random variables ξ and η, as well as their expected values and variances.  
**(d)** Determine the joint distribution of the vector (ξ, η) and calculate cov(ξ, η). Are ξ and η independent?

## 2. Student Year Probability
At the Faculty of Physics, there are n students, of whom $n_k$ (k = 1, 2, 3, 4) study in the k-th year. Two students are randomly selected, and it is found that one of them has been studying longer than the other. What is the probability that this student is in the third year?

## 3. Tennis Balls Problem
A box contains 15 tennis balls, 9 of which are new. For the first game, three balls are randomly selected and returned to the box after the game. For the second game, three balls are also randomly selected. Find the probability that all balls selected for the second game are new.

## 4. Normal Distribution
The probability density function of a normally distributed random variable ξ is given by:  

$$
f_\xi(x) = \text{const} \cdot e^{-(x-\mu)^2 / (2\sigma^2)}, \quad -\infty < x < \infty
$$

**(a)** Determine the constant.  
**(b)** Determine the expected value and variance of ξ.  
**(c)** Determine the characteristic function $χ_ξ$(x).

## 5. Sum of Normal Random Variables
Using characteristic functions, prove that the sum of N independent normally distributed random variables with parameters ($µ_i$, $σ_i$) has a normal distribution. Specify the parameters of this distribution.

## 6. Linear Transformation of a Normal Random Variable
Let ξ be normally distributed with parameters (µ, σ²). Define a random variable η as  

$$
\eta = a\xi + b, \quad a < 0
$$

Determine the probability density function of η and sketch $f_η(x)$.

## 7. Transformation of a Continuous Random Variable
A random variable ξ has the distribution  

$$
f_\xi(x) = x^n, \quad x \in [-3a/2, -a/2], \quad n \text{ even}
$$

It is transformed as $η = sin(πξ / 2a)$. Find the cumulative distribution function and probability density of η. Determine the median m of the distribution.

## 8. Joint Distribution in a Square
Given the joint probability density  

$$
f_{\xi, \eta}(x, y) = \text{const} \cdot (x+y)
$$

of two continuous random variables ξ and η over the square ABCD with vertices A = (0,0), B = (0,1), C = (1,1), D = (1,0):  

**(a)** Find the constant.  
**(b)** Find the marginal densities fξ(x) and fη(y). Determine whether ξ and η are dependent.  
**(c)** Determine the expected values and variances of ξ and η.  
**(d)** Find the correlation coefficient of ξ and η. Are these variables correlated?  
**(e)** Write the regression equation of ξ on η and plot the regression line in the square ABCD.  
**(f)** Write the linear least squares regression equation for ξ and η and plot it in the square ABCD.

## 9. Sequence of Random Variables
A random variable Xn takes the values $e^{-n \cdot ln 2}$ and $e^{n \cdot ln 1.2}$ with equal probabilities. Can the law of large numbers be applied to the sequence Xn?

## 10. Python Implementation of Logistic Random Variable
Write a Python class implementing a generator for a logistic random variable ξ with probability density  

$$
f_\xi(x) = \frac{\lambda e^{-\lambda x}}{(1 + e^{-\lambda x})^2}, \quad \lambda > 0
$$

Use a uniform random variable generator with the rejection method and the inverse transform method. Compare the results with the implementation in `scipy.stats.logistic`.
