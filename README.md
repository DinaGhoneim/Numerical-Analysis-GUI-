# Numerical Analysis Project

Welcome to the Numerical Analysis Project! This project provides an interactive GUI for exploring various numerical methods for solving equations. The methods implemented include:

- Bisection Method
- False Position Method
- Simple Fixed Point Method
- Newton Method
- Secant Method


Additionally, Chapter Two offers methods for solving systems of linear equations:

- Gauss Elimination
- Partial Gauss Elimination
- LU Decomposition
- LU Partial Pivoting
- Cramer's Rule
- Gauss-Jordan Elimination
- Jordan Partial Pivoting

## Installation

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. Install the required libraries using pip:
    ```sh
    pip install customtkinter sympy
    ```
3. Clone the repository to your local machine:
    ```sh
    git clone <repository_url>
    ```

## Usage

1. Navigate to the project directory.
2. Run the main script:
    ```sh
    python main.py
    ```

This will launch the main window of the application.

## Features

### Main Window

The main window provides access to two chapters:

- **Chapter One**: Contains methods for root finding.
- **Chapter Two**: Contains methods for solving systems of linear equations.

### Chapter One

Click on "Chapter One" to access the root finding methods:

- **Bisection Method**: 
  - This method involves finding the root by repeatedly bisecting the interval and selecting the subinterval in which the root lies.
- **False Position Method**: 
  - Also known as Regula Falsi, this method is similar to the bisection method but uses a linear approximation to find the root.
- **Simple Fixed Point Method**: 
  - This method involves rearranging the function and iterating from an initial guess until convergence.
- **Newton Method**: 
  - This method uses the derivative of the function to find successively better approximations to the root.
- **Secant Method**: 
  - This method is similar to Newton's method but does not require the calculation of the derivative.

### Detailed Method Explanation

#### Bisection Method

To use the Bisection Method:
1. Enter the function `f(x)`.
2. Enter the lower (`x_l`) and upper (`x_u`) bounds of the interval.
3. Specify the error tolerance (`ε_a`) or the number of iterations.
4. Click "Calculate" to find the root and display the intermediate steps.

#### False Position Method

To use the False Position Method:
1. Enter the function `f(x)`.
2. Enter the lower (`x_l`) and upper (`x_u`) bounds of the interval.
3. Specify the error tolerance (`ε_a`) or the number of iterations.
4. Click "Calculate" to find the root and display the intermediate steps.

#### Simple Fixed Point Method

To use the Simple Fixed Point Method:
1. Enter the function `f(x)`.
2. Enter the initial guess (`X_0`).
3. Specify the error tolerance (`ε_a`) or the number of iterations.
4. Click "Calculate" to find the root and display the intermediate steps.

#### Newton Method

To use the Newton Method:
1. Enter the function `f(x)`.
2. Enter the initial guess (`X_0`).
3. Specify the error tolerance (`ε_a`) or the number of iterations.
4. Click "Calculate" to find the root and display the intermediate steps.

#### Secant Method

To use the Secant Method:
1. Enter the function `f(x)`.
2. Enter the initial guesses (`X_0` and `X_1`).
3. Specify the error tolerance (`ε_a`) or the number of iterations.
4. Click "Calculate" to find the root and display the intermediate steps.


### Chapter Two

Click on "Chapter Two" to access methods for solving systems of linear equations:

1. **Gauss Elimination**: 
    - Enter the coefficient matrix and the constants vector.
    - Click "Calculate" to obtain the solution.

2. **Partial Gauss Elimination**: 
    - Enter the coefficient matrix and the constants vector.
    - Click "Calculate" to obtain the solution.

3. **LU Decomposition**: 
    - Enter the coefficient matrix and the constants vector.
    - Click "Calculate" to obtain the solution.

4. **LU Partial Pivoting**: 
    - Enter the coefficient matrix and the constants vector.
    - Click "Calculate" to obtain the solution.

5. **Cramer's Rule**: 
    - Enter the coefficient matrix and the constants vector.
    - Click "Calculate" to obtain the solution.

6. **Gauss-Jordan Elimination**: 
    - Enter the coefficient matrix and the constants vector.
    - Click "Calculate" to obtain the solution.

7. **Jordan Partial Pivoting**: 
    - Enter the coefficient matrix and the constants vector.
    - Click "Calculate" to obtain the solution.


### Customization

You can customize the look and feel of the application by modifying the `fg_color`, `text_color`, and other parameters in the code.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or new features.

### Contact Information
For questions, feedback, or issues, please reach out to:

# Dina Shalaby

# Email: dina90736@gmail.com

#GitHub: DinaGhoneim
---

