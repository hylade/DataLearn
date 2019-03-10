#### Gradient descent intuition

Repeat until convergence:

$\theta_1:=\theta_1-\alpha\frac{d}{d\theta_1}J(\theta_1) \tag{1}$

Regardless of the slope's sign for $\frac{d}{d\theta_1}J(\theta_1)$, $\theta_1$ eventually converges to its minimum value; when the slope is negative, the value of $\theta_1$ increases and when it is positive, the value of $\theta_1$ decreases;

We should adjust our parameter $\alpha$ to ensure that the gradient descent algorithm converges in a reasonable time. Failure to converge or too much time to obtain the minimum value imply that our step size is wrong

At the minimum, the derivative will always be 0 and thus we get: $\theta-1：=\theta_1-\alpha\times 0$



Gradient descent can converge to a local minimum, even with the learning rate $\alpha$ fixed, we can know from the $(1)$, as we approach a local minimum, gradient descent will automatically take smaller steps. So, no need to decrease $\alpha$ over time.

------

When specifically applied to the case of linear regression, a new form of the gradient descent equation can be derived, repeat until convergence:{

$\theta_0:=\theta_0-\alpha\frac{1}{m}\sum\limits^{m}_{i=1}(h_{\theta}(x_i)-y_i)$

$\theta_1:=\theta_1-\alpha\frac{1}{m}\sum\limits^{m}_{i=1}((h_{\theta}(x_i)-y_i)x_i)$

}

where m is the size of the training set, $\theta_0$ a constant that will be changing simultaneously with $\theta_1$ and $x_i$, $y_i$ are values of the given training set(data).



#### batch gradient descent

The method looks at every example in the entire training set on every step

------

### Matrices and vectors

Matrix: Rectangular array of numbers

Dimension of matrix: number of rows $\times$ numbers of columns

Vector: An n $\times$ 1 matrix



All our vectors and matrices will be 1-indexed. Note that for some programming languages, the arrays are 0-indexed; Matrices are usually denoted by uppercase names while vectors are lowercase.
