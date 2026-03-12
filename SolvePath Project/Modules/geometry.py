# solvepath/geometry.py
"""
==========================================================
              SolvePath Geometry Module
==========================================================

Covers step-by-step geometry calculations for:

• Triangles
• Circles
• Polygons
• 3D Solids

Behavior:
• show_steps = False → returns final numeric result
• show_steps = True  → returns Solution object with full explanation

Teaching level:
• Beginner friendly
• No skipped reasoning
• Clear mathematical logic
==========================================================
"""

import math
from typing import Union
from solvepath.solution import Solution

Number = Union[int, float]
PI = 3.14  # Fixed School Standard Value

# ========================================================
#                 INTERNAL VALIDATION
# ========================================================

def _ensure_positive(x: Number, name="value"):
    if not isinstance(x, (int, float)):
        raise TypeError(f"SolvePath Error: {name} must be a number.")
    if x <= 0:
        raise ValueError(f"SolvePath Error: {name} must be greater than zero.")
    return x

# ========================================================
#                       TRIANGLES
# ========================================================

def triangle_area(base: Number, height: Number, show_steps=False):
    _ensure_positive(base, "base")
    _ensure_positive(height, "height")

    result = 0.5 * base * height

    if not show_steps: return result

    return Solution(
        problem_understanding="Calculate the area occupied by a triangle.",
        given=f"Base = {base}, Height = {height}",
        to_find="Area (A)",
        equation="0.5 * b * h",
        formula_name="Triangle Area Formula",
        formula_used="A = 0.5 × b × h",
        formula_reason="A triangle is exactly half of a rectangle with the same base and height.",
        symbol_explanation="0.5 is the decimal form of 1/2.",
        explanation="Area represents the 2D space inside the three sides.",
        steps=[
            f"Step 1: Identify the given measurements.",
            f"   >> Base (b) = {base}",
            f"   >> Height (h) = {height}",
            "Step 2: Recall the formula: Area = 0.5 × Base × Height.",
            "Step 3: Substitute the values into the formula.",
            f"   >> A = 0.5 × {base} × {height}",
            "Step 4: Multiply the Base by the Height first.",
            f"   >> {base} * {height}",
            f"   >> Product = {base * height}",
            "Step 5: Now, multiply that product by 0.5 (or divide by 2).",
            f"   >> 0.5 * {base * height}",
            f"Step 6: Calculate the final value.",
            f"   >> {result}",
            "Step 7: Assign square units.",
            f"   >> {result} square units.",
            "Step 8: Final Answer."
        ],
        answer=f"{result} sq units"
    )

def triangle_perimeter(a: Number, b: Number, c: Number, show_steps=False):
    _ensure_positive(a, "side a")
    _ensure_positive(b, "side b")
    _ensure_positive(c, "side c")

    result = a + b + c

    if not show_steps: return result

    return Solution(
        problem_understanding="Find the total distance around the triangle.",
        given=f"Sides = {a}, {b}, {c}",
        to_find="Perimeter (P)",
        equation="a + b + c",
        formula_name="Triangle Perimeter Formula",
        formula_used="P = a + b + c",
        formula_reason="Perimeter is the sum of all boundary lengths.",
        symbol_explanation="+ means addition.",
        explanation="We simply add the length of all three sides.",
        steps=[
            "Step 1: Identify the three sides.",
            f"   >> Side 1: {a}, Side 2: {b}, Side 3: {c}",
            "Step 2: Set up the summation equation.",
            f"   >> P = {a} + {b} + {c}",
            "Step 3: Add the first two sides together.",
            f"   >> {a} + {b} = {a+b}",
            "Step 4: Add the third side to that intermediate sum.",
            f"   >> {a+b} + {c}",
            "Step 5: Calculate the final Total.",
            f"   >> {result}",
            "Step 6: Assign linear units.",
            f"   >> {result} units.",
            "Step 7: Final Answer."
        ],
        answer=f"{result} units"
    )

