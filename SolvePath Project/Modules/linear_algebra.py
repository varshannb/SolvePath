# solvepath/linear_algebra.py
"""
=========================================================
              SolvePath Linear Algebra Module
=========================================================

Includes HIGHLY DETAILED, TUTOR-STYLE step-by-step solutions for:

• Matrix Addition & Subtraction
• Scalar Multiplication
• Matrix Multiplication (Dot Product steps)
• Determinants (2×2, 3×3)
• Inverse (2×2)
• Transpose
• Identity Matrix
• Solving 2×2 Systems (Cramer's Rule)

Returns:
• Solution object when show_steps=True
• Raw result when show_steps=False

=========================================================
"""

from typing import List, Union, Any
from solvepath.solution import Solution

# =========================================================
# INTERNAL HELPERS
# =========================================================

def _validate_matrix(M, name="Matrix"):
    if not isinstance(M, list) or not all(isinstance(row, list) for row in M):
        raise TypeError(f"{name} must be a list of lists (e.g., [[1,2], [3,4]]).")

def _fmt_mat(M):
    """Formats a matrix for nicer printing in steps."""
    return str(M).replace("],", "],\n   ")

# =========================================================
# MATRIX ADDITION
# =========================================================

def matrix_add(A: List[List[float]], B: List[List[float]], show_steps=False):
    _validate_matrix(A, "A")
    _validate_matrix(B, "B")
    
    rows = len(A)
    cols = len(A[0])
    
    # Calculate Result
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

    if not show_steps:
        return result

    steps = [
        f"Step 1: Check Dimensions.",
        f"   Matrix A is {rows}×{cols}. Matrix B is {rows}×{cols}.",
        f"   Dimensions match. Proceed.",
        "Step 2: Add corresponding elements (A_ij + B_ij)."
    ]

    for i in range(rows):
        for j in range(cols):
            val_a = A[i][j]
            val_b = B[i][j]
            res = val_a + val_b
            steps.append(f"   Position ({i+1},{j+1}): {val_a} + {val_b} = {res}")

    steps.append(f"Step 3: Final Matrix.\n   {result}")

    return Solution(
        given=f"A = {A}, B = {B}",
        to_find="A + B",
        equation="C_{ij} = A_{ij} + B_{ij}",
        formula_name="Matrix Addition",
        formula_used="A_{ij} + B_{ij}",
        formula_reason="We combine entries that occupy the same position in the grid.",
        explanation="The sum matrix is found by simply adding the numbers in the same spots.",
        steps=steps,
        answer=result
    )

# =========================================================
# MATRIX SUBTRACTION
# =========================================================

def matrix_sub(A: List[List[float]], B: List[List[float]], show_steps=False):
    _validate_matrix(A, "A")
    _validate_matrix(B, "B")
    
    rows = len(A)
    cols = len(A[0])
    
    result = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]

    if not show_steps:
        return result

    steps = [
        f"Step 1: Check Dimensions.",
        f"   Dimensions match ({rows}×{cols}). Proceed.",
        "Step 2: Subtract corresponding elements (A_ij - B_ij)."
    ]

    for i in range(rows):
        for j in range(cols):
            val_a = A[i][j]
            val_b = B[i][j]
            res = val_a - val_b
            steps.append(f"   Position ({i+1},{j+1}): {val_a} - {val_b} = {res}")

    steps.append(f"Step 3: Final Matrix.\n   {result}")

    return Solution(
        given=f"A = {A}, B = {B}",
        to_find="A - B",
        equation="C_{ij} = A_{ij} - B_{ij}",
        formula_name="Matrix Subtraction",
        formula_used="A_{ij} - B_{ij}",
        explanation="The difference matrix is found by subtracting the numbers in the same spots.",
        steps=steps,
        answer=result
    )

# =========================================================
# SCALAR MULTIPLICATION
# =========================================================

