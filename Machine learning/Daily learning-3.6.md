### Gradient descent for multiple variables

Hypothesis: $h_{\theta}(x)=\theta^Tx=\theta_0x_0+\theta_1x_1+\cdots+\theta_nx_n$

Parameters: $\theta_0, \theta_1, \cdots,\theta_n$

Cost function: $J(\theta_0, \theta_1, \cdots, \theta_n)=\frac{1}{2m}\sum\limits_{i=1}^m(h_{\theta}(x^{(i)})-y^{(i)})^2$

Gradient descent: Repeat{

$\theta_j:=\theta_j-\alpha\frac{\partial}{\partial\theta_j}J(\theta_0,\cdots,\theta_n)$, (simultaneously update for every $j=0,\cdots,n$)

}

For multiple variables ($n\geq1$):

Repeat{

$\theta_j=\theta_j-\alpha\frac{1}{m}\sum\limits_{i=1}^m(h_{\theta}(x^{(i)})-y^{(i)})x_j^{(i)}$, simultaneously update $\theta_j$ for $j=0, \cdots,n$

}



### Gradient descent in practice - Feature scaling

Idea: Make sure features are on a similar scale; Get every feature into ==approximately== a $-1\leq x_i\leq1​$ range.

To speed up gradient descent by having each of input values in roughly the same range; this is because $\theta$ will descend quickly on small ranges and slowly on large ranges, and so will oscillate inefficiently down to the optimum when the variables are very uneven



#### Mean normalization

Replace $x_i$ with $x_i-\mu_i$ to make features have approximately zero mean (==Do not apply to $x_0=1$==)

$x_i=\frac{x_i-\mu_i}{S_i}$

where, $\mu_i​$ is the average of $x_i​$ in training set; and $S_i​$ is the range (max-min)



### Gradient descent in practice - learning rate

#### Debugging gradient descent

Make a plot with number of iterations on the x-axis. Now plot the cost function, $J(\theta)$ over the number of iterations of gradient descent. If $J(\theta)$ ever increases, then you probably need to decrease $\alpha$



#### Automatic convergence test

Declare convergence if $J(\theta)$ decreases by less than E in one iteration, where E is some small value such as $10^{-3}$.



### Summary

1. If $\alpha$ is too small: slow convergence
2. If $\alpha$ is too large: may not decrease on every iteration and thus may not converge



### Features and polynomial regression

We can combine multiple features into one

We can change the behavior or curve of our hypothesis function by making it a quadratic, cubic or square root function (or any other form)



#### Normal equation

We will minimize $J$ by explicitly taking its derivatives with respect to the $\theta_j$, and setting them to zero

$\theta=(X^TX)^{-1}X^Ty$

There is ==no need== to do feature scaling with the normal equation



|      Gradient Descent      |               Normal Equation               |
| :------------------------: | :-----------------------------------------: |
|    Need to choose alpha    |           No need to choose alpha           |
|   Needs many iterations    |             No need to iterate              |
|         O($kn^2$)          | O(n^3), need to calculate inverse of $X^TX$ |
| Works well when n is large |           Slow if n is very large           |



### Normal equation noninvertibility

The 'pinv' function will give you a value of $\theta$ even if $X^T$ is not invertible



If $X^TX$ is noninvertible, the common causes might be having:

1. Redundant features, where two features are very closely related
2. Too many features. In this case, delete some features or use "regularization"