def equilateral_triangle_area(a: Number, show_steps=False):
    _ensure_positive(a, "side")

    # Using 1.732 for sqrt(3) standard approximation
    sqrt3_approx = 1.732
    result = (sqrt3_approx / 4) * a * a

    if not show_steps: return result

    return Solution(
        problem_understanding="Calculate area of a triangle where all sides are equal.",
        given=f"Side length a = {a}",
        to_find="Area",
        equation="(√3 / 4) × a²",
        formula_name="Equilateral Triangle Area",
        formula_used="A = (1.732 / 4) × a²",
        formula_reason="Derived from Pythagoras theorem given equal sides.",
        symbol_explanation="We use √3 ≈ 1.732",
        explanation="Optimized formula for equilateral triangles.",
        steps=[
            f"Step 1: Identify side length a = {a}.",
            "Step 2: Calculate a squared (a²).",
            f"   >> {a} × {a} = {a*a}",
            "Step 3: Use the standard approximation for √3.",
            f"   >> √3 ≈ {sqrt3_approx}",
            "Step 4: Multiply a² by 1.732.",
            f"   >> {a*a} * {sqrt3_approx} = {a*a * sqrt3_approx}",
            "Step 5: Divide the result by 4.",
            f"   >> {a*a * sqrt3_approx} ÷ 4",
            f"Step 6: Calculate final result.",
            f"   >> {result}",
            "Step 7: Assign square units.",
            f"   >> {result} sq units.",
            "Step 8: Final Answer."
        ],
        answer=f"{result} sq units"
    )

def herons_formula(a: Number, b: Number, c: Number, show_steps=False):
    _ensure_positive(a, "side a")
    _ensure_positive(b, "side b")
    _ensure_positive(c, "side c")

    # Semi-perimeter
    s = (a + b + c) / 2
    try:
        val = s * (s - a) * (s - b) * (s - c)
        if val < 0: raise ValueError("Impossible Triangle")
        result = math.sqrt(val)
    except ValueError:
        raise ValueError("SolvePath Error: Inputs do not form a valid triangle.")

    if not show_steps: return result

    return Solution(
        problem_understanding="Calculate area using only side lengths (no height given).",
        given=f"Sides: {a}, {b}, {c}",
        to_find="Area",
        equation="√[s(s-a)(s-b)(s-c)]",
        formula_name="Heron's Formula",
        formula_used="A = √s(s-a)(s-b)(s-c)",
        formula_reason="Standard method for SSS (Side-Side-Side) area.",
        symbol_explanation="s = Semi-perimeter (Half the perimeter)",
        explanation="We first find half the perimeter, then apply the root formula.",
        steps=[
            f"Step 1: Identify sides a={a}, b={b}, c={c}.",
            "Step 2: Calculate Perimeter (P) and Semi-perimeter (s).",
            f"   >> P = {a} + {b} + {c} = {a+b+c}",
            f"   >> s = {a+b+c} / 2 = {s}",
            "Step 3: Calculate difference terms (s - side).",
            f"   >> (s - a) = {s} - {a} = {s-a}",
            f"   >> (s - b) = {s} - {b} = {s-b}",
            f"   >> (s - c) = {s} - {c} = {s-c}",
            "Step 4: Multiply s by all three differences.",
            f"   >> {s} * {s-a} * {s-b} * {s-c}",
            f"   >> Product = {val}",
            "Step 5: Apply the Square Root to the product.",
            f"   >> √{val}",
            "Step 6: Calculate the final root value.",
            f"   >> {result:.2f}",
            "Step 7: Final Answer."
        ],
        answer=f"{result:.2f} sq units"
    )

# ========================================================
#                         CIRCLES
# ========================================================

def circle_area(r: Number, show_steps=False):
    _ensure_positive(r, "radius")
    # Using 3.14 explicitly
    result = PI * r * r

    if not show_steps: return result

    return Solution(
        problem_understanding="Calculate the space occupied by a circle.",
        given=f"Radius r = {r}", to_find="Area", equation="3.14 * r²",
        formula_name="Circle Area Formula", formula_used="A = π × r²",
        formula_reason="Area grows with the square of the radius.",
        symbol_explanation=f"π ≈ {PI} (School Standard)",
        explanation="We multiply 3.14 by the radius squared.",
        steps=[
            f"Step 1: Identify Radius r = {r}.",
            "Step 2: Recall the formula Area = πr².",
            "Step 3: Calculate r squared (r²).",
            f"   >> {r} × {r} = {r*r}",
            f"Step 4: Use the standard value π = {PI}.",
            "Step 5: Substitute values into the formula.",
            f"   >> A = {PI} × {r*r}",
            "Step 6: Perform the multiplication.",
            f"   >> {PI * r * r}",
            "Step 7: Assign square units.",
            f"   >> {result} sq units.",
            "Step 8: Final Answer."
        ],
        answer=f"{result} sq units"
    )

