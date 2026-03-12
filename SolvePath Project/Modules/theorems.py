# solvepath/theorems.py
"""
==========================================================
              SolvePath Theorems Module
==========================================================

Includes HIGHLY DETAILED step-by-step explanations and results for:

• Pythagorean Theorem
• Binomial Theorem
• Taylor Series (Conceptual)
• Maclaurin Series (Conceptual)
• Euler’s Formula
• Green’s Theorem
• Gauss Divergence Theorem
• Stokes’ Theorem
• Fundamental Theorem of Calculus
• Mean Value Theorem
• Intermediate Value Theorem
• AM–GM Inequality
• Cauchy–Schwarz Inequality
• Triangle Inequality

==========================================================
"""

import math
from math import comb
from typing import Union, List, Tuple
from solvepath.solution import Solution

# ==========================================================
# INTERNAL VALIDATION HELPERS
# ==========================================================

def _validate_positive(val, name):
    if not isinstance(val, (int, float)):
        raise TypeError(f"{name} must be a number.")
    if val < 0:
        raise ValueError(f"{name} cannot be negative.")

def _validate_integer(val, name):
    if not isinstance(val, int):
        raise TypeError(f"{name} must be an integer.")
    if val < 0:
        raise ValueError(f"{name} cannot be negative.")

# ==========================================================
# PYTHAGOREAN THEOREM
# ==========================================================

def pythagoras(a: float, b: float, show_steps=False):
    # Validation
    _validate_positive(a, "Side 'a'")
    _validate_positive(b, "Side 'b'")

    result = math.sqrt(a * a + b * b)

    if not show_steps:
        return result

    return Solution(
        given=f"Right-angled triangle sides: a = {a}, b = {b}",
        to_find="The hypotenuse c",
        equation="c² = a² + b²",
        formula_name="Pythagorean Theorem",
        formula_used="c = √(a² + b²)",
        formula_reason="To find the longest side of a right triangle given the two shorter sides.",
        symbol_explanation="a, b are legs; c is the hypotenuse.",
        explanation="The area of the square on the hypotenuse equals the sum of the areas of the squares on the other two sides.",
        steps=[
            f"Step 1: Identify the legs.\n   a = {a}, b = {b}",
            f"Step 2: Square the first side.\n   a² = {a} × {a} = {a*a}",
            f"Step 3: Square the second side.\n   b² = {b} × {b} = {b*b}",
            f"Step 4: Sum the squares.\n   {a*a} + {b*b} = {a*a + b*b}",
            f"Step 5: Take the square root.\n   c = √({a*a + b*b})",
            f"Step 6: Final Calculation.\n   c = {result}"
        ],
        answer=result
    )

# ==========================================================
# BINOMIAL THEOREM
# ==========================================================

def binomial_theorem(a: float, b: float, n: int, show_steps=False):
    # Validation
    _validate_integer(n, "Exponent 'n'")
    
    terms = []
    # Pre-calculate terms for the result
    for k in range(n + 1):
        coeff = comb(n, k)
        term_val = coeff * (a ** (n - k)) * (b ** k)
        terms.append(term_val)

    result = sum(terms)

    if not show_steps:
        return result

    steps = [
        f"Step 1: Setup.\n   Expand ({a} + {b})^{n}",
        "Step 2: Apply Binomial Formula.\n   Σ (n choose k) * a^(n-k) * b^k",
        "Step 3: Calculate each term individually:"
    ]

    for k in range(n + 1):
        c = comb(n, k)
        p_a = n - k
        p_b = k
        term_val = terms[k]
        
        # Detailed arithmetic for this term
        steps.append(
            f"   k={k}: Coeff C({n},{k})={c} | a^{p_a}={a**p_a} | b^{p_b}={b**p_b}\n"
            f"         Term = {c} * {a**p_a} * {b**p_b} = {term_val}"
        )

    steps.append(f"Step 4: Sum all terms.\n   { ' + '.join(map(str, terms)) }")
    steps.append(f"Step 5: Final Result.\n   {result}")

    return Solution(
        given=f"a = {a}, b = {b}, n = {n}",
        to_find="Expansion of (a + b)ⁿ",
        equation="(a + b)ⁿ = Σ C(n,k) aⁿ⁻ᵏ bᵏ",
        formula_name="Binomial Theorem",
        formula_used="Σ C(n,k) aⁿ⁻ᵏ bᵏ",
        formula_reason="To expand powers of binomials without multiplying them out manually.",
        symbol_explanation="C(n,k) comes from Pascal's Triangle.",
        explanation="We distribute the power n across a and b in every possible combination.",
        steps=steps,
        answer=result
    )

