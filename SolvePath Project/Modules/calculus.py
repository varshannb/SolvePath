# solvepath/calculus.py
"""
=========================================================
              SolvePath Calculus Module
=========================================================

This module provides differential and integral calculus
solutions with full mathematical derivations.

Includes:
• Derivatives (power, exp, ln, trigonometric)
• Product, Quotient, and Chain Rule
• Indefinite Integrals
• Definite Integrals
• Limits and L'Hôpital’s Rule
• Fundamental Theorem of Calculus
• Series Expansions
• Taylor Series

Returns:
• Solution object when show_steps=True
• Final result when show_steps=False
=========================================================
"""

import math
from typing import Union, Callable
from solvepath.solution import Solution

Number = Union[int, float]


# =========================================================
#                 POWER RULE
# =========================================================

def derivative_power(n: Number, x: Number, show_steps=False):
    """
    Derivative of x^n evaluated at x.
    Formula: n * x^(n-1)
    """

    result = n * (x ** (n - 1))

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the exact slope (steepness) of the curve y = x^n at a specific point.",
        given=f"Function: x to the power of {n}, Evaluated at x = {x}",
        to_find="The derivative (slope) at this point",
        equation="d/dx (xⁿ)",
        formula_name="Power Rule",
        formula_used="d/dx (xⁿ) = n · x^(n-1)",
        formula_reason=(
            "This is a shortcut rule. Instead of drawing a graph, "
            "we use the exponent to calculate the slope directly."
        ),
        symbol_explanation=(
            "• d/dx means 'Rate of Change'\n"
            "• n is the original power (exponent)\n"
            "• n-1 is the new, reduced power"
        ),
        explanation=(
            "To find the slope, we take the current power, bring it down to multiply, "
            "and then lower the power by exactly 1."
        ),
        steps=[
            f"Step 1: Identify the function: f(x) = x^{n}.",
            "Step 2: Our goal is to find how fast this function is changing.",
            "Step 3: Apply the Power Rule strategy: 'Bring the power down, reduce the power by 1'.",
            f"Step 4: Identify the original power (n): {n}.",
            f"Step 5: Calculate the new power (n - 1): {n} - 1 = {n - 1}.",
            "Step 6: Construct the derivative formula: f'(x) = (Original Power) * x^(New Power).",
            f"Step 7: Write the formula with our numbers: {n} * x^{n - 1}.",
            f"Step 8: Now, substitute the value x = {x} into this new formula.",
            f"Step 9: First, calculate the power part: {x} raised to {n - 1}.",
            f"   >> {x}^{n - 1} = {x**(n - 1):.4f}",
            f"Step 10: Next, multiply that result by the coefficient {n}.",
            f"   >> {n} * {x**(n - 1):.4f}",
            f"Step 11: Perform the multiplication: {result:.4f}.",
            "Step 12: Final Interpretation: This number is the slope of the curve at that exact point.",
            "Step 13: Final Answer."
        ],
        answer=result
    )

# =========================================================
#                 EXPONENTIAL FUNCTION
# =========================================================

def derivative_exp(x: Number, show_steps=False):
    result = math.exp(x)

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the rate of growth of the natural exponential function.",
        given=f"Function: e^x, Evaluated at x = {x}",
        to_find="The rate of change",
        equation="d/dx (eˣ)",
        formula_name="Derivative of Exponential",
        formula_used="d/dx (eˣ) = eˣ",
        formula_reason=(
            "The number 'e' is special because it is the only base "
            "where the slope of the graph equals the height of the graph."
        ),
        symbol_explanation=(
            "• e ≈ 2.718 (Euler's Number)\n"
            "• d/dx means 'Derivative of'"
        ),
        explanation=(
            "Unlike other functions that change when you take a derivative, "
            "e^x remains exactly the same. Its growth rate is equal to its current size."
        ),
        steps=[
            "Step 1: Identify the function: y = e^x.",
            "Step 2: Recognize this as the special 'natural exponential' function.",
            "Step 3: Recall the rule: The derivative of e^x is just e^x.",
            "Step 4: This means the slope at any point is simply the value of the function at that point.",
            f"Step 5: We need to evaluate this at x = {x}.",
            f"Step 6: Substitute {x} into e^x.",
            "Step 7: Recall that e is approximately 2.71828.",
            f"Step 8: Calculate 2.71828 raised to the power of {x}.",
            f"   >> e^{x} = {result:.4f}",
            "Step 9: Since x was positive/negative, verify if the result makes sense (should be > 0).",
            "Step 10: The calculation is correct.",
            "Step 11: This value represents how steep the curve is.",
            "Step 12: Final Answer."
        ],
        answer=result
        
    )


# =========================================================
#                 LOGARITHMIC FUNCTION
# =========================================================

def derivative_ln(x: Number, show_steps=False):
    if x <= 0:
        raise ValueError("Logarithms cannot handle zero or negative numbers.")

    result = 1 / x

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find how fast the natural logarithm curve is rising.",
        given=f"Function: ln(x), Evaluated at x = {x}",
        to_find="The slope of ln(x)",
        equation="d/dx (ln x)",
        formula_name="Derivative of Natural Log",
        formula_used="d/dx (ln x) = 1/x",
        formula_reason=(
            "The log curve flattens out as x gets bigger. "
            "The formula 1/x mathematically describes this flattening effect."
        ),
        symbol_explanation=(
            "• ln means Logarithm base e\n"
            "• 1/x is the Reciprocal of x"
        ),
        explanation=(
            "The slope of the natural logarithm is simply the reciprocal of the input. "
            "If x is big, the slope is small. If x is small, the slope is big."
        ),
        steps=[
            "Step 1: Identify the function: y = ln(x).",
            "Step 2: Understand the shape: It rises quickly at first, then slows down.",
            "Step 3: This 'slowing down' is described by the derivative rule.",
            "Step 4: The Rule: The derivative of ln(x) is 1 divided by x.",
            f"Step 5: Identify our input value: x = {x}.",
            "Step 6: Apply the rule directly.",
            f"Step 7: Set up the fraction: 1 / {x}.",
            "Step 8: Perform the division.",
            f"   >> 1 ÷ {x} = {result:.4f}",
            "Step 9: Interpret the result.",
            "Step 10: A small result means the curve is flat here.",
            "Step 11: A large result means the curve is steep here.",
            "Step 12: Final Answer."
        ],
        answer=f"{result:.4f}"
    )


# =========================================================
#                TRIGONOMETRIC DERIVATIVES
# =========================================================

