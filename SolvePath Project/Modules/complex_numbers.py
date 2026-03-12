# solvepath/complex_numbers.py
"""
=========================================================
              SolvePath Complex Numbers Module
=========================================================

Includes HIGHLY DETAILED, TUTOR-STYLE step-by-step solutions for:

• Complex Addition & Subtraction
• Complex Multiplication (FOIL method)
• Complex Division (Conjugate method)
• Modulus (Magnitude)
• Conjugate
• Argument (Phase Angle)
• Polar Form
• Euler’s Formula
• Polar → Rectangular Conversion

Returns:
• Solution object when show_steps=True
• Final complex/numeric value when show_steps=False

=========================================================
"""

import math
import cmath
from typing import Union, Tuple, List
from solvepath.solution import Solution

Number = Union[int, float, complex]

# ======================================================
# INTERNAL HELPERS
# ======================================================

def _to_complex(z) -> complex:
    """
    Validates and converts input into a Python complex number.
    """
    if isinstance(z, complex):
        return z
    if isinstance(z, (int, float)):
        return complex(z, 0)
    if isinstance(z, (tuple, list)):
        if len(z) == 2:
            return complex(z[0], z[1])
        if len(z) == 1:
            return complex(z[0], 0)
    raise TypeError(f"Input {z} is not a valid complex number representation.")

def _fmt(z: complex) -> str:
    """
    Formats a complex number to look like standard math notation (a + bi)
    instead of Python notation (a + bj).
    """
    real = round(z.real, 4)
    imag = round(z.imag, 4)
    if imag >= 0:
        return f"{real} + {imag}i"
    else:
        return f"{real} - {abs(imag)}i"

# ======================================================
# COMPLEX ADDITION
# ======================================================

def complex_add(z1, z2, show_steps=False):
    z1 = _to_complex(z1)
    z2 = _to_complex(z2)
    result = z1 + z2

    if not show_steps:
        return result

    return Solution(
        given=f"z₁ = {_fmt(z1)}, z₂ = {_fmt(z2)}",
        to_find="The Sum (z₁ + z₂)",
        equation="(a + bi) + (c + di) = (a + c) + (b + d)i",
        formula_name="Complex Addition Formula",
        formula_used="(a + c) + (b + d)i",
        formula_reason="We add real parts to real parts, and imaginary parts to imaginary parts.",
        explanation="We combine the real parts together and the imaginary parts together.",
        steps=[
            f"Step 1: Identify the components.",
            f"   z₁: Real = {z1.real}, Imaginary = {z1.imag}i",
            f"   z₂: Real = {z2.real}, Imaginary = {z2.imag}i",
            f"Step 2: Apply Formula (Group Real parts).",
            f"   ({z1.real} + {z2.real}) = {z1.real + z2.real}",
            f"Step 3: Apply Formula (Group Imaginary parts).",
            f"   ({z1.imag}i + {z2.imag}i) = ({z1.imag + z2.imag})i",
            f"Step 4: Combine into final form.",
            f"   {_fmt(result)}"
        ],
        answer=result
    )

# ======================================================
# COMPLEX SUBTRACTION
# ======================================================

def complex_sub(z1, z2, show_steps=False):
    z1 = _to_complex(z1)
    z2 = _to_complex(z2)
    result = z1 - z2

    if not show_steps:
        return result

    return Solution(
        given=f"z₁ = {_fmt(z1)}, z₂ = {_fmt(z2)}",
        to_find="The Difference (z₁ - z₂)",
        equation="(a + bi) - (c + di) = (a - c) + (b - d)i",
        formula_name="Complex Subtraction Formula",
        formula_used="(a - c) + (b - d)i",
        formula_reason="Subtraction requires distributing the minus sign to BOTH parts of the second number.",
        explanation="We subtract the real part of z₂ from z₁, and the imaginary part of z₂ from z₁.",
        steps=[
            f"Step 1: Set up equation.",
            f"   ({_fmt(z1)}) - ({_fmt(z2)})",
            f"Step 2: Distribute negative sign.",
            f"   -({z2.real}) becomes {-z2.real}",
            f"   -({z2.imag}i) becomes {-z2.imag}i",
            f"Step 3: Subtract Real parts.",
            f"   {z1.real} - {z2.real} = {z1.real - z2.real}",
            f"Step 4: Subtract Imaginary parts.",
            f"   {z1.imag}i - {z2.imag}i = {z1.imag - z2.imag}i",
            f"Step 5: Final Result.",
            f"   {_fmt(result)}"
        ],
        answer=result
    )