def circle_circumference(r: Number, show_steps=False):
    _ensure_positive(r, "radius")
    result = 2 * PI * r

    if not show_steps: return result

    return Solution(
        problem_understanding="Calculate the distance around the edge of a circle.",
        given=f"Radius r = {r}", to_find="Circumference (C)", equation="2 * 3.14 * r",
        formula_name="Circumference Formula", formula_used="C = 2 × π × r",
        formula_reason="Linear distance around the circle.",
        symbol_explanation=f"π ≈ {PI}",
        explanation="Double the radius to get diameter, then multiply by 3.14.",
        steps=[
            f"Step 1: Identify Radius r = {r}.",
            "Step 2: Use the formula C = 2πr.",
            "Step 3: Calculate Diameter (2r).",
            f"   >> 2 × {r} = {2*r}",
            f"Step 4: Use the standard value π = {PI}.",
            "Step 5: Multiply Diameter by π.",
            f"   >> {2*r} × {PI}",
            "Step 6: Perform the multiplication.",
            f"   >> {result}",
            "Step 7: Assign linear units.",
            f"   >> {result} units.",
            "Step 8: Final Answer."
        ],
        answer=f"{result} units"
    )

# ========================================================
#                     SECTORS & ARCS
# ========================================================

def sector_area(r: Number, theta: Number, show_steps=False):
    _ensure_positive(r, "radius")
    _ensure_positive(theta, "angle")
    
    result = (theta / 360) * PI * r * r

    if not show_steps: return result

    return Solution(
        problem_understanding="Calculate area of a slice of the circle.",
        given=f"r={r}, θ={theta}°", to_find="Sector Area", equation="(θ/360) * 3.14 * r²",
        formula_name="Sector Area Formula", formula_used="A = (θ/360) × πr²",
        formula_reason="Sector is a fraction of the full circle area.",
        symbol_explanation=f"π ≈ {PI}",
        explanation="Find full area, then take the specific fraction.",
        steps=[
            f"Step 1: Identify radius {r} and angle {theta}°.",
            "Step 2: Calculate the fraction of the circle.",
            f"   >> Fraction = {theta} / 360 = {theta/360:.4f}",
            "Step 3: Calculate r squared (r²).",
            f"   >> {r} × {r} = {r*r}",
            "Step 4: Calculate Full Circle Area (πr²).",
            f"   >> {PI} × {r*r} = {PI * r * r}",
            "Step 5: Multiply the Full Area by the Fraction.",
            f"   >> {theta/360:.4f} × {PI * r * r}",
            "Step 6: Perform the final multiplication.",
            f"   >> {result:.2f}",
            "Step 7: Final Answer."
        ],
        answer=f"{result:.2f} sq units"
    )

def arc_length(r: Number, theta: Number, show_steps=False):
    _ensure_positive(r, "radius")
    _ensure_positive(theta, "angle")
    
    result = (theta / 360) * 2 * PI * r

    if not show_steps: return result

    return Solution(
        problem_understanding="Calculate length of the curved edge of a sector.",
        given=f"r={r}, θ={theta}°", to_find="Arc Length", equation="(θ/360) * 2 * 3.14 * r",
        formula_name="Arc Length Formula", formula_used="L = (θ/360) × 2πr",
        formula_reason="Arc is a fraction of the circumference.",
        symbol_explanation=f"π ≈ {PI}",
        explanation="Find full circumference, then take the specific fraction.",
        steps=[
            f"Step 1: Identify radius {r} and angle {theta}°.",
            "Step 2: Calculate the fraction of the circle.",
            f"   >> Fraction = {theta} / 360 = {theta/360:.4f}",
            "Step 3: Calculate Diameter (2r).",
            f"   >> 2 × {r} = {2*r}",
            "Step 4: Calculate Full Circumference (π × Diameter).",
            f"   >> {PI} × {2*r} = {PI * 2 * r}",
            "Step 5: Multiply Circumference by Fraction.",
            f"   >> {theta/360:.4f} × {PI * 2 * r}",
            "Step 6: Perform calculation.",
            f"   >> {result:.2f}",
            "Step 7: Final Answer."
        ],
        answer=f"{result:.2f} units"
    )