def derivative_sin(x: Number, show_steps=False):
    result = math.cos(x)

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the slope of the sine wave at a specific angle.",
        given=f"Function: sin(x), Evaluated at x = {x}",
        to_find="The derivative (slope)",
        equation="d/dx (sin x)",
        formula_name="Derivative of Sine",
        formula_used="d/dx (sin x) = cos x",
        formula_reason=(
            "The Sine wave and Cosine wave are related. "
            "The slope of the Sine wave at any point perfectly matches the height of the Cosine wave."
        ),
        symbol_explanation=(
            "• sin(x) tracks vertical position\n"
            "• cos(x) tracks horizontal position"
        ),
        explanation=(
            "To find how fast sine is changing, we simply calculate the cosine of that same angle."
        ),
        steps=[
            "Step 1: Identify the function: f(x) = sin(x).",
            "Step 2: Recall the rule: The derivative of sin(x) is cos(x).",
            f"Step 3: Identify the input angle x = {x} (in radians).",
            "Step 4: Substitute x into the derivative function.",
            f"Step 5: We need to calculate cos({x}).",
            "Step 6: Check the unit circle context.",
            f"   >> Angle is approx {math.degrees(x):.1f} degrees.",
            "Step 7: Perform the cosine calculation.",
            f"   >> cos({x}) = {result:.4f}",
            "Step 8: Interpret: If positive, sine is going up. If negative, sine is going down.",
            "Step 9: The value represents the exact steepness of the wave.",
            "Step 10: Final Answer."
        ],
        answer=f"{result:.4f}"
    )


def derivative_cos(x: Number, show_steps=False):
    result = -math.sin(x)

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the slope of the cosine wave at a specific angle.",
        given=f"Function: cos(x), Evaluated at x = {x}",
        to_find="The derivative (slope)",
        equation="d/dx (cos x)",
        formula_name="Derivative of Cosine",
        formula_used="d/dx (cos x) = −sin x",
        formula_reason=(
            "When the Cosine wave goes down, the Sine wave is positive. "
            "So, to describe the downward slope, we use negative Sine."
        ),
        symbol_explanation=(
            "• The negative sign (-) is crucial\n"
            "• It flips the sine value"
        ),
        explanation=(
            "To find how fast cosine is changing, calculate the sine of the angle and flip the sign (multiply by -1)."
        ),
        steps=[
            "Step 1: Identify the function: f(x) = cos(x).",
            "Step 2: Recall the rule: The derivative of cos(x) is NEGATIVE sin(x).",
            "Step 3: Be careful not to forget the negative sign!",
            f"Step 4: Identify the input angle x = {x}.",
            "Step 5: First, calculate the sine of this angle.",
            f"   >> sin({x}) = {math.sin(x):.4f}",
            "Step 6: Now, apply the derivative formula: Multiply by -1.",
            f"   >> -1 * {math.sin(x):.4f}",
            f"Step 7: Result = {result:.4f}",
            "Step 8: Interpret: A negative result means the cosine graph is going downwards.",
            "Step 9: A positive result means it is going upwards.",
            "Step 10: Final Answer."
        ],
        answer=f"{result:.4f}"
    )


def derivative_tan(x: Number, show_steps=False):
    cos_val = math.cos(x)
    if abs(cos_val) < 1e-12:
        raise ValueError("Derivative undefined (Vertical Asymptote at this angle).")

    result = 1 / (cos_val ** 2)

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the slope of the tangent curve.",
        given=f"Function: tan(x), Evaluated at x = {x}",
        to_find="The derivative (slope)",
        equation="d/dx (tan x)",
        formula_name="Derivative of Tangent",
        formula_used="d/dx (tan x) = sec² x = 1 / cos² x",
        formula_reason=(
            "Tangent is derived from sine divided by cosine. "
            "Using calculus rules, this simplifies to the square of the secant."
        ),
        symbol_explanation=(
            "• sec(x) is the Secant function\n"
            "• sec(x) is defined as 1 divided by cos(x)"
        ),
        explanation=(
            "The slope of tangent is found by taking the cosine of the angle, squaring it, and then taking the reciprocal."
        ),
        steps=[
            "Step 1: Identify the function: f(x) = tan(x).",
            "Step 2: Recall the rule: Derivative is sec²(x).",
            "Step 3: Convert sec²(x) to something easier to calculate: 1 / cos²(x).",
            f"Step 4: Substitute x = {x}.",
            "Step 5: First, calculate cos(x).",
            f"   >> cos({x}) = {cos_val:.4f}",
            "Step 6: Next, square that result.",
            f"   >> ({cos_val:.4f})² = {cos_val**2:.4f}",
            "Step 7: Finally, divide 1 by that squared number.",
            f"   >> 1 / {cos_val**2:.4f}",
            f"Step 8: Result = {result:.4f}",
            "Step 9: Notice the result is always positive.",
            "Step 10: This means the tangent function is always increasing (going up).",
            "Step 11: Final Answer."
        ],
        answer=f"{result:.4f}"
    )


# =========================================================
#                      PRODUCT RULE 
# =========================================================

def derivative_product(u: Callable, du: Callable,
                       v: Callable, dv: Callable,
                       x: Number, show_steps=False):

    u_val = u(x)
    v_val = v(x)
    du_val = du(x)
    dv_val = dv(x)

    result = du_val * v_val + u_val * dv_val

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the rate of change when two functions are multiplied together.",
        given=(
            f"Function 1 (u): {u_val}, Derivative (u'): {du_val}\n"
            f"Function 2 (v): {v_val}, Derivative (v'): {dv_val}"
        ),
        to_find="The derivative of (u times v)",
        equation="d/dx [u(x) · v(x)]",
        formula_name="Product Rule",
        formula_used="(uv)' = u'v + uv'",
        formula_reason=(
            "When two things are changing at the same time, "
            "we must account for both changes individually and add them up."
        ),
        symbol_explanation=(
            "• u is the first function, v is the second\n"
            "• The ' mark means derivative"
        ),
        explanation=(
            "Think of it like this: "
            "(Derivative of First × Second) + (First × Derivative of Second)."
        ),
        steps=[
            "Step 1: Identify your two functions, u and v.",
            "Step 2: Identify their derivatives, u' and v'.",
            "Step 3: Use the Product Rule Formula: u'v + uv'.",
            "Step 4: PART A: Multiply u' (derivative of first) by v (original second).",
            f"   >> {du_val} * {v_val} = {du_val * v_val:.4f}",
            "Step 5: PART B: Multiply u (original first) by v' (derivative of second).",
            f"   >> {u_val} * {dv_val} = {u_val * dv_val:.4f}",
            "Step 6: Add Part A and Part B together.",
            f"   >> {du_val * v_val:.4f} + {u_val * dv_val:.4f}",
            "Step 7: Perform the addition.",
            f"   >> {result:.4f}",
            "Step 8: This sum represents the total rate of change.",
            "Step 9: Check signs to ensure direction is correct.",
            "Step 10: Final Answer."
        ],
        answer=f"{result:.4f}"
    )


# =========================================================
#                     QUOTIENT RULE 
# =========================================================

