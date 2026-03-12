# solvepath/vectors.py
"""
=========================================================
              SolvePath Vector Module
=========================================================

Includes HIGHLY DETAILED, TUTOR-STYLE step-by-step solutions for:

• Vector Addition & Subtraction
• Dot Product (Scalar Product)
• Cross Product (2D & 3D)
• Magnitude (Length) & Normalization (Unit Vector)
• Projection & Rejection
• Angle Between Vectors

Returns:
• Solution object when show_steps=True
• Final result when show_steps=False

=========================================================
"""

import math
from typing import Tuple, List, Union
from solvepath.solution import Solution

# =========================================================
# INTERNAL VALIDATION
# =========================================================

def _ensure_same_dimension(a, b):
    if len(a) != len(b):
        raise ValueError(f"Vectors must have the same dimension. Got {len(a)} and {len(b)}.")

def _fmt_vec(v):
    """Formats a vector for nicer printing."""
    return f"({', '.join(map(str, v))})"

# =========================================================
# VECTOR ADDITION
# =========================================================

def vector_add(a: tuple, b: tuple, show_steps=False):
    _ensure_same_dimension(a, b)
    result = tuple(a[i] + b[i] for i in range(len(a)))

    if not show_steps:
        return result

    steps = [
        f"Step 1: Identify Vectors.",
        f"   a = {_fmt_vec(a)}",
        f"   b = {_fmt_vec(b)}",
        "Step 2: Add corresponding components (x+x, y+y, ...)."
    ]

    components = ["x", "y", "z", "w"]
    for i in range(len(a)):
        comp_name = components[i] if i < 4 else f"dim_{i+1}"
        val_a = a[i]
        val_b = b[i]
        res = val_a + val_b
        steps.append(f"   {comp_name}: {val_a} + {val_b} = {res}")

    steps.append(f"Step 3: Assemble Result.\n   {_fmt_vec(result)}")

    return Solution(
        given=f"a={_fmt_vec(a)}, b={_fmt_vec(b)}",
        to_find="Vector Sum a + b",
        equation="c_i = a_i + b_i",
        formula_name="Vector Addition",
        formula_used="(a₁ + b₁, a₂ + b₂, ...)",
        formula_reason="Vectors add 'tip-to-tail'. We add their independent directional components.",
        explanation="We simply add the numbers in the same positions.",
        steps=steps,
        answer=result
    )

# =========================================================
# VECTOR SUBTRACTION
# =========================================================

def vector_sub(a: tuple, b: tuple, show_steps=False):
    _ensure_same_dimension(a, b)
    result = tuple(a[i] - b[i] for i in range(len(a)))

    if not show_steps:
        return result

    steps = [
        f"Step 1: Identify Vectors.",
        f"   a = {_fmt_vec(a)}",
        f"   b = {_fmt_vec(b)}",
        "Step 2: Subtract components of b from a."
    ]

    components = ["x", "y", "z", "w"]
    for i in range(len(a)):
        comp_name = components[i] if i < 4 else f"dim_{i+1}"
        val_a = a[i]
        val_b = b[i]
        res = val_a - val_b
        steps.append(f"   {comp_name}: {val_a} - {val_b} = {res}")

    steps.append(f"Step 3: Assemble Result.\n   {_fmt_vec(result)}")

    return Solution(
        given=f"a={_fmt_vec(a)}, b={_fmt_vec(b)}",
        to_find="Vector Difference a - b",
        equation="c_i = a_i - b_i",
        formula_name="Vector Subtraction",
        formula_used="(a₁ - b₁, a₂ - b₂, ...)",
        formula_reason="Represents the displacement vector from the tip of b to the tip of a.",
        explanation="We subtract the second vector's components from the first.",
        steps=steps,
        answer=result
    )

# =========================================================
# DOT PRODUCT
# =========================================================

def dot(a: tuple, b: tuple, show_steps=False):
    _ensure_same_dimension(a, b)
    
    products = []
    for i in range(len(a)):
        products.append(a[i] * b[i])
        
    result = sum(products)

    if not show_steps:
        return result

    steps = [
        f"Step 1: Identify Vectors.",
        f"   a = {_fmt_vec(a)}",
        f"   b = {_fmt_vec(b)}",
        "Step 2: Multiply corresponding pairs."
    ]

    calc_parts = []
    for i in range(len(a)):
        p = products[i]
        steps.append(f"   {a[i]} × {b[i]} = {p}")
        calc_parts.append(str(p))

    sum_str = " + ".join(calc_parts)
    steps.append(f"Step 3: Sum the products.")
    steps.append(f"   {sum_str} = {result}")

    return Solution(
        given=f"a={_fmt_vec(a)}, b={_fmt_vec(b)}",
        to_find="Dot Product a · b",
        equation="a · b = Σ a_i b_i",
        formula_name="Dot Product (Scalar Product)",
        formula_used="a₁b₁ + a₂b₂ + ... + aₙbₙ",
        formula_reason="Measures how much two vectors point in the same direction.",
        explanation="We multiply matching components and add them all up to get a single number (scalar).",
        steps=steps,
        answer=result
    )