# ========================================================
#                         POLYGONS
# ========================================================

def interior_angle_sum(n: int, show_steps=False):
    if n < 3: raise ValueError("Polygon must have at least 3 sides.")
    result = (n - 2) * 180

    if not show_steps: return result

    return Solution(
        problem_understanding="Find total sum of angles inside the polygon.",
        given=f"n = {n} sides", to_find="Sum of Angles", equation="(n-2) * 180",
        formula_name="Interior Angle Sum", formula_used="Sum = (n-2) × 180°",
        formula_reason="Polygon can be split into (n-2) triangles.",
        symbol_explanation="Each triangle = 180°.",
        explanation="We count triangles and multiply by 180.",
        steps=[
            f"Step 1: Identify number of sides n = {n}.",
            "Step 2: Determine number of triangles formed (n - 2).",
            f"   >> {n} - 2 = {n-2} triangles",
            "Step 3: Recall sum of angles in one triangle is 180°.",
            "Step 4: Multiply number of triangles by 180°.",
            f"   >> {n-2} × 180",
            "Step 5: Perform multiplication.",
            f"   >> {result}",
            "Step 6: Assign units (degrees).",
            f"   >> {result}°.",
            "Step 7: Final Answer."
        ],
        answer=f"{result} degrees"
    )

def exterior_angle(n: int, show_steps=False):
    if n < 3: raise ValueError("Polygon must have at least 3 sides.")
    result = 360 / n

    if not show_steps: return result

    return Solution(
        problem_understanding="Find the angle at each corner on the outside of a regular polygon.",
        given=f"n = {n}", to_find="Exterior Angle", equation="360 / n",
        formula_name="Exterior Angle Formula", formula_used="Angle = 360° / n",
        formula_reason="Sum of exterior angles is always 360°.",
        symbol_explanation="360 is full turn.",
        explanation="Divide total turn (360) by number of turns (n).",
        steps=[
            f"Step 1: Identify n = {n}.",
            "Step 2: Recall total exterior sum is 360°.",
            "Step 3: Set up division.",
            f"   >> 360 ÷ {n}",
            "Step 4: Perform division.",
            f"   >> {result}",
            "Step 5: Assign units.",
            f"   >> {result}°.",
            "Step 6: Final Answer."
        ],
        answer=f"{result} degrees"
    )

def polygon_diagonals(n: int, show_steps=False):
    if n < 3: raise ValueError("Polygon must have at least 3 sides.")
    result = n * (n - 3) / 2

    if not show_steps: return result

    return Solution(
        problem_understanding="Count lines connecting non-adjacent vertices.",
        given=f"n = {n}", to_find="Diagonals", equation="n(n-3)/2",
        formula_name="Diagonals Formula", formula_used="D = n(n-3) / 2",
        formula_reason="Each vertex connects to n-3 others, double counted.",
        symbol_explanation="n-3 excludes self and neighbors.",
        explanation="Connect vertices, remove edges, divide by 2.",
        steps=[
            f"Step 1: Identify n = {n}.",
            "Step 2: Calculate connections per vertex (n-3).",
            f"   >> {n} - 3 = {n-3}",
            "Step 3: Multiply by number of vertices (n).",
            f"   >> {n} × {n-3} = {n*(n-3)}",
            "Step 4: Divide by 2 (remove double counts).",
            f"   >> {n*(n-3)} ÷ 2",
            "Step 5: Calculate final integer result.",
            f"   >> {int(result)}",
            "Step 6: Final Answer."
        ],
        answer=f"{int(result)} diagonals"
    )