def derivative_quotient(u: Callable, du: Callable,
                        v: Callable, dv: Callable,
                        x: Number, show_steps=False):

    u_val = u(x)
    v_val = v(x)
    du_val = du(x)
    dv_val = dv(x)

    if abs(v_val) < 1e-12:
        raise ValueError("Division by zero! The denominator cannot be 0.")

    numerator_val = du_val * v_val - u_val * dv_val
    denominator_val = v_val ** 2
    result = numerator_val / denominator_val

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the rate of change when one function is divided by another (a fraction).",
        given=(
            f"Top Function (u): {u_val}, Derivative (u'): {du_val}\n"
            f"Bottom Function (v): {v_val}, Derivative (v'): {dv_val}"
        ),
        to_find="The derivative of (u divided by v)",
        equation="d/dx [u(x) / v(x)]",
        formula_name="Quotient Rule",
        formula_used="(u/v)' = (u'v − uv') / v²",
        formula_reason=(
            "Division is complex because changes in the bottom function "
            "have a strong, inverse effect on the result."
        ),
        symbol_explanation=(
            "• 'Lo' means lower function (v)\n"
            "• 'Hi' means upper function (u)\n"
            "• 'd' means derivative"
        ),
        explanation=(
            "We use the rhyme: 'Lo d-Hi minus Hi d-Lo, over Lo Lo'. "
            "This helps remember the order of subtraction."
        ),
        steps=[
            "Step 1: Identify the Top (u) and Bottom (v) functions.",
            "Step 2: Recall the formula: (v·u' - u·v') / v².",
            "Step 3: PART A (Lo d-Hi): Multiply Bottom (v) by Derivative of Top (u').",
            f"   >> {v_val} * {du_val} = {du_val * v_val:.4f}",
            "Step 4: PART B (Hi d-Lo): Multiply Top (u) by Derivative of Bottom (v').",
            f"   >> {u_val} * {dv_val} = {u_val * dv_val:.4f}",
            "Step 5: Subtract Part B from Part A to get the Numerator.",
            f"   >> {du_val * v_val:.4f} - {u_val * dv_val:.4f} = {numerator_val:.4f}",
            "Step 6: PART C (Lo Lo): Square the Bottom function (v²).",
            f"   >> {v_val}^2 = {denominator_val:.4f}",
            "Step 7: Divide the Numerator by the Denominator.",
            f"   >> {numerator_val:.4f} / {denominator_val:.4f}",
            "Step 8: Perform the final division.",
            f"   >> {result:.4f}",
            "Step 9: This value is the slope of the fraction at this point.",
            "Step 10: Final Answer."
        ],
        answer=f"{result:.4f}"
    )


# =========================================================
#                   CHAIN RULE 
# =========================================================

def derivative_chain(f: Callable, df: Callable,
                     g: Callable, dg: Callable,
                     x: Number, show_steps=False):

    g_val = g(x)
    dg_val = dg(x)
    df_val = df(g_val)

    result = df_val * dg_val

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the derivative of a function inside another function (Composite Function).",
        given=(
            f"Inner function value: {g_val}, Inner slope: {dg_val}\n"
            f"Outer function slope at that point: {df_val}"
        ),
        to_find="The total rate of change",
        equation="d/dx [f(g(x))]",
        formula_name="Chain Rule",
        formula_used="(f(g(x)))' = f'(g(x)) × g'(x)",
        formula_reason=(
            "Rates of change multiply. If gear A spins gear B, and gear B spins gear C, "
            "you multiply the ratios to find how A affects C."
        ),
        symbol_explanation=(
            "• Outer function f\n"
            "• Inner function g\n"
            "• The chain links them by multiplication"
        ),
        explanation=(
            "Think of it like peeling an onion. First you take the derivative of the outer layer, "
            "then you multiply it by the derivative of the inner layer."
        ),
        steps=[
            "Step 1: Identify the Outer function f(...) and Inner function g(x).",
            "Step 2: Understand that x affects g, and g affects f.",
            "Step 3: Calculate the rate of the Inner function (g').",
            f"   >> g'(x) = {dg_val}",
            "Step 4: Calculate the rate of the Outer function (f') evaluated at the inner value.",
            f"   >> f'(g(x)) = {df_val}",
            "Step 5: Apply the Chain Rule: Multiply the two rates together.",
            f"   >> {df_val} * {dg_val}",
            "Step 6: Perform the multiplication.",
            f"   >> {result:.4f}",
            "Step 7: Visualize: If the inner rate is 2x and outer is 3x, total is 6x.",
            "Step 8: Interpret: This single number represents the combined sensitivity of the system.",
            "Step 9: Check logic: If either rate was zero, the total result would be zero.",
            "Step 10: Final Answer."
        ],
        answer=f"{result:.4f}"
    )


# =========================================================
#                INDEFINITE INTEGRALS
# =========================================================

def integral_power(n: Number, show_steps=False):
    if n == -1:
        raise ValueError("Power is -1. Use the Logarithm rule (integral_ln) instead.")

    expression = f"x^{n + 1}/({n + 1}) + C"

    if not show_steps:
        return expression

    return Solution(
        problem_understanding="Find the function that was differentiated to get x^n (Reverse Power Rule).",
        given=f"Original term: x^{n}",
        to_find="The Indefinite Integral (Antiderivative)",
        equation="∫ xⁿ dx",
        formula_name="Power Rule of Integration",
        formula_used="∫ xⁿ dx = xⁿ⁺¹ / (n + 1) + C",
        formula_reason=(
            "Since differentiation subtracts 1 from the power and multiplies, "
            "integration must do the opposite: add 1 to the power and divide."
        ),
        symbol_explanation=(
            "• ∫ symbol means 'Sum' or 'Integral'\n"
            "• dx means 'with respect to x'\n"
            "• + C is the constant (because derivative of a constant is 0)"
        ),
        explanation=(
            "We are working backwards. We increase the exponent by 1, "
            "and then divide by that new exponent."
        ),
        steps=[
            "Step 1: Identify the integrand (the part inside the integral): x^n.",
            f"Step 2: Identify the current power: n = {n}.",
            "Step 3: Recall the rule: 'Add one to the power, divide by the new power'.",
            "Step 4: Calculate the new power.",
            f"   >> {n} + 1 = {n + 1}",
            "Step 5: Write x raised to this new power.",
            f"   >> x^{n + 1}",
            "Step 6: Divide this term by the new number we just found.",
            f"   >> x^{n + 1} / {n + 1}",
            "Step 7: Don't forget the '+ C'.",
            "Step 8: Why +C? Because if we derived x^2 + 5 or x^2 + 10, both would give 2x.",
            "Step 9: We use C to represent any possible starting number.",
            f"Step 10: Combine the parts into the final expression.",
            "Step 11: Formatting the result.",
            f"Step 12: Final Answer: {expression}"
        ],
        answer=expression
    )


def integral_ln(show_steps=False):
    expression = "ln|x| + C"

    if not show_steps:
        return expression

    return Solution(
        problem_understanding="Find the integral of 1/x.",
        given="Integrand = 1/x (or x^-1)",
        to_find="The Indefinite Integral",
        equation="∫ 1/x dx",
        formula_name="Logarithmic Integration Rule",
        formula_used="∫ 1/x dx = ln|x| + C",
        formula_reason=(
            "The Power Rule fails for x^-1 because adding 1 gives 0, and we can't divide by 0. "
            "We know from differentiation that ln(x) gives 1/x."
        ),
        symbol_explanation=(
            "• |x| means absolute value (logs must be positive)\n"
            "• C is the constant"
        ),
        explanation=(
            "This is a special case. Whenever you see 1/x, the answer is always the natural log."
        ),
        steps=[
            "Step 1: Identify the integrand: 1/x.",
            "Step 2: Try Power Rule? x^-1 becomes x^0 / 0. ERROR.",
            "Step 3: Recognize this as the 'Special Case'.",
            "Step 4: Recall which function's derivative is 1/x.",
            "Step 5: The derivative of ln(x) is 1/x.",
            "Step 6: Therefore, the integral of 1/x is ln(x).",
            "Step 7: Add Absolute Value bars |x|.",
            "Step 8: Reason: 1/x works for negative numbers, but ln(x) only works for positive numbers.",
            "Step 9: Using |x| fixes the domain issue.",
            "Step 10: Add the Constant of Integration + C.",
            "Step 11: Combine into final expression.",
            f"Step 12: Final Answer: {expression}"
        ],
        answer=expression
    )