# =========================================================
# CROSS PRODUCT (3D)
# =========================================================

def cross_3d(a: tuple, b: tuple, show_steps=False):
    if len(a) != 3 or len(b) != 3:
        raise ValueError("Cross product is only defined for 3D vectors in this module.")

    ax, ay, az = a
    bx, by, bz = b

    # Components
    cx = ay*bz - az*by
    cy = az*bx - ax*bz
    cz = ax*by - ay*bx
    
    result = (cx, cy, cz)

    if not show_steps:
        return result

    steps = [
        f"Step 1: Identify Components.",
        f"   a = (ax={ax}, ay={ay}, az={az})",
        f"   b = (bx={bx}, by={by}, bz={bz})",
        "Step 2: Calculate i-component (x).",
        f"   (ay·bz) - (az·by)",
        f"   ({ay}·{bz}) - ({az}·{by}) = {ay*bz} - {az*by} = {cx}",
        "Step 3: Calculate j-component (y).",
        f"   (az·bx) - (ax·bz)",
        f"   ({az}·{bx}) - ({ax}·{bz}) = {az*bx} - {ax*bz} = {cy}",
        "Step 4: Calculate k-component (z).",
        f"   (ax·by) - (ay·bx)",
        f"   ({ax}·{by}) - ({ay}·{bx}) = {ax*by} - {ay*bx} = {cz}",
        f"Step 5: Assemble Vector.\n   {result}"
    ]

    return Solution(
        given=f"a={a}, b={b}",
        to_find="Cross Product a × b",
        equation="c = a × b",
        formula_name="Cross Product",
        formula_used="(ay bz - az by, az bx - ax bz, ax by - ay bx)",
        formula_reason="Produces a vector perpendicular (orthogonal) to both input vectors.",
        explanation="We use the determinant method (Sarrus rule) to find the orthogonal components.",
        steps=steps,
        answer=result
    )

# =========================================================
# CROSS PRODUCT (2D – SCALAR)
# =========================================================

def cross_2d(a: tuple, b: tuple, show_steps=False):
    if len(a) != 2 or len(b) != 2:
        raise ValueError("2D Cross Product requires 2D vectors.")

    ax, ay = a
    bx, by = b
    result = ax*by - ay*bx

    if not show_steps:
        return result

    return Solution(
        given=f"a={a}, b={b}",
        to_find="Scalar Cross Product (2D)",
        equation="det(a, b)",
        formula_name="2D Cross Product / Determinant",
        formula_used="ax·by - ay·bx",
        formula_reason="Represents the signed area of the parallelogram formed by the vectors.",
        explanation="In 2D, the cross product returns a single number representing rotation/area.",
        steps=[
            f"Step 1: Identify components.",
            f"   a = ({ax}, {ay}), b = ({bx}, {by})",
            f"Step 2: Apply formula (ad - bc).",
            f"   ({ax} · {by}) - ({ay} · {bx})",
            f"   {ax*by} - {ay*bx} = {result}"
        ],
        answer=result
    )

# =========================================================
# MAGNITUDE
# =========================================================

def magnitude(v: tuple, show_steps=False):
    squares = [x*x for x in v]
    sum_sq = sum(squares)
    result = math.sqrt(sum_sq)

    if not show_steps:
        return result

    sq_str = " + ".join(str(s) for s in squares)

    steps = [
        f"Step 1: Square each component.",
        f"   v = {_fmt_vec(v)}",
        f"   Squares: {squares}",
        f"Step 2: Sum the squares.",
        f"   {sq_str} = {sum_sq}",
        f"Step 3: Take the square root.",
        f"   √{sum_sq} = {result}"
    ]

    return Solution(
        given=f"v = {v}",
        to_find="Magnitude |v|",
        equation="|v| = √(x² + y² + ...)",
        formula_name="Vector Magnitude",
        formula_used="√(Σ v_i²)",
        formula_reason="Based on the Pythagorean theorem extended to N dimensions.",
        explanation="We find the geometric length of the vector.",
        steps=steps,
        answer=result
    )

# =========================================================
# NORMALIZATION
# =========================================================

def normalize(v: tuple, show_steps=False):
    mag = magnitude(v, show_steps=False)

    if mag == 0:
        raise ValueError("Cannot normalize a zero vector.")

    result = tuple(x / mag for x in v)

    if not show_steps:
        return result

    steps = [
        f"Step 1: Calculate Magnitude |v|.",
        f"   |v| = {mag:.4f}",
        f"Step 2: Divide each component by |v|.",
        f"   v̂ = v / {mag:.4f}"
    ]

    for i, x in enumerate(v):
        steps.append(f"   Component {i+1}: {x} / {mag:.4f} = {result[i]:.4f}")

    return Solution(
        given=f"v = {v}",
        to_find="Unit Vector v̂",
        equation="v̂ = v / |v|",
        formula_name="Vector Normalization",
        formula_used="v_i / √(Σ v_i²)",
        formula_reason="To find a vector pointing in the same direction but with length 1.",
        explanation="We scale the vector down by its own length.",
        steps=steps,
        answer=result
    )

