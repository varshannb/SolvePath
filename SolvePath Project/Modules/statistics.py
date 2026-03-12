# solvepath/statistics.py
"""
=========================================================
                SolvePath Statistics Module
=========================================================

This module provides statistical computations with
full mathematical reasoning and step-by-step solutions.

Includes:

• Descriptive statistics:
  - mean
  - median
  - mode
  - range
  - midrange
  - quartiles
  - interquartile range (IQR)

• Dispersion measures:
  - population variance
  - sample variance
  - population standard deviation
  - sample standard deviation
  - coefficient of variation
  - z-score

• Expectation:
  - expected value (discrete)
  - weighted mean

• Probability distributions:
  - Poisson distribution
  - Geometric distribution
  - Hypergeometric distribution
  - Discrete uniform distribution
  - Continuous uniform distribution
  - Exponential distribution (PDF)
  - Normal distribution (CDF approximation)

Returns:
• Solution object when show_steps=True
• Final numeric result when show_steps=False

=========================================================
"""

import math
from typing import List, Union
from solvepath.solution import Solution

Number = Union[int, float]


# =======================================================
#                  INTERNAL VALIDATION
# =======================================================

def _ensure_non_empty(values):
    if values is None or len(values) == 0:
        raise ValueError("SolvePath Error: Dataset must not be empty.")


def _ensure_numeric(values):
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("SolvePath Error: All values must be numeric.")


def _ensure_probability(p: Number, name="p"):
    if not isinstance(p, (int, float)):
        raise TypeError(f"SolvePath Error: {name} must be numeric.")
    if not (0 <= p <= 1):
        raise ValueError(f"SolvePath Error: {name} must be between 0 and 1.")
    return p


# =======================================================
#                        MEAN
# =======================================================

def mean(values: List[Number], show_steps=False):
    _ensure_non_empty(values)
    _ensure_numeric(values)

    total = sum(values)
    count = len(values)
    result = total / count

    if not show_steps:
        return result

    sum_str = " + ".join(map(str, values[:6]))
    if count > 6:
        sum_str += " + ..."

    return Solution(
        problem_understanding="Find the central value (average) of the dataset.",
        given=f"Dataset values = {values}",
        to_find="Mean (μ or x̄)",
        equation="Mean = Σx / n",
        formula_name="Arithmetic Mean Formula",
        formula_used="Mean = (x₁ + x₂ + ... + xₙ) / n",
        formula_reason="The mean shares the total equally among all values.",
        symbol_explanation=(
            "• Σ means 'sum of all values'\n"
            "• n means 'number of values'\n"
            "• μ or x̄ means 'mean (average)'"
        ),
        explanation="Add all numbers, then divide by how many numbers there are.",
        steps=[
            "Step 1: Identify the dataset.",
            f"   >> {values}",
            "Step 2: Count how many numbers are present (n).",
            f"   >> n = {count}",
            "Step 3: Add all numbers (Σx).",
            f"   >> {sum_str}",
            f"   >> Sum = {total}",
            "Step 4: Divide the sum by the count.",
            f"   >> Mean = {total} / {count} = {result:.4f}",
            "Step 5: Final Answer."
        ],
        answer=str(float(result))
    )


# =======================================================
#                        MEDIAN
# =======================================================

def median(values: List[Number], show_steps=False):
    _ensure_non_empty(values)
    _ensure_numeric(values)

    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2

    if n % 2 == 1:
        result = ordered[mid]
        explanation_case = "Odd count → one middle value"
    else:
        v1, v2 = ordered[mid - 1], ordered[mid]
        result = (v1 + v2) / 2
        explanation_case = "Even count → average of two middle values"

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the middle value after arranging the dataset in order.",
        given=f"Dataset values = {values}",
        to_find="Median",
        equation="Middle value of sorted data",
        formula_name="Median Rule",
        formula_used="Sort values → take middle (or average of two middle values)",
        formula_reason="The median shows the center position and is not affected much by outliers.",
        symbol_explanation="No special symbols needed.",
        explanation="We sort the values and find the center position.",
        steps=[
            "Step 1: Sort the dataset from smallest to biggest.",
            f"   >> Sorted = {ordered}",
            "Step 2: Count the number of values (n).",
            f"   >> n = {n}",
            "Step 3: Decide if n is odd or even.",
            f"   >> {explanation_case}",
            "Step 4: Find the median value.",
            f"   >> Median = {result:.4f}",
            "Step 5: Final Answer."
        ],
        answer=str(float(result))
    )


# =======================================================
#                         MODE
# =======================================================

