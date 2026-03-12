# solvepath/differential_equations.py
"""
=========================================================
          SolvePath Differential Equations Module
=========================================================

Includes HIGHLY DETAILED, TUTOR-STYLE step-by-step solutions for:

• Exponential Growth/Decay (dy/dx = ky)
• Simple Linear Equations (dy/dx = ax + b)
• Second-Order Linear DEs (ar² + br + c = 0) with:
    - Distinct Real Roots
    - Repeated Real Roots
    - Complex Roots

Also includes METHODOLOGICAL GUIDES for:
• Separable Equations
• First-Order Linear (Integrating Factor)
• Exact Equations
• Homogeneous Equations

Returns:
• Solution object when show_steps=True
• Final result/string when show_steps=False

=========================================================
"""

import math
import cmath
from solvepath.solution import Solution

# =========================================================
# INTERNAL VALIDATION
# =========================================================

def _validate_number(n, name="Input"):
    if not isinstance(n, (int, float)):
        raise TypeError(f"{name} must be a number.")

# =========================================================
# dy/dx = k y  (Exponential Growth / Decay)
# =========================================================

def de_exp_growth(k: float, C: float = 1, show_steps: bool = False):
    _validate_number(k, "k")
    _validate_number(C, "C")

    # The actual python function for the result
    result_func = lambda x: C * math.exp(k * x)
    
    # Text representation of the solution
    result_str = f"y(x) = {C}e^({k}x)"

    if not show_steps:
        return result_func

    steps = [
        f"Step 1: Write the differential equation.",
        f"   dy/dx = {k}y",
        "Step 2: Separate the variables (y on left, x on right).",
        "   (1/y) dy = k dx",
        "Step 3: Integrate both sides.",
        "   ∫ (1/y) dy = ∫ k dx",
        "   ln|y| = kx + C₁",
        "Step 4: Solve for y by exponentiating both sides.",
        "   |y| = e^(kx + C₁)",
        "   y = ±e^C₁ · e^(kx)",
        "Step 5: Define constant C = ±e^C₁.",
        f"   y(x) = Ce^({k}x)",
        f"Step 6: Substitute given constant C = {C}.",
        f"   {result_str}"
    ]

    return Solution(
        given=f"dy/dx = {k}y, Initial Constant C={C}",
        to_find="General Solution y(x)",
        equation="dy/dx = ky",
        formula_name="Exponential Growth/Decay",
        formula_used="∫(1/y)dy = ∫k dx",
        formula_reason="The rate of change is proportional to the current amount.",
        explanation="We separate variables and integrate logarithmic terms to find the exponential solution.",
        steps=steps,
        answer=result_str
    )

# =========================================================
# dy/dx = ax + b
# =========================================================

def de_linear_axb(a: float, b: float, C: float = 0, show_steps: bool = False):
    _validate_number(a, "a")
    _validate_number(b, "b")
    
    result_func = lambda x: (a / 2) * x**2 + b * x + C
    result_str = f"y(x) = {a/2}x² + {b}x + {C}"

    if not show_steps:
        return result_func

    steps = [
        f"Step 1: Write the equation.",
        f"   dy/dx = {a}x + {b}",
        "Step 2: Integrate both sides with respect to x.",
        f"   y = ∫ ({a}x + {b}) dx",
        "Step 3: Apply Power Rule for integration.",
        f"   ∫ {a}x dx = {a} · (x²/2) = {a/2}x²",
        f"   ∫ {b} dx = {b}x",
        "Step 4: Add the constant of integration C.",
        f"   y(x) = {a/2}x² + {b}x + C",
        f"Step 5: Substitute specific C = {C}.",
        f"   {result_str}"
    ]

    return Solution(
        given=f"dy/dx = {a}x + {b}, C={C}",
        to_find="General Solution y(x)",
        equation="y = ∫(ax + b) dx",
        formula_name="Direct Integration",
        formula_used="∫ xⁿ dx = xⁿ⁺¹/(n+1)",
        formula_reason="Since the derivative depends only on x, we can integrate directly.",
        explanation="We find the antiderivative of the linear function ax + b.",
        steps=steps,
        answer=result_str
    )

# =========================================================
# SEPARABLE DIFFERENTIAL EQUATION (METHOD GUIDE)
# =========================================================