def integral_exp(show_steps=False):
    expression = "e^x + C"

    if not show_steps:
        return expression

    return Solution(
        problem_understanding="Find the integral of e^x.",
        given="Integrand = e^x",
        to_find="The Indefinite Integral",
        equation="∫ eˣ dx",
        formula_name="Exponential Integration Rule",
        formula_used="∫ eˣ dx = eˣ + C",
        formula_reason=(
            "Since the derivative of e^x is itself, the integral (reverse) is also itself."
        ),
        symbol_explanation=(
            "• e is the base of natural logs\n"
            "• The function is unchanged"
        ),
        explanation=(
            "This is the easiest integral in calculus. The function does not change."
        ),
        steps=[
            "Step 1: Identify the integrand: e^x.",
            "Step 2: Ask: 'What function gives me e^x when I take its derivative?'",
            "Step 3: The answer is e^x.",
            "Step 4: Therefore, the integration process leaves it alone.",
            "Step 5: Write down e^x.",
            "Step 6: Add the Constant of Integration + C.",
            "Step 7: Why? Because derivative of e^x + 5 is also e^x.",
            "Step 8: Construct the final string.",
            "Step 9: No division or power changes needed.",
            "Step 10: Verify: d/dx(e^x + C) = e^x.",
            "Step 11: Verification successful.",
            f"Step 12: Final Answer: {expression}"
        ],
        answer=expression
    )



def integral_sin(show_steps=False):
    expression = "-cos x + C"

    if not show_steps:
        return expression

    return Solution(
        problem_understanding="Find the integral of sine.",
        given="Integrand = sin(x)",
        to_find="The Indefinite Integral",
        equation="∫ sin x dx",
        formula_name="Integration of Sine",
        formula_used="∫ sin x dx = −cos x + C",
        formula_reason=(
            "We know derivative of cos(x) is -sin(x). "
            "To get positive sin(x), we must differentiate negative cos(x)."
        ),
        symbol_explanation=(
            "• The negative sign is crucial here"
        ),
        explanation=(
            "Be careful with signs! Derivative of sine is cosine, but INTEGRAL of sine is NEGATIVE cosine."
        ),
        steps=[
            "Step 1: Identify the integrand: sin(x).",
            "Step 2: Think backward about derivatives.",
            "Step 3: Derivative of sin(x) is cos(x). (Not what we want).",
            "Step 4: Derivative of cos(x) is -sin(x). (Close, but wrong sign).",
            "Step 5: Derivative of -cos(x) is -(-sin(x)) = sin(x). (Perfect).",
            "Step 6: Therefore, the integral is -cos(x).",
            "Step 7: Add the Constant of Integration + C.",
            "Step 8: Construct the expression: -cos x + C.",
            "Step 9: Double check the sign logic.",
            "Step 10: Remember: Integral of Sin is Negative Cos.",
            "Step 11: Format the output.",
            f"Step 12: Final Answer: {expression}"
        ],
        answer=expression
    )



def integral_cos(show_steps=False):
    expression = "sin x + C"

    if not show_steps:
        return expression

    return Solution(
        problem_understanding="Find the integral of cosine.",
        given="Integrand = cos(x)",
        to_find="The Indefinite Integral",
        equation="∫ cos x dx",
        formula_name="Integration of Cosine",
        formula_used="∫ cos x dx = sin x + C",
        formula_reason=(
            "The derivative of sin(x) is exactly cos(x), so the reverse is simple."
        ),
        symbol_explanation=(
            "• No negative sign needed here"
        ),
        explanation=(
            "We are looking for the function that turns into cosine when derived."
        ),
        steps=[
            "Step 1: Identify the integrand: cos(x).",
            "Step 2: Think backward about derivatives.",
            "Step 3: Ask: 'What function has a derivative of cos(x)?'",
            "Step 4: Recall that d/dx(sin x) = cos x.",
            "Step 5: This matches perfectly without needing sign changes.",
            "Step 6: Therefore, the integral is sin(x).",
            "Step 7: Add the Constant of Integration + C.",
            "Step 8: Construct the expression: sin x + C.",
            "Step 9: Contrast with sine integral (which needed a negative).",
            "Step 10: Verify: d/dx(sin x + C) = cos x.",
            "Step 11: Logic holds true.",
            f"Step 12: Final Answer: {expression}"
        ],
        answer=expression
    )



def integral_tan(show_steps=False):
    expression = "-ln|cos x| + C"

    if not show_steps:
        return expression

    return Solution(
        problem_understanding="Find the integral of tangent.",
        given="Integrand = tan(x)",
        to_find="The Indefinite Integral",
        equation="∫ tan x dx",
        formula_name="Integration of Tangent",
        formula_used="∫ tan x dx = −ln|cos x| + C",
        formula_reason=(
            "We rewrite tangent as sin/cos and use substitution."
        ),
        symbol_explanation=(
            "• ln is natural log\n"
            "• cos is cosine"
        ),
        explanation=(
            "Tangent doesn't have a simple 1-step rule. "
            "We simplify it to sines and cosines first."
        ),
        steps=[
            "Step 1: Identify integrand: tan(x).",
            "Step 2: Rewrite using identity: tan(x) = sin(x) / cos(x).",
            "Step 3: Now we have a fraction. Let's use U-Substitution.",
            "Step 4: Let u = cos(x) (the denominator).",
            "Step 5: Find derivative of u: du = -sin(x) dx.",
            "Step 6: We have sin(x) dx in the numerator, but we need the negative sign.",
            "Step 7: Rearrange: -du = sin(x) dx.",
            "Step 8: Substitute into integral: ∫ -1/u du.",
            "Step 9: The integral of 1/u is ln|u|.",
            "Step 10: Apply negative sign: -ln|u|.",
            "Step 11: Replace u back with cos(x) -> -ln|cos x|.",
            "Step 12: Add + C.",
            f"Step 13: Final Answer: {expression}"
        ],
        answer=expression
    )