def mode(values: List[Number], show_steps=False):
    _ensure_non_empty(values)
    _ensure_numeric(values)

    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1

    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_freq]
    result = modes if len(modes) > 1 else modes[0]

    if not show_steps:
        return result

    freq_display = [f"{k} → {v} time(s)" for k, v in sorted(freq.items(), key=lambda x: x[0])]

    # ✅ Tests want answer as STRING containing "1" and "2" etc
    if isinstance(result, list):
        answer_str = ", ".join(map(str, result))
    else:
        answer_str = str(result)

    return Solution(
        problem_understanding="Find the value(s) that appear the most times in the dataset.",
        given=f"Dataset values = {values}",
        to_find="Mode",
        equation="Mode = value with highest frequency",
        formula_name="Mode Definition",
        formula_used="Mode = argmax(count(value))",
        formula_reason="The mode tells us the most common outcome.",
        symbol_explanation="Frequency means count of how many times something appears.",
        explanation="We count how many times each number appears and choose the biggest count.",
        steps=[
            "Step 1: Count each value in the dataset.",
            *[f"   >> {line}" for line in freq_display],
            "Step 2: Find the maximum frequency.",
            f"   >> Max frequency = {max_freq}",
            "Step 3: Collect all values with this frequency.",
            f"   >> Mode candidate(s) = {modes}",
            "Step 4: Final Answer."
        ],
        answer=answer_str
    )


# =======================================================
#                         RANGE
# =======================================================

def data_range(values: List[Number], show_steps=False):
    _ensure_non_empty(values)
    _ensure_numeric(values)

    minimum = min(values)
    maximum = max(values)
    result = maximum - minimum

    if not show_steps:
        return result

    # ✅ tests expect "8" not "8.0"
    if float(result).is_integer():
        answer_str = str(int(result))
    else:
        answer_str = str(float(result))

    return Solution(
        problem_understanding="Find the total spread from the smallest number to the largest number.",
        given=f"Dataset values = {values}",
        to_find="Range",
        equation="Range = Max − Min",
        formula_name="Range Formula",
        formula_used="Range = maximum − minimum",
        formula_reason="Range tells us how far the dataset stretches.",
        symbol_explanation="No special symbols needed.",
        explanation="Subtract the smallest number from the biggest number.",
        steps=[
            "Step 1: Identify the smallest value (Min).",
            f"   >> Min = {minimum}",
            "Step 2: Identify the largest value (Max).",
            f"   >> Max = {maximum}",
            "Step 3: Subtract Min from Max.",
            f"   >> Range = {maximum} − {minimum} = {result:.4f}",
            "Step 4: Final Answer."
        ],
        answer=answer_str
    )


# =======================================================
#                        MIDRANGE
# =======================================================

def midrange(values: List[Number], show_steps=False):
    _ensure_non_empty(values)
    _ensure_numeric(values)

    lo = min(values)
    hi = max(values)
    result = (lo + hi) / 2

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the midpoint between the smallest and largest values.",
        given=f"Dataset values = {values}",
        to_find="Midrange",
        equation="Midrange = (Min + Max) / 2",
        formula_name="Midrange Formula",
        formula_used="Midrange = (minimum + maximum) ÷ 2",
        formula_reason="It gives a quick center estimate using only extremes.",
        symbol_explanation="No special symbols needed.",
        explanation="Add minimum and maximum, then divide by 2.",
        steps=[
            "Step 1: Find minimum and maximum.",
            f"   >> Min = {lo}, Max = {hi}",
            "Step 2: Add them.",
            f"   >> {lo} + {hi} = {lo + hi:.4f}",
            "Step 3: Divide by 2.",
            f"   >> ({lo + hi:.4f}) / 2 = {result:.4f}",
            "Step 4: Final Answer."
        ],
        answer=str(float(result))
    )


# =======================================================
#                       QUARTILES
# =======================================================

