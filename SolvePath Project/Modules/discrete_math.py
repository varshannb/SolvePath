# solvepath/discrete_math.py
"""
=========================================================
            SolvePath Discrete Mathematics Module
=========================================================

Includes step-by-step solutions for:

• Factorial
• Permutations (nPr)
• Combinations (nCr)
• Linear recurrence relations
• Fibonacci numbers
• Graph theory:
  - Degree of vertices
  - Number of edges
  - Path existence
  - Connected components

Returns:
• Solution object when show_steps=True
• Final result when show_steps=False

=========================================================
"""



import math
from typing import Dict, List, Any
from solvepath.solution import Solution

# ======================================================
# INTERNAL VALIDATION
# ======================================================

def _validate_non_negative(n, name="n"):
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"{name} must be a non-negative integer.")

def _expand_factorial_str(n):
    """Helper to return string '5 × 4 × 3 × 2 × 1'."""
    if n == 0: return "1"
    if n > 10: return f"{n} × {n-1} × ... × 1" # Truncate for readability
    return " × ".join(str(i) for i in range(n, 0, -1))

# ======================================================
# FACTORIAL
# ======================================================

def factorial(n: int, show_steps=False):
    _validate_non_negative(n, "n")
    result = math.factorial(n)

    if not show_steps:
        return result

    expansion = _expand_factorial_str(n)

    steps = [
        f"Step 1: Definition.",
        f"   n! = n × (n-1) × ... × 1",
        f"Step 2: Substitution.",
        f"   {n}! = {expansion}",
        f"Step 3: Calculation.",
        f"   {n}! = {result}"
    ]

    return Solution(
        given=f"n = {n}",
        to_find="Factorial n!",
        equation="n! = Π k",
        formula_name="Factorial",
        formula_used="n × (n-1)!",
        explanation="Product of all positive integers ≤ n.",
        steps=steps,
        answer=result
    )

# ======================================================
# PERMUTATIONS (nPr)
# ======================================================

def permutation(n: int, r: int, show_steps=False):
    _validate_non_negative(n, "n")
    _validate_non_negative(r, "r")
    if r > n:
        raise ValueError("r cannot be greater than n")

    # Math Logic
    n_fact_val = math.factorial(n)
    denom = n - r
    denom_fact_val = math.factorial(denom)
    result = n_fact_val // denom_fact_val

    if not show_steps:
        return result

    # Visual Expansion Logic
    numer_str = _expand_factorial_str(n)
    denom_str = _expand_factorial_str(denom)
    
    # Show cancellation conceptually
    if denom > 0 and n > denom:
        kept_terms = " × ".join(str(i) for i in range(n, denom, -1))
        cancellation_msg = f"   = {kept_terms}   (Terms 1 to {denom} cancel out)"
    else:
        cancellation_msg = "   (No simplification possible)"

    return Solution(
        given=f"n={n}, r={r}",
        to_find="Permutations P(n, r)",
        equation="P(n, r) = n! / (n-r)!",
        formula_name="Permutation Formula",
        formula_used="n! / (n-r)!",
        formula_reason="Order matters (Arrangements).",
        explanation="We calculate total arrangements and divide by the unselected arrangements.",
        steps=[
            f"Step 1: Substitute into Formula.",
            f"   P({n}, {r}) = {n}! / ({n}-{r})!",
            f"   P({n}, {r}) = {n}! / {denom}!",
            f"Step 2: Expand Factorials (Symbolic Working).",
            f"   Numerator:   {numer_str}",
            f"   Denominator: {denom_str}",
            f"Step 3: Cancel Common Terms.",
            cancellation_msg,
            f"Step 4: Final Calculation.",
            f"   {result}"
        ],
        answer=result
    )

# ======================================================
# COMBINATIONS (nCr)
# ======================================================

