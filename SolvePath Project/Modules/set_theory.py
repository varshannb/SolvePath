#solvepath/set_theory.py
"""
=========================================================
              SolvePath Set Theory Module
=========================================================

Includes HIGHLY DETAILED, TUTOR-STYLE step-by-step solutions for:

• Union
• Intersection
• Difference
• Complement
• Power Set
• Cardinality
• Subset / Superset Checks
• Cartesian Product
• Combinations (k-Subsets)
• Partitions

Returns:
• Solution object when show_steps=True
• Final result only when show_steps=False

=========================================================
"""

from typing import Set, Any, Iterable, List
from itertools import combinations, product
from solvepath.solution import Solution

# ======================================================
# INTERNAL VALIDATION & FORMATTING
# ======================================================

def _validate_set(s, name="Input"):
    if not isinstance(s, (set, list, tuple)):
        raise TypeError(f"{name} must be a set, list, or tuple.")
    return set(s)

def _format_set(s):
    """Returns a string representation of a set, sorted for readability."""
    try:
        return "{" + ", ".join(map(str, sorted(list(s)))) + "}"
    except Exception:
        return str(s)

def _safe_sorted_list(s: set):
    """Safely tries to sort, falls back to list order if not sortable."""
    try:
        return sorted(list(s))
    except Exception:
        return list(s)

# ======================================================
# UNION
# ======================================================

def union(A: Set[Any], B: Set[Any], show_steps=False):
    A = _validate_set(A, "Set A")
    B = _validate_set(B, "Set B")

    result = A | B

    if not show_steps:
        return result

    steps = [
        "Step 1: Inspect the input sets.",
        f"   Set A contains: {_format_set(A)}",
        f"   Set B contains: {_format_set(B)}",
        "Step 2: Start with all elements from Set A.",
        f"   Current Collection: {_safe_sorted_list(A)}",
        "Step 3: Add elements from Set B one by one (ignoring duplicates)."
    ]

    current_collection = list(A)
    for item in B:
        if item in A:
            steps.append(f"   Inspect '{item}' from B... It is ALREADY in A. Skip it.")
        else:
            steps.append(f"   Inspect '{item}' from B... It is NEW. Add it.")
            current_collection.append(item)

    steps.append("Step 4: Final Collection (Union).")
    steps.append(f"   {_format_set(result)}")

    return Solution(
        given=f"A = {_format_set(A)}, B = {_format_set(B)}",
        to_find="A ∪ B (Union)",
        equation="A ∪ B = {x | x ∈ A OR x ∈ B}",
        formula_name="Union Definition",
        formula_used="A ∪ B = {x | x ∈ A ∨ x ∈ B}",
        formula_reason="Union gathers every element that appears in EITHER set.",
        explanation="We merge the two groups, ensuring no element is counted twice.",
        steps=steps,
        answer=result
    )

# ======================================================
# INTERSECTION
# ======================================================

def intersection(A: Set[Any], B: Set[Any], show_steps=False):
    A = _validate_set(A, "Set A")
    B = _validate_set(B, "Set B")

    result = A & B

    if not show_steps:
        return result

    steps = [
        "Step 1: Inspect the input sets.",
        f"   A = {_format_set(A)}",
        f"   B = {_format_set(B)}",
        "Step 2: Check for common elements (The Overlap)."
    ]

    if not A or not B:
        steps.append("   At least one set is empty, so there is no overlap.")
    else:
        source_set = A if len(A) < len(B) else B
        target_set = B if len(A) < len(B) else A

        for item in source_set:
            if item in target_set:
                steps.append(f"   Check '{item}'... FOUND in both sets! -> Keep it.")
            else:
                steps.append(f"   Check '{item}'... Not found in the other set. -> Discard.")

    steps.append("Step 3: Final Intersection Set.")
    steps.append(f"   {_format_set(result)}")

    return Solution(
        given=f"A = {_format_set(A)}, B = {_format_set(B)}",
        to_find="A ∩ B (Intersection)",
        equation="A ∩ B = {x | x ∈ A AND x ∈ B}",
        formula_name="Intersection Definition",
        formula_used="A ∩ B = {x | x ∈ A ∧ x ∈ B}",
        formula_reason="Intersection finds items that satisfy BOTH conditions simultaneously.",
        explanation="We keep only the elements that exist in both Set A and Set B.",
        steps=steps,
        answer=result
    )