def regular_polygon_area(n: int, side: Number, apothem: Number, show_steps=False):
    _ensure_positive(side, "side")
    _ensure_positive(apothem, "apothem")
    
    perimeter = n * side
    result = 0.5 * perimeter * apothem

    if not show_steps: return result

    return Solution(
        problem_understanding="Calculate area of regular polygon using apothem.",
        given=f"n={n}, side={side}, a={apothem}", to_find="Area",
        equation="0.5 * P * a", formula_name="Regular Polygon Area",
        formula_used="A = 0.5 × Perimeter × Apothem",
        formula_reason="Sum of areas of n triangles.",
        symbol_explanation="Apothem is height of internal triangles.",
        explanation="Find perimeter, then treat as large triangle with height=apothem.",
        steps=[
            f"Step 1: Identify inputs: n={n}, side={side}, apothem={apothem}.",
            "Step 2: Calculate Perimeter (P = n × side).",
            f"   >> {n} × {side} = {perimeter}",
            "Step 3: Recall formula Area = 0.5 × Perimeter × Apothem.",
            "Step 4: Substitute P and a.",
            f"   >> 0.5 × {perimeter} × {apothem}",
            "Step 5: Multiply Perimeter by Apothem.",
            f"   >> {perimeter} × {apothem} = {perimeter*apothem}",
            "Step 6: Multiply by 0.5 (Divide by 2).",
            f"   >> {perimeter*apothem} ÷ 2",
            f"Step 7: Calculate final value.",
            f"   >> {result}",
            "Step 8: Final Answer."
        ],
        answer=f"{result} sq units"
    )

# ========================================================
#                        3D GEOMETRY
# ========================================================

def cube_volume(a: Number, show_steps=False):
    _ensure_positive(a, "edge")
    result = a ** 3

    if not show_steps: return result

    return Solution(
        problem_understanding="Find space occupied by a cube.",
        given=f"Edge a = {a}", to_find="Volume", equation="a³",
        formula_name="Cube Volume", formula_used="V = a³",
        formula_reason="L x W x H where L=W=H=a.",
        symbol_explanation="None.", explanation="Multiply edge by itself three times.",
        steps=[
            f"Step 1: Identify edge length {a}.",
            "Step 2: Recall Formula V = a × a × a.",
            "Step 3: Calculate a squared.",
            f"   >> {a} × {a} = {a*a}",
            "Step 4: Multiply by a again.",
            f"   >> {a*a} × {a}",
            "Step 5: Perform final multiplication.",
            f"   >> {result}",
            "Step 6: Assign cubic units.",
            f"   >> {result} cubic units.",
            "Step 7: Final Answer."
        ],
        answer=f"{result} cubic units"
    )

def cube_surface_area(a: Number, show_steps=False):
    _ensure_positive(a, "edge")
    result = 6 * a * a

    if not show_steps: return result

    return Solution(
        problem_understanding="Find total area of all 6 faces.",
        given=f"Edge a = {a}", to_find="Surface Area", equation="6a²",
        formula_name="Cube Surface Area", formula_used="SA = 6 × a²",
        formula_reason="6 faces, each is a square of area a².",
        symbol_explanation="None.", explanation="Calculate one face, multiply by 6.",
        steps=[
            f"Step 1: Identify edge length {a}.",
            "Step 2: Calculate area of ONE face (a²).",
            f"   >> {a} × {a} = {a*a}",
            "Step 3: Recall a cube has 6 identical faces.",
            "Step 4: Multiply face area by 6.",
            f"   >> 6 × {a*a}",
            "Step 5: Perform multiplication.",
            f"   >> {result}",
            "Step 6: Assign square units.",
            f"   >> {result} sq units.",
            "Step 7: Final Answer."
        ],
        answer=f"{result} sq units"
    )

def sphere_volume(r: Number, show_steps=False):
    _ensure_positive(r, "radius")
    
    # Use 1.3333 for 4/3 to show standard decimal math
    fraction_approx = 1.3333
    result = fraction_approx * PI * r**3

    if not show_steps: return result

    return Solution(
        problem_understanding="Find space inside a sphere.",
        given=f"r={r}", to_find="Volume", equation="(4/3) * 3.14 * r³",
        formula_name="Sphere Volume", formula_used="V = 1.3333 × 3.14 × r³",
        formula_reason="Standard geometric formula.",
        symbol_explanation=f"π ≈ {PI}, 4/3 ≈ {fraction_approx}", 
        explanation="Apply formula step-by-step using standard decimals.",
        steps=[
            f"Step 1: Identify radius {r}.",
            "Step 2: Calculate r cubed (r³).",
            f"   >> {r} × {r} × {r} = {r**3}",
            "Step 3: Use the decimal approximation for 4/3.",
            f"   >> 4 ÷ 3 ≈ {fraction_approx}",
            "Step 4: Use the standard value π = 3.14.",
            "Step 5: Set up multiplication: 1.3333 × 3.14 × r³.",
            f"   >> {fraction_approx} × {PI} × {r**3}",
            "Step 6: Multiply π by r³ first.",
            f"   >> {PI} × {r**3} = {PI * r**3}",
            "Step 7: Multiply by 1.3333.",
            f"   >> {fraction_approx} × {PI * r**3}",
            "Step 8: Calculate final result.",
            f"   >> {result:.2f}",
            "Step 9: Final Answer."
        ],
        answer=f"{result:.2f} cubic units"
    )