# ==========================================================
# TAYLOR SERIES (CONCEPTUAL)
# ==========================================================

def taylor_series(f_name: str, a: float, n: int, show_steps=False):
    """
    Conceptual explanation of Taylor Series expansion.
    """
    _validate_integer(n, "Number of terms 'n'")

    result = f"Taylor series of {f_name}(x) about x = {a} (first {n} terms)"

    if not show_steps:
        return result

    return Solution(
        given=f"Function f(x) = {f_name}(x), Center a = {a}",
        to_find=f"Approximation using first {n} terms",
        equation="f(x) ≈ Σ f⁽ᵏ⁾(a)(x − a)ᵏ / k!",
        formula_name="Taylor Series",
        formula_used="f(a) + f'(a)(x-a) + f''(a)(x-a)²/2! + ...",
        formula_reason="Approximates complex curves using simple polynomials.",
        symbol_explanation="f⁽ᵏ⁾ is the kth derivative. k! is factorial.",
        explanation="We match the height, slope, curvature, and higher derivatives of the function at a single point.",
        steps=[
            f"Step 1: Evaluation Point.\n   We are building the approximation around a = {a}.",
            "Step 2: Derivatives.",
            f"   Find f(a), f'(a), f''(a)... up to the {n-1}th derivative.",
            "Step 3: Construct Terms.",
            "   Term 0: f(a)",
            "   Term 1: f'(a) * (x - a)",
            "   Term 2: f''(a) * (x - a)² / 2",
            "   ...",
            f"Step 4: Summation.\n   Add these first {n} terms together to get the polynomial."
        ],
        answer=result
    )

# ==========================================================
# MACLAURIN SERIES
# ==========================================================

def maclaurin_series(f_name: str, n: int, show_steps=False):
    """
    Conceptual explanation of Maclaurin Series expansion.
    """
    _validate_integer(n, "Number of terms 'n'")

    result = f"Maclaurin series of {f_name}(x) (first {n} terms)"

    if not show_steps:
        return result

    return Solution(
        given=f"Function f(x) = {f_name}(x)",
        to_find="Series expansion at x=0",
        equation="f(x) ≈ Σ f⁽ᵏ⁾(0)xᵏ / k!",
        formula_name="Maclaurin Series",
        formula_used="f(0) + f'(0)x + f''(0)x²/2! + ...",
        formula_reason="Special case of Taylor Series centered at zero, common in physics.",
        symbol_explanation="Derivatives are evaluated strictly at 0.",
        explanation="Constructs a polynomial that behaves exactly like the function near the origin.",
        steps=[
            "Step 1: Center Point.\n   Set a = 0 (this distinguishes it from Taylor series).",
            "Step 2: Evaluate Derivatives at 0.",
            f"   Calculate f(0), f'(0), ... f^({n-1})(0).",
            "Step 3: Build Power Terms.",
            "   Multiply the kth derivative by x^k and divide by k!.",
            f"Step 4: Combine.\n   Sum the first {n} terms."
        ],
        answer=result
    )

# ==========================================================
# EULER’S FORMULA
# ==========================================================

def euler_formula(theta: float, show_steps=False):
    result = "e^(iθ) = cosθ + i sinθ"

    if not show_steps:
        return result

    return Solution(
        given=f"Angle θ = {theta}",
        to_find="Rectangular form of e^(iθ)",
        equation="e^(iθ) = cos(θ) + i·sin(θ)",
        formula_name="Euler’s Formula",
        formula_used="e^(ix) = cos x + i sin x",
        formula_reason="Links exponential growth to circular motion.",
        symbol_explanation="i is imaginary unit; result is a point on the unit circle.",
        explanation="Any complex exponential represents a rotation in the complex plane.",
        steps=[
            f"Step 1: Input Angle.\n   θ = {theta}",
            "Step 2: Real Part.\n   Calculate cos(θ). This is the horizontal (x) distance.",
            "Step 3: Imaginary Part.\n   Calculate sin(θ). This is the vertical (y) distance.",
            "Step 4: Combine.\n   The result is the complex number: cos(θ) + i·sin(θ)."
        ],
        answer=result
    )

