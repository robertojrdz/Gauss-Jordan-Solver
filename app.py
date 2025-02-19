from flask import Flask, render_template, request
from fractions import Fraction
import numpy as np
app = Flask(__name__)
app.debug = True

def convert_integral_floats(matrix):
    return np.where(matrix == matrix.astype(int), matrix.astype(int), matrix)

def fraction_filter(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)  # Show as integer
    elif isinstance(value, float):
        return str(Fraction(value).limit_denominator(1000))  # Convert to fraction
    return value  # Keep other values unchanged
app.jinja_env.filters["fraction"] = fraction_filter  # Register the filter
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/entry", methods = ['POST'])
def entry():
    if request.method == "POST":
        n = int(request.form['n'])
        matrix = np.zeros((n, n))
        return render_template("input.html", matrix=matrix, n=n)
    return render_template("index.html")
@app.route("/solve/<int:n>", methods = ['POST'])
def solve(n):
    m = n + 1
    n_matrix = (n*n) + 1
    if request.method == "POST":
        steps = np.zeros((n_matrix, n, m))
        matrix = np.zeros((n, m))
        initial = np.zeros((n, m))
        # Fill the Matrix
        for i in range(n):
            for j in range(m):
                matrix[i,j] = request.form[f"{i+1}_{j+1}"]
                initial[i,j] = request.form[f"{i+1}_{j+1}"]
                steps[0, i, j] = request.form[f"{i+1}_{j+1}"]
        matrix_2 = matrix.copy()
        print(matrix)
        print("")
        c = 1
        for h in range(n):
            if matrix[h, h] == 0:
                max_row = h + np.argmax(np.abs(matrix[h:, h]))  # Find row with max absolute value in column h
                if matrix[max_row, h] == 0:
                    # raise ValueError("Matriz singular detectada. El sistema no se puede resolver.")
                    return render_template("noResult.html", matrix = initial)
                matrix[[h, max_row]] = matrix[[max_row, h]]  # Swap rows

            isequal = matrix == matrix_2
            if not isequal.all():
                matrix_2 = matrix.copy()
                print(matrix)
                print("")
                for i in range(n):
                    for j in range(m):
                        steps[c, i, j] = matrix[i, j]
                c += 1

            x = matrix[h, h]
            for i in range(m):
                matrix[h, i] /= x

            isequal = matrix == matrix_2
            if not isequal.all():
                matrix_2 = matrix.copy()
                print(matrix)
                print("")
                for i in range(n):
                    for j in range(m):
                        steps[c, i, j] = matrix[i, j]
                c += 1
            y = []
            for i in range(n):
                y.append(matrix[i, h])
            for i in range(n):
                #steps
                for j in range(m):
                    if h != i:
                        matrix[i, j] = (matrix[h, j] *(-y[i])) + matrix[i, j]
                isequal = matrix == matrix_2
                if not isequal.all():
                    matrix_2 = matrix.copy()
                    print(matrix)
                    print("")
                    for l in range(n):
                        for j in range(m):
                            steps[c, l, j] = matrix[l, j]
                    c += 1
        initial = np.array(convert_integral_floats(initial))
        steps = np.array([convert_integral_floats(matrix) for matrix in steps], dtype=object)
        filtered_steps = np.array([matrix for matrix in steps if not np.all(matrix == 0)])
        solution = []
        for i in range(n):
            solution.append(matrix[i, n])
        return render_template("result.html", steps=filtered_steps, matrix = initial, solution=solution)
    return render_template("index.html")


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run(host='localhost', port=5000)