def sphere_surface_area(r: Number, show_steps=False):
    _ensure_positive(r, "radius")
    result = 4 * PI * r * r

    if not show_steps: return result

    return Solution(
        problem_understanding="Find area of sphere's skin.",
        given=f"r={r}", to_find="Surface Area", equation="4 * 3.14 * r²",
        formula_name="Sphere Surface Area", formula_used="SA = 4 × 3.14 × r²",
        formula_reason="Equal to 4 large circles.",
        symbol_explanation=f"π ≈ {PI}", explanation="4 times area of central cross-section.",
        steps=[
            f"Step 1: Identify radius {r}.",
            "Step 2: Calculate r squared (r²).",
            f"   >> {r} × {r} = {r*r}",
            "Step 3: Use π = 3.14.",
            "Step 4: Multiply π by r².",
            f"   >> {PI} × {r*r} = {PI * r * r}",
            "Step 5: Multiply that result by 4.",
            f"   >> 4 × {PI * r * r}",
            "Step 6: Calculate final value.",
            f"   >> {result}",
            "Step 7: Assign square units.",
            f"   >> {result} sq units.",
            "Step 8: Final Answer."
        ],
        answer=f"{result} sq units"
    )

def hemisphere_volume(r: Number, show_steps=False):
    _ensure_positive(r, "radius")
    # 2/3 approx
    fraction_approx = 0.6667
    result = fraction_approx * PI * r**3

    if not show_steps: return result

    return Solution(
        problem_understanding="Find space inside half a sphere.",
        given=f"r={r}", to_find="Volume", equation="(2/3) * 3.14 * r³",
        formula_name="Hemisphere Volume", formula_used="V = 0.6667 × 3.14 × r³",
        formula_reason="Half of sphere volume (4/3 becomes 2/3).",
        symbol_explanation=f"π ≈ {PI}", explanation="Calculate sphere volume then halve it.",
        steps=[
            f"Step 1: Identify radius {r}.",
            "Step 2: Calculate r cubed (r³).",
            f"   >> {r} × {r} × {r} = {r**3}",
            "Step 3: Use decimal approximation for 2/3.",
            f"   >> 2 ÷ 3 ≈ {fraction_approx}",
            "Step 4: Set up multiplication: 0.6667 × 3.14 × r³.",
            f"   >> {fraction_approx} × {PI} × {r**3}",
            "Step 5: Multiply π by r³.",
            f"   >> {PI} × {r**3} = {PI * r**3}",
            "Step 6: Multiply by 0.6667.",
            f"   >> {fraction_approx} × {PI * r**3}",
            "Step 7: Calculate final result.",
            f"   >> {result:.2f}",
            "Step 8: Final Answer."
        ],
        answer=f"{result:.2f} cubic units"
    )

def hemisphere_surface_area(r: Number, show_steps=False):
    _ensure_positive(r, "radius")
    result = 3 * PI * r * r

    if not show_steps: return result

    return Solution(
        problem_understanding="Find total surface area of solid hemisphere.",
        given=f"r={r}", to_find="Total SA", equation="3 * 3.14 * r²",
        formula_name="Hemisphere Total Surface Area", formula_used="SA = 3 × π × r²",
        formula_reason="2πr² (curved) + πr² (flat base).",
        symbol_explanation=f"π ≈ {PI}", explanation="Add curved area and base area.",
        steps=[
            f"Step 1: Identify radius {r}.",
            "Step 2: Calculate r squared (r²).",
            f"   >> {r} × {r} = {r*r}",
            "Step 3: Use π = 3.14.",
            "Step 4: Multiply π by r².",
            f"   >> {PI} × {r*r} = {PI * r * r}",
            "Step 5: Multiply by 3 (2 for dome + 1 for base).",
            f"   >> 3 × {PI * r * r}",
            "Step 6: Calculate final value.",
            f"   >> {result}",
            "Step 7: Assign square units.",
            "Step 8: Final Answer."
        ],
        answer=f"{result} sq units"
    )