def combination(n: int, r: int, show_steps=False):
    _validate_non_negative(n, "n")
    _validate_non_negative(r, "r")
    if r > n:
        raise ValueError("r cannot be greater than n")

    # Math Logic
    n_fact_val = math.factorial(n)
    r_fact_val = math.factorial(r)
    n_minus_r = n - r
    n_minus_r_fact_val = math.factorial(n_minus_r)
    result = n_fact_val // (r_fact_val * n_minus_r_fact_val)

    if not show_steps:
        return result

    # Expansion Logic
    numer_str = _expand_factorial_str(n)
    r_str = _expand_factorial_str(r)
    nmr_str = _expand_factorial_str(n_minus_r)

    return Solution(
        given=f"n={n}, r={r}",
        to_find="Combinations C(n, r)",
        equation="C(n, r) = n! / (r!(n-r)!)",
        formula_name="Combination Formula",
        formula_used="n! / (r! × (n-r)!)",
        formula_reason="Order does NOT matter (Selections).",
        explanation="Permutations divided by r! to remove duplicate groups.",
        steps=[
            f"Step 1: Substitute into Formula.",
            f"   C({n}, {r}) = {n}! / ({r}! × ({n}-{r})!)",
            f"   C({n}, {r}) = {n}! / ({r}! × {n_minus_r}!)",
            f"Step 2: Expand Factorials.",
            f"   Numerator: {numer_str}",
            f"   Denom A:   {r_str}",
            f"   Denom B:   {nmr_str}",
            f"Step 3: Compute Values.",
            f"   {n_fact_val} / ({r_fact_val} × {n_minus_r_fact_val})",
            f"   {n_fact_val} / {r_fact_val * n_minus_r_fact_val}",
            f"Step 4: Final Division.",
            f"   {result}"
        ],
        answer=result
    )

# ======================================================
# LINEAR RECURRENCE RELATION
# ======================================================

def recurrence_linear(a0: int, a1: int, n: int, c1: int, c0: int, show_steps=False):
    _validate_non_negative(n, "n")
    
    values = [a0, a1]
    steps = [
        f"Step 1: Formula definition.",
        f"   aₙ = {c1}·aₙ₋₁ + {c0}·aₙ₋₂",
        f"Step 2: Initial values.",
        f"   a₀ = {a0}, a₁ = {a1}",
        f"Step 3: Iteration.",
    ]

    if n < 2:
        steps.append(f"   Target n={n} is a base case. Value is {values[n]}.")
    else:
        for i in range(2, n + 1):
            prev1 = values[i-1]
            prev2 = values[i-2]
            current = c1 * prev1 + c0 * prev2
            values.append(current)
            steps.append(f"   n={i}: a_{i} = ({c1} × {prev1}) + ({c0} × {prev2}) = {current}")

    result = values[n] if n < len(values) else values[-1]

    if not show_steps:
        return result

    return Solution(
        given=f"a₀={a0}, a₁={a1}, c₁={c1}, c₀={c0}",
        to_find=f"a_{n}",
        equation=f"aₙ = {c1}aₙ₋₁ + {c0}aₙ₋₂",
        formula_name="Linear Recurrence",
        formula_used="aₙ = c₁aₙ₋₁ + c₀aₙ₋₂",
        explanation="Iterative calculation of the sequence term.",
        steps=steps,
        answer=result
    )

# ======================================================
# FIBONACCI NUMBERS
# ======================================================

def fibonacci(n: int, show_steps=False):
    _validate_non_negative(n, "n")
    
    a, b = 0, 1
    steps = [
        "Step 1: Formula definition.",
        "   Fₙ = Fₙ₋₁ + Fₙ₋₂",
        "Step 2: Base cases.",
        "   F₀ = 0, F₁ = 1",
        "Step 3: Iteration."
    ]
    
    if n == 0: return 0
    if n == 1: return 1

    for i in range(2, n + 1):
        c = a + b
        steps.append(f"   n={i}: F_{i} = {b} + {a} = {c}")
        a, b = b, c

    if not show_steps:
        return b

    return Solution(
        given=f"n = {n}",
        to_find=f"F_{n}",
        equation="Fₙ = Fₙ₋₁ + Fₙ₋₂",
        formula_name="Fibonacci Sequence",
        formula_used="Fₙ₋₁ + Fₙ₋₂",
        explanation="Sum of the two preceding terms.",
        steps=steps,
        answer=b
    )

# ======================================================
# GRAPH THEORY: DEGREES
# ======================================================