# ======================================================
# COMPLEX MULTIPLICATION
# ======================================================

def complex_mul(z1, z2, show_steps=False):
    z1 = _to_complex(z1)
    z2 = _to_complex(z2)
    
    a, b = z1.real, z1.imag
    c, d = z2.real, z2.imag
    
    # Components of FOIL
    first = a * c
    outer = a * d
    inner = b * c
    last = b * d  # This will be multiplied by i^2
    
    result = z1 * z2

    if not show_steps:
        return result

    return Solution(
        given=f"z₁ = ({_fmt(z1)}), z₂ = ({_fmt(z2)})",
        to_find="The Product (z₁ × z₂)",
        equation="(a+bi)(c+di) = (ac - bd) + (ad + bc)i",
        formula_name="Complex Multiplication (FOIL)",
        formula_used="(ac - bd) + (ad + bc)i",
        formula_reason="Standard binomial multiplication where i² = -1.",
        explanation="We expand the brackets using First, Outer, Inner, Last (FOIL), then simplify i² to -1.",
        steps=[
            f"Step 1: Identify coefficients.",
            f"   a={a}, b={b}, c={c}, d={d}",
            f"Step 2: Expand using FOIL.",
            f"   First: {a} * {c} = {first}",
            f"   Outer: {a} * {d}i = {outer}i",
            f"   Inner: {b}i * {c} = {inner}i",
            f"   Last:  {b}i * {d}i = {last}i²",
            f"Step 3: Apply the Identity i² = -1.",
            f"   The 'Last' term becomes: {last} * (-1) = {-last}",
            f"Step 4: Group Real terms (First + Last).",
            f"   {first} + ({-last}) = {first - last}",
            f"Step 5: Group Imaginary terms (Outer + Inner).",
            f"   {outer}i + {inner}i = {outer + inner}i",
            f"Step 6: Final Result.",
            f"   {_fmt(result)}"
        ],
        answer=result
    )

# ======================================================
# COMPLEX DIVISION
# ======================================================

def complex_div(z1, z2, show_steps=False):
    z1 = _to_complex(z1)
    z2 = _to_complex(z2)

    if z2 == 0:
        raise ZeroDivisionError("Cannot divide by zero complex number (0 + 0i).")

    # Conjugate of denominator
    conj = z2.conjugate()
    
    # Numerator multiplication
    num_real = (z1.real * conj.real) - (z1.imag * conj.imag)
    num_imag = (z1.real * conj.imag) + (z1.imag * conj.real)
    
    # Denominator multiplication
    denom_val = (z2.real**2) + (z2.imag**2)
    
    result = z1 / z2

    if not show_steps:
        return result

    return Solution(
        given=f"Numerator = {_fmt(z1)}, Denominator = {_fmt(z2)}",
        to_find="Quotient (z₁ / z₂)",
        equation="z₁/z₂ = (z₁ · z̄₂) / (z₂ · z̄₂)",
        formula_name="Complex Division (Conjugate Method)",
        formula_used="(ac + bd)/(c² + d²) + (bc - ad)/(c² + d²)i",
        formula_reason="Multiplying by the conjugate turns the denominator into a standard real number (c² + d²).",
        explanation="We rationalize the denominator by multiplying top and bottom by the conjugate.",
        steps=[
            f"Step 1: Find the Conjugate of the denominator (z̄₂).",
            f"   Denominator z₂ = {_fmt(z2)}",
            f"   Conjugate z̄₂   = {_fmt(conj)} (Sign of i changes)",
            f"Step 2: Multiply Denominator by Conjugate (z₂ · z̄₂).",
            f"   ({_fmt(z2)}) * ({_fmt(conj)}) = {z2.real}² + {z2.imag}²",
            f"   New Denominator = {denom_val} (Notice i is gone!)",
            f"Step 3: Multiply Numerator by Conjugate (z₁ · z̄₂).",
            f"   ({_fmt(z1)}) * ({_fmt(conj)})",
            f"   = (FOIL expansion) -> {num_real} + {num_imag}i",
            f"Step 4: Divide both parts by the new Real Denominator.",
            f"   Real: {num_real} / {denom_val} = {result.real}",
            f"   Imag: {num_imag} / {denom_val} = {result.imag}",
            f"Step 5: Final Result.",
            f"   {_fmt(result)}"
        ],
        answer=result
    )

