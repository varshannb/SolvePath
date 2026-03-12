# solvepath/probability.py
"""
=========================================================
                SolvePath Probability Module
=========================================================

Includes:

• Basic probability
• Complement rule
• Conditional probability
• Independent events
• Bayes theorem
• Bernoulli trials
• Binomial distribution
• Normal distribution (PDF)

Teaching Rules:
• Same detailed steps for EVERY function
• Beginner / 1st grade friendly
• BODMAS only when mathematically required
• No formula removed
=========================================================
"""

import math
from typing import Union
from solvepath.solution import Solution

Number = Union[int, float]

# ======================================================
#                 INTERNAL VALIDATION
# ======================================================

def _ensure_probability(p: Number, name="p"):
    if not isinstance(p, (int, float)):
        raise TypeError(f"SolvePath Error: {name} must be numeric.")
    if not (0 <= p <= 1):
        raise ValueError(f"SolvePath Error: {name} must be between 0 and 1.")
    return p

# ======================================================
#                 BASIC PROBABILITY
# ======================================================

def probability(success: Number, total: Number, show_steps=False):
    if total <= 0:
        raise ValueError("Total outcomes must be positive.")
    if success < 0 or success > total:
        raise ValueError("Invalid success count.")

    result = success / total

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Determine how likely a specific event is to happen compared to everything that could happen.",
        given=f"Successful Outcomes = {success}, Total Outcomes = {total}",
        to_find="Probability P(E)",
        equation=f"{success} / {total}",
        formula_name="Basic Probability Ratio",
        formula_used="P(E) = Successes / Total",
        formula_reason="Probability is fundamentally a ratio: the 'part' divided by the 'whole'.",
        symbol_explanation="P(E) stands for Probability of Event E.",
        explanation="We divide the number of ways we can 'win' by the total number of possibilities.",
        steps=[
            f"Step 1: Identify the number of 'winning' outcomes (Successes).",
            f"   >> Successes = {success}",
            f"Step 2: Identify the total size of the sample space (Total).",
            f"   >> Total = {total}",
            "Step 3: Set up the ratio.",
            f"   >> Ratio = {success} ÷ {total}",
            "Step 4: Perform the division to get a decimal.",
            f"   >> {result:.4f}",
            "Step 5: Convert to a percentage to make it easier to understand.",
            f"   >> {result:.4f} × 100 = {result*100:.2f}%",
            "Step 6: Check logic: Is the probability between 0 (Impossible) and 1 (Certain)?",
            f"   >> 0 <= {result:.4f} <= 1? Yes.",
            f"Step 7: Final Answer is {result:.4f}."
        ],
        answer=f"{result:.4f}"
    )

# ======================================================
#                  COMPLEMENT RULE
# ======================================================

def complement(p: Number, show_steps=False):
    p = _ensure_probability(p)
    result = 1 - p

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the chance that an event does NOT happen.",
        given=f"P(Event Happening) = {p}",
        to_find="P(Event Not Happening)",
        equation="1 - P(E)",
        formula_name="Complement Rule",
        formula_used="P(E') = 1 - P(E)",
        formula_reason="The probabilities of all possible outcomes must add up to 100% (or 1).",
        symbol_explanation="E' (read E-prime) means 'Not E'.",
        explanation="Since something either happens or it doesn't, we subtract the 'Happening' chance from 1.",
        steps=[
            f"Step 1: Identify the known probability P(E).",
            f"   >> P(E) = {p}",
            "Step 2: The total probability space is 1. We know the slice for P(E).",
            "Step 3: We need to find the rest of the pie (P(E')).",
            f"   >> Formula: 1 - {p}",
            "Step 4: Perform the subtraction.",
            f"   >> {result:.4f}",
            "Step 5: Verify the logic.",
            f"   >> {p} (Happens) + {result:.4f} (Doesn't Happen) = 1.0. Correct.",
            "Step 6: Interpret result.",
            f"   >> There is a {result*100:.2f}% chance the event will NOT occur.",
            f"Step 7: Final Answer is {result:.4f}."
        ],
        answer=f"{result:.4f}"
    )

# ======================================================
#              CONDITIONAL PROBABILITY
# ======================================================

