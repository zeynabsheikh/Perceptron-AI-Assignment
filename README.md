# 🧠 Single Layer Perceptron Implementation

## 📌 Overview
This project presents a complete implementation of a **single-layer perceptron** built from scratch using Python. The perceptron is one of the earliest and simplest machine learning models, designed to perform **binary classification** by learning a linear decision boundary.

This implementation demonstrates how a perceptron learns from data through weight updates and bias adjustments.

---

## 🎯 Objective
The main objectives of this project are:
- To understand the fundamentals of the perceptron algorithm
- To implement the perceptron without using any machine learning libraries
- To train the model on a simple logical dataset
- To observe how weights and bias are updated during training

---

## ⚙️ Technologies Used
- **Python 3.12**
- **NumPy**
- **Visual Studio Code (VS Code)**

---

## 🧩 Algorithm Explanation
The perceptron follows these steps:

1. Initialize weights and bias with zero values  
2. Loop over the dataset for a fixed number of epochs  
3. For each input:
   - Compute linear output:  
     `output = (weights ⋅ input) + bias`
   - Apply activation function (step function)
   - Calculate error:  
     `error = actual - predicted`
   - Update weights and bias:
     ```
     weights = weights + (learning_rate × error × input)
     bias = bias + (learning_rate × error)
     ```
4. Repeat until the model learns the pattern

---

## 📊 Dataset Used
A simple **AND Gate dataset** is used for training:

| Input 1 | Input 2 | Output |
|--------|--------|--------|
|   0    |   0    |   0    |
|   0    |   1    |   0    |
|   1    |   0    |   0    |
|   1    |   1    |   1    |

---

## 🧪 How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/Perceptron-AI-Assignment.git
