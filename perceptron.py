import numpy as np

class Perceptron:
    def __init__(self, lr=0.1, epochs=10):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def activation(self, x):
        return 1 if x >= 0 else 0

    def fit(self, X, y):
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            for i in range(len(X)):
                linear_output = np.dot(X[i], self.weights) + self.bias
                y_pred = self.activation(linear_output)

                error = y[i] - y_pred

                self.weights += self.lr * error * X[i]
                self.bias += self.lr * error

    def predict(self, X):
        outputs = []
        for x in X:
            linear_output = np.dot(x, self.weights) + self.bias
            outputs.append(self.activation(linear_output))
        return outputs


# Example Dataset (AND Gate)
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y = np.array([0,0,0,1])

model = Perceptron(lr=0.1, epochs=10)
model.fit(X, y)

print("Weights:", model.weights)
print("Bias:", model.bias)

print("Predictions:", model.predict(X))