def conditional_probability(p_a_and_b: Number, p_b: Number, show_steps=False):
    p_a_and_b = _ensure_probability(p_a_and_b, "P(A and B)")
    p_b = _ensure_probability(p_b, "P(B)")

    if p_b == 0:
        raise ValueError("SolvePath Error: P(B) cannot be 0 in conditional probability.")

    if p_a_and_b > p_b:
        raise ValueError("SolvePath Error: Intersection (Overlap) cannot be larger than the Condition itself.")

    result = p_a_and_b / p_b

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the probability of A, assuming we KNOW B has already happened.",
        given=f"P(Both A and B) = {p_a_and_b}, P(Condition B) = {p_b}",
        to_find="P(A | B)",
        equation=f"{p_a_and_b} / {p_b}",
        formula_name="Conditional Probability Formula",
        formula_used="P(A | B) = P(A ∩ B) / P(B)",
        formula_reason="Since B occurred, our 'Total Universe' shrinks from 1 down to just P(B).",
        symbol_explanation="| means 'Given', ∩ means 'Intersection' (Overlap).",
        explanation="We zoom in on circle B. We ask: What portion of circle B is also part of A?",
        steps=[
            f"Step 1: Identify the Overlap Probability P(A ∩ B).",
            f"   >> {p_a_and_b} (This is the part shared by both)",
            f"Step 2: Identify the Condition Probability P(B).",
            f"   >> {p_b} (This is our new 'Total')",
            "Step 3: Visualize restricting our view to only the B circle.",
            "Step 4: Set up the new ratio: Overlap ÷ New Total.",
            f"   >> {p_a_and_b} ÷ {p_b}",
            "Step 5: Perform the division.",
            f"   >> {result:.4f}",
            "Step 6: Sanity Check 1 (Must be <= 1).",
            f"   >> {result:.4f} <= 1? Yes.",
            "Step 7: Sanity Check 2 (Must be >= Original Overlap).",
            f"   >> Since the sample space shrunk, the probability should go up. {result:.4f} >= {p_a_and_b}? Yes.",
            "Step 8: Interpret result.",
            f"   >> Given that B happened, there is a {result*100:.2f}% chance A also happened.",
            f"Step 9: Final Answer is {result:.4f}."
        ],
        answer=f"{result:.4f}"
    )

# ======================================================
#               INDEPENDENT EVENTS
# ======================================================

def independent_events(p_a: Number, p_b: Number, show_steps=False):
    p_a = _ensure_probability(p_a, "P(A)")
    p_b = _ensure_probability(p_b, "P(B)")

    result = p_a * p_b

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Calculate the chance of two unrelated events both happening.",
        given=f"P(A) = {p_a}, P(B) = {p_b}",
        to_find="P(A AND B)",
        equation=f"{p_a} * {p_b}",
        formula_name="Multiplication Rule (Independent)",
        formula_used="P(A ∩ B) = P(A) × P(B)",
        formula_reason="Since A doesn't change B, we just take the fraction of a fraction.",
        symbol_explanation="∩ means Intersection (AND).",
        explanation="We need Event A to happen, AND then within that reality, Event B to happen.",
        steps=[
            f"Step 1: Identify probability of first event P(A).",
            f"   >> {p_a}",
            f"Step 2: Identify probability of second event P(B).",
            f"   >> {p_b}",
            "Step 3: Imagine flipping two coins. One result does not stop the other.",
            "Step 4: Set up the multiplication.",
            f"   >> {p_a} × {p_b}",
            "Step 5: Perform calculation.",
            f"   >> {result:.4f}",
            "Step 6: Logic Check.",
            "   >> Getting TWO specific things is harder than getting one, so the probability should be smaller.",
            f"   >> {result:.4f} is smaller than {p_a}. Correct.",
            f"Step 7: Final Answer is {result:.4f}."
        ],
        answer=f"{result:.4f}"
    )

# ======================================================
#                   BAYES THEOREM
# ======================================================

