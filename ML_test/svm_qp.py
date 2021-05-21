import argparse
import cvxopt
import numpy as np
import utils
import numpy as np

def predict(X, w, bias):

    '''
    Parameters
    ----------
    X: matrix of shape (n, d)
       Training data

    w: matrix of shape (d, 1)
       SVM weight vector

    bias: scalar

    Returns
    -------
    y_pred: matrix of shape (n, 1)
            Predicted values
    '''
    


def make_P(**kwargs):
    '''
    Parameters
    ----------
    kwargs: change to whatever you want

    Returns
    -------
    P: matrix of shape (n, n)
       positive semidefinite matrix for the quadratic program
    '''
    raise NotImplementedError

def make_q(**kwargs):
    '''
    Return the q vector in the standard quadratic program formulation of the SVM dual problem

    Parameters
    ----------
    kwargs: change to whatever you want

    Returns
    -------
    q: matrix of shape (n, 1)
       positive semidefinite matrix for the quadratic program
    '''
    raise NotImplementedError

def make_inequality_constraints(**kwargs):
    '''
    Return the G, h matrices/vectors in the standard quadratic program formulation
        for the SVM dual problem

    Parameters
    ----------
    kwargs: change to whatever you want

    Returns
    -------
    G: matrix of shape (m, n)

    h: matrix of shape (m, 1)
    '''
    raise NotImplementedError

def make_equality_constraints(**kwargs):
    '''
    Return the A, b matrices/vectors in the standard quadratic program for the SVM dual problem

    Parameters
    ----------
    kwargs: change to whatever you want

    Returns
    -------
    A: matrix of shape (p, n)

    b: matrix of shape (p, 1)
    '''
    raise NotImplementedError

def accuracy(X, y, w, bias):
    '''
    Compute the accuracy of the prediction rule determined by the
        given weight and bias vector on input data X, y

    Parameters
    ----------
    X: matrix of shape (n, d)
       Training data

    y: matrix of shape (n, 1)
       Target values

    w: matrix of shape (d, 1)
       SVM weight vector

    bias: scalar
          SVM bias term

    Returns
    -------
    acc: float
         accuracy
    '''
    raise NotImplementedError

def make_weight_bias(X, y, qp_solution):
    '''
    Given the solution of the SVM dual quadratic program
    construct the corresponding w weight vector

    Parameters
    ----------
    X: matrix of shape (n, d)
       Training data

    y: matrix of shape (n, 1)
       Target values

    qp_solution: output of cvxopt.solvers.qp

    Returns
    -------
    w: vector of shape (d, 1)
       SVM weight vector
    bias: scalar
          bias term
    '''
    raise NotImplementedError

def dual_svm(X_train, y_train, X_test, y_test, C):
    '''
    Minimize     1/2 alpha^T P alpha - q^T x
    Subject to   Gx <= h
                 Ax  = b

    here alphas = x
    G = X @ X.T
    '''

    print(f'X_train.shape : {X_train.shape}, y_train.shape : {y_train.shape}')

    P_value = np.multiply(y_train, X_train)
    P_value = np.dot(P_value, P_value.T) * 1.0

    q_value = -np.ones((X_train.shape[0], 1))

    G_value = np.vstack((np.vstack((np.eye(X_train.shape[0])*1.0, np.eye(X_train.shape[0])))))
    h_value = np.hstack((np.zeros(X_train.shape[0]), np.ones(X.shape[0]) * C))

    A_value = y_train.reshape(1, -1)

    b_value = np.zeros(1)

    # YOUR CODE HERE
    P = cvxopt.matrix(P_value)
    q = cvxopt.matrix(q_value)
    G = cvxopt.matrix(G_value)
    h = cvxopt.matrix(h_value)
    A = cvxopt.matrix(A_value)
    b = cvxopt.matrix(b_value)

    # Note that the cvxopt.solvers.qp function expects objects of type cvxopt.matrix
    # See: https://cvxopt.org/examples/tutorial/numpy.html
    sol = cvxopt.solvers.qp(P, q, G, h, A, b)

    weight, bias = make_weight_bias(X_train, y_train, sol)
    test_acc = accuracy(X_test, y_test, weight, bias)
    train_acc = accuracy(X_train, y_train, weight, bias)
    print("Train acc: {:.3f}".format(train_acc))
    print("Test acc: {:.3f}".format(test_acc))

def main(args):
    # Note that we do not add bias here
    X_train, y_train, X_test, y_test = utils.load_data(args.fname, add_bias=False)
    dual_svm(X_train, y_train, X_test, y_test, args.C)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fname', type=str, default='news.mat')
    parser.add_argument('--C', type=float, default=1.0)
    args = parser.parse_args()
    main(args)