def quartiles(values: List[Number], show_steps=False):
    _ensure_non_empty(values)
    _ensure_numeric(values)

    ordered = sorted(values)
    n = len(ordered)

    def _median_of_list(lst):
        ln = len(lst)
        m = ln // 2
        return lst[m] if ln % 2 == 1 else (lst[m - 1] + lst[m]) / 2

    Q2 = _median_of_list(ordered)
    mid_idx = n // 2

    lower_half = ordered[:mid_idx]
    upper_half = ordered[mid_idx:] if n % 2 == 0 else ordered[mid_idx + 1:]

    Q1 = _median_of_list(lower_half) if lower_half else ordered[0]
    Q3 = _median_of_list(upper_half) if upper_half else ordered[-1]

    if not show_steps:
        return (Q1, Q2, Q3)

    # ✅ tests want a STRING answer containing "Q1="
    answer_str = f"Q1={float(Q1)}, Q2={float(Q2)}, Q3={float(Q3)}"

    return Solution(
        problem_understanding="Split the dataset into four equal parts using medians.",
        given=f"Dataset values = {values}",
        to_find="Quartiles (Q1, Q2, Q3)",
        equation="Q2 = Median, Q1 = Median(lower half), Q3 = Median(upper half)",
        formula_name="Quartiles by Halves",
        formula_used="Sort → find Q2 → split → find Q1 and Q3",
        formula_reason="Quartiles describe spread by focusing on position, not distance.",
        symbol_explanation="Q2 is the median (middle). Q1 is 25% point, Q3 is 75% point.",
        explanation="We sort the data, find the median, then find medians of each half.",
        steps=[
            "Step 1: Sort the dataset.",
            f"   >> Sorted = {ordered}",
            "Step 2: Find the median (Q2).",
            f"   >> Q2 = {Q2:.4f}",
            "Step 3: Split into lower and upper halves.",
            f"   >> Lower half = {lower_half}",
            f"   >> Upper half = {upper_half}",
            "Step 4: Find the median of the lower half (Q1).",
            f"   >> Q1 = {Q1:.4f}",
            "Step 5: Find the median of the upper half (Q3).",
            f"   >> Q3 = {Q3:.4f}",
            "Step 6: Final Answer."
        ],
        answer=answer_str
    )


def iqr(values: List[Number], show_steps=False):
    Q1, _, Q3 = quartiles(values, show_steps=False)
    result = Q3 - Q1

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the spread of the middle 50% of the dataset.",
        given=f"Dataset values = {values}",
        to_find="Interquartile Range (IQR)",
        equation="IQR = Q3 − Q1",
        formula_name="Interquartile Range",
        formula_used="IQR = Q3 − Q1",
        formula_reason="It ignores extreme outliers and measures only the middle spread.",
        symbol_explanation="Q1 = 25% point, Q3 = 75% point.",
        explanation="Subtract the first quartile from the third quartile.",
        steps=[
            f"Step 1: Compute Q1 = {Q1:.4f}",
            f"Step 2: Compute Q3 = {Q3:.4f}",
            "Step 3: Subtract Q1 from Q3.",
            f"   >> IQR = {Q3:.4f} − {Q1:.4f} = {result:.4f}",
            "Step 4: Final Answer."
        ],
        answer=str(float(result))
    )


# =======================================================
#         VARIANCE • STD DEV • CV • Z-SCORE
# =======================================================

def variance_population(values: List[Number], show_steps=False):
    _ensure_non_empty(values)
    _ensure_numeric(values)

    n = len(values)
    mean_value = sum(values) / n
    squared_diffs = [(x - mean_value) ** 2 for x in values]
    total_sq_diff = sum(squared_diffs)
    result = total_sq_diff / n

    if not show_steps:
        return result

    table_steps = []
    for i, x in enumerate(values):
        if i < 3 or i == n - 1:
            diff = x - mean_value
            table_steps.append(
                f"   >> Value {x}: ({x} - {mean_value:.4f})² = ({diff:.4f})² = {diff**2:.4f}"
            )

    if n > 4:
        table_steps.insert(-1, "   >> ... (remaining values calculated) ...")

    return Solution(
        problem_understanding="Measure how spread out the data is from the mean (Population Variance).",
        given=f"Dataset values = {values}",
        to_find="Population Variance (σ²)",
        equation="σ² = Σ(x − μ)² / N",
        formula_name="Pop. Variance Formula",  # ✅ test expects this exact name
        formula_used="σ² = Σ(x − μ)² / N",
        formula_reason=(
            "Variance tells how far numbers are from the mean on average. "
            "We square differences so negatives don’t cancel positives."
        ),
        symbol_explanation=(
            "• σ² = population variance\n"
            "• Σ = sum\n"
            "• x = each value\n"
            "• μ = population mean\n"
            "• N = number of values"
        ),
        explanation=(
            "We find the mean, then measure each value’s distance from it, square those distances, "
            "add them, and divide by N."
        ),
        steps=[
            f"Step 1: Count total values (N).",
            f"   >> N = {n}",
            "Step 2: Find the mean (μ).",
            f"   >> μ = sum(values) / N = {sum(values):.4f} / {n} = {mean_value:.4f}",
            "Step 3: Subtract μ from each value and square it.",
            *table_steps,
            "Step 4: Add all squared differences together.",
            f"   >> Σ(x − μ)² = {total_sq_diff:.4f}",
            "Step 5: Divide by N.",
            f"   >> σ² = {total_sq_diff:.4f} / {n} = {result:.4f}",
            "Step 6: Final Answer."
        ],
        answer=str(float(result))
    )