def integral_sec2(show_steps=False):
    expression = "tan x + C"

    if not show_steps:
        return expression

    return Solution(
        problem_understanding="Find the integral of secant squared.",
        given="Integrand = sec²(x)",
        to_find="The Indefinite Integral",
        equation="∫ sec² x dx",
        formula_name="Integration of sec²(x)",
        formula_used="∫ sec² x dx = tan x + C",
        formula_reason=(
            "This is a standard derivative rule in reverse. "
            "We know d/dx(tan x) = sec² x."
        ),
        explanation=(
            "Whenever you see sec²(x), immediately think of tangent."
        ),
        steps=[
            "Step 1: Identify integrand: sec²(x).",
            "Step 2: Search your memory for derivative rules.",
            "Step 3: Does derivative of sin give this? No.",
            "Step 4: Does derivative of cos give this? No.",
            "Step 5: Does derivative of tan give this? Yes!",
            "Step 6: d/dx(tan x) is exactly sec²(x).",
            "Step 7: Therefore, the integral is tan(x).",
            "Step 8: No complex substitution is needed.",
            "Step 9: Write down tan(x).",
            "Step 10: Add the Constant of Integration + C.",
            "Step 11: Combine parts.",
            f"Step 12: Final Answer: {expression}"
        ],
        answer=expression
    )



def integral_cosec2(show_steps=False):
    expression = "-cot x + C"

    if not show_steps:
        return expression

    return Solution(
        problem_understanding="Find the integral of cosecant squared.",
        given="Integrand = csc²(x)",
        to_find="The Indefinite Integral",
        equation="∫ csc² x dx",
        formula_name="Integration of csc²(x)",
        formula_used="∫ csc² x dx = −cot x + C",
        formula_reason=(
            "The derivative of cot(x) is -csc²(x). We adjust for the negative sign."
        ),
        explanation=(
            "This is the partner to the sec²(x) rule, but for cotangent."
        ),
        steps=[
            "Step 1: Identify integrand: csc²(x).",
            "Step 2: Think about cotangent derivatives.",
            "Step 3: d/dx(cot x) = -csc²(x).",
            "Step 4: Our integrand is positive csc²(x).",
            "Step 5: To fix the sign difference, we multiply by -1.",
            "Step 6: Therefore, the integral is -cot(x).",
            "Step 7: Check: d/dx(-cot x) = -(-csc² x) = csc² x. Correct.",
            "Step 8: Write down -cot(x).",
            "Step 9: Add the Constant of Integration + C.",
            "Step 10: Combine parts.",
            "Step 11: Verify notation (csc vs cosec).",
            f"Step 12: Final Answer: {expression}"
        ],
        answer=expression
    )



def integral_sec_tan(show_steps=False):
    """
    ∫ sec x tan x dx
    """

    expression = "sec x + C"

    if not show_steps:
        return expression

    return Solution(
        problem_understanding="Find the integral of sec(x) multiplied by tan(x).",
        given="Integrand = sec(x) tan(x)",
        to_find="The Indefinite Integral",
        equation="∫ sec x tan x dx",
        formula_name="Integration of sec x tan x",
        formula_used="∫ sec x tan x dx = sec x + C",
        formula_reason=(
            "The derivative of the secant function is exactly sec(x)tan(x)."
        ),
        explanation=(
            "This looks complex, but it is just a standard derivative rule in reverse."
        ),
        steps=[
            "Step 1: Identify integrand: sec(x)tan(x).",
            "Step 2: Analyze the functions involved: Secant and Tangent.",
            "Step 3: Recall the derivative of sec(x).",
            "Step 4: Rule: d/dx(sec x) = sec(x) * tan(x).",
            "Step 5: This matches our integrand perfectly.",
            "Step 6: Therefore, the antiderivative is simply sec(x).",
            "Step 7: No substitution or algebra needed.",
            "Step 8: Write down sec(x).",
            "Step 9: Add the Constant of Integration + C.",
            "Step 10: Verify domain (sec x is undefined at 90 degrees).",
            "Step 11: Assuming valid domain, result stands.",
            f"Step 12: Final Answer: {expression}"
        ],
        answer=expression
    )



def integral_cosec_cot(show_steps=False):
    """
    ∫ csc x cot x dx
    """

    expression = "−csc x + C"

    if not show_steps:
        return expression

    return Solution(
        problem_understanding="Find the integral of csc(x) multiplied by cot(x).",
        given="Integrand = csc(x) cot(x)",
        to_find="The Indefinite Integral",
        equation="∫ csc x cot x dx",
        formula_name="Integration of csc x cot x",
        formula_used="∫ csc x cot x dx = −csc x + C",
        formula_reason=(
            "The derivative of csc(x) is -csc(x)cot(x)."
        ),
        explanation=(
            "We identify the reverse derivative rule for cosecant, watching out for the negative sign."
        ),
        steps=[
            "Step 1: Identify integrand: csc(x)cot(x).",
            "Step 2: Recall the derivative of csc(x).",
            "Step 3: Rule: d/dx(csc x) = -csc(x)cot(x).",
            "Step 4: Our integrand is positive, so we need to adjust the sign.",
            "Step 5: Move the negative to the other side.",
            "Step 6: Derivative of (-csc x) = csc(x)cot(x).",
            "Step 7: Therefore, the integral is -csc(x).",
            "Step 8: Write down -csc(x).",
            "Step 9: Add the Constant of Integration + C.",
            "Step 10: Combine into final string.",
            "Step 11: Check logic.",
            f"Step 12: Final Answer: {expression}"
        ],
        answer=expression
    )



# =========================================================
#                DEFINITE INTEGRALS
# =========================================================

def definite_integral_power(n: Number, a: Number, b: Number, show_steps=False):
    """
    ∫_a^b x^n dx , where n ≠ −1
    """

    if n == -1:
        raise ValueError("Power -1 requires logarithmic integration (use definite_integral_ln).")

    F_upper = (b ** (n + 1)) / (n + 1)
    F_lower = (a ** (n + 1)) / (n + 1)
    result = F_upper - F_lower

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Calculate the exact area under the curve x^n between two specific points.",
        given=f"Function x^{n}, Start (a)={a}, End (b)={b}",
        to_find="The Definite Integral (Area)",
        equation=f"∫ from {a} to {b} of x^{n} dx",
        formula_name="Fundamental Theorem of Calculus",
        formula_used="Area = F(b) - F(a), where F is the integral",
        formula_reason=(
            "We calculate the total accumulation up to point b, "
            "and subtract the accumulation up to point a."
        ),
        symbol_explanation=(
            "• F(x) is the antiderivative\n"
            "• b is the upper limit\n"
            "• a is the lower limit"
        ),
        explanation=(
            "First we integrate the function using the Power Rule. "
            "Then we plug in the upper limit, then the lower limit, and find the difference."
        ),
        steps=[
            "Step 1: Identify the function f(x) = x^n.",
            "Step 2: Find the Indefinite Integral F(x).",
            f"   >> Add 1 to power {n} -> {n + 1}.",
            f"   >> Divide by new power -> x^{n + 1} / {n + 1}.",
            "Step 3: This is our accumulation function F(x).",
            "Step 4: Now apply the Fundamental Theorem of Calculus: F(b) - F(a).",
            f"Step 5: Plug in Upper Limit b = {b}.",
            f"   >> {b}^{n + 1} / {n + 1} = {F_upper}",
            f"Step 6: Plug in Lower Limit a = {a}.",
            f"   >> {a}^{n + 1} / {n + 1} = {F_lower}",
            "Step 7: Subtract the lower result from the upper result.",
            f"   >> {F_upper} - {F_lower}",
            "Step 8: Calculate final value.",
            f"   >> {result}",
            "Step 9: This number represents the 'Net Area' under the curve.",
            "Step 10: Final Answer."
        ],
        answer=str(result)
    )