def scalar_mul(A: List[List[float]], k: float, show_steps=False):
    _validate_matrix(A, "A")
    
    rows = len(A)
    cols = len(A[0])
    
    result = [[A[i][j] * k for j in range(cols)] for i in range(rows)]

    if not show_steps:
        return result

    steps = [
        f"Step 1: Identify Scalar k = {k}.",
        "Step 2: Multiply every single element in A by k."
    ]

    for i in range(rows):
        for j in range(cols):
            val = A[i][j]
            res = val * k
            steps.append(f"   Position ({i+1},{j+1}): {val} × {k} = {res}")

    steps.append(f"Step 3: Final Matrix.\n   {result}")

    return Solution(
        given=f"Matrix A = {A}, k = {k}",
        to_find="Scalar Product kA",
        equation="B_{ij} = k · A_{ij}",
        formula_name="Scalar Multiplication",
        formula_used="k × A_{ij}",
        explanation="We scale the entire matrix by multiplying every entry by the constant k.",
        steps=steps,
        answer=result
    )

# =========================================================
# MATRIX MULTIPLICATION
# =========================================================

def matrix_mul(A: List[List[float]], B: List[List[float]], show_steps=False):
    _validate_matrix(A, "A")
    _validate_matrix(B, "B")

    m, n_a = len(A), len(A[0])
    n_b, p = len(B), len(B[0])

    if n_a != n_b:
        raise ValueError(
            f"Incompatible dimensions: A is {m}x{n_a}, B is {n_b}x{p}. "
            f"Cols of A must equal Rows of B."
        )

    # Result will be m x p
    result = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            val_sum = 0
            for k in range(n_a):
                val_sum += A[i][k] * B[k][j]
            result[i][j] = val_sum

    # ✅ IMPORTANT: When show_steps=False, return raw result directly
    if not show_steps:
        return result

    steps = [
        f"Step 1: Check Dimensions.",
        f"   A is {m}×{n_a}. B is {n_b}×{p}.",
        f"   Match confirmed ({n_a} = {n_b}). Result will be {m}×{p}.",
        "Step 2: Calculate Dot Products (Row of A × Col of B)."
    ]

    for i in range(m):
        for j in range(p):
            dot_terms = []
            val_sum = 0
            for k in range(n_a):
                a_val = A[i][k]
                b_val = B[k][j]
                product = a_val * b_val
                val_sum += product
                dot_terms.append(f"({a_val}×{b_val})")

            calculation_str = " + ".join(dot_terms)
            steps.append(f"   Cell ({i+1},{j+1}): Row {i+1} of A · Col {j+1} of B")
            steps.append(f"      = {calculation_str}")
            steps.append(f"      = {val_sum}")

    steps.append(f"Step 3: Assemble Final Matrix.\n   {result}")

    return Solution(
        given=f"A = {A}, B = {B}",
        to_find="Product AB",
        equation="(AB)_{ij} = Σ (A_{ik} · B_{kj})",
        formula_name="Matrix Multiplication",
        formula_used="Σ_{k=1}^{n} A_{ik} B_{kj}",
        formula_reason="Each entry is the dot product of a row from A and a column from B.",
        explanation="We multiply rows by columns and sum the products.",
        steps=steps,
        answer=result
    )


# =========================================================
# DETERMINANT 2×2
# =========================================================

def det_2x2(A: List[List[float]], show_steps=False):
    _validate_matrix(A)
    if len(A) != 2 or len(A[0]) != 2:
        raise ValueError("Input must be a 2x2 matrix.")

    a, b = A[0]
    c, d = A[1]
    result = a*d - b*c

    if not show_steps:
        return result

    return Solution(
        given=f"Matrix A = {A}",
        to_find="Determinant |A|",
        equation="|A| = ad - bc",
        formula_name="2×2 Determinant",
        formula_used="ad - bc",
        explanation="Product of the main diagonal minus the product of the other diagonal.",
        steps=[
            f"Step 1: Identify elements.",
            f"   a={a}, b={b}",
            f"   c={c}, d={d}",
            f"Step 2: Multiply diagonals.",
            f"   Main diagonal (ad) = {a} × {d} = {a*d}",
            f"   Other diagonal (bc) = {b} × {c} = {b*c}",
            f"Step 3: Subtract.",
            f"   {a*d} - {b*c} = {result}"
        ],
        answer=result
    )

# =========================================================
# DETERMINANT 3×3
# =========================================================