def cylinder_volume(r: Number, h: Number, show_steps=False):
    _ensure_positive(r, "radius")
    _ensure_positive(h, "height")
    result = PI * r * r * h

    if not show_steps: return result

    return Solution(
        problem_understanding="Find space inside cylinder.",
        given=f"r={r}, h={h}", to_find="Volume", equation="3.14 * r² * h",
        formula_name="Cylinder Volume", formula_used="V = 3.14 × r² × h",
        formula_reason="Base Area x Height.",
        symbol_explanation=f"π ≈ {PI}", explanation="Stacking circles of area πr².",
        steps=[
            f"Step 1: Identify radius {r} and height {h}.",
            "Step 2: Calculate Base Area (πr²).",
            f"   >> r² = {r} × {r} = {r*r}",
            f"   >> Area = {PI} × {r*r} = {PI*r*r}",
            "Step 3: Multiply Base Area by Height.",
            f"   >> {PI*r*r} × {h}",
            "Step 4: Calculate Result.",
            f"   >> {result}",
            "Step 5: Assign cubic units.",
            f"   >> {result} cubic units.",
            "Step 6: Final Answer."
        ],
        answer=f"{result} cubic units"
    )

def cylinder_surface_area(r: Number, h: Number, show_steps=False):
    _ensure_positive(r, "radius")
    _ensure_positive(h, "height")
    result = 2 * PI * r * (r + h)

    if not show_steps: return result

    return Solution(
        problem_understanding="Find total outer area of cylinder.",
        given=f"r={r}, h={h}", to_find="Surface Area", equation="2 * 3.14 * r(r+h)",
        formula_name="Cylinder Surface Area", formula_used="SA = 2 × 3.14 × r(r + h)",
        formula_reason="Two circles (2πr²) + Rectangle wrapper (2πrh).",
        symbol_explanation=f"π ≈ {PI}", explanation="Unroll the side to get a rectangle.",
        steps=[
            f"Step 1: Identify r={r}, h={h}.",
            "Step 2: Calculate Circumference (2πr).",
            f"   >> 2 × {PI} × {r} = {2*PI*r}",
            "Step 3: Calculate sum of radius and height (r + h).",
            f"   >> {r} + {h} = {r+h}",
            "Step 4: Multiply Circumference by (r+h).",
            f"   >> {2*PI*r} × {r+h}",
            "Step 5: Calculate Result.",
            f"   >> {result}",
            "Step 6: Assign square units.",
            f"   >> {result} sq units.",
            "Step 7: Final Answer."
        ],
        answer=f"{result} sq units"
    )

def cone_volume(r: Number, h: Number, show_steps=False):
    _ensure_positive(r, "radius")
    _ensure_positive(h, "height")
    
    fraction_approx = 0.3333
    result = fraction_approx * PI * r * r * h

    if not show_steps: return result

    return Solution(
        problem_understanding="Find space inside cone.",
        given=f"r={r}, h={h}", to_find="Volume", equation="0.3333 * 3.14 * r² * h",
        formula_name="Cone Volume", formula_used="V = 0.3333 × πr²h",
        formula_reason="Exactly 1/3 of a cylinder with same dim.",
        symbol_explanation=f"π ≈ {PI}, 1/3 ≈ {fraction_approx}", 
        explanation="Calculate cylinder volume, multiply by 0.3333.",
        steps=[
            f"Step 1: Identify r={r}, h={h}.",
            "Step 2: Calculate Cylinder Volume first (πr²h).",
            f"   >> r² = {r*r}",
            f"   >> {PI} × {r*r} × {h} = {PI*r*r*h}",
            "Step 3: Multiply by 0.3333 (1/3).",
            f"   >> {PI*r*r*h} × {fraction_approx}",
            "Step 4: Calculate Result.",
            f"   >> {result:.2f}",
            "Step 5: Assign cubic units.",
            f"   >> {result:.2f} cubic units.",
            "Step 6: Final Answer."
        ],
        answer=f"{result:.2f} cubic units"
    )