def bayes(p_b_given_a: Number, p_a: Number, p_b: Number, show_steps=False):
    p_b_given_a = _ensure_probability(p_b_given_a, "P(B|A)")
    p_a = _ensure_probability(p_a, "P(A)")
    p_b = _ensure_probability(p_b, "P(B)")

    if p_b == 0:
        raise ValueError("SolvePath Error: P(B) cannot be 0 in Bayes theorem.")

    numerator = p_b_given_a * p_a
    result = numerator / p_b

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Update the probability of a Cause (A) after seeing an Effect (B).",
        given=f"Likelihood P(B|A)={p_b_given_a}, Prior P(A)={p_a}, Evidence P(B)={p_b}",
        to_find="Posterior Probability P(A | B)",
        equation="(P(B|A) * P(A)) / P(B)",
        formula_name="Bayes' Theorem",
        formula_used="P(A | B) = (P(B | A) × P(A)) / P(B)",
        formula_reason="It flips conditional probability: determining the Cause given the Effect.",
        symbol_explanation="P(A) is Prior (Initial belief), P(A|B) is Posterior (Updated belief).",
        explanation="We calculate the 'True Positive' rate relative to all 'Positive' flags.",
        steps=[
            "Step 1: Identify the Likelihood P(B|A) (How often the Cause creates the Effect).",
            f"   >> {p_b_given_a}",
            "Step 2: Identify the Prior P(A) (How common the Cause was originally).",
            f"   >> {p_a}",
            "Step 3: Calculate the Numerator (The probability of True Positive).",
            f"   >> P(B|A) * P(A) = {p_b_given_a} * {p_a}",
            f"   >> Numerator = {numerator:.4f} (This is P(A and B))",
            "Step 4: Identify the Marginal Evidence P(B) (How common the Effect is in general).",
            f"   >> {p_b}",
            "Step 5: Normalize the result by dividing True Positives by Total Positives.",
            f"   >> {numerator:.4f} ÷ {p_b}",
            "Step 6: Perform division.",
            f"   >> {result:.4f}",
            "Step 7: Interpret.",
            f"   >> Before seeing evidence B, belief in A was {p_a*100}%.",
            f"   >> After seeing evidence B, belief in A is updated to {result*100:.2f}%.",
            f"Step 8: Final Answer is {result:.4f}."
        ],
        answer=f"{result:.4f}"
    )

# ======================================================
#                BERNOULLI TRIAL
# ======================================================

def bernoulli(p: Number, outcome: int, show_steps=False):
    p = _ensure_probability(p)
    if outcome not in (0, 1):
        raise ValueError("Outcome must be 0 (fail) or 1 (success).")

    if outcome == 1:
        result = p
        desc = "Success"
    else:
        result = 1 - p
        desc = "Failure"

    if not show_steps:
        return result

    return Solution(
        problem_understanding=f"Find probability of a single trial resulting in {desc}.",
        given=f"P(Success)={p}, Desired Outcome={outcome}",
        to_find=f"P(X={outcome})",
        equation="p^x * (1-p)^(1-x)",
        formula_name="Bernoulli Distribution",
        formula_used="P(x) = p^x (1 - p)^(1 - x)",
        formula_reason="Mathematical way to select P if Success, or 1-P if Failure.",
        symbol_explanation="x=1 for success, x=0 for failure.",
        explanation="If we want Success (1), the prob is p. If Failure (0), it is 1-p.",
        steps=[
            f"Step 1: Identify probability of success (p).",
            f"   >> p = {p}",
            f"Step 2: Identify probability of failure (q = 1-p).",
            f"   >> q = 1 - {p} = {1-p:.4f}",
            f"Step 3: Check which outcome we want.",
            f"   >> x = {outcome} ({desc})",
            "Step 4: Select the correct probability.",
            f"   >> We want {desc}, so we take {'p' if outcome==1 else 'q'}.",
            f"Step 5: Result = {result:.4f}",
            f"Step 6: Final Answer."
        ],
        answer=f"{result:.4f}"
    )

# ======================================================
#               BINOMIAL DISTRIBUTION
# ======================================================

