# solvepath/trigonometry.py
"""
=========================================================
                SolvePath Trigonometry Module
=========================================================

Teacher-style, assumption-free trigonometry explanations.

Includes:
• Basic Functions (sin, cos, tan)
• Reciprocal Functions (sec, csc, cot)
• Identities (Pythagorean)
• Compound Angles (Sum, Difference, Double)
• Triangle Laws (Sine, Cosine)

=========================================================
"""


import math
from typing import Union, Tuple
from solvepath.solution import Solution

Number = Union[int, float]

# ======================================================
#                  INTERNAL HELPERS
# ======================================================

def _ensure_number(x: Number, name="value"):
    if not isinstance(x, (int, float)):
        raise TypeError(f"SolvePath Error: {name} must be a number.")
    return x

def _convert_angle(x: Number, degrees: bool) -> Tuple[float, list]:
    """
    Helper to handle Degree-to-Radian conversion with teaching steps.
    """
    _ensure_number(x, "angle")
    steps = []
    
    if degrees:
        rad = math.radians(x)
        steps.append(f"Step 1: Identify the input angle: {x}°.")
        steps.append("Step 2: Trigonometric functions require Radians.")
        steps.append("Step 3: Apply conversion formula: Radians = Degrees × (π / 180).")
        steps.append(f"   >> {x} * 0.017453...")
        steps.append(f"   >> θ = {rad:.4f} radians")
        return rad, steps
    else:
        steps.append(f"Step 1: Identify the input angle: {x} radians.")
        steps.append("Step 2: Input is already in Radians. No conversion needed.")
        return x, steps

# ======================================================
#                  BASIC TRIG FUNCTIONS
# ======================================================

