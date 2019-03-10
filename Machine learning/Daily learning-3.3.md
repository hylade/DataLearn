#### Cost function

Idea: Choose $\theta_0$, $\theta_1$ so that $h_\theta(x)$ is close to $y$ for our training examples $(x, y)$

即$\min\sum\limits^{m}_{i=1}(h_{\theta}(x^{(i)})-y^{(i)})^2​$

令$J(\theta_0,\theta_1)=\frac{1}{2m}\sum\limits^{m}_{i=1}(h_{\theta}(x^{(i)})-y^{(i)})^2$,将$J(\theta_0,\theta_1)$，称为 Cost function，也被称为 squared error function



#### Contour plot

A contour plot is a graph that contains many contour lines. A contour line of a two variable function has a constant value at all points of the same line

Taking any color and going along the circle, one would expect to get the same value of the cost function



### Linear regression with one variable

#### Gradient descent

1. Start with some $\theta_0​$, $\theta_1​$
2. Keep changing $\theta_0$, ​$\theta_1$ to reduce $J(\theta_0,\theta_1)$ until we hopefully end up at a minimum

repeat until convergence{

$\theta_j:=\theta_j-\alpha\frac{\partial}{\partial\theta_j}J(\theta_0,\theta_1)(for\ j=0\ and\ j=1)$

}

Where $\alpha$ is the learning rate;



Correct: Simultaneous update

$temp0 := \theta_0-\alpha\frac{\partial}{\partial\theta_0}J(\theta_0,\theta_1)​$

$temp1 := \theta_1-\alpha\frac{\partial}{\partial\theta_1}J(\theta_0,\theta_1)​$

$\theta_0 := temp0​$

$\theta_1:=temp1​$



Incorrect:

$temp0 := \theta_0-\alpha\frac{\partial}{\partial\theta_0}J(\theta_0,\theta_1)​$

$\theta_0 := temp0$

$temp1 := \theta_1-\alpha\frac{\partial}{\partial\theta_1}J(\theta_0,\theta_1)$

$\theta_1:=temp1$