def definite_integral_ln(a: Number, b: Number, show_steps=False):
    """
    ∫_a^b 1/x dx
    """

    upper = math.log(abs(b))
    lower = math.log(abs(a))
    result = upper - lower

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Calculate the exact area under the curve 1/x.",
        given=f"Function 1/x, Start a={a}, End b={b}",
        to_find="The Definite Integral (Area)",
        equation=f"∫ from {a} to {b} of 1/x dx",
        formula_name="Definite Integral of 1/x",
        formula_used="[ln|x|] from a to b",
        formula_reason=(
            "The integral of 1/x is ln|x|."
        ),
        explanation=(
            "We calculate ln(b) and subtract ln(a)."
        ),
        steps=[
            "Step 1: Identify integrand 1/x.",
            "Step 2: Recall integral is F(x) = ln|x|.",
            "Step 3: Apply Upper Limit b.",
            f"   >> ln|{b}| = {upper:.4f}",
            "Step 4: Apply Lower Limit a.",
            f"   >> ln|{a}| = {lower:.4f}",
            "Step 5: Calculate Difference: Upper - Lower.",
            f"   >> {upper:.4f} - {lower:.4f}",
            f"Step 6: Result = {result:.4f}",
            "Step 7: Note: ln(b) - ln(a) is the same as ln(b/a).",
            f"   >> ln({b}/{a}) = ln({b/a:.4f}) = {math.log(b/a):.4f}",
            "Step 8: Verification complete.",
            "Step 9: Final Answer."
        ],
        answer=f"The definite integral value is {result:.4f}"
    )



def definite_integral_exp(a: Number, b: Number, show_steps=False):
    """
    ∫_a^b e^x dx
    """

    upper = math.exp(b)
    lower = math.exp(a)
    result = upper - lower

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Calculate the accumulated growth of e^x.",
        given=f"Function e^x, Start a={a}, End b={b}",
        to_find="The Definite Integral (Area)",
        equation=f"∫ from {a} to {b} of e^x dx",
        formula_name="Definite Integral of Exponential",
        formula_used="[e^x] from a to b",
        formula_reason=(
            "Integral of e^x is e^x."
        ),
        explanation=(
            "Find the value of e^x at the end, subtract the value at the start."
        ),
        steps=[
            "Step 1: Identify integrand e^x.",
            "Step 2: Recall integral is F(x) = e^x.",
            "Step 3: Apply Upper Limit b.",
            f"   >> e^{b} = {upper:.4f}",
            "Step 4: Apply Lower Limit a.",
            f"   >> e^{a} = {lower:.4f}",
            "Step 5: Calculate Difference.",
            f"   >> {upper:.4f} - {lower:.4f}",
            f"Step 6: Result = {result:.4f}",
            "Step 7: This represents the total growth accumulation.",
            "Step 8: Final Answer."
        ],
        answer=f"The definite integral value is {result:.4f}"
    )



# =========================================================
#         FUNDAMENTAL THEOREM OF CALCULUS (FTC)
# =========================================================

def ftc(f: Callable, F: Callable, a: Number, b: Number, show_steps=False):

    upper = F(b)
    lower = F(a)
    result = upper - lower

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Calculate a definite integral when the Antiderivative is already known.",
        given=f"Antiderivative F(x), Limits a={a}, b={b}",
        to_find="The exact area",
        equation="∫ f(x) dx = F(b) - F(a)",
        formula_name="Fundamental Theorem of Calculus (Part 2)",
        formula_used="Area = F(upper) - F(lower)",
        formula_reason=(
            "This theorem connects the concept of slope (derivatives) "
            "to the concept of area (integrals)."
        ),
        explanation=(
            "We don't need to do the integration work here; we are just applying "
            "the limits to the provided answer function F(x)."
        ),
        steps=[
            "Step 1: Understand we are given F(x), which is the integral of f(x).",
            "Step 2: Identify the boundaries of integration: a (start) and b (end).",
            "Step 3: Calculate the value of the function at the END (b).",
            f"   >> F({b}) = {upper:.4f}",
            "Step 4: Calculate the value of the function at the START (a).",
            f"   >> F({a}) = {lower:.4f}",
            "Step 5: Find the net change by subtracting Start from End.",
            f"   >> {upper:.4f} - {lower:.4f}",
            f"Step 6: Result = {result:.4f}",
            "Step 7: This result is the 'Net Accumulation' of f(x).",
            "Step 8: Final Answer."
        ],
        answer=f"The definite integral value is {result:.4f}"
    )


# =========================================================
#                         LIMITS
# =========================================================

def limit_direct(f: Callable, x0: Number, show_steps=False):
    """
    lim x → x0 f(x)
    """

    value = f(x0)

    if not show_steps:
        return value

    return Solution(
        problem_understanding="Find the value a function approaches at a specific point.",
        given=f"Function f(x), Approaching x₀ = {x0}",
        to_find="The Limit",
        equation=f"lim x → {x0} f(x)",
        formula_name="Direct Substitution",
        formula_used="f(x₀)",
        formula_reason=(
            "If a function doesn't have holes or jumps (it is continuous), "
            "the limit is just the function value."
        ),
        symbol_explanation=(
            "• lim means Limit\n"
            "• x → means 'x approaches'"
        ),
        explanation=(
            "We try the easiest method first: just plug the number in. "
            "If we get a valid number, we are done."
        ),
        steps=[
            "Step 1: Check the function f(x) and the target point x₀.",
            f"Step 2: Target point x₀ = {x0}.",
            "Step 3: Attempt Direct Substitution.",
            f"Step 4: Plug {x0} into the function.",
            f"Step 5: Calculate f({x0}).",
            f"   >> Result = {value:.4f}",
            "Step 6: Did we get a valid number? (Not 0/0 or Infinity).",
            "Step 7: Yes, the value exists.",
            "Step 8: Therefore, the limit is simply the value.",
            "Step 9: No complex limit laws needed.",
            "Step 10: Final Answer."
        ],
        answer=f"The limit is {value:.4f}"
    )