def de_separable(show_steps: bool = False):
    result = "Method: ∫ (1/h(y)) dy = ∫ g(x) dx"

    if not show_steps:
        return result

    return Solution(
        given="dy/dx = g(x) · h(y)",
        to_find="General Solution y(x)",
        equation="dy/h(y) = g(x) dx",
        formula_name="Separation of Variables",
        formula_used="∫ N(y) dy = ∫ M(x) dx",
        formula_reason="We can group all 'y' terms on one side and 'x' terms on the other.",
        explanation="This technique turns a differential equation into two separate integration problems.",
        steps=[
            "Step 1: Identify the structure.",
            "   Is the equation in the form dy/dx = g(x)h(y)?",
            "Step 2: Separate the variables.",
            "   Divide by h(y) and multiply by dx:",
            "   (1 / h(y)) dy = g(x) dx",
            "Step 3: Integrate both sides.",
            "   LHS: ∫ (1/h(y)) dy",
            "   RHS: ∫ g(x) dx",
            "Step 4: Solve for y (if possible).",
            "   Combine constants of integration into one '+ C'."
        ],
        answer=result
    )

# =========================================================
# FIRST-ORDER LINEAR DIFFERENTIAL EQUATION (METHOD GUIDE)
# =========================================================

def de_first_order_linear(show_steps: bool = False):
    result = "y(x) = (1/μ(x)) · [ ∫ μ(x)Q(x) dx + C ]"

    if not show_steps:
        return result

    return Solution(
        given="dy/dx + P(x)y = Q(x)",
        to_find="General Solution y(x)",
        equation="y' + Py = Q",
        formula_name="Integrating Factor Method",
        formula_used="μ(x) = e^(∫ P(x) dx)",
        formula_reason="Multiplying by μ(x) forces the LHS to become the derivative of a product (y · μ).",
        explanation="This method solves linear equations that are not separable.",
        steps=[
            "Step 1: Standardize the equation.",
            "   Ensure it looks like: dy/dx + P(x)y = Q(x)",
            "Step 2: Calculate the Integrating Factor (μ).",
            "   μ(x) = exp( ∫ P(x) dx )",
            "Step 3: Multiply the entire equation by μ(x).",
            "   μ(x)y' + μ(x)P(x)y = μ(x)Q(x)",
            "   Notice LHS becomes: d/dx [ μ(x) · y ]",
            "Step 4: Integrate both sides.",
            "   μ(x) · y = ∫ μ(x)Q(x) dx + C",
            "Step 5: Solve for y.",
            "   Divide by μ(x) to isolate y."
        ],
        answer=result
    )

# =========================================================
# EXACT DIFFERENTIAL EQUATION (METHOD GUIDE)
# =========================================================

def de_exact(show_steps: bool = False):
    result = "Ψ(x, y) = C"

    if not show_steps:
        return result

    return Solution(
        given="M(x,y) dx + N(x,y) dy = 0",
        to_find="Potential Function Ψ(x,y)",
        equation="∂M/∂y = ∂N/∂x",
        formula_name="Exactness Test",
        formula_used="Ψ = ∫ M dx + g(y)",
        formula_reason="If ∂M/∂y = ∂N/∂x, the field is conservative and a potential function exists.",
        explanation="The solution is the level curves of a potential function Ψ.",
        steps=[
            "Step 1: Check for Exactness.",
            "   Calculate ∂M/∂y and ∂N/∂x. Are they equal?",
            "Step 2: Integrate M with respect to x.",
            "   Ψ(x,y) = ∫ M(x,y) dx + g(y)",
            "   (g(y) is an unknown constant relative to x)",
            "Step 3: Differentiate Ψ with respect to y.",
            "   ∂Ψ/∂y = ∂/∂y [∫ M dx] + g'(y)",
            "Step 4: Set equal to N(x,y) and solve for g'(y).",
            "   ∂Ψ/∂y = N(x,y)  =>  Solve for g(y)",
            "Step 5: Write final solution.",
            "   Ψ(x,y) = C"
        ],
        answer=result
    )

# =========================================================
# HOMOGENEOUS DIFFERENTIAL EQUATION (METHOD GUIDE)
# =========================================================