# ==========================================================
# GREEN’S THEOREM
# ==========================================================

def greens_theorem(show_steps=False):
    result = "∮C (P dx + Q dy) = ∬R (∂Q/∂x − ∂P/∂y) dA"

    if not show_steps:
        return result

    return Solution(
        given="Region R enclosed by curve C",
        to_find="Relation between boundary line integral and area integral",
        equation=result,
        formula_name="Green’s Theorem",
        formula_used="∮ (Pdx + Qdy) = ∬ (curl_2D) dA",
        formula_reason="Converts difficult line integrals into easier double integrals (or vice-versa).",
        symbol_explanation="(∂Q/∂x − ∂P/∂y) is the 2D 'micro-circulation' or curl.",
        explanation="Summing the microscopic rotation inside the region equals the macroscopic rotation along the boundary.",
        steps=[
            "Step 1: Check Orientation.\n   Ensure curve C is traversed counter-clockwise.",
            "Step 2: Identify Vector Field.\n   F = <P, Q>.",
            "Step 3: Calculate Curl.\n   Compute ∂Q/∂x and ∂P/∂y.",
            "Step 4: Setup Double Integral.\n   Integrate (∂Q/∂x - ∂P/∂y) over the area R.",
            "Step 5: Solve.\n   This result equals the work done moving along boundary C."
        ],
        answer=result
    )

# ==========================================================
# GAUSS DIVERGENCE THEOREM
# ==========================================================

def gauss_divergence(show_steps=False):
    result = "∭V (∇·F) dV = ∬S F·n dS"

    if not show_steps:
        return result

    return Solution(
        given="Volume V bounded by Surface S",
        to_find="Flux of vector field F",
        equation=result,
        formula_name="Divergence Theorem",
        formula_used="Total Divergence in Volume = Total Flux through Surface",
        formula_reason="Relates flow generated inside a volume to flow passing through its shell.",
        symbol_explanation="∇·F is divergence (source/sink density). n is outward normal.",
        explanation="If you sum up all the sources/sinks inside a box, that amount must flow out of the box's skin.",
        steps=[
            "Step 1: Identify Volume V and Surface S.",
            "Step 2: Calculate Divergence.\n   Compute ∇·F = ∂P/∂x + ∂Q/∂y + ∂R/∂z.",
            "Step 3: Setup Volume Integral.\n   Integrate the divergence over the entire volume V.",
            "Step 4: Conclusion.\n   The result equals the total flux flowing across the boundary surface S."
        ],
        answer=result
    )

# ==========================================================
# STOKES’ THEOREM
# ==========================================================

def stokes_theorem(show_steps=False):
    result = "∮C F·dr = ∬S (∇×F)·n dS"

    if not show_steps:
        return result

    return Solution(
        given="Surface S bounded by Curve C",
        to_find="Circulation of F around C",
        equation=result,
        formula_name="Stokes’ Theorem",
        formula_used="Line Integral of F = Surface Integral of Curl(F)",
        formula_reason="Generalizes Green's Theorem to 3D surfaces.",
        symbol_explanation="∇×F is the Curl vector.",
        explanation="The total swirling along the edge (C) equals the sum of all the little swirls on the surface (S).",
        steps=[
            "Step 1: Compute Curl.\n   Find ∇×F (the determinant of the curl matrix).",
            "Step 2: Find Normal Vector.\n   Determine the unit normal n to the surface S.",
            "Step 3: Dot Product.\n   Calculate (∇×F) · n.",
            "Step 4: Integrate.\n   Perform the double integral over the surface S."
        ],
        answer=result
    )

# ==========================================================
# FUNDAMENTAL THEOREM OF CALCULUS
# ==========================================================