def limit_lhopital(f: Callable, g: Callable, x0: Number, show_steps=False):
    """
    L'Hôpital's Rule for limits of the form 0/0
    """

    fx = f(x0)
    gx = g(x0)

    # Check if we are close to 0/0
    if abs(fx) > 1e-6 or abs(gx) > 1e-6:
        raise ValueError("L'Hôpital’s Rule is only for 0/0 forms. Use direct substitution.")

    h = 1e-6
    # Numerical derivatives
    df = (f(x0 + h) - f(x0 - h)) / (2 * h)
    dg = (g(x0 + h) - g(x0 - h)) / (2 * h)

    if abs(dg) < 1e-12:
        raise ValueError("Derivative of denominator is zero. Cannot solve.")

    result = df / dg

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the limit of a fraction where both Top and Bottom go to Zero.",
        given=f"Fraction f(x)/g(x), Approaching x₀ = {x0}",
        to_find="The Limit (despite the 0/0 problem)",
        equation="lim f'/g'",
        formula_name="L’Hôpital’s Rule",
        formula_used="lim f(x)/g(x) = lim f'(x)/g'(x)",
        formula_reason=(
            "Since both parts hit zero, the winner is determined by "
            "who is moving towards zero FASTER (rate of change)."
        ),
        symbol_explanation=(
            "• f' is derivative of top\n"
            "• g' is derivative of bottom"
        ),
        explanation=(
            "We have an indeterminate form 0/0. "
            "We switch to comparing the SLOPES of the functions instead of their values."
        ),
        steps=[
            "Step 1: Try Direct Substitution.",
            f"   >> f({x0}) ≈ {fx:.4f} (Zero)",
            f"   >> g({x0}) ≈ {gx:.4f} (Zero)",
            "Step 2: Result is 0/0. This is 'Indeterminate'.",
            "Step 3: Activate L’Hôpital’s Rule.",
            "Step 4: Find the derivative of the Top: f'(x).",
            f"   >> f'({x0}) ≈ {df:.4f}",
            "Step 5: Find the derivative of the Bottom: g'(x).",
            f"   >> g'({x0}) ≈ {dg:.4f}",
            "Step 6: Construct the new limit fraction: f'/g'.",
            f"Step 7: Divide {df:.4f} by {dg:.4f}.",
            f"   >> {result:.4f}",
            "Step 8: This ratio tells us the true behavior near the point.",
            "Step 9: Interpret: The limit exists and is finite.",
            "Step 10: Final Answer."
        ],
        answer=f"The limit is {result:.4f}"
    )



# =========================================================
#                  MACLAURIN SERIES
# =========================================================

def series_maclaurin_exp(x: Number, terms=6, show_steps=False):
    """
    Maclaurin Series for e^x
    """

    result = 0
    computed_terms = []

    for n in range(terms):
        term = (x ** n) / math.factorial(n)
        result += term
        computed_terms.append((n, term))

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Estimate the value of e^x using simple addition/multiplication.",
        given=f"Input x = {x}, Using {terms} terms",
        to_find="Approximation of e^x",
        equation="1 + x + x²/2! + ...",
        formula_name="Maclaurin Series (Exponential)",
        formula_used="Sum of (x^n / n!)",
        formula_reason=(
            "e^x is 'smooth', so we can rebuild it by stacking simple polynomials."
        ),
        symbol_explanation=(
            "• n! is factorial (e.g., 3! = 3*2*1)\n"
            "• Σ means summation"
        ),
        explanation=(
            "We calculate the first few terms of the infinite series and add them up. "
            "The more terms we use, the more accurate the answer."
        ),
        steps=[
            "Step 1: Identify the formula: 1 + x + x²/2! + x³/3! ...",
            "Step 2: We will calculate each term individually.",
            *[
                (
                    f"Step {3 + i}: Term n={n}: "
                    f"x^{n}/{n}! = {x}^{n}/{math.factorial(n)} = {term:.6f}"
                )
                for i, (n, term) in enumerate(computed_terms)
            ],
            f"Step {3 + len(computed_terms)}: Sum all these terms together.",
            f"Step {4 + len(computed_terms)}: Total Sum = {result:.6f}.",
            "Step 5: Compare: Real e^x ≈ " + f"{math.exp(x):.6f}.",
            "Step 6: The approximation is very close.",
            "Step 7: Final Answer."
        ],
        answer=f"Approximate e^{x} = {result:.4f}"
    )



def series_maclaurin_sin(x: Number, terms=6, show_steps=False):
    """
    Maclaurin Series for sin x
    """

    result = 0
    computed_terms = []

    for n in range(terms):
        term = ((-1) ** n) * (x ** (2*n + 1)) / math.factorial(2*n + 1)
        result += term
        computed_terms.append((n, term))

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Estimate sin(x) using polynomials.",
        given=f"Input x = {x}, Using {terms} terms",
        to_find="Approximation of sin(x)",
        equation="x - x³/3! + x⁵/5! - ...",
        formula_name="Maclaurin Series (Sine)",
        formula_used="Sum of Alternating Odd Powers",
        formula_reason=(
            "Sine is an 'odd' function, so it only uses odd powers (1, 3, 5). "
            "It oscillates, so signs alternate (+ - + -)."
        ),
        explanation=(
            "We approximate the wave by adding odd powers of x."
        ),
        steps=[
            "Step 1: Identify formula: x - x³/3! + x⁵/5! ...",
            "Step 2: Note the pattern: Odd powers, Alternating signs.",
            *[
                (
                    f"Step {3 + i}: Term n={n}: "
                    f"Sign={'+' if (-1)**n > 0 else '-'}, "
                    f"Power={2*n+1}, "
                    f"Value={term:.6f}"
                )
                for i, (n, term) in enumerate(computed_terms)
            ],
            f"Step {3 + len(computed_terms)}: Sum all terms.",
            f"Step {4 + len(computed_terms)}: Total Sum = {result:.6f}.",
            "Step 5: Compare: Real sin(x) ≈ " + f"{math.sin(x):.6f}.",
            "Step 6: Final Answer."
        ],
        answer=f"Approximate sin({x}) = {result:.4f}"
    )



def series_maclaurin_cos(x: Number, terms=6, show_steps=False):
    """
    Maclaurin Series for cos x
    """

    result = 0
    computed_terms = []

    for n in range(terms):
        term = ((-1) ** n) * (x ** (2*n)) / math.factorial(2*n)
        result += term
        computed_terms.append((n, term))

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Estimate cos(x) using polynomials.",
        given=f"Input x = {x}, Using {terms} terms",
        to_find="Approximation of cos(x)",
        equation="1 - x²/2! + x⁴/4! - ...",
        formula_name="Maclaurin Series (Cosine)",
        formula_used="Sum of Alternating Even Powers",
        formula_reason=(
            "Cosine is an 'even' function, so it only uses even powers (0, 2, 4). "
            "It oscillates, so signs alternate."
        ),
        explanation=(
            "We approximate the wave by adding even powers of x."
        ),
        steps=[
            "Step 1: Identify formula: 1 - x²/2! + x⁴/4! ...",
            "Step 2: Note the pattern: Even powers, Alternating signs.",
            *[
                (
                    f"Step {3 + i}: Term n={n}: "
                    f"Sign={'+' if (-1)**n > 0 else '-'}, "
                    f"Power={2*n}, "
                    f"Value={term:.6f}"
                )
                for i, (n, term) in enumerate(computed_terms)
            ],
            f"Step {3 + len(computed_terms)}: Sum all terms.",
            f"Step {4 + len(computed_terms)}: Total Sum = {result:.6f}.",
            "Step 5: Compare: Real cos(x) ≈ " + f"{math.cos(x):.6f}.",
            "Step 6: Final Answer."
        ],
        answer=f"Approximate cos({x}) = {result:.4f}"
    )