# ======================================================
# DIFFERENCE
# ======================================================

def difference(A: Set[Any], B: Set[Any], show_steps=False):
    A = _validate_set(A, "Set A")
    B = _validate_set(B, "Set B")

    result = A - B

    if not show_steps:
        return result

    steps = [
        "Step 1: Start with Set A (The minuend).",
        f"   Starting items: {_format_set(A)}",
        "Step 2: Identify items to remove (from Set B).",
        f"   Banned items: {_format_set(B)}",
        "Step 3: Subtract B from A element by element."
    ]

    for item in A:
        if item in B:
            steps.append(f"   Inspect '{item}' in A... It IS in B. -> DELETE it.")
        else:
            steps.append(f"   Inspect '{item}' in A... It is SAFE (not in B). -> Keep it.")

    steps.append("Step 4: Final Remaining Set.")
    steps.append(f"   {_format_set(result)}")

    return Solution(
        given=f"A = {_format_set(A)}, B = {_format_set(B)}",
        to_find="A - B (Difference)",
        equation="A − B = {x | x ∈ A AND x ∉ B}",
        formula_name="Set Difference Definition",
        formula_used="A \\ B = {x | x ∈ A ∧ x ∉ B}",
        formula_reason="Difference removes specific elements from a group.",
        explanation="We take Set A and remove any element that also appears in Set B.",
        steps=steps,
        answer=result
    )

# ======================================================
# COMPLEMENT
# ======================================================

def complement(U: Set[Any], A: Set[Any], show_steps=False):
    U = _validate_set(U, "Universal Set U")
    A = _validate_set(A, "Set A")

    result = U - A

    if not show_steps:
        return result

    steps = [
        "Step 1: Define the Universe U.",
        f"   U = {_format_set(U)}",
        "Step 2: Define the Exclusion Set A.",
        f"   A = {_format_set(A)}",
        "Step 3: Find everything in U that is NOT in A."
    ]

    for item in U:
        if item in A:
            steps.append(f"   Check '{item}'... It belongs to A. -> Exclude.")
        else:
            steps.append(f"   Check '{item}'... It is NOT in A. -> Include in Complement.")

    steps.append("Step 4: Final Complement Set (A').")
    steps.append(f"   {_format_set(result)}")

    return Solution(
        given=f"U = {_format_set(U)}, A = {_format_set(A)}",
        to_find="A' (Complement)",
        equation="A' = U − A",
        formula_name="Set Complement",
        formula_used="Aᶜ = {x | x ∈ U ∧ x ∉ A}",
        formula_reason="Complement finds everything in U that is outside A.",
        explanation="It represents everything in the universe that is NOT part of A.",
        steps=steps,
        answer=result
    )

# ======================================================
# POWER SET
# ======================================================

def power_set(A: Set[Any], show_steps=False):
    A = _validate_set(A, "Set A")
    elements = _safe_sorted_list(A)
    n = len(elements)

    subsets_list = [set(c) for r in range(n + 1) for c in combinations(elements, r)]

    if not show_steps:
        return subsets_list

    expected = 2 ** n

    steps = [
        "Step 1: Analyze Set A.",
        f"   Elements: {elements}",
        f"   Size (n): {n}",
        "Step 2: Calculate Total Subsets.",
        f"   Formula: 2^n = 2^{n} = {expected} total subsets expected.",
        "Step 3: Build subsets by size."
    ]

    count = 0
    for size in range(0, n + 1):
        steps.append(f"   -- Size {size} --")
        for subset in (s for s in subsets_list if len(s) == size):
            count += 1
            steps.append(f"   {count}. {_format_set(subset)}")

    steps.append("Step 4: Verification.")
    steps.append(f"   We found exactly {count} subsets, which matches 2^{n} = {expected}.")

    return Solution(
        given=f"Set A = {_format_set(A)}",
        to_find="Power Set P(A)",
        equation="P(A) = { S | S ⊆ A }",
        formula_name="Power Set",
        formula_used="P(A) = {x | x ⊆ A}",
        formula_reason="Power Set contains every possible subset (every possible selection).",
        explanation="We list every possible selection of elements, including the empty set and the full set.",
        steps=steps,
        answer=subsets_list
    )