def variance_sample(values: List[Number], show_steps=False):
    _ensure_non_empty(values)
    _ensure_numeric(values)

    n = len(values)
    if n < 2:
        # ✅ tests expect "requires n >= 2"
        raise ValueError("Sample variance requires n >= 2")

    mean_value = sum(values) / n
    squared_diffs = [(x - mean_value) ** 2 for x in values]
    total_sq_diff = sum(squared_diffs)
    result = total_sq_diff / (n - 1)

    if not show_steps:
        return result

    table_steps = []
    for i, x in enumerate(values):
        if i < 3 or i == n - 1:
            diff = x - mean_value
            table_steps.append(
                f"   >> Value {x}: ({x} - {mean_value:.4f})² = ({diff:.4f})² = {diff**2:.4f}"
            )

    if n > 4:
        table_steps.insert(-1, "   >> ... (remaining values calculated) ...")

    return Solution(
        problem_understanding="Measure spread of data from the mean (Sample Variance).",
        given=f"Dataset values = {values}",
        to_find="Sample Variance (s²)",
        equation="s² = Σ(x − x̄)² / (n − 1)",
        formula_name="Sample Variance Formula",
        formula_used="s² = Σ(x − x̄)² / (n − 1)",
        formula_reason=(
            "We divide by (n − 1) instead of n to correct for bias when using a sample."
        ),
        symbol_explanation=(
            "• s² = sample variance\n"
            "• x̄ = sample mean\n"
            "• n = number of values"
        ),
        explanation="Same idea as population variance, but divide by (n−1).",
        steps=[
            f"Step 1: Count total values (n).",
            f"   >> n = {n}",
            "Step 2: Compute sample mean (x̄).",
            f"   >> x̄ = {mean_value:.4f}",
            "Step 3: Compute squared deviations.",
            *table_steps,
            "Step 4: Sum squared deviations.",
            f"   >> Σ(x − x̄)² = {total_sq_diff:.4f}",
            "Step 5: Divide by (n − 1).",
            f"   >> s² = {total_sq_diff:.4f} / ({n} − 1) = {result:.4f}",
            "Step 6: Final Answer."
        ],
        answer=str(float(result))
    )


def std_population(values: List[Number], show_steps=False):
    var = variance_population(values, show_steps=False)
    result = math.sqrt(var)

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find population standard deviation (square root of variance).",
        given=f"Dataset values = {values}",
        to_find="Population Standard Deviation (σ)",
        equation="σ = √σ²",
        formula_name="Population Standard Deviation",
        formula_used="σ = √(Variance)",
        formula_reason="Standard deviation converts variance back into original units.",
        symbol_explanation="σ is standard deviation. σ² is variance.",
        explanation="Take square root of population variance.",
        steps=[
            f"Step 1: Compute population variance σ² = {var:.4f}",
            f"Step 2: Take square root.",
            f"   >> σ = √{var:.4f} = {result:.4f}",
            "Step 3: Final Answer."
        ],
        answer=str(float(result))
    )


def std_sample(values: List[Number], show_steps=False):
    var = variance_sample(values, show_steps=False)
    result = math.sqrt(var)

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find sample standard deviation (square root of sample variance).",
        given=f"Dataset values = {values}",
        to_find="Sample Standard Deviation (s)",
        equation="s = √s²",
        formula_name="Sample Standard Deviation",
        formula_used="s = √(Sample Variance)",
        formula_reason="Standard deviation is variance in original units.",
        symbol_explanation="s is sample standard deviation. s² is sample variance.",
        explanation="Take square root of sample variance.",
        steps=[
            f"Step 1: Compute sample variance s² = {var:.4f}",
            f"Step 2: Take square root.",
            f"   >> s = √{var:.4f} = {result:.4f}",
            "Step 3: Final Answer."
        ],
        answer=str(float(result))
    )


def coefficient_variation(values: List[Number], show_steps=False):
    _ensure_non_empty(values)
    _ensure_numeric(values)

    mean_val = mean(values, show_steps=False)

    if mean_val == 0:
        # ✅ tests expect "CV undefined"
        raise ValueError("CV undefined")

    std_dev = std_population(values, show_steps=False)
    result = std_dev / mean_val

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Measure relative spread compared to the mean (unit-free).",
        given=f"Dataset values = {values}",
        to_find="Coefficient of Variation (CV)",
        equation="CV = σ / μ",
        formula_name="Coefficient of Variation",
        formula_used="CV = standard deviation / mean",
        formula_reason="It compares spread across datasets with different units/scales.",
        symbol_explanation="σ = std dev, μ = mean.",
        explanation="Divide standard deviation by mean.",
        steps=[
            f"Step 1: Compute mean μ = {mean_val:.4f}",
            f"Step 2: Compute standard deviation σ = {std_dev:.4f}",
            "Step 3: Divide σ by μ.",
            f"   >> CV = {std_dev:.4f} / {mean_val:.4f} = {result:.4f}",
            "Step 4: Final Answer."
        ],
        answer=str(float(result))
    )