# =========================================================
# PROJECTION
# =========================================================

def projection(a: tuple, b: tuple, show_steps=False):
    _ensure_same_dimension(a, b)

    # Re-use our own functions for calculations to keep steps consistent
    # But for display, we do explicit math here.
    
    # Dot products
    dot_ab = sum(x*y for x,y in zip(a,b))
    dot_bb = sum(x*x for x in b)

    if dot_bb == 0:
        raise ValueError("Cannot project onto a zero vector.")

    scale = dot_ab / dot_bb
    result = tuple(scale * x for x in b)

    if not show_steps:
        return result

    steps = [
        f"Step 1: Calculate Dot Product a · b.",
        f"   a · b = {dot_ab}",
        f"Step 2: Calculate Dot Product b · b (Magnitude squared).",
        f"   b · b = {dot_bb}",
        f"Step 3: Calculate Scalar Factor.",
        f"   k = (a·b) / (b·b) = {dot_ab} / {dot_bb} = {scale:.4f}",
        f"Step 4: Scale vector b by k.",
        f"   {scale:.4f} × {b} = {result}"
    ]

    return Solution(
        given=f"a={a}, b={b}",
        to_find="Projection of a onto b",
        equation="proj_b(a) = ( (a·b) / |b|² ) · b",
        formula_name="Vector Projection",
        formula_used="((a·b)/(b·b)) * b",
        formula_reason="Finds the 'shadow' of vector a cast onto vector b.",
        explanation="We scale vector b by the amount of a that points in b's direction.",
        steps=steps,
        answer=result
    )

# =========================================================
# REJECTION
# =========================================================

def rejection(a: tuple, b: tuple, show_steps=False):
    _ensure_same_dimension(a, b)
    
    proj = projection(a, b, show_steps=False)
    result = tuple(a[i] - proj[i] for i in range(len(a)))

    if not show_steps:
        return result

    steps = [
        f"Step 1: Calculate Projection of a onto b (p).",
        f"   p = {proj}",
        f"Step 2: Subtract Projection from original vector a.",
        f"   Rej = a - p",
        f"   {a} - {proj} = {result}"
    ]

    return Solution(
        given=f"a={a}, b={b}",
        to_find="Vector Rejection",
        equation="Rej = a - proj_b(a)",
        formula_name="Vector Rejection",
        formula_used="a - ((a·b)/(b·b))b",
        formula_reason="Finds the component of a that is perpendicular (orthogonal) to b.",
        explanation="The original vector equals Projection + Rejection. We rearrange this to find Rejection.",
        steps=steps,
        answer=result
    )

# =========================================================
# ANGLE BETWEEN VECTORS
# =========================================================

def angle_between(a: tuple, b: tuple, degrees=False, show_steps=False):
    _ensure_same_dimension(a, b)

    dot_ab = sum(x*y for x,y in zip(a,b))
    mag_a = math.sqrt(sum(x*x for x in a))
    mag_b = math.sqrt(sum(x*x for x in b))

    if mag_a == 0 or mag_b == 0:
        raise ValueError("Angle undefined for zero vectors.")

    cos_val = dot_ab / (mag_a * mag_b)
    # Clamp for floating point errors
    cos_val = max(-1.0, min(1.0, cos_val))
    
    theta_rad = math.acos(cos_val)
    result = math.degrees(theta_rad) if degrees else theta_rad
    unit = "degrees" if degrees else "radians"

    if not show_steps:
        return result

    steps = [
        f"Step 1: Calculate Dot Product a · b.",
        f"   {dot_ab}",
        f"Step 2: Calculate Magnitudes.",
        f"   |a| = {mag_a:.4f}",
        f"   |b| = {mag_b:.4f}",
        f"Step 3: Calculate Cosine of angle.",
        f"   cos(θ) = (a·b) / (|a||b|)",
        f"   cos(θ) = {dot_ab} / ({mag_a:.4f} × {mag_b:.4f})",
        f"   cos(θ) = {cos_val:.4f}",
        f"Step 4: Take Inverse Cosine (arccos).",
        f"   θ = arccos({cos_val:.4f}) = {result:.4f} {unit}"
    ]

    return Solution(
        given=f"a={a}, b={b}",
        to_find=f"Angle θ ({unit})",
        equation="cos(θ) = (a · b) / (|a| |b|)",
        formula_name="Angle Between Vectors",
        formula_used="arccos( (a·b) / (|a||b|) )",
        formula_reason="Derived from the definition of the Dot Product: a·b = |a||b|cos(θ).",
        explanation="We isolate cos(θ) and solve for θ.",
        steps=steps,
        answer=result
    )

# =========================================================
# EXPORT
# =========================================================

__all__ = [
    "vector_add", "vector_sub", "dot",
    "cross_2d", "cross_3d",
    "magnitude", "normalize",
    "projection", "rejection",
    "angle_between"
]