def det_3x3(A: List[List[float]], show_steps=False):
    _validate_matrix(A)
    if len(A) != 3 or len(A[0]) != 3:
        raise ValueError("Input must be a 3x3 matrix.")

    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]

    # Calculate 2x2 minors
    minor_a = e*i - f*h
    minor_b = d*i - f*g
    minor_c = d*h - e*g
    
    result = a*minor_a - b*minor_b + c*minor_c

    if not show_steps:
        return result

    return Solution(
        given=f"Matrix A = {A}",
        to_find="Determinant det(A)",
        equation="|A| = a(ei-fh) - b(di-fg) + c(dh-eg)",
        formula_name="3×3 Determinant (Cofactor Expansion)",
        formula_used="Σ (-1)^(i+j) · a_{ij} · M_{ij}",
        explanation="We expand along the top row, multiplying each element by its corresponding 2x2 minor determinant.",
        steps=[
            "Step 1: Expand along Row 1 (a, b, c).",
            f"   Elements: {a}, {b}, {c}",
            "Step 2: Calculate Minors (2x2 determinants).",
            f"   Minor for a ({a}): |{e} {f}| / |{h} {i}| = ({e}×{i}) - ({f}×{h}) = {minor_a}",
            f"   Minor for b ({b}): |{d} {f}| / |{g} {i}| = ({d}×{i}) - ({f}×{g}) = {minor_b}",
            f"   Minor for c ({c}): |{d} {e}| / |{g} {h}| = ({d}×{h}) - ({e}×{g}) = {minor_c}",
            "Step 3: Combine with signs (+ - +).",
            f"   {a}({minor_a}) - {b}({minor_b}) + {c}({minor_c})",
            f"   = {a*minor_a} - {b*minor_b} + {c*minor_c}",
            f"   = {result}"
        ],
        answer=result
    )

# =========================================================
# INVERSE 2×2
# =========================================================

def inverse_2x2(A: List[List[float]], show_steps=False):
    _validate_matrix(A, "A")
    if len(A) != 2 or len(A[0]) != 2:
        raise ValueError("Input must be a 2x2 matrix.")

    det = det_2x2(A)

    # ✅ Case 1: No inverse if determinant is 0
    if det == 0:
        msg = "Determinant is 0. Inverse does not exist (Matrix is Singular)."

        if not show_steps:
            return None

        return Solution(
            given=f"A = {A}",
            to_find="Inverse A⁻¹",
            equation="A⁻¹ does not exist when |A| = 0",
            formula_name="Singular Matrix",
            formula_used="If |A| = 0 ⇒ no inverse",
            explanation=msg,
            steps=[
                "Step 1: Compute determinant |A|.",
                f"   >> |A| = {det}",
                "Step 2: Check invertibility rule.",
                "   >> If |A| = 0, the matrix is singular.",
                "Step 3: Therefore inverse does NOT exist.",
            ],
            answer=None
        )

    # ✅ Case 2: Inverse exists
    a, b = A[0]
    c, d = A[1]

    # Adjugate matrix elements
    new_a, new_b = d, -b
    new_c, new_d = -c, a

    # Scale by 1/det
    res_a, res_b = new_a / det, new_b / det
    res_c, res_d = new_c / det, new_d / det

    result = [[res_a, res_b], [res_c, res_d]]

    if not show_steps:
        return result

    return Solution(
        given=f"A = {A}",
        to_find="Inverse A⁻¹",
        equation="A⁻¹ = (1/|A|) · Adj(A)",
        formula_name="2×2 Matrix Inverse",
        formula_used="(1/(ad-bc)) × [[d, -b], [-c, a]]",
        explanation="1. Calculate determinant. 2. Swap main diagonal elements. 3. Change signs of other diagonal. 4. Divide by determinant.",
        steps=[
            f"Step 1: Calculate Determinant.",
            f"   |A| = ({a}×{d}) - ({b}×{c}) = {det}",
            f"Step 2: Form the Adjugate Matrix.",
            f"   Swap a & d: {a} ↔ {d}",
            f"   Negate b & c: {b} → {-b}, {c} → {-c}",
            f"   Adj(A) = [[{new_a}, {new_b}], [{new_c}, {new_d}]]",
            f"Step 3: Multiply by 1/det (1/{det}).",
            f"   Row 1: {new_a}/{det}, {new_b}/{det}",
            f"   Row 2: {new_c}/{det}, {new_d}/{det}",
            f"Step 4: Final Inverse Matrix.",
            f"   {result}"
        ],
        answer=result
    )