# ======================================================
# CARDINALITY
# ======================================================

def cardinality(A: Set[Any], show_steps=False):
    A = _validate_set(A, "Set A")
    result = len(A)

    if not show_steps:
        return result

    steps = [
        "Step 1: List the elements of the set.",
        f"   Items: {list(A)}",
        "Step 2: Sets remove duplicates automatically.",
        "Step 3: Count the unique items."
    ]

    for i, item in enumerate(A, 1):
        steps.append(f"   {i}. Found element: {item}")

    steps.append("Step 4: Final Count (Cardinality).")
    steps.append(f"   |A| = {result}")

    return Solution(
        given=f"Set A = {_format_set(A)}",
        to_find="Cardinality |A|",
        equation="|A| = n",
        formula_name="Cardinality",
        formula_used="|A| = Σ 1 for x ∈ A",
        explanation="Cardinality means how many elements are inside the set.",
        steps=steps,
        answer=result
    )

# ======================================================
# SUBSET / SUPERSET CHECKS
# ======================================================

def is_subset(A: Set[Any], B: Set[Any], show_steps=False):
    A = _validate_set(A, "Set A")
    B = _validate_set(B, "Set B")
    result = A.issubset(B)

    if not show_steps:
        return result

    steps = [
        "Step 1: Subset Rule.",
        "   A ⊆ B is TRUE if every element in A is also inside B.",
        "Step 2: Check each element of A."
    ]

    if not A:
        steps.append("   A is empty. Empty set is a subset of every set. -> True")
    else:
        for item in A:
            steps.append(f"   - Is '{item}' in B? {'YES' if item in B else 'NO'}")

    steps.append("Step 3: Final Verdict.")
    steps.append(f"   {result}")

    return Solution(
        given=f"A = {_format_set(A)}, B = {_format_set(B)}",
        to_find="Is A ⊆ B?",
        equation="A ⊆ B",
        formula_name="Subset Definition",
        formula_used="∀x (x ∈ A ⟹ x ∈ B)",
        explanation="We verify whether A is completely contained in B.",
        steps=steps,
        answer=result
    )

def is_superset(A: Set[Any], B: Set[Any], show_steps=False):
    A = _validate_set(A, "Set A")
    B = _validate_set(B, "Set B")
    result = A.issuperset(B)

    if not show_steps:
        return result

    steps = [
        "Step 1: Superset Rule.",
        "   A ⊇ B is TRUE if every element in B is also inside A.",
        "Step 2: Check each element of B."
    ]

    for item in B:
        steps.append(f"   - Is '{item}' in A? {'YES' if item in A else 'NO'}")

    steps.append("Step 3: Final Verdict.")
    steps.append(f"   {result}")

    return Solution(
        given=f"A = {_format_set(A)}, B = {_format_set(B)}",
        to_find="Is A ⊇ B?",
        equation="A ⊇ B",
        formula_name="Superset Definition",
        formula_used="∀x (x ∈ B ⟹ x ∈ A)",
        explanation="We verify whether A contains all elements of B.",
        steps=steps,
        answer=result
    )

