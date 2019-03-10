### Inverse and Transpose

A non square matrix does not have an inverse matrix. We can compute inverse of matrices in octave with the $pinv(A)$ function and in Matlab with the $inv(A)$ function.

Matrices that don't have an inverse are singular or degenerate



### Multivariate linear regression

Linear regression with multiple variables is also known as "Multivariate linear regression"

$x_j^{(i)}$ = value of feature $j$ in the $i^{th}$ training example

$x^{(i)}$ = the input (features) of the $i^{(th)}$ training example

$m$ = the number of training examples

$n$ = the number of features



$h_{\theta}(x)=\begin{bmatrix}\theta_0 &\theta_1&\cdots&\theta_n \end{bmatrix} \begin{bmatrix} x_0\\x_1\\ \vdots\\x_n \end{bmatrix} = \theta^Tx$ 