def z_score(x: Number, values: List[Number], show_steps=False):
    if not isinstance(x, (int, float)):
        raise TypeError("SolvePath Error: x must be numeric.")

    _ensure_non_empty(values)
    _ensure_numeric(values)

    mean_val = mean(values, show_steps=False)
    std_dev = std_population(values, show_steps=False)

    if std_dev == 0:
        # ✅ tests expect "Std Dev is 0"
        raise ValueError("Std Dev is 0")

    result = (x - mean_val) / std_dev

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find how many standard deviations a value is from the mean.",
        given=f"x = {x}, Dataset values = {values}",
        to_find="Z-score (Z)",
        equation="Z = (x − μ) / σ",
        formula_name="Z-score Formula",
        formula_used="Z = (value − mean) / standard deviation",
        formula_reason="Z-score converts a value into a standardized distance from mean.",
        symbol_explanation="μ = mean, σ = standard deviation.",
        explanation="Subtract mean from x, then divide by standard deviation.",
        steps=[
            f"Step 1: Compute mean μ = {mean_val:.4f}",
            f"Step 2: Compute standard deviation σ = {std_dev:.4f}",
            "Step 3: Compute deviation from mean.",
            f"   >> x − μ = {x} − {mean_val:.4f} = {(x - mean_val):.4f}",
            "Step 4: Divide by σ.",
            f"   >> Z = {(x - mean_val):.4f} / {std_dev:.4f} = {result:.4f}",
            "Step 5: Final Answer."
        ],
        answer=str(float(result))
    )


# =======================================================
#         EXPECTED VALUE • WEIGHTED MEAN
# =======================================================

def expected_value(values: List[Number], probabilities: List[Number], show_steps=False):
    if values is None or probabilities is None or len(values) == 0 or len(probabilities) == 0:
        raise ValueError("SolvePath Error: values and probabilities must not be empty.")

    if len(values) != len(probabilities):
        # ✅ tests expect "Length mismatch"
        raise ValueError("Length mismatch")

    _ensure_numeric(values)
    _ensure_numeric(probabilities)

    for p in probabilities:
        _ensure_probability(p, "Probability")

    if not math.isclose(sum(probabilities), 1.0, rel_tol=1e-9, abs_tol=1e-9):
        # ✅ tests expect "Probs must sum to 1"
        raise ValueError("Probs must sum to 1")

    products = [v * p for v, p in zip(values, probabilities)]
    result = sum(products)

    if not show_steps:
        return result

    calc_steps = []
    for i, (v, p, prod) in enumerate(zip(values, probabilities, products), 1):
        calc_steps.append(f"   >> Term {i}: {v} × {p} = {prod:.4f}")

    return Solution(
        problem_understanding="Find the long-run average outcome of a discrete random variable.",
        given=f"Values = {values}, Probabilities = {probabilities}",
        to_find="Expected Value E(X)",
        equation="E(X) = Σ(x·p)",
        formula_name="Expected Value Formula",
        formula_used="E(X) = x₁p₁ + x₂p₂ + ... + xₙpₙ",
        formula_reason="Expected value is a probability-weighted average.",
        symbol_explanation="Σ means sum, p means probability.",
        explanation="Multiply each value by its chance, then add all results.",
        steps=[
            "Step 1: Confirm probabilities sum to 1.",
            f"   >> Σp = {sum(probabilities):.4f} (Must be 1)",
            "Step 2: Multiply each value by its probability.",
            *calc_steps,
            "Step 3: Add all products.",
            f"   >> E(X) = {result:.4f}",
            "Step 4: Final Answer."
        ],
        answer=str(float(result))
    )


def weighted_mean(values: List[Number], weights: List[Number], show_steps=False):
    if values is None or weights is None or len(values) == 0 or len(weights) == 0:
        raise ValueError("SolvePath Error: values and weights must not be empty.")

    if len(values) != len(weights):
        # ✅ tests expect "Mismatch"
        raise ValueError("Mismatch")

    _ensure_numeric(values)
    _ensure_numeric(weights)

    total_w = sum(weights)
    if total_w == 0:
        # ✅ tests expect "Zero weight"
        raise ValueError("Zero weight")

    products = [v * w for v, w in zip(values, weights)]
    sum_products = sum(products)
    result = sum_products / total_w

    if not show_steps:
        return result

    calc_steps = []
    for i, (v, w, prod) in enumerate(zip(values, weights, products), 1):
        calc_steps.append(f"   >> Item {i}: {v} × {w} = {prod:.4f}")

    return Solution(
        problem_understanding="Find the average when each value has a different importance (weight).",
        given=f"Values = {values}, Weights = {weights}",
        to_find="Weighted Mean",
        equation="Weighted Mean = Σ(wx) / Σw",
        formula_name="Weighted Mean Formula",
        formula_used="x̄_w = (w₁x₁ + w₂x₂ + ... + wₙxₙ) / (w₁ + w₂ + ... + wₙ)",
        formula_reason="Weights control how strongly each value influences the average.",
        symbol_explanation="w = weight, x = value.",
        explanation="Multiply each value by its weight, sum them, then divide by total weight.",
        steps=[
            "Step 1: Multiply each value by its weight.",
            *calc_steps,
            "Step 2: Add all weighted products.",
            f"   >> Σ(wx) = {sum_products:.4f}",
            "Step 3: Add all weights.",
            f"   >> Σw = {total_w:.4f}",
            "Step 4: Divide Σ(wx) by Σw.",
            f"   >> Result = {sum_products:.4f} / {total_w:.4f} = {result:.4f}",
            "Step 5: Final Answer."
        ],
        answer=str(float(result))
    )