def proper_subset(A: Set[Any], B: Set[Any], show_steps=False):
    A = _validate_set(A, "Set A")
    B = _validate_set(B, "Set B")
    result = A < B

    if not show_steps:
        return result

    steps = [
        "Step 1: Proper Subset Rule.",
        "   A ⊂ B is TRUE only if:",
        "   1) A ⊆ B",
        "   2) A ≠ B",
        f"Step 2: Check A ⊆ B -> {A.issubset(B)}",
        f"Step 3: Check A ≠ B -> {A != B}",
        f"Step 4: Final Verdict -> {result}"
    ]

    return Solution(
        given=f"A = {_format_set(A)}, B = {_format_set(B)}",
        to_find="Is A ⊂ B?",
        equation="A ⊂ B",
        formula_name="Proper Subset",
        formula_used="(A ⊆ B) ∧ (A ≠ B)",
        explanation="A must be inside B, but not equal to B.",
        steps=steps,
        answer=result
    )

def proper_superset(A: Set[Any], B: Set[Any], show_steps=False):
    A = _validate_set(A, "Set A")
    B = _validate_set(B, "Set B")
    result = A > B

    if not show_steps:
        return result

    steps = [
        "Step 1: Proper Superset Rule.",
        "   A ⊃ B is TRUE only if:",
        "   1) A ⊇ B",
        "   2) A ≠ B",
        f"Step 2: Check A ⊇ B -> {A.issuperset(B)}",
        f"Step 3: Check A ≠ B -> {A != B}",
        f"Step 4: Final Verdict -> {result}"
    ]

    return Solution(
        given=f"A = {_format_set(A)}, B = {_format_set(B)}",
        to_find="Is A ⊃ B?",
        equation="A ⊃ B",
        formula_name="Proper Superset",
        formula_used="(A ⊇ B) ∧ (A ≠ B)",
        explanation="A must contain B fully and also have extra elements.",
        steps=steps,
        answer=result
    )

# ======================================================
# CARTESIAN PRODUCT
# ======================================================

def cartesian_product(*sets: Iterable[Any], show_steps=False):
    sets_list = [list(_validate_set(s)) for s in sets]
    result = list(product(*sets_list))

    if not show_steps:
        return result

    steps = ["Step 1: Identify Input Sets."]
    for i, s in enumerate(sets_list, 1):
        steps.append(f"   Set {i}: {s}")

    steps.append("Step 2: Form ordered pairs/tuples.")
    steps.append("   Take one element from each set in order to form a tuple.")

    limit = 8
    for i, pair in enumerate(result[:limit], 1):
        steps.append(f"   Combination {i}: {pair}")

    if len(result) > limit:
        steps.append(f"   ... (and {len(result) - limit} more pairs)")

    steps.append("Step 3: Total number of tuples.")
    steps.append(f"   Size = {len(result)}")

    return Solution(
        given=f"Input Sets: {sets_list}",
        to_find="Cartesian Product",
        equation="A₁ × ... × Aₙ",
        formula_name="Cartesian Product",
        formula_used="A × B = {(a,b) | a∈A, b∈B}",
        formula_reason="We want every possible ordered combination.",
        explanation="We combine every element of the first set with every element of the next sets.",
        steps=steps,
        answer=result
    )

# ======================================================
# k-SUBSETS
# ======================================================

def subsets_of_size(A: Set[Any], k: int, show_steps=False):
    A = _validate_set(A, "Set A")

    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer.")

    elements = _safe_sorted_list(A)

    # ✅ IMPORTANT: If k > n, combinations result is empty (no error)
    if k > len(elements):
        result = []
    else:
        result = [set(c) for c in combinations(elements, k)]

    if not show_steps:
        return result

    steps = [
        "Step 1: Identify the pool of elements.",
        f"   Elements: {elements}",
        f"Step 2: Target size k = {k}.",
        "Step 3: Generate combinations."
    ]

    if len(result) == 0:
        steps.append("   No combinations possible because k > number of elements.")
    else:
        for i, res in enumerate(result, 1):
            steps.append(f"   {i}. {_format_set(res)}")

    steps.append(f"Step 4: Total combinations = {len(result)}.")

    return Solution(
        given=f"Set A = {_format_set(A)}, k = {k}",
        to_find="k-Subsets (Combinations)",
        equation="nCk",
        formula_name="Combinations",
        formula_used="C(n, k) = n! / (k!(n-k)!)",
        explanation=f"We list every way to choose {k} items from the set without caring about order.",
        steps=steps,
        answer=result
    )


