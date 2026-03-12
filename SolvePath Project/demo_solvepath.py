"""
=========================================================
                SOLVEPATH – MASTER DEMO
=========================================================
This demo showcases the core capabilities of the SolvePath
library across multiple mathematical domains.

Key Objectives:
• Pedagogical Transparency: Step-by-step explanations [cite: 3, 5]
• Operational Efficiency: Error-gated computation [cite: 23]
• Professional Output: Structured Solution architecture [cite: 30]
=========================================================
"""

# Professional Header Utilities for Structured Delivery 
def section_header(title):
    print(f"\n\n{'='*65}")
    print(f" {title.upper()} ".center(65, "="))
    print(f"{'='*65}\n")

def sub_header(title):
    print(f"\n--- {title} ---\n")

# =========================================================
# 1. ARITHMETIC (Operational Efficiency)
# =========================================================
from solvepath.arithmetic import add, divide, percentage

section_header("Arithmetic")

sub_header("Add (10 + 5)")
print(add(10, 5, show_steps=True))

sub_header("Divide (20 ÷ 4)")
print(divide(20, 4, show_steps=True))

sub_header("Percentage (25 out of 200)")
print(percentage(25, 200, show_steps=True))

# =========================================================
# 2. ALGEBRA (Logic Execution) [cite: 43]
# =========================================================
from solvepath.algebra import (
    solve_linear, quadratic_roots, expand_square_plus, 
    polynomial_eval, ap_nth_term
)

section_header("Algebra")

sub_header("Linear Equation (2x - 4 = 0)")
print(solve_linear(2, -4, show_steps=True))

sub_header("Quadratic Equation (x² - 5x + 6 = 0)")
print(quadratic_roots(1, -5, 6, show_steps=True))

sub_header("Expand (a + b)² where a=3, b=4")
print(expand_square_plus(3, 4, show_steps=True))

sub_header("Polynomial Evaluation f(x) at x=2")
# Uses Horner's Method for optimized sourcing of results [cite: 43]
print(polynomial_eval([1, -3, 2], 2, show_steps=True))

sub_header("Arithmetic Progression (a=2, d=3, n=5)")
print(ap_nth_term(2, 3, 5, show_steps=True))

# =========================================================
# 3. GEOMETRY & TRIGONOMETRY (Spatial Analytics)
# =========================================================
from solvepath.geometry import triangle_area, circle_area
from solvepath.trigonometry import sin_angle, cos_angle

section_header("Geometry & Trigonometry")

sub_header("Area of Triangle (Base=10, Height=5)")
print(triangle_area(10, 5, show_steps=True))

sub_header("Area of Circle (Radius=7)")
print(circle_area(7, show_steps=True))

sub_header("Sine Ratio (30°)")
# Uses verified aliases to ensure system reliability [cite: 10]
print(sin_angle(30, show_steps=True))

# =========================================================
# 4. CALCULUS (Advanced Analytics)
# =========================================================
from solvepath.calculus import (
    derivative_power, derivative_ln, integral_power, 
    integral_sin, limit_direct, series_maclaurin_exp
)

section_header("Calculus")

sub_header("Derivative of x³ at x = 2")
print(derivative_power(3, 2, show_steps=True))

sub_header("Integration: ∫ x² dx")
print(integral_power(2, show_steps=True))

sub_header("Limit: lim x→2 (x² + 1)")
print(limit_direct(lambda x: x*x + 1, 2, show_steps=True))

sub_header("Maclaurin Series (e¹ to 5 terms)")
print(series_maclaurin_exp(1, terms=5, show_steps=True))

# =========================================================
# 5. ADVANCED DOMAINS
# =========================================================
from solvepath.linear_algebra import matrix_add
from solvepath.vectors import dot
from solvepath.statistics import mean, median
from solvepath.probability import probability
from solvepath.number_theory import gcd, lcm
from solvepath.expression_solver import solve_expression

section_header("Statistics, Advanced & Expressions")

sub_header("Matrix Addition (A + B)")
A, B = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
print(matrix_add(A, B, show_steps=True))

sub_header("Dot Product of Vectors")
print(dot([1, 2, 3], [4, 5, 6], show_steps=True))

sub_header("Mean Calculation")
print(mean([2, 4, 6, 8, 10], show_steps=True))

sub_header("GCD Analysis (48, 18)")
print(gcd(48, 18, show_steps=True))

sub_header("Expression Solver (2 + 3 * 4)")
# Automates quantity estimates and reduces manual errors [cite: 40]
print(solve_expression("2 + 3 * 4", show_steps=True))

print("\n\n" + "="*65)
print("SOLVEPATH DEMO EXECUTION FINALIZED".center(65))
print("="*65 + "\n")