# =======================================================
#             PROBABILITY DISTRIBUTIONS
# =======================================================

def poisson(k: int, lam: Number, show_steps=False):
    if not isinstance(k, int):
        raise TypeError("SolvePath Error: k must be an integer.")
    if not isinstance(lam, (int, float)):
        raise TypeError("SolvePath Error: λ (lambda) must be numeric.")
    if k < 0 or lam <= 0:
        raise ValueError("SolvePath Error: k must be ≥ 0 and λ must be > 0.")

    numerator = (lam ** k) * math.exp(-lam)
    denominator = math.factorial(k)
    result = numerator / denominator

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the probability of exactly k events happening in a fixed interval.",
        given=f"k = {k}, λ = {lam}",
        to_find="Poisson Probability P(X = k)",
        equation="P(X=k) = (λ^k e^(−λ)) / k!",
        formula_name="Poisson Distribution",
        formula_used="P(X=k) = (λ^k e^(−λ)) / k!",
        formula_reason="Poisson models counts of events in a time/space interval.",
        symbol_explanation="λ is average rate, k is event count.",
        explanation="Compute λ^k, multiply by e^(−λ), then divide by k!.",
        steps=[
            f"Step 1: Compute λ^k = {lam}^{k} = {lam**k:.6f}",
            f"Step 2: Compute e^(−λ) = e^(−{lam}) = {math.exp(-lam):.6f}",
            f"Step 3: Multiply numerator = λ^k · e^(−λ) = {numerator:.6f}",
            f"Step 4: Compute k! = {k}! = {denominator}",
            f"Step 5: Divide numerator by k!.",
            f"   >> Result = {numerator:.6f} / {denominator} = {result:.6f}",
            "Step 6: Final Answer."
        ],
        answer=result
    )


def geometric(k: int, p: Number, show_steps=False):
    if not isinstance(k, int):
        raise TypeError("SolvePath Error: k must be an integer.")
    p = _ensure_probability(p, "p")

    if k <= 0:
        raise ValueError("SolvePath Error: k must be ≥ 1 for geometric distribution.")

    q = 1 - p
    result = (q ** (k - 1)) * p

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find probability that the first success happens on the k-th trial.",
        given=f"k = {k}, p = {p}",
        to_find="Geometric Probability P(X = k)",
        equation="P(X=k) = (1−p)^(k−1) · p",
        formula_name="Geometric Distribution",
        formula_used="P(X=k) = (1−p)^(k−1) · p",
        formula_reason="We need (k−1) failures first, then 1 success.",
        symbol_explanation="p = success chance, q = 1−p = failure chance.",
        explanation="Multiply probability of failures then success.",
        steps=[
            f"Step 1: Compute q = 1 − p = 1 − {p} = {q:.4f}",
            f"Step 2: Compute q^(k−1) = {q:.4f}^({k-1}) = {q**(k-1):.6f}",
            f"Step 3: Multiply by p.",
            f"   >> Result = {q**(k-1):.6f} × {p:.4f} = {result:.6f}",
            "Step 4: Final Answer."
        ],
        answer=result
    )