# ======================================================
# SIMPLE k-PARTITION
# ======================================================

def partitions_k(A: Set[Any], k: int, show_steps=False):
    A = _validate_set(A, "Set A")

    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer.")

    # ✅ IMPORTANT: Do NOT raise when k > len(A)
    if k > len(A):
        msg = "SolvePath Error: You cannot split a set into more groups than elements (groups cannot be empty)."

        # ✅ show_steps=False must return the message string (tests expect this)
        if not show_steps:
            return msg

        # ✅ show_steps=True must return Solution with formula_name="Partition Error"
        return Solution(
            given=f"Set A = {_format_set(A)}, k = {k}",
            to_find="Partition into k groups",
            equation="⋃ Si = A and Si ∩ Sj = ∅",
            formula_name="Partition Error",
            formula_used="k must be ≤ number of elements in A",
            explanation=(
                "A partition divides a set into k non-empty groups. "
                "If k is greater than the number of elements, at least one group would be empty, "
                "so the partition is not possible."
            ),
            steps=[
                "Step 1: Count the number of elements in the set.",
                f"   >> |A| = {len(A)}",
                "Step 2: Compare k with |A|.",
                f"   >> k = {k}",
                f"   >> Since k > |A| ({k} > {len(A)}), a partition is not possible.",
                "Step 3: Final Answer (Error Message)."
            ],
            answer=msg
        )

    # ✅ Normal valid partition
    elements = _safe_sorted_list(A)
    buckets = [[] for _ in range(k)]

    for i, el in enumerate(elements):
        bucket_index = i % k
        buckets[bucket_index].append(el)

    result = [set(b) for b in buckets]

    # ✅ Tests expect Solution EVEN when show_steps=False
    if not show_steps:
        return Solution(
            given=f"Set A = {_format_set(A)}, k = {k}",
            to_find="Representative Partition",
            equation="⋃ Si = A and Si ∩ Sj = ∅",
            formula_name="Set Partition",
            formula_used="⋃ Si = A ∧ Si ∩ Sj = ∅",
            explanation="We split the set into k non-overlapping groups that cover the whole set.",
            steps=[
                f"Step 1: Split the set into {k} groups using round-robin distribution.",
                "Step 2: Final Answer."
            ],
            answer=result
        )

    # ✅ show_steps=True → include steps
    steps = [
        f"Step 1: Setup {k} empty buckets (groups).",
        f"Step 2: Line up elements: {elements}.",
        "Step 3: Deal elements into buckets (Round-Robin style)."
    ]

    for i, el in enumerate(elements):
        bucket_index = i % k
        steps.append(f"   - Place '{el}' into Bucket {bucket_index + 1}.")

    steps.append("Step 4: Final Partition Groups.")
    for i, res in enumerate(result, 1):
        steps.append(f"   Group {i}: {_format_set(res)}")

    return Solution(
        given=f"Set A = {_format_set(A)}, k = {k}",
        to_find="Representative Partition",
        equation="⋃ Si = A and Si ∩ Sj = ∅",
        formula_name="Set Partition",
        formula_used="⋃ Si = A ∧ Si ∩ Sj = ∅",
        explanation="We split the set into k non-overlapping groups that cover the whole set.",
        steps=steps,
        answer=result
    )




# ======================================================
# EXPORT
# ======================================================

__all__ = [
    "union", "intersection", "difference", "complement",
    "power_set", "cardinality",
    "is_subset", "is_superset", "proper_subset", "proper_superset",
    "cartesian_product", "subsets_of_size", "partitions_k"
]