# =========================================================
# TRANSPOSE
# =========================================================

def transpose(A: List[List[float]], show_steps=False):
    _validate_matrix(A)
    rows = len(A)
    cols = len(A[0])
    
    result = [[A[j][i] for j in range(rows)] for i in range(cols)]

    if not show_steps:
        return result

    steps = [
        f"Step 1: Identify dimensions.",
        f"   Input is {rows}×{cols}. Output will be {cols}×{rows}.",
        "Step 2: Swap rows and columns."
    ]
    
    for i in range(rows):
        steps.append(f"   Row {i+1} {A[i]} becomes Column {i+1} of the result.")

    steps.append(f"Step 3: Final Result.\n   {result}")

    return Solution(
        given=f"A = {A}",
        to_find="Transpose Aᵀ",
        equation="(Aᵀ)_{ij} = A_{ji}",
        formula_name="Matrix Transpose",
        formula_used="Swap indices i and j",
        explanation="We flip the matrix over its main diagonal. Rows become columns.",
        steps=steps,
        answer=result
    )

# =========================================================
# SOLVE 2×2 SYSTEM (CRAMER)
# =========================================================

def solve_2x2(A: List[List[float]], b: List[float], show_steps=False):
    # System Ax = b
    # A = [[a1, b1], [a2, b2]], b = [c1, c2]
    detA = det_2x2(A)

    if detA == 0:
        return None # Simplified handling for singularity

    # Construct matrices for Cramer's rule
    # Dx replaces 1st column with b
    Dx_mat = [[b[0], A[0][1]], [b[1], A[1][1]]]
    detX = det_2x2(Dx_mat)
    
    # Dy replaces 2nd column with b
    Dy_mat = [[A[0][0], b[0]], [A[1][0], b[1]]]
    detY = det_2x2(Dy_mat)

    x = detX / detA
    y = detY / detA
    result = (x, y)

    if not show_steps:
        return result

    return Solution(
        given=f"Matrix A={A}, Vector b={b}",
        to_find="Solution vector x",
        equation="x = Dx/D, y = Dy/D",
        formula_name="Cramer's Rule",
        formula_used="x_i = det(A_i) / det(A)",
        explanation="We solve the system by calculating determinants of modified matrices.",
        steps=[
            f"Step 1: Calculate Main Determinant (D).",
            f"   D = |A| = {detA}",
            f"Step 2: Calculate D_x (Replace col 1 with b).",
            f"   Matrix X: {Dx_mat}",
            f"   D_x = {detX}",
            f"Step 3: Calculate D_y (Replace col 2 with b).",
            f"   Matrix Y: {Dy_mat}",
            f"   D_y = {detY}",
            f"Step 4: Solve for variables.",
            f"   x = D_x / D = {detX} / {detA} = {x}",
            f"   y = D_y / D = {detY} / {detA} = {y}"
        ],
        answer=result
    )

# =========================================================
# IDENTITY MATRIX
# =========================================================

def identity(n: int, show_steps=False):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Size n must be a positive integer.")

    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    if not show_steps:
        return result

    steps = [
        f"Step 1: Create an empty {n}×{n} matrix.",
        "Step 2: Fill the main diagonal (top-left to bottom-right) with 1s.",
        "Step 3: Fill all other positions with 0s."
    ]
    
    return Solution(
        given=f"Size n = {n}",
        to_find=f"Identity Matrix I_{n}",
        equation="I_{ij} = 1 if i=j else 0",
        formula_name="Identity Matrix Construction",
        formula_used="Kronecker Delta δ_{ij}",
        explanation="The Identity matrix is the '1' of matrices. Multiplying by it leaves a matrix unchanged.",
        steps=steps,
        answer=result
    )

# =========================================================
# EXPORT
# =========================================================

__all__ = [
    "matrix_add",
    "matrix_sub",
    "scalar_mul",
    "matrix_mul",
    "det_2x2",
    "det_3x3",
    "inverse_2x2",
    "transpose",
    "solve_2x2",
    "identity"
]