def graph_degrees(adj: Dict[int, List[int]], show_steps=False):
    degrees = {v: len(neighbors) for v, neighbors in adj.items()}

    if not show_steps:
        return degrees

    steps = [
        "Step 1: Apply Degree Formula.",
        "   deg(v) = |Neighbors(v)|",
        "Step 2: Calculation for each vertex."
    ]

    for v, neighbors in adj.items():
        count = len(neighbors)
        # Mathematical notation for set cardinality
        steps.append(f"   deg({v}) = |{set(neighbors)}| = {count}")

    return Solution(
        given=f"Graph G(V, E)",
        to_find="Vertex Degrees",
        equation="deg(v) = |N(v)|",
        formula_name="Vertex Degree",
        formula_used="Count(Neighbors)",
        explanation="Counting incident edges for every vertex.",
        steps=steps,
        answer=degrees
    )

# ======================================================
# GRAPH THEORY: EDGE COUNT
# ======================================================

def count_edges(adj: Dict[int, List[int]], show_steps=False):
    deg_sum = sum(len(v) for v in adj.values())
    edges = deg_sum // 2

    if not show_steps:
        return edges

    steps = [
        "Step 1: Calculate Sum of Degrees (Σ deg(v))."
    ]
    
    calc_str = []
    for v, n in adj.items():
        d = len(n)
        calc_str.append(str(d))
    
    sum_str = " + ".join(calc_str)
    steps.append(f"   Sum = {sum_str} = {deg_sum}")
    
    steps.append("Step 2: Apply Handshaking Lemma.")
    steps.append("   2|E| = Σ deg(v)")
    steps.append(f"   |E| = {deg_sum} / 2")
    steps.append(f"   |E| = {edges}")

    return Solution(
        given="Adjacency List",
        to_find="Edge Count |E|",
        equation="2|E| = Σ deg(v)",
        formula_name="Handshaking Lemma",
        formula_used="|E| = Σ deg(v) / 2",
        explanation="Each edge contributes 2 to the sum of degrees.",
        steps=steps,
        answer=edges
    )

# ======================================================
# GRAPH THEORY: PATH FINDING
# ======================================================

def graph_has_path(adj: Dict[int, List[int]], start: int, end: int, show_steps=False):
    visited = set()
    stack = [start]
    
    steps = [
        f"Step 1: Setup Search (DFS).",
        f"   Start: {start} -> Target: {end}",
        "Step 2: Traversal Log."
    ]
    
    found = False
    while stack:
        node = stack.pop()
        
        if node == end:
            steps.append(f"   Current: {node}. MATCH FOUND!")
            found = True
            break
        
        if node not in visited:
            visited.add(node)
            neighbors = adj.get(node, [])
            steps.append(f"   Visit {node}. Neighbors={neighbors}. Stack ← Stack ∪ {neighbors}")
            
            for n in neighbors:
                if n not in visited:
                    stack.append(n)
        else:
            steps.append(f"   Visit {node}. Already visited. Skip.")

    steps.append(f"Step 3: Result -> {found}")

    if not show_steps:
        return found

    return Solution(
        given=f"Start={start}, End={end}",
        to_find="Path Existence",
        equation="∃ path u → ... → v",
        formula_name="Depth First Search",
        formula_used="Stack-based Traversal",
        explanation="Traversing graph edges to find connectivity.",
        steps=steps,
        answer=found
    )

# ======================================================
# GRAPH THEORY: CONNECTED COMPONENTS
# ======================================================

def connected_components(adj: Dict[int, List[int]], show_steps=False):
    visited = set()
    components = []
    
    steps = [
        "Step 1: Initialize Sets.",
        f"   V = {list(adj.keys())}, Visited = ∅",
        "Step 2: Iterate through V."
    ]

    for node in adj:
        if node not in visited:
            comp = []
            stack = [node]
            visited.add(node)
            
            steps.append(f"   Node {node} ∉ Visited. Start Component C_{len(components)+1}.")
            
            while stack:
                v = stack.pop()
                comp.append(v)
                
                neighbors = adj.get(v, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            
            comp.sort()
            components.append(comp)
            steps.append(f"   Component Complete: {comp}")

    if not show_steps:
        return components

    return Solution(
        given="Graph G",
        to_find="Connected Components",
        equation="G = C₁ ∪ C₂ ∪ ...",
        formula_name="Component Search",
        formula_used="DFS / BFS",
        explanation="Partitioning vertices into disjoint connected sets.",
        steps=steps,
        answer=components
    )

# ======================================================
# EXPORT
# ======================================================

__all__ = [
    "factorial",
    "permutation",
    "combination",
    "recurrence_linear",
    "fibonacci",
    "graph_degrees",
    "count_edges",
    "graph_has_path",
    "connected_components",
]