def cone_surface_area(r: Number, s: Number, show_steps=False):
    _ensure_positive(r, "radius")
    _ensure_positive(s, "slant")
    result = PI * r * (r + s)

    if not show_steps: return result

    return Solution(
        problem_understanding="Find total area of cone.",
        given=f"r={r}, slant={s}", to_find="Surface Area", equation="3.14 * r(r+s)",
        formula_name="Cone Surface Area", formula_used="SA = 3.14 × r(r + s)",
        formula_reason="Base circle + curved sector.",
        symbol_explanation=f"π ≈ {PI}", explanation="Add circular base and lateral area.",
        steps=[
            f"Step 1: Identify r={r}, s={s}.",
            "Step 2: Calculate base term (πr).",
            f"   >> {PI} × {r} = {PI*r}",
            "Step 3: Calculate sum (r + s).",
            f"   >> {r} + {s} = {r+s}",
            "Step 4: Multiply terms.",
            f"   >> {PI*r} × {r+s}",
            "Step 5: Calculate Result.",
            f"   >> {result}",
            "Step 6: Assign square units.",
            f"   >> {result} sq units.",
            "Step 7: Final Answer."
        ],
        answer=f"{result} sq units"
    )

def prism_volume(l: Number, w: Number, h: Number, show_steps=False):
    _ensure_positive(l, "length")
    _ensure_positive(w, "width")
    _ensure_positive(h, "height")
    result = l * w * h

    if not show_steps: return result

    return Solution(
        problem_understanding="Find volume of rectangular prism.",
        given=f"l={l}, w={w}, h={h}", to_find="Volume", equation="lwh",
        formula_name="Prism Volume", formula_used="V = l × w × h",
        formula_reason="Area of base × height.",
        symbol_explanation="None.", explanation="Multiply dimensions.",
        steps=[
            f"Step 1: Identify length {l}, width {w}, height {h}.",
            "Step 2: Calculate Base Area.",
            f"   >> {l} × {w} = {l*w}",
            "Step 3: Multiply by height.",
            f"   >> {l*w} × {h}",
            "Step 4: Calculate Result.",
            f"   >> {result}",
            "Step 5: Assign cubic units.",
            f"   >> {result} cubic units.",
            "Step 6: Final Answer."
        ],
        answer=f"{result} cubic units"
    )

def pyramid_volume(area_base: Number, h: Number, show_steps=False):
    _ensure_positive(area_base, "base area")
    _ensure_positive(h, "height")
    
    fraction_approx = 0.3333
    result = fraction_approx * area_base * h

    if not show_steps: return result

    return Solution(
        problem_understanding="Find volume of pyramid.",
        given=f"Base Area={area_base}, h={h}", to_find="Volume", equation="0.3333 * B * h",
        formula_name="Pyramid Volume", formula_used="V = 0.3333 × BaseArea × h",
        formula_reason="1/3 of prism with same base/height.",
        symbol_explanation="1/3 ≈ 0.3333", explanation="Multiply base area by height, multiply by 0.3333.",
        steps=[
            f"Step 1: Identify Base Area={area_base}, Height={h}.",
            "Step 2: Multiply Base Area by Height.",
            f"   >> {area_base} × {h} = {area_base*h}",
            "Step 3: Multiply by 0.3333 (1/3).",
            f"   >> {area_base*h} × {fraction_approx}",
            "Step 4: Calculate Result.",
            f"   >> {result:.2f}",
            "Step 5: Assign cubic units.",
            f"   >> {result:.2f} cubic units.",
            "Step 6: Final Answer."
        ],
        answer=f"{result:.2f} cubic units"
    )

# ========================================================
#                       ALIASES
# ========================================================

area_circle = circle_area  # Alias for test compatibility

# ========================================================
#                        EXPORT
# ========================================================

__all__ = [
    # ---------- TRIANGLES ----------
    "triangle_area",
    "triangle_perimeter",
    "equilateral_triangle_area",
    "herons_formula",

    # ---------- CIRCLES ----------
    "circle_area",
    "area_circle", # Exported alias
    "circle_circumference",
    "sector_area",
    "arc_length",

    # ---------- POLYGONS ----------
    "interior_angle_sum",
    "exterior_angle",
    "polygon_diagonals",
    "regular_polygon_area",

    # ---------- 3D GEOMETRY ----------
    "cube_volume",
    "cube_surface_area",
    "sphere_volume",
    "sphere_surface_area",
    "hemisphere_volume",
    "hemisphere_surface_area",
    "cylinder_volume",
    "cylinder_surface_area",
    "cone_volume",
    "cone_surface_area",
    "prism_volume",
    "pyramid_volume"
]