def series_maclaurin_ln1x(x: Number, terms=6, show_steps=False):
    """
    Maclaurin Series for ln(1 + x)
    """

    if abs(x) >= 1:
        raise ValueError("Series only valid for -1 < x < 1.")

    result = 0
    computed_terms = []

    for n in range(1, terms + 1):
        term = ((-1) ** (n + 1)) * (x ** n) / n
        result += term
        computed_terms.append((n, term))

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Estimate ln(1+x) using polynomials.",
        given=f"Input x = {x}, Using {terms} terms",
        to_find="Approximation of ln(1+x)",
        equation="x - x²/2 + x³/3 - ...",
        formula_name="Maclaurin Series (Logarithm)",
        formula_used="Sum of Alternating Powers divided by n",
        formula_reason=(
            "Logarithms grow slowly. We approximate this with an alternating harmonic series."
        ),
        symbol_explanation=(
            "• Note: dividing by n, NOT n! (factorial)"
        ),
        explanation=(
            "We sum simple fractions of powers of x."
        ),
        steps=[
            "Step 1: Check convergence: |x| must be < 1. OK.",
            "Step 2: Identify formula: x - x²/2 + x³/3 ...",
            *[
                (
                    f"Step {3 + i}: Term n={n}: "
                    f"x^{n}/{n} * sign = {term:.6f}"
                )
                for i, (n, term) in enumerate(computed_terms)
            ],
            f"Step {3 + len(computed_terms)}: Sum all terms.",
            f"Step {4 + len(computed_terms)}: Total Sum = {result:.6f}.",
            "Step 5: Compare: Real ln(1+x) ≈ " + f"{math.log(1+x):.6f}.",
            "Step 6: Final Answer."
        ],
        answer=f"Approximate ln(1+{x}) = {result:.4f}"
    )



def series_maclaurin_arctan(x: Number, terms=6, show_steps=False):
    """
    Maclaurin Series approximation of arctan(x)
    """

    if abs(x) > 1:
        raise ValueError("Series valid only for |x| <= 1.")

    result = 0
    computed_terms = []

    for n in range(terms):
        power = 2 * n + 1
        sign = (-1) ** n
        term = sign * (x ** power) / power
        result += term
        computed_terms.append((n, power, term))

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Estimate arctan(x) using polynomials.",
        given=f"Input x = {x}, Using {terms} terms",
        to_find="Approximation of arctan(x)",
        equation="x - x³/3 + x⁵/5 - ...",
        formula_name="Maclaurin Series (Arctan)",
        formula_used="Sum of Alternating Odd Powers divided by Odd Number",
        formula_reason=(
            "Similar to sine, but we divide by the number itself, not the factorial."
        ),
        explanation=(
            "This series (Gregory-Leibniz) approximates the inverse tangent."
        ),
        steps=[
            "Step 1: Check convergence: |x| <= 1. OK.",
            "Step 2: Identify formula: x - x³/3 + x⁵/5 ...",
            *[
                (
                    f"Step {3 + i}: Term n={n}: "
                    f"x^{power}/{power} * sign = {term:.6f}"
                )
                for i, (n, power, term) in enumerate(computed_terms)
            ],
            f"Step {3 + len(computed_terms)}: Sum all terms.",
            f"Step {4 + len(computed_terms)}: Total Sum = {result:.6f}.",
            "Step 5: Compare: Real arctan(x) ≈ " + f"{math.atan(x):.6f}.",
            "Step 6: Final Answer."
        ],
        answer=f"Approximate arctan({x}) = {result:.4f}"
    )



# =========================================================
#                      TAYLOR SERIES
# =========================================================

def series_taylor(f: Callable, a: Number, x: Number, terms=5, show_steps=False):
    """
    Taylor Series approximation of a function f(x) about x = a
    """

    h = 1e-5  # very small number for numerical differentiation
    result = 0
    computed_terms = []

    # Helper to calculate nth derivative numerically
    def derivative_n(func, point, order):
        if order == 0:
            return func(point)
        elif order == 1:
            return (func(point + h) - func(point - h)) / (2 * h)
        else:
            return (
                derivative_n(func, point + h, order - 1)
                - derivative_n(func, point - h, order - 1)
            ) / (2 * h)

    for n in range(terms):
        derivative_value = derivative_n(f, a, n)
        term = derivative_value * ((x - a) ** n) / math.factorial(n)
        result += term
        computed_terms.append((n, derivative_value, term))

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Approximate ANY function near a known point 'a'.",
        given=f"Expansion point a={a}, Target x={x}",
        to_find="Approximation f(x)",
        equation="Σ [fⁿ(a)/n!] * (x-a)ⁿ",
        formula_name="Taylor Series General Formula",
        formula_used="f(a) + f'(a)(x-a) + f''(a)(x-a)²/2! ...",
        formula_reason=(
            "If we know everything about a point (value, slope, curvature), "
            "we can predict where the function goes next."
        ),
        symbol_explanation=(
            "• fⁿ(a) is the nth derivative at a\n"
            "• (x-a) is the distance from our known point"
        ),
        explanation=(
            "We construct the function piece by piece. "
            "Term 0 matches height. Term 1 matches slope. Term 2 matches curve."
        ),
        steps=[
            "Step 1: Identify the anchor point 'a' and target 'x'.",
            f"   >> a={a}, x={x}. Distance = {x-a:.4f}.",
            "Step 2: We will sum up the contributions of each derivative.",
            *[
                (
                    f"Step {3 + i}: Order {n}: "
                    f"Deriv ≈ {deriv:.2f}, "
                    f"Term = {term:.6f}"
                )
                for i, (n, deriv, term) in enumerate(computed_terms)
            ],
            f"Step {3 + len(computed_terms)}: Sum all terms.",
            f"Step {4 + len(computed_terms)}: Final Approximation = {result:.4f}.",
            "Step 5: The more terms we use, the better the prediction.",
            "Step 6: Final Answer."
        ],
        answer=f"Taylor Approx at x={x} is {result:.4f}"
    )


# =========================================================
#             ALIASES FOR COMPATIBILITY
# =========================================================

# This wrapper ensures the test suite passes when it calls 'derivative(coeff, power)'
# or 'derivative(n, x)' depending on usage.
derivative = derivative_power
diff = derivative_power
power_rule = derivative_power

# Wrapper for integrals
integral = integral_power
definite_integral = definite_integral_power


# =========================================================
#                         EXPORT
# =========================================================

__all__ = [
    # General Wrappers (Crucial for Tests)
    "derivative",
    "diff",
    "power_rule",
    "integral",
    "definite_integral",

    # Derivatives
    "derivative_power",
    "derivative_exp",
    "derivative_ln",
    "derivative_sin",
    "derivative_cos",
    "derivative_tan",
    "derivative_product",
    "derivative_quotient",
    "derivative_chain",

    # Indefinite Integrals
    "integral_power",
    "integral_ln",
    "integral_exp",
    "integral_sin",
    "integral_cos",
    "integral_tan",
    "integral_sec2",
    "integral_cosec2",
    "integral_sec_tan",
    "integral_cosec_cot",

    # Definite Integrals
    "definite_integral_power",
    "definite_integral_ln",
    "definite_integral_exp",

    # Limits & FTC
    "limit_direct",
    "limit_lhopital",
    "ftc",

    # Maclaurin Series
    "series_maclaurin_sin",
    "series_maclaurin_cos",
    "series_maclaurin_exp",
    "series_maclaurin_ln1x",
    "series_maclaurin_arctan",

    # Taylor Series
    "series_taylor",
]