# ======================================================
# MODULUS
# ======================================================

def modulus(z, show_steps=False):
    z = _to_complex(z)
    a, b = z.real, z.imag
    result = abs(z)

    if not show_steps:
        return result
    
    return Solution(
        given=f"z = {_fmt(z)}",
        to_find="Modulus |z|",
        equation="|z| = √(a² + b²)",
        formula_name="Modulus Formula",
        formula_used="√(a² + b²)",
        formula_reason="The modulus represents the distance from the origin (0,0) to the point (a,b).",
        explanation="We treat the real part as 'a' and imaginary part as 'b' and apply the Pythagorean theorem.",
        steps=[
            "",
            f"Step 1: Identify components.",
            f"   a (Real) = {a}",
            f"   b (Imag) = {b}",
            f"Step 2: Square both components.",
            f"   a² = {a*a}",
            f"   b² = {b*b} (Note: b² is always positive)",
            f"Step 3: Add them together.",
            f"   {a*a} + {b*b} = {a*a + b*b}",
            f"Step 4: Take the square root.",
            f"   √({a*a + b*b}) = {result}"
        ],
        answer=result
    )

# ======================================================
# CONJUGATE
# ======================================================

def conjugate(z, show_steps=False):
    z = _to_complex(z)
    result = z.conjugate()

    if not show_steps:
        return result

    return Solution(
        given=f"z = {_fmt(z)}",
        to_find="Conjugate z̄",
        equation="z̄ = a - bi",
        formula_name="Complex Conjugate Formula",
        formula_used="a - bi",
        formula_reason="The conjugate is used to flip the imaginary component.",
        explanation="We keep the real number exactly the same, but reverse the sign (positive/negative) of the imaginary number.",
        steps=[
            f"Step 1: Identify the Imaginary part.",
            f"   Imaginary part = {z.imag}i",
            f"Step 2: Flip the sign.",
            f"   {z.imag} becomes {-z.imag}",
            f"Step 3: Construct the conjugate.",
            f"   Real part ({z.real}) remains unchanged.",
            f"   Result: {_fmt(result)}"
        ],
        answer=result
    )

# ======================================================
# ARGUMENT
# ======================================================

def argument(z, degrees=True, show_steps=False):
    z = _to_complex(z)
    
    # Calculate radians first
    rads = math.atan2(z.imag, z.real)
    
    # Convert to degrees if requested
    result = math.degrees(rads) if degrees else rads
    unit = "degrees" if degrees else "radians"

    if not show_steps:
        return result

    return Solution(
        given=f"z = {_fmt(z)}",
        to_find=f"Argument (Phase Angle) in {unit}",
        equation="θ = arctan(b / a)",
        formula_name="Argument Formula",
        formula_used="atan2(b, a)",
        formula_reason="Calculates the angle the vector makes with the positive Real axis.",
        explanation="We use the coordinates (a, b) to determine direction. We use 'atan2' because it correctly handles all four quadrants.",
        steps=[
            f"Step 1: Identify coordinates.",
            f"   x (Real) = {z.real}",
            f"   y (Imag) = {z.imag}",
            f"Step 2: Calculate angle in Radians.",
            f"   atan2({z.imag}, {z.real}) = {rads:.4f} rad",
            f"Step 3: Convert to {unit}.",
            f"   {result:.4f}°"
        ],
        answer=result
    )

# ======================================================
# POLAR FORM
# ======================================================