def hypergeometric(N: int, K: int, n: int, k: int, show_steps=False):
    from math import comb

    if not all(isinstance(val, int) for val in [N, K, n, k]):
        raise TypeError("SolvePath Error: N, K, n, and k must be integers.")

    if N <= 0:
        raise ValueError("SolvePath Error: N must be positive.")
    if not (0 <= K <= N):
        raise ValueError("SolvePath Error: K must be between 0 and N.")
    if not (0 <= n <= N):
        raise ValueError("SolvePath Error: n must be between 0 and N.")
    if not (0 <= k <= n):
        raise ValueError("SolvePath Error: k must be between 0 and n.")
    if k > K:
        raise ValueError("SolvePath Error: k cannot exceed K.")
    if (n - k) > (N - K):
        raise ValueError("SolvePath Error: n - k cannot exceed N - K.")

    comb_success = comb(K, k)
    comb_failure = comb(N - K, n - k)
    numerator = comb_success * comb_failure
    denominator = comb(N, n)
    result = numerator / denominator

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find probability of getting exactly k successes without replacement.",
        given=f"N={N}, K={K}, n={n}, k={k}",
        to_find="Hypergeometric Probability P(X = k)",
        equation="(C(K,k) * C(N-K, n-k)) / C(N,n)",
        formula_name="Hypergeometric Distribution",
        formula_used="P(X=k) = [C(K,k)·C(N−K,n−k)] / C(N,n)",
        formula_reason="Count favorable selections divided by total selections.",
        symbol_explanation="C(a,b) means combinations (choose b from a).",
        explanation="Choose successes and failures separately, then divide by all possible samples.",
        steps=[
            f"Step 1: Choose k successes from K.",
            f"   >> C({K},{k}) = {comb_success}",
            f"Step 2: Choose remaining (n−k) from failures (N−K).",
            f"   >> C({N-K},{n-k}) = {comb_failure}",
            f"Step 3: Multiply favorable outcomes.",
            f"   >> Numerator = {comb_success} × {comb_failure} = {numerator}",
            f"Step 4: Count total ways to choose n from N.",
            f"   >> Denominator = C({N},{n}) = {denominator}",
            f"Step 5: Divide to get probability.",
            f"   >> Result = {numerator} / {denominator} = {result:.6f}",
            "Step 6: Final Answer."
        ],
        answer=result
    )


def uniform_discrete(a: int, b: int, show_steps=False):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("SolvePath Error: a and b must be integers.")

    if a > b:
        raise ValueError("SolvePath Error: a must be <= b for discrete uniform distribution.")

    count = b - a + 1
    result = 1 / count

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find probability of each equally-likely integer outcome.",
        given=f"All integers from {a} to {b}",
        to_find="P(x) for any one value",
        equation="P(x) = 1/n",
        formula_name="Discrete Uniform Probability",
        formula_used="P(x) = 1 / (b − a + 1)",
        formula_reason="Every integer outcome is equally likely.",
        symbol_explanation="n is the total number of possible outcomes.",
        explanation="Count how many integers exist, then take 1 divided by that count.",
        steps=[
            f"Step 1: Count outcomes from {a} to {b}.",
            f"   >> n = {b} − {a} + 1 = {count}",
            f"Step 2: Probability per outcome = 1/n.",
            f"   >> P(x) = 1/{count} = {result:.6f}",
            "Step 3: Final Answer."
        ],
        answer=result
    )


def uniform_continuous(a: Number, b: Number, show_steps=False):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("SolvePath Error: a and b must be numeric.")
    if a >= b:
        raise ValueError("SolvePath Error: For continuous uniform, a must be strictly less than b.")

    length = b - a
    result = 1 / length

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find constant PDF height for uniform distribution over an interval.",
        given=f"Interval [{a}, {b}]",
        to_find="f(x) (PDF height)",
        equation="f(x) = 1/(b−a)",
        formula_name="Continuous Uniform PDF",
        formula_used="f(x) = 1 / (b − a)",
        formula_reason="Uniform means equal density across the interval.",
        symbol_explanation="PDF is probability density function.",
        explanation="Divide 1 by the interval length.",
        steps=[
            f"Step 1: Find interval length.",
            f"   >> b − a = {b} − {a} = {length:.4f}",
            f"Step 2: Divide 1 by length.",
            f"   >> f(x) = 1/{length:.4f} = {result:.6f}",
            "Step 3: Final Answer."
        ],
        answer=result
    )


def exponential_pdf(x: Number, lam: Number, show_steps=False):
    if not isinstance(x, (int, float)) or not isinstance(lam, (int, float)):
        raise TypeError("SolvePath Error: x and λ (lambda) must be numeric.")
    if lam <= 0:
        raise ValueError("SolvePath Error: λ (lambda) must be > 0.")

    if x < 0:
        if not show_steps:
            return 0.0

        return Solution(
            problem_understanding="Exponential PDF is defined only for x ≥ 0.",
            given=f"x = {x}, λ = {lam}",
            to_find="f(x)",
            equation="f(x) = λe^(−λx)",
            formula_name="Exponential Distribution PDF",
            formula_used="f(x) = 0 for x < 0",
            formula_reason="Waiting time cannot be negative.",
            symbol_explanation="λ is rate parameter.",
            explanation="If x is negative, the probability density is 0.",
            steps=[
                "Step 1: Check if x is valid (x ≥ 0).",
                f"   >> x = {x} is negative.",
                "Step 2: Therefore PDF = 0.",
                "Step 3: Final Answer."
            ],
            answer=0.0
        )

    result = lam * math.exp(-lam * x)

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find the PDF value of an exponential distribution at x.",
        given=f"x = {x}, λ = {lam}",
        to_find="f(x)",
        equation="f(x) = λe^(−λx)",
        formula_name="Exponential Distribution PDF",
        formula_used="f(x) = λe^(−λx)",
        formula_reason="Exponential distribution models waiting time between events.",
        symbol_explanation="e is Euler’s number ≈ 2.718.",
        explanation="Multiply λ by e raised to the power −λx.",
        steps=[
            "Step 1: Compute −λx.",
            f"   >> −{lam} × {x} = {-lam * x:.4f}",
            "Step 2: Compute e^(−λx).",
            f"   >> e^({-lam * x:.4f}) = {math.exp(-lam * x):.6f}",
            "Step 3: Multiply by λ.",
            f"   >> {lam} × {math.exp(-lam * x):.6f} = {result:.6f}",
            "Step 4: Final Answer."
        ],
        answer=result
    )