def fundamental_theorem(show_steps=False):
    result = "∫ₐᵇ f(x) dx = F(b) − F(a)"

    if not show_steps:
        return result

    return Solution(
        given="Continuous function f(x)",
        to_find="Definite integral from a to b",
        equation=result,
        formula_name="FTC Part 2",
        formula_used="∫ f(x) dx = F(b) - F(a)",
        formula_reason="Connects Integration (area) with Differentiation (slope).",
        symbol_explanation="F(x) is the antiderivative, such that F'(x) = f(x).",
        explanation="The net accumulation of change equals the difference between the final and initial states.",
        steps=[
            "Step 1: Find Antiderivative.\n   Find a function F(x) whose derivative is f(x).",
            "Step 2: Evaluate at Limits.\n   Calculate F(b) (upper limit) and F(a) (lower limit).",
            "Step 3: Subtract.\n   Compute F(b) - F(a).",
            "Step 4: Result.\n   This value represents the signed area under the curve."
        ],
        answer=result
    )

# ==========================================================
# MEAN VALUE THEOREM
# ==========================================================

def mean_value_theorem(show_steps=False):
    result = "∃ c ∈ (a,b) such that f′(c) = (f(b) − f(a)) / (b − a)"

    if not show_steps:
        return result

    return Solution(
        given="Differentiable function f on [a, b]",
        to_find="Point c where tangent equals secant",
        equation="f'(c) = Average Rate of Change",
        formula_name="Mean Value Theorem (MVT)",
        formula_used="f′(c) = (f(b) - f(a)) / (b - a)",
        formula_reason="Guarantees a point with a specific derivative.",
        symbol_explanation="LHS is instantaneous slope; RHS is average slope.",
        explanation="If you drive from A to B with an average speed of 60mph, at some specific moment you must have been going exactly 60mph.",
        steps=[
            "Step 1: Check Conditions.\n   Is f continuous on [a,b] and differentiable on (a,b)?",
            "Step 2: Calculate Average Slope.\n   Slope = (f(b) - f(a)) / (b - a).",
            "Step 3: Take Derivative.\n   Find f'(x).",
            "Step 4: Solve for c.\n   Set f'(c) = Average Slope and solve."
        ],
        answer=result
    )

# ==========================================================
# INTERMEDIATE VALUE THEOREM
# ==========================================================

def intermediate_value_theorem(show_steps=False):
    result = "If f(a) < N < f(b), there exists c such that f(c) = N"

    if not show_steps:
        return result

    return Solution(
        given="Continuous function f on [a, b]",
        to_find="Existence of a value",
        equation="f(c) = N",
        formula_name="Intermediate Value Theorem (IVT)",
        formula_used="Logic of Continuity",
        formula_reason="Used to show roots exist without solving for them.",
        symbol_explanation="N is any value between f(a) and f(b).",
        explanation="If a continuous line goes from below the x-axis to above it, it MUST cross the axis somewhere.",
        steps=[
            "Step 1: Verify Continuity.\n   The function must not have breaks or holes.",
            "Step 2: Evaluate Endpoints.\n   Find f(a) and f(b).",
            "Step 3: Check N.\n   Is N strictly between f(a) and f(b)?",
            "Step 4: Conclusion.\n   There must be at least one c where f(c) = N."
        ],
        answer=result
    )

# ==========================================================
# AM–GM INEQUALITY
# ==========================================================

def am_gm(a: float, b: float, show_steps=False):
    # Validation
    _validate_positive(a, "Value 'a'")
    _validate_positive(b, "Value 'b'")

    AM = (a + b) / 2
    GM = math.sqrt(a * b)
    is_valid = AM >= GM

    if not show_steps:
        return is_valid

    return Solution(
        given=f"Values: a = {a}, b = {b}",
        to_find="Comparison of AM and GM",
        equation="AM ≥ GM",
        formula_name="Arithmetic Mean – Geometric Mean Inequality",
        formula_used="(a+b)/2 ≥ √(ab)",
        formula_reason="Fundamental inequality used in optimization.",
        symbol_explanation="AM (Arithmetic Mean), GM (Geometric Mean).",
        explanation="The arithmetic mean is always greater than or equal to the geometric mean for non-negative numbers.",
        steps=[
            f"Step 1: Calculate AM.\n   ({a} + {b}) / 2 = {AM}",
            f"Step 2: Calculate GM.\n   √({a} * {b}) = √({a*b}) = {GM:.4f}",
            f"Step 3: Compare.\n   Is {AM} ≥ {GM:.4f}?",
            f"Step 4: Conclusion.\n   The inequality holds (Equality only if a=b)."
        ],
        answer=f"Inequality Holds: {is_valid}"
    )

# ==========================================================
# CAUCHY–SCHWARZ INEQUALITY
# ==========================================================