def polar(z, degrees=True, show_steps=False):
    z = _to_complex(z)
    
    # We reuse our own detailed functions to get r and theta
    r = modulus(z, show_steps=False)
    theta = argument(z, degrees=degrees, show_steps=False)
    
    unit = "°" if degrees else " rad"

    if not show_steps:
        return (r, theta)

    return Solution(
        given=f"z = {_fmt(z)}",
        to_find="Polar Form (r, θ)",
        equation="z = r(cosθ + i·sinθ)",
        formula_name="Polar Conversion Formula",
        formula_used="r=|z|, θ=arg(z)",
        explanation="Rectangular form (x+iy) describes a location grid-style. Polar form describes it by distance (r) and direction (θ).",
        steps=[
            f"Step 1: Calculate Modulus (r) using √(a² + b²).",
            f"   r = {r:.4f}",
            f"Step 2: Calculate Argument (θ) using atan2(b,a).",
            f"   θ = {theta:.4f}{unit}",
            f"Step 3: Assemble.",
            f"   Polar Form: {r:.4f}(cos {theta:.2f}{unit} + i·sin {theta:.2f}{unit})"
        ],
        answer=(r, theta)
    )

# ======================================================
# EULER FORMULA
# ======================================================

def euler(theta, degrees=True, show_steps=False):
    # Logic
    if degrees:
        rad = math.radians(theta)
        angle_str = f"{theta}°"
    else:
        rad = theta
        angle_str = f"{theta} rad"
        
    real_part = math.cos(rad)
    imag_part = math.sin(rad)
    result = complex(real_part, imag_part)

    if not show_steps:
        return result

    return Solution(
        given=f"θ = {angle_str}",
        to_find="Rectangular value of e^(iθ)",
        equation="e^(iθ) = cos(θ) + i·sin(θ)",
        formula_name="Euler's Formula",
        formula_used="cos(θ) + i·sin(θ)",
        formula_reason="Euler's formula describes a point on the unit circle at angle θ.",
        explanation="This connects exponential functions to trigonometry. The result always has a magnitude (r) of 1.",
        steps=[
            f"Step 1: Ensure angle is in radians.",
            f"   Radians = {rad:.4f}",
            f"Step 2: Calculate Real part (Cosine).",
            f"   cos({rad:.4f}) = {real_part:.4f}",
            f"Step 3: Calculate Imaginary part (Sine).",
            f"   sin({rad:.4f}) = {imag_part:.4f}",
            f"Step 4: Combine.",
            f"   {_fmt(result)}"
        ],
        answer=result
    )

# ======================================================
# POLAR → RECTANGULAR
# ======================================================

def from_polar(r, theta, degrees=True, show_steps=False):
    # Logic
    if degrees:
        rad = math.radians(theta)
        angle_input = f"{theta}°"
    else:
        rad = theta
        angle_input = f"{theta} rad"
        
    x = r * math.cos(rad)
    y = r * math.sin(rad)
    result = complex(x, y)

    if not show_steps:
        return result

    return Solution(
        given=f"r = {r}, θ = {angle_input}",
        to_find="Rectangular Form (a + bi)",
        equation="z = r·cos(θ) + i·r·sin(θ)",
        formula_name="Polar to Rectangular Formula",
        formula_used="x = r cosθ, y = r sinθ",
        explanation="We project the radius vector onto the x-axis (Real) and y-axis (Imaginary).",
        steps=[
            f"Step 1: Calculate Real part (x).",
            f"   x = {r} * cos({angle_input})",
            f"   x = {r} * {math.cos(rad):.4f} = {x:.4f}",
            f"Step 2: Calculate Imaginary part (y).",
            f"   y = {r} * sin({angle_input})",
            f"   y = {r} * {math.sin(rad):.4f} = {y:.4f}",
            f"Step 3: Combine.",
            f"   {_fmt(result)}"
        ],
        answer=result
    )

# ======================================================
# ALIASES & EXPORT
# ======================================================

# Fix AttributeError for test suite
phase = argument
to_polar = polar

__all__ = [
    "complex_add", "complex_sub", "complex_mul", "complex_div",
    "modulus", "conjugate", "argument", "phase",
    "polar", "to_polar", "euler", "from_polar"
]