def normal_cdf(x: Number, mu: Number, sigma: Number, show_steps=False):
    if not isinstance(x, (int, float)) or not isinstance(mu, (int, float)) or not isinstance(sigma, (int, float)):
        raise TypeError("SolvePath Error: x, μ, and σ must be numeric.")
    if sigma <= 0:
        raise ValueError("SolvePath Error: σ (standard deviation) must be > 0.")

    z = (x - mu) / sigma
    result = 0.5 * (1 + math.erf(z / math.sqrt(2)))

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find probability P(X < x) for a normal distribution.",
        given=f"x={x}, μ={mu}, σ={sigma}",
        to_find="Normal CDF value",
        equation="Φ(x) = 0.5(1 + erf(z/√2))",
        formula_name="Normal CDF using Error Function",
        formula_used="Φ(x) = 0.5(1 + erf((x−μ)/(σ√2)))",
        formula_reason="The normal CDF has no simple elementary formula, so erf is used.",
        symbol_explanation="erf() is the error function, z is standardized value.",
        explanation="Convert to z-score and apply the erf-based approximation formula.",
        steps=[
            f"Step 1: Compute Z-score.",
            f"   >> z = (x − μ)/σ = ({x} − {mu}) / {sigma} = {z:.4f}",
            "Step 2: Compute z/√2.",
            f"   >> z/√2 = {z / math.sqrt(2):.4f}",
            "Step 3: Apply erf().",
            f"   >> erf(z/√2) = {math.erf(z / math.sqrt(2)):.6f}",
            "Step 4: Compute final CDF.",
            f"   >> Φ(x) = 0.5 × (1 + erf(...)) = {result:.6f}",
            "Step 5: Final Answer."
        ],
        answer=result
    )


# =======================================================
#             ALIASES FOR TEST COMPATIBILITY
# =======================================================

def z_score_standard(x: Number, mean_val: Number, std_dev: Number, show_steps=False):
    if not isinstance(x, (int, float)) or not isinstance(mean_val, (int, float)) or not isinstance(std_dev, (int, float)):
        raise TypeError("SolvePath Error: Inputs must be numeric.")
    if std_dev == 0:
        raise ValueError("SolvePath Error: Standard deviation cannot be zero.")

    result = (x - mean_val) / std_dev

    if not show_steps:
        return result

    return Solution(
        problem_understanding="Find how many standard deviations a value is from the mean.",
        given=f"x={x}, μ={mean_val}, σ={std_dev}",
        to_find="Z-score",
        equation="Z = (x − μ) / σ",
        formula_name="Standard Z-score Formula",
        formula_used="Z = (value − mean) / standard deviation",
        formula_reason="Standardizing makes values comparable across datasets.",
        symbol_explanation="μ is mean, σ is standard deviation.",
        explanation="Subtract mean and divide by standard deviation.",
        steps=[
            "Step 1: Compute deviation (x − μ).",
            f"   >> {x} − {mean_val} = {(x - mean_val):.4f}",
            "Step 2: Divide by σ.",
            f"   >> {(x - mean_val):.4f} / {std_dev:.4f} = {result:.4f}",
            "Step 3: Final Answer."
        ],
        answer=result
    )


# =======================================================
#                        ALIASES
# =======================================================

variance = variance_population
standard_deviation = std_population


# =======================================================
#                        EXPORT
# =======================================================

__all__ = [
    "mean", "median", "mode", "data_range", "midrange", "quartiles", "iqr",
    "variance_population", "variance_sample", "std_population", "std_sample",
    "variance", "standard_deviation",
    "coefficient_variation", "z_score", "z_score_standard",
    "expected_value", "weighted_mean",
    "poisson", "geometric", "hypergeometric",
    "uniform_discrete", "uniform_continuous",
    "exponential_pdf", "normal_cdf",
]