def cauchy_schwarz(u: Tuple[float, float], v: Tuple[float, float], show_steps=False):
    # Validation handled by type hints mostly, but ensuring length is consistent conceptually
    ux, uy = u
    vx, vy = v

    dot_prod = ux * vx + uy * vy
    lhs = dot_prod ** 2
    
    mag_u_sq = ux**2 + uy**2
    mag_v_sq = vx**2 + vy**2
    rhs = mag_u_sq * mag_v_sq
    
    is_valid = lhs <= rhs + 1e-9 # Float tolerance

    if not show_steps:
        return is_valid

    return Solution(
        given=f"Vectors u={u}, v={v}",
        to_find="Verification of Cauchy-Schwarz",
        equation="|u·v|² ≤ |u|²|v|²",
        formula_name="Cauchy–Schwarz Inequality",
        formula_used="(Σ u_i v_i)² ≤ (Σ u_i²) (Σ v_i²)",
        formula_reason="Relates dot products to magnitudes.",
        symbol_explanation="· is dot product. || is magnitude.",
        explanation="The squared dot product is never larger than the product of the squared lengths.",
        steps=[
            f"Step 1: Compute Dot Product (u·v).\n   ({ux}*{vx}) + ({uy}*{vy}) = {dot_prod}",
            f"Step 2: Square the Dot Product (LHS).\n   ({dot_prod})² = {lhs}",
            f"Step 3: Compute Squared Magnitudes.\n   |u|² = {ux}² + {uy}² = {mag_u_sq}\n   |v|² = {vx}² + {vy}² = {mag_v_sq}",
            f"Step 4: Multiply Magnitudes (RHS).\n   {mag_u_sq} * {mag_v_sq} = {rhs}",
            f"Step 5: Compare.\n   Is {lhs} ≤ {rhs}?"
        ],
        answer=f"Inequality Holds: {is_valid}"
    )

# ==========================================================
# TRIANGLE INEQUALITY
# ==========================================================

def triangle_inequality(u: Tuple[float, float], v: Tuple[float, float], show_steps=False):
    ux, uy = u
    vx, vy = v

    # Sum vector
    sum_x = ux + vx
    sum_y = uy + vy
    
    lhs = math.sqrt(sum_x**2 + sum_y**2)
    mag_u = math.sqrt(ux**2 + uy**2)
    mag_v = math.sqrt(vx**2 + vy**2)
    rhs = mag_u + mag_v
    
    is_valid = lhs <= rhs + 1e-9 # Tolerance for float comparison

    if not show_steps:
        return is_valid

    return Solution(
        given=f"Vectors u={u}, v={v}",
        to_find="Verification of Triangle Inequality",
        equation="|u + v| ≤ |u| + |v|",
        formula_name="Triangle Inequality",
        formula_used="|u+v| ≤ |u| + |v|",
        formula_reason="Geometric principle: shortest path between two points is a straight line.",
        symbol_explanation="|u| is the length of vector u.",
        explanation="The length of the resultant vector cannot exceed the sum of the lengths of the component vectors.",
        steps=[
            f"Step 1: Compute Resultant Vector (u+v).\n   ({ux}+{vx}, {uy}+{vy}) = ({sum_x}, {sum_y})",
            f"Step 2: Compute Length of Resultant (LHS).\n   √({sum_x}² + {sum_y}²) = {lhs:.4f}",
            f"Step 3: Compute Individual Lengths.\n   |u| = {mag_u:.4f}\n   |v| = {mag_v:.4f}",
            f"Step 4: Sum Individual Lengths (RHS).\n   {mag_u:.4f} + {mag_v:.4f} = {rhs:.4f}",
            f"Step 5: Compare.\n   Is {lhs:.4f} ≤ {rhs:.4f}?"
        ],
        answer=f"Inequality Holds: {is_valid}"
    )

# ==========================================================
# EXPORT
# ==========================================================

__all__ = [
    "pythagoras",
    "binomial_theorem",
    "taylor_series",
    "maclaurin_series",
    "euler_formula",
    "greens_theorem",
    "gauss_divergence",
    "stokes_theorem",
    "fundamental_theorem",
    "mean_value_theorem",
    "intermediate_value_theorem",
    "am_gm",
    "cauchy_schwarz",
    "triangle_inequality",
]