def binomial(n: int, k: int, p: Number, show_steps=False):
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers.")
    if n < 0 or k < 0 or k > n:
        raise ValueError("Invalid n or k values.")
    p = _ensure_probability(p, "p")

    comb_val = math.comb(n, k)
    prob_success = p ** k
    prob_failure = (1 - p) ** (n - k)
    result = comb_val * prob_success * prob_failure

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find probability of getting exactly 'k' successes in 'n' tries.",
        given=f"Trials n={n}, Successes k={k}, Prob(Success) p={p}",
        to_find="P(X=k)",
        equation="nCk * p^k * (1-p)^(n-k)",
        formula_name="Binomial Distribution Formula",
        formula_used="P(k) = (nCk) · (p^k) · ((1-p)^(n-k))",
        formula_reason="We need to account for probability AND the number of ways it can happen.",
        symbol_explanation="nCk = Combinations (The 'Scenarios Factor').",
        explanation="Multiply the number of scenarios by the probability of that specific scenario.",
        steps=[
            f"Step 1: Identify the parameters.",
            f"   >> n={n} (Total flips/tries), k={k} (Wins needed), p={p} (Win chance).",
            "Step 2: PART 1: Calculate The 'Scenarios Factor' (nCk).",
            f"   >> How many ways can we arrange {k} wins in {n} tries?",
            f"   >> nCk = {n}C{k} = {comb_val}",
            "Step 3: PART 2: Calculate The 'Success Factor' (p^k).",
            f"   >> Probability of winning {k} times.",
            f"   >> {p}^{k} = {prob_success:.6f}",
            "Step 4: PART 3: Calculate The 'Failure Factor' (1-p)^(n-k).",
            f"   >> We need the remaining {n-k} trials to be failures.",
            f"   >> Failure Chance q = 1 - {p} = {1-p:.2f}",
            f"   >> Exponent = {n} - {k} = {n-k}",
            f"   >> {1-p:.2f}^{n-k} = {prob_failure:.6f}",
            "Step 5: COMBINE: Multiply all three parts.",
            f"   >> (Scenarios) * (Successes) * (Failures)",
            f"   >> {comb_val} * {prob_success:.6f} * {prob_failure:.6f}",
            "Step 6: Perform final calculation.",
            f"   >> {result:.4f}",
            "Step 7: Interpret.",
            f"   >> There is a {result*100:.2f}% chance of getting exactly {k} successes.",
            f"Step 8: Final Answer is {result:.4f}."
        ],
        answer=f"{result:.4f}"
    )

# ======================================================
#             NORMAL DISTRIBUTION (PDF)
# ======================================================

def normal_pdf(x: Number, mu: Number, sigma: Number, show_steps=False):
    if sigma <= 0:
        raise ValueError("Standard deviation must be positive.")

    coeff_part = 1 / (sigma * math.sqrt(2 * math.pi))
    z_score_sq = ((x - mu) ** 2) / (sigma ** 2)
    exponent = -0.5 * z_score_sq
    exp_val = math.exp(exponent)
    result = coeff_part * exp_val

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the probability density (height of the bell curve) at a specific point x.",
        given=f"Point x={x}, Mean μ={mu}, StdDev σ={sigma}",
        to_find="f(x) (Height)",
        equation="Gaussian Function",
        formula_name="Normal Distribution PDF",
        formula_used="f(x) = (1 / σ√2π) · e^(-0.5((x-μ)/σ)^2)",
        formula_reason="Describes the Bell Curve shape mathematically.",
        symbol_explanation="e ≈ 2.718 (Euler's number), π ≈ 3.141.",
        explanation="This formula has two parts: a 'Height Scaler' and a 'Decay Factor'.",
        steps=[
            f"Step 1: Identify parameters x={x}, Mean={mu}, StdDev={sigma}.",
            "Step 2: PART 1: Calculate the 'Height Scaler' (Coefficient).",
            f"   >> Formula: 1 / (σ * √2π)",
            f"   >> √2π ≈ {math.sqrt(2*math.pi):.4f}",
            f"   >> Denom = {sigma} * 2.5066 = {sigma * math.sqrt(2*math.pi):.4f}",
            f"   >> Coefficient = 1 / {sigma * math.sqrt(2*math.pi):.4f} = {coeff_part:.4f}",
            "Step 3: PART 2: Calculate the 'Decay Factor' (Exponential).",
            "   >> First, find the Z-score (Standardized distance).",
            f"   >> Z = ({x} - {mu}) / {sigma} = {(x-mu)/sigma:.4f}",
            "Step 4: Square the Z-score.",
            f"   >> Z² = ({(x-mu)/sigma:.4f})^2 = {z_score_sq:.4f}",
            "Step 5: Apply the -0.5 factor.",
            f"   >> -0.5 * {z_score_sq:.4f} = {exponent:.4f}",
            "Step 6: Exponentiate e (e^power).",
            f"   >> e^({exponent:.4f}) = {exp_val:.4f}",
            "Step 7: COMBINE: Multiply Scaler by Decay.",
            f"   >> {coeff_part:.4f} * {exp_val:.4f}",
            f"Step 8: Final Result = {result:.4f}"
        ],
        # ✅ IMPORTANT FIX: answer must be FULL PRECISION float for tests
        answer=result
    )

# ======================================================
#                    ALIASES
# ======================================================

probability_simple = probability

# ======================================================
#                  EXPORTS
# ======================================================

__all__ = [
    "probability",
    "probability_simple",
    "complement",
    "conditional_probability",
    "independent_events",
    "bayes",
    "bernoulli",
    "binomial",
    "normal_pdf",
]