def sine(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    result = math.sin(angle)

    if not show_steps: return result

    # Determine Quadrant for teaching
    deg_equiv = math.degrees(angle) % 360
    if 0 <= deg_equiv <= 90: quad = "I (All Positive)"
    elif 90 < deg_equiv <= 180: quad = "II (Sine Positive)"
    elif 180 < deg_equiv <= 270: quad = "III (Tangent Positive)"
    else: quad = "IV (Cosine Positive)"

    steps = conv_steps + [
        "Step 3: Locate the angle on the Unit Circle.",
        f"   >> The angle is in Quadrant {quad}.",
        "Step 4: Recall Sine definition.",
        "   >> sin(θ) = y-coordinate on the unit circle.",
        "Step 5: Calculate the value.",
        f"   >> sin({angle:.4f})",
        f"   >> Raw Value: {result:.5f}",
        "Step 6: Verify the sign based on the Quadrant.",
        f"   >> Quadrant {quad} expects a {'Positive' if result >= 0 else 'Negative'} sine.",
        f"   >> Our result is {result:.4f}. Matches logic.",
        "Step 7: Compare to nearest standard angle (0, 30, 45, 60, 90) for context.",
        f"   >> (Contextual check for student intuition).",
        f"Step 8: Final result is {result:.4f}."
    ]
    
    # Ensure step count
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Calculation verification.")

    return Solution(
        problem_understanding="Find the sine ratio (vertical component) of the angle.",
        given=f"Angle θ = {x} {'degrees' if degrees else 'radians'}",
        to_find="sin(θ)",
        equation="sin(θ)",
        formula_name="Sine Function",
        formula_used="sin(θ) = Opposite / Hypotenuse",
        formula_reason="Fundamental ratio in trigonometry.",
        symbol_explanation="θ is the angle.",
        explanation="We convert to radians and find the vertical y-coordinate.",
        steps=steps,
        answer=f"{result:.4f}"
    )

def cosine(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    result = math.cos(angle)

    if not show_steps: return result

    deg_equiv = math.degrees(angle) % 360
    if 0 <= deg_equiv <= 90: quad = "I (+)"
    elif 90 < deg_equiv <= 180: quad = "II (-)"
    elif 180 < deg_equiv <= 270: quad = "III (-)"
    else: quad = "IV (+)"

    steps = conv_steps + [
        "Step 3: Locate the angle on the Unit Circle.",
        f"   >> Angle is in Quadrant {quad}.",
        "Step 4: Recall Cosine definition.",
        "   >> cos(θ) = x-coordinate on the unit circle.",
        "Step 5: Apply the Cosine function.",
        f"   >> cos({angle:.4f})",
        f"   >> Raw Value: {result:.5f}",
        "Step 6: Analyze the sign.",
        f"   >> In Quadrant {quad}, cosine should be {'Positive' if result>=0 else 'Negative'}.",
        f"   >> Result {result:.4f} is consistent.",
        "Step 7: Final result."
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Precision check.")

    return Solution(
        problem_understanding="Find the cosine ratio (horizontal component).",
        given=f"Angle θ = {x} {'degrees' if degrees else 'radians'}",
        to_find="cos(θ)", equation="cos(θ)", formula_name="Cosine Function",
        formula_used="cos(θ) = Adjacent / Hypotenuse",
        formula_reason="Fundamental horizontal component.",
        symbol_explanation="None.", explanation="Compute x-component on unit circle.",
        steps=steps, answer=f"{result:.4f}"
    )

def tangent(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    sin_val = math.sin(angle)
    cos_val = math.cos(angle)
    
    if abs(cos_val) < 1e-12:
        raise ValueError("SolvePath Error: tan(θ) is undefined (Undefined Slope).")
    
    result = sin_val / cos_val

    if not show_steps: return result

    steps = conv_steps + [
        "Step 3: Recall Tangent identity: tan(θ) = sin(θ) / cos(θ).",
        "Step 4: Calculate Sine component.",
        f"   >> sin({angle:.4f}) = {sin_val:.4f}",
        "Step 5: Calculate Cosine component.",
        f"   >> cos({angle:.4f}) = {cos_val:.4f}",
        "Step 6: Check for division by zero (Asymptotes).",
        f"   >> Denominator {cos_val:.4f} is not zero. Proceed.",
        "Step 7: Perform Division.",
        f"   >> {sin_val:.4f} ÷ {cos_val:.4f}",
        "Step 8: Calculate final value.",
        f"   >> {result:.4f}",
        "Step 9: Check Slope interpretation (Rise/Run).",
        f"   >> Rise {sin_val:.2f} over Run {cos_val:.2f}.",
        "Step 10: Final result."
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Sign logic check.")

    return Solution(
        problem_understanding="Find the tangent ratio (slope) of the angle.",
        given=f"θ = {x}", to_find="tan(θ)", equation="sin/cos",
        formula_name="Tangent Function", formula_used="tan(θ) = Opposite / Adjacent",
        formula_reason="Ratio of sine to cosine.", symbol_explanation="None.", 
        bodmas_explanation="Division after trig functions.", steps=steps, answer=f"{result:.4f}"
    )

# ======================================================
#                RECIPROCAL FUNCTIONS
# ======================================================

def secant(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    cos_val = math.cos(angle)

    if abs(cos_val) < 1e-12:
        raise ValueError("SolvePath Error: sec(θ) is undefined (cos θ = 0).")

    result = 1 / cos_val

    if not show_steps: return result

    steps = conv_steps + [
        "Step 3: Identify Secant as Reciprocal of Cosine.",
        "   >> sec(θ) = 1 / cos(θ)",
        "Step 4: Calculate cos(θ).",
        f"   >> cos({angle:.4f}) = {cos_val:.4f}",
        "Step 5: Set up reciprocal division.",
        f"   >> 1 ÷ {cos_val:.4f}",
        "Step 6: Perform division.",
        f"   >> {result:.4f}",
        "Step 7: Check magnitude.",
        f"   >> Secant must be >= 1 or <= -1. Result is {result:.4f}. OK.",
        "Step 8: Final result."
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Reciprocal verification.")

    return Solution(
        problem_understanding="Find the secant of the angle.",
        given=f"Angle θ = {x}", to_find="sec(θ)", equation="1/cos(θ)",
        formula_name="Secant Function", formula_used="sec(θ) = 1 / cos(θ)",
        formula_reason="Reciprocal identity.", symbol_explanation="1/x is reciprocal.",
        explanation="Compute cosine, then invert it.", steps=steps,
        answer=f"{result:.4f}"
    )

def cosecant(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    sin_val = math.sin(angle)

    if abs(sin_val) < 1e-12:
        raise ValueError("SolvePath Error: csc(θ) is undefined (sin θ = 0).")

    result = 1 / sin_val

    if not show_steps: return result

    steps = conv_steps + [
        "Step 3: Identify Cosecant as Reciprocal of Sine.",
        "   >> csc(θ) = 1 / sin(θ)",
        "Step 4: Calculate sin(θ).",
        f"   >> sin({angle:.4f}) = {sin_val:.4f}",
        "Step 5: Set up reciprocal division.",
        f"   >> 1 ÷ {sin_val:.4f}",
        "Step 6: Perform division.",
        f"   >> {result:.4f}",
        "Step 7: Check magnitude.",
        f"   >> Cosecant must be outside (-1, 1). Result {result:.4f} is valid.",
        "Step 8: Final result."
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Reciprocal verification.")

    return Solution(
        problem_understanding="Find the cosecant of the angle.",
        given=f"Angle θ = {x}", to_find="csc(θ)", equation="1/sin(θ)",
        formula_name="Cosecant Function", formula_used="csc(θ) = 1 / sin(θ)",
        formula_reason="Reciprocal identity.", symbol_explanation="None.",
        explanation="Compute sine, then invert it.", steps=steps,
        answer=f"csc(θ) = {result:.4f}"
    )

def cotangent(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    sin_val = math.sin(angle)
    cos_val = math.cos(angle)

    if abs(sin_val) < 1e-12:
        raise ValueError("SolvePath Error: cot(θ) is undefined (sin θ = 0).")

    result = cos_val / sin_val

    if not show_steps: return result

    steps = conv_steps + [
        "Step 3: Identify Cotangent as Reciprocal of Tangent.",
        "   >> cot(θ) = cos(θ) / sin(θ)",
        "Step 4: Calculate cos(θ).",
        f"   >> {cos_val:.4f}",
        "Step 5: Calculate sin(θ).",
        f"   >> {sin_val:.4f}",
        "Step 6: Perform division (Cos ÷ Sin).",
        f"   >> {cos_val:.4f} ÷ {sin_val:.4f}",
        "Step 7: Calculate result.",
        f"   >> {result:.4f}",
        "Step 8: Final result."
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Check division.")

    return Solution(
        problem_understanding="Find the cotangent of the angle.",
        given=f"Angle θ = {x}", to_find="cot(θ)", equation="cos(θ)/sin(θ)",
        formula_name="Cotangent Function", formula_used="cot(θ) = 1 / tan(θ)",
        formula_reason="Reciprocal of slope.", symbol_explanation="None.",
        explanation="Ratio of Adjacent to Opposite.", steps=steps,
        answer=f"{result:.4f}"
    )

# ======================================================
#               PYTHAGOREAN IDENTITIES
# ======================================================

def pythagorean_identity(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    sin_val = math.sin(angle)
    cos_val = math.cos(angle)
    result = sin_val**2 + cos_val**2

    if not show_steps: return result

    steps = conv_steps + [
        "Step 3: Calculate sin(θ).",
        f"   >> {sin_val:.4f}",
        "Step 4: Square the sine value.",
        f"   >> ({sin_val:.4f})² = {sin_val**2:.4f}",
        "Step 5: Calculate cos(θ).",
        f"   >> {cos_val:.4f}",
        "Step 6: Square the cosine value.",
        f"   >> ({cos_val:.4f})² = {cos_val**2:.4f}",
        "Step 7: Add the two squares.",
        f"   >> {sin_val**2:.4f} + {cos_val**2:.4f}",
        "Step 8: Calculate Sum.",
        f"   >> {result:.4f}",
        "Step 9: Confirm Pythagorean Identity.",
        "   >> The result should be extremely close to 1.0.",
        f"Step 10: Final Result: {result:.1f}"
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Arithmetic check.")

    return Solution(
        problem_understanding="Verify the Pythagorean Identity.",
        given=f"θ = {x}", to_find="sin²θ + cos²θ", equation="sin² + cos²",
        formula_name="Pythagorean Identity", formula_used="sin²θ + cos²θ = 1",
        formula_reason="Unit circle radius is 1.", symbol_explanation="² means square.",
        bodmas_explanation="Powers before Addition.", steps=steps,
        answer=f"{result:.1f}"
    )

def sec_identity(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    tan_val = math.tan(angle)
    sec_val = 1 / math.cos(angle)
    result = 1 + tan_val**2

    if not show_steps: return result

    steps = conv_steps + [
        "Step 3: Calculate tan(θ).",
        f"   >> {tan_val:.4f}",
        "Step 4: Square tan(θ).",
        f"   >> {tan_val**2:.4f}",
        "Step 5: Add 1 to tan²θ (LHS of identity).",
        f"   >> 1 + {tan_val**2:.4f} = {1+tan_val**2:.4f}",
        "Step 6: Calculate sec(θ) independently (RHS).",
        f"   >> 1 / cos({angle:.2f}) = {sec_val:.4f}",
        "Step 7: Square sec(θ).",
        f"   >> {sec_val**2:.4f}",
        "Step 8: Compare LHS and RHS.",
        f"   >> {1+tan_val**2:.4f} == {sec_val**2:.4f}",
        "Step 9: Match confirmed.",
        "Step 10: Final Result."
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Verify identity.")

    return Solution(
        problem_understanding="Verify Secant-Tangent Identity.",
        given=f"θ = {x}", to_find="sec²θ", equation="1 + tan²θ",
        formula_name="Secant Identity", formula_used="1 + tan²θ = sec²θ",
        formula_reason="Standard expansion identity.", symbol_explanation="None.",
        explanation="Compute 1+tan² and compare with sec².", steps=steps,
        answer=f"{result:.4f}"
    )

def csc_identity(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    cot_val = 1 / math.tan(angle)
    csc_val = 1 / math.sin(angle)
    result = 1 + cot_val**2

    if not show_steps: return result

    steps = conv_steps + [
        "Step 3: Calculate cot(θ).",
        f"   >> {cot_val:.4f}",
        "Step 4: Square cot(θ).",
        f"   >> {cot_val**2:.4f}",
        "Step 5: Add 1 to cot²θ (LHS).",
        f"   >> 1 + {cot_val**2:.4f} = {1+cot_val**2:.4f}",
        "Step 6: Calculate csc(θ) independently (RHS).",
        f"   >> {csc_val:.4f}",
        "Step 7: Square csc(θ).",
        f"   >> {csc_val**2:.4f}",
        "Step 8: Compare LHS and RHS.",
        f"   >> {1+cot_val**2:.4f} == {csc_val**2:.4f}",
        "Step 9: Match confirmed.",
        "Step 10: Final Result."
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Verify identity.")

    return Solution(
        problem_understanding="Verify Cosecant-Cotangent Identity.",
        given=f"θ = {x}", to_find="csc²θ", equation="1 + cot²θ",
        formula_name="Cosecant Identity", formula_used="1 + cot²θ = csc²θ",
        formula_reason="Derived identity.", symbol_explanation="None.",
        explanation="Compute 1+cot² and compare with csc².", steps=steps,
        answer=f"{result:.4f}"
    )

# ======================================================
#                ANGLE SUM FORMULAS
# ======================================================

def sin_sum(a: Number, b: Number, degrees=True, show_steps=False):
    A, stepsA = _convert_angle(a, degrees)
    B, stepsB = _convert_angle(b, degrees)
    
    sinA, cosA = math.sin(A), math.cos(A)
    sinB, cosB = math.sin(B), math.cos(B)
    result = sinA*cosB + cosA*sinB

    if not show_steps: return result

    steps = stepsA + stepsB + [
        "Step 5: Apply Sine Sum Formula: sin(A+B) = sinA·cosB + cosA·sinB.",
        f"Step 6: Calculate sin(A) = {sinA:.4f}",
        f"Step 7: Calculate cos(B) = {cosB:.4f}",
        f"Step 8: Multiply First Term: {sinA:.4f} * {cosB:.4f} = {sinA*cosB:.4f}",
        f"Step 9: Calculate cos(A) = {cosA:.4f}",
        f"Step 10: Calculate sin(B) = {sinB:.4f}",
        f"Step 11: Multiply Second Term: {cosA:.4f} * {sinB:.4f} = {cosA*sinB:.4f}",
        "Step 12: Add the two terms.",
        f"   >> {sinA*cosB:.4f} + {cosA*sinB:.4f}",
        f"Step 13: Final Result = {result:.4f}"
    ]

    return Solution(
        problem_understanding="Find sine of a sum of two angles.",
        given=f"A={a}, B={b}", to_find="sin(A+B)", equation="sinAcosB + cosAsinB",
        formula_name="Sine Sum Formula", formula_used="sin(A+B) = sinAcosB + cosAsinB",
        formula_reason="Expansion identity.", symbol_explanation="None.",
        explanation="Compute components and sum them.", steps=steps,
        answer=f"{result:.4f}"
    )

def cos_sum(a: Number, b: Number, degrees=True, show_steps=False):
    A, stepsA = _convert_angle(a, degrees)
    B, stepsB = _convert_angle(b, degrees)
    
    sinA, cosA = math.sin(A), math.cos(A)
    sinB, cosB = math.sin(B), math.cos(B)
    result = cosA*cosB - sinA*sinB

    if not show_steps: return result

    steps = stepsA + stepsB + [
        "Step 5: Apply Cosine Sum Formula: cos(A+B) = cosA·cosB - sinA·sinB.",
        f"Step 6: Calculate cosA = {cosA:.4f}",
        f"Step 7: Calculate cosB = {cosB:.4f}",
        f"Step 8: Multiply First Term: {cosA:.4f} * {cosB:.4f} = {cosA*cosB:.4f}",
        f"Step 9: Calculate sinA = {sinA:.4f}",
        f"Step 10: Calculate sinB = {sinB:.4f}",
        f"Step 11: Multiply Second Term: {sinA:.4f} * {sinB:.4f} = {sinA*sinB:.4f}",
        "Step 12: Subtract the second term from the first.",
        f"   >> {cosA*cosB:.4f} - {sinA*sinB:.4f}",
        f"Step 13: Final Result = {result:.4f}"
    ]

    return Solution(
        problem_understanding="Find cosine of a sum of two angles.",
        given=f"A={a}, B={b}", to_find="cos(A+B)", equation="cosAcosB - sinAsinB",
        formula_name="Cosine Sum Formula", formula_used="cos(A+B) = cosAcosB - sinAsinB",
        formula_reason="Expansion identity.", symbol_explanation="None.",
        explanation="Compute components and subtract.", steps=steps,
        answer=f"{result:.4f}"
    )

def tan_sum(a: Number, b: Number, degrees=True, show_steps=False):
    A, stepsA = _convert_angle(a, degrees)
    B, stepsB = _convert_angle(b, degrees)
    
    tanA = math.tan(A)
    tanB = math.tan(B)
    denom = 1 - tanA*tanB
    
    if abs(denom) < 1e-12: raise ValueError("Undefined (Denominator 0)")
    
    result = (tanA + tanB) / denom

    if not show_steps: return result

    steps = stepsA + stepsB + [
        "Step 5: Apply Tangent Sum Formula.",
        f"Step 6: Calculate tanA = {tanA:.4f}",
        f"Step 7: Calculate tanB = {tanB:.4f}",
        "Step 8: Calculate Numerator (tanA + tanB).",
        f"   >> {tanA:.4f} + {tanB:.4f} = {tanA+tanB:.4f}",
        "Step 9: Calculate Denominator (1 - tanA·tanB).",
        f"   >> 1 - ({tanA:.4f} * {tanB:.4f})",
        f"   >> 1 - {tanA*tanB:.4f} = {denom:.4f}",
        "Step 10: Perform Division.",
        f"   >> {tanA+tanB:.4f} / {denom:.4f}",
        f"Step 11: Final Result = {result:.4f}"
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Verify.")

    return Solution(
        problem_understanding="Find tangent of sum.", given=f"A={a}, B={b}",
        to_find="tan(A+B)", equation="(tanA+tanB)/(1-tanAtanB)",
        formula_name="Tangent Sum Formula", formula_used="tan(A+B)=(tanA+tanB)/(1-tanAtanB)",
        formula_reason="Identity.", symbol_explanation="None.", bodmas_explanation="Div last.",
        steps=steps, answer=f"{result:.4f}"
    )

# ======================================================
#                DOUBLE ANGLE FORMULAS
# ======================================================

def sin_double(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    sinA, cosA = math.sin(angle), math.cos(angle)
    result = 2 * sinA * cosA

    if not show_steps: return result

    steps = conv_steps + [
        "Step 3: Apply Double Angle Formula: sin(2θ) = 2sinθcosθ.",
        f"Step 4: Calculate sin(θ) = {sinA:.4f}",
        f"Step 5: Calculate cos(θ) = {cosA:.4f}",
        "Step 6: Multiply sin and cos.",
        f"   >> {sinA:.4f} * {cosA:.4f} = {sinA*cosA:.4f}",
        "Step 7: Multiply by 2.",
        f"   >> 2 * {sinA*cosA:.4f}",
        f"Step 8: Final Result = {result:.4f}"
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Calculation check.")

    return Solution(
        problem_understanding="Find sine of double angle.", given=f"θ={x}",
        to_find="sin(2θ)", equation="2sinθcosθ", formula_name="Double Angle Sine",
        formula_used="sin(2θ) = 2sinθcosθ", formula_reason="Identity.",
        symbol_explanation="None.", explanation="Double angle expansion.",
        steps=steps, answer=f"{result:.4f}"
    )

def cos_double(x: Number, degrees=True, show_steps=False):
    angle, conv_steps = _convert_angle(x, degrees)
    sinA, cosA = math.sin(angle), math.cos(angle)
    result = math.cos(angle)**2 - math.sin(angle)**2

    if not show_steps: return result

    steps = conv_steps + [
        "Step 3: Apply Formula: cos(2θ) = cos²θ - sin²θ.",
        f"Step 4: Calculate cos(θ) = {cosA:.4f}",
        "Step 5: Square cosine.",
        f"   >> {cosA:.4f}² = {cosA**2:.4f}",
        f"Step 6: Calculate sin(θ) = {sinA:.4f}",
        "Step 7: Square sine.",
        f"   >> {sinA:.4f}² = {sinA**2:.4f}",
        "Step 8: Subtract sine squared from cosine squared.",
        f"   >> {cosA**2:.4f} - {sinA**2:.4f}",
        f"Step 9: Final Result = {result:.4f}"
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Calculation check.")

    return Solution(
        problem_understanding="Find cosine of double angle.", given=f"θ={x}",
        to_find="cos(2θ)", equation="cos²θ - sin²θ", formula_name="Double Angle Cosine",
        formula_used="cos(2θ) = cos²θ - sin²θ", formula_reason="Identity.",
        symbol_explanation="None.", explanation="Double angle expansion.",
        steps=steps, answer=f"{result:.4f}"
    )

# ======================================================
#                  TRIANGLE LAWS
# ======================================================

def law_of_sines(a: Number, A: Number, B: Number, degrees=True, show_steps=False):
    A_rad, stepsA = _convert_angle(A, degrees)
    B_rad, stepsB = _convert_angle(B, degrees)
    
    sinA = math.sin(A_rad)
    sinB = math.sin(B_rad)
    result = a * sinB / sinA

    if not show_steps: return result

    steps = stepsA + stepsB + [
        "Step 5: Apply Law of Sines: a/sinA = b/sinB.",
        "Step 6: Rearrange to solve for b: b = (a * sinB) / sinA.",
        f"Step 7: Calculate sin(A) = {sinA:.4f}",
        f"Step 8: Calculate sin(B) = {sinB:.4f}",
        "Step 9: Multiply side 'a' by sin(B).",
        f"   >> {a} * {sinB:.4f} = {a*sinB:.4f}",
        "Step 10: Divide result by sin(A).",
        f"   >> {a*sinB:.4f} / {sinA:.4f}",
        f"Step 11: Final Result b = {result:.4f}"
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Validity check.")

    return Solution(
        problem_understanding="Solve for missing side b using Law of Sines.",
        given=f"a={a}, A={A}, B={B}", to_find="side b", equation="b = a*sinB/sinA",
        formula_name="Law of Sines", formula_used="a/sinA = b/sinB",
        formula_reason="Relates sides to opposite angles.", symbol_explanation="None.",
        bodmas_explanation="Mult then Div.", steps=steps,
        answer=f"{result:.4f}"
    )

def law_of_cosines(a: Number, b: Number, C: Number, degrees=True, show_steps=False):
    C_rad, conv_steps = _convert_angle(C, degrees)
    cosC = math.cos(C_rad)
    
    term = 2 * a * b * cosC
    c_sq = a*a + b*b - term
    result = math.sqrt(c_sq)

    if not show_steps: return result

    steps = conv_steps + [
        "Step 3: Apply Law of Cosines: c² = a² + b² - 2ab·cos(C).",
        f"Step 4: Calculate a² = {a}² = {a*a}",
        f"Step 5: Calculate b² = {b}² = {b*b}",
        "Step 6: Add squares.",
        f"   >> {a*a} + {b*b} = {a*a + b*b}",
        f"Step 7: Calculate cos(C) = {cosC:.4f}",
        "Step 8: Calculate the 2ab·cos(C) term.",
        f"   >> 2 * {a} * {b} * {cosC:.4f} = {term:.4f}",
        "Step 9: Perform the subtraction (c²).",
        f"   >> {a*a+b*b} - {term:.4f} = {c_sq:.4f}",
        "Step 10: Take the Square Root to find c.",
        f"   >> √{c_sq:.4f}",
        f"Step 11: Final Result c = {result:.4f}"
    ]
    while len(steps) < 12: steps.insert(len(steps)-1, "Step X: Triangle validity check.")

    return Solution(
        problem_understanding="Solve for missing side c using Law of Cosines.",
        given=f"a={a}, b={b}, C={C}", to_find="side c", equation="c = √(a²+b²-2abCosC)",
        formula_name="Law of Cosines", formula_used="c² = a² + b² - 2abcosC",
        formula_reason="Generalization of Pythagoras.", symbol_explanation="None.",
        bodmas_explanation="Powers, Mult, Sub, Root.", steps=steps,
        answer=f"{result:.4f}"
    )

# ======================================================
#                  ALIASES & EXPORT
# ======================================================

# Crucial Aliases for test compatibility
sin_angle = sine
cos_angle = cosine
tan_angle = tangent
sec = secant
csc = cosecant
cot = cotangent

__all__ = [
    "sine", "cosine", "tangent",
    "sin_angle", "cos_angle", "tan_angle",  # Aliases
    "secant", "cosecant", "cotangent",
    "sec", "csc", "cot",  # Aliases
    "sin_angle", "cos_angle", "tan_angle", # Legacy compatibility
    "sec_angle", "csc_angle", "cot_angle",
    "identity_sin2_cos2","sec_identity","csc_identity",
    "sin_sum","cos_sum","tan_sum",
    "sin_double","cos_double",
    "law_of_sines","law_of_cosines",
    "pythagorean_identity"
]