def de_homogeneous(show_steps: bool = False):
    result = "Substitute y = vx, then Separate Variables"

    if not show_steps:
        return result

    return Solution(
        given="dy/dx = F(y/x)",
        to_find="General Solution y(x)",
        equation="v + x(dv/dx) = F(v)",
        formula_name="Homogeneous Substitution",
        formula_used="y = vx  =>  dy/dx = v + x(dv/dx)",
        formula_reason="Substitution reduces a homogeneous equation into a separable one.",
        explanation="We transform the dependent variable from y to v.",
        steps=[
            "Step 1: Verify Homogeneity.",
            "   Can dy/dx be written as a function of (y/x)?",
            "Step 2: Perform Substitution.",
            "   Let y = vx. Then dy/dx = v + x(dv/dx).",
            "Step 3: Rewrite the Equation.",
            "   v + x(dv/dx) = F(v)",
            "Step 4: Separate Variables.",
            "   dx/x = dv / (F(v) - v)",
            "Step 5: Integrate and Substitute back.",
            "   Solve for v, then replace v with y/x."
        ],
        answer=result
    )

# =========================================================
# SECOND-ORDER LINEAR DIFFERENTIAL EQUATION
# =========================================================

def de_second_order(a: float, b: float, c: float, show_steps: bool = False):
    _validate_number(a, "a")
    _validate_number(b, "b")
    _validate_number(c, "c")

    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0 for a second-order equation.")

    # Calculate Discriminant
    discriminant = b**2 - 4*a*c
    
    steps = [
        f"Step 1: Write the Characteristic Equation.",
        f"   {a}r² + {b}r + {c} = 0",
        f"Step 2: Calculate Discriminant (Δ).",
        f"   Δ = b² - 4ac",
        f"   Δ = ({b})² - 4({a})({c})",
        f"   Δ = {b**2} - {4*a*c} = {discriminant}"
    ]

    # Analyze Roots
    if discriminant > 0:
        # Distinct Real Roots
        r1 = (-b + math.sqrt(discriminant)) / (2*a)
        r2 = (-b - math.sqrt(discriminant)) / (2*a)
        
        steps.append("Step 3: Analyze Roots (Δ > 0).")
        steps.append("   Two distinct real roots exist.")
        steps.append(f"   r₁ = (-{b} + √{discriminant}) / {2*a} = {r1:.2f}")
        steps.append(f"   r₂ = (-{b} - √{discriminant}) / {2*a} = {r2:.2f}")
        
        result_str = f"y(x) = C₁e^({r1:.2f}x) + C₂e^({r2:.2f}x)"
        
    elif discriminant == 0:
        # Repeated Real Roots
        r = -b / (2*a)
        
        steps.append("Step 3: Analyze Roots (Δ = 0).")
        steps.append("   One repeated real root exists.")
        steps.append(f"   r = -{b} / {2*a} = {r:.2f}")
        
        result_str = f"y(x) = (C₁ + C₂x)e^({r:.2f}x)"
        
    else:
        # Complex Roots
        alpha = -b / (2*a)
        beta = math.sqrt(abs(discriminant)) / (2*a)
        
        steps.append("Step 3: Analyze Roots (Δ < 0).")
        steps.append("   Complex conjugate roots exist: α ± βi.")
        steps.append(f"   α (Real part) = -{b} / {2*a} = {alpha:.2f}")
        steps.append(f"   β (Imaginary part) = √{abs(discriminant)} / {2*a} = {beta:.2f}")
        
        result_str = f"y(x) = e^({alpha:.2f}x) [ C₁cos({beta:.2f}x) + C₂sin({beta:.2f}x) ]"

    steps.append(f"Step 4: General Solution.\n   {result_str}")

    if not show_steps:
        return result_str

    return Solution(
        given=f"{a}y'' + {b}y' + {c}y = 0",
        to_find="General Solution y(x)",
        equation="ar² + br + c = 0",
        formula_name="Characteristic Equation",
        formula_used="(-b ± √Δ) / 2a",
        formula_reason="The form of the solution depends on the roots of the auxiliary polynomial.",
        explanation="We convert the differential equation into an algebraic equation to find the roots r.",
        steps=steps,
        answer=result_str
    )

# =========================================================
# EXPORT
# =========================================================

__all__ = [
    "de_exp_growth",
    "de_linear_axb",
    "de_separable",
    "de_first_order_linear",
    "de_exact",
    "de_homogeneous",
    "de_second_order",
]
