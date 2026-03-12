# solvepath/activation.py
"""
==========================================================
            SolvePath Activation Functions Module
==========================================================

Includes step-by-step explanations for:

• Sigmoid
• ReLU
• Leaky ReLU
• Tanh
• Softplus
• Swish
• GELU
• Softmax

Also includes NUMERICALLY STABLE variants (non-breaking):

• sigmoid_stable
• softplus_stable
• softmax_stable
• swish_stable
• gelu_stable

==========================================================
"""

# solvepath/activation.py
"""
==========================================================
              SolvePath Activation Functions Module
==========================================================

Includes HIGHLY DETAILED, TUTOR-STYLE step-by-step explanations for:

• Sigmoid & Stable Sigmoid
• ReLU & Leaky ReLU
• Tanh
• Softplus & Stable Softplus
• Swish & Stable Swish
• GELU
• Softmax & Stable Softmax

==========================================================
"""

import math
from typing import List, Union
from solvepath.solution import Solution

# ==========================================================
# INTERNAL VALIDATION HELPERS
# ==========================================================

def _validate_number(x, name="Input"):
    if not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be a number (int or float).")

def _validate_list(x, name="Input"):
    if not isinstance(x, (list, tuple)) or not all(isinstance(i, (int, float)) for i in x):
        raise TypeError(f"{name} must be a list of numbers.")

# ==========================================================
# SIGMOID
# ==========================================================

def sigmoid(x: float, show_steps=False):
    _validate_number(x, "x")
    
    # Calculation
    neg_x = -x
    exp_val = math.exp(neg_x)
    denom = 1 + exp_val
    result = 1 / denom

    if not show_steps:
        return result

    return Solution(
        given=f"Input value x = {x}",
        to_find="The sigmoid activation value σ(x)",
        equation="σ(x) = 1 / (1 + e⁻ˣ)",
        formula_name="Sigmoid Function",
        formula_used="σ(x) = 1 / (1 + e⁻ˣ)",
        formula_reason="Sigmoid is used to transform any real number into a probability (0 to 1).",
        symbol_explanation="e is Euler's number (approx 2.718). It is the base of natural logarithms.",
        explanation="We treat the input as a negative exponent to decay the value, then normalize it.",
        steps=[
            f"Step 1: Prepare the exponent.\n   The formula requires -x. Since x is {x}, then -x = {neg_x}.",
            f"Step 2: Calculate the exponential term (e^-x).\n   We calculate e raised to the power of {neg_x}.\n   e^({neg_x}) ≈ {exp_val:.6f}",
            f"Step 3: Calculate the denominator.\n   Add 1 to the result from Step 2.\n   1 + {exp_val:.6f} = {denom:.6f}",
            f"Step 4: Final Division.\n   Divide 1 by the denominator to squash the result.\n   1 / {denom:.6f} = {result:.6f}"
        ],
        answer=result
    )

def sigmoid_stable(x: float, show_steps=False):
    _validate_number(x, "x")
    
    if x >= 0:
        branch = "Positive branch (Standard Formula)"
        explanation = "Since x is positive (or zero), e^-x will be small (between 0 and 1). This is safe to compute."
        neg_x = -x
        exp_val = math.exp(neg_x)
        denom = 1 + exp_val
        result = 1 / denom
        formula_used = "1 / (1 + e⁻ˣ)"
        step2_desc = f"e^({neg_x}) = {exp_val:.6f}"
    else:
        branch = "Negative branch (Alternative Formula)"
        explanation = "Since x is negative, e^-x would be huge (overflow risk). We rewrite the formula to use e^x instead, which will be tiny and safe."
        exp_pos = math.exp(x)
        denom = 1 + exp_pos
        result = exp_pos / denom
        formula_used = "eˣ / (1 + eˣ)"
        step2_desc = f"e^({x}) = {exp_pos:.6f}"

    if not show_steps:
        return result

    return Solution(
        given=f"Input value x = {x}",
        to_find="Numerically Stable Sigmoid",
        equation="σ(x) = 1 / (1 + e⁻ˣ)",
        formula_name="Stable Sigmoid",
        formula_used=formula_used,
        formula_reason="To prevent computer errors (OverflowError) when handling very large or very small numbers.",
        explanation=explanation,
        steps=[
            f"Step 1: Check the sign of x.\n   x is {x}. We select the: {branch}.",
            f"Step 2: Calculate the safe exponential.\n   {step2_desc}",
            f"Step 3: Calculate the denominator.\n   1 + {step2_desc.split('=')[1].strip()} = {denom:.6f}",
            f"Step 4: Final Division.\n   Result = {result:.6f}"
        ],
        answer=result
    )

# ==========================================================
# RELU
# ==========================================================

def relu(x: float, show_steps=False):
    _validate_number(x, "x")
    
    result = max(0.0, float(x))

    if not show_steps:
        return result

    logic_msg = "Since the input is positive, we keep it exactly as it is." if x > 0 else "Since the input is negative (or zero), we replace it with 0."

    return Solution(
        given=f"Input value x = {x}",
        to_find="ReLU Output",
        equation="ReLU(x) = max(0, x)",
        formula_name="Rectified Linear Unit (ReLU)",
        formula_used="max(0, x)",
        formula_reason="ReLU introduces non-linearity by deactivating neurons with negative input. It is computationally very fast.",
        explanation="Think of it as a gate: Positive numbers pass through; negative numbers are blocked.",
        steps=[
            f"Step 1: Inspect the input value x = {x}.",
            f"Step 2: Compare with zero.\n   Is {x} > 0? -> {'Yes' if x > 0 else 'No'}.",
            f"Step 3: Apply the logic.\n   {logic_msg}",
            f"Step 4: Final Result.\n   {result}"
        ],
        answer=result
    )

# ==========================================================
# LEAKY RELU
# ==========================================================

def leaky_relu(x: float, alpha=0.01, show_steps=False):
    _validate_number(x, "x")
    
    if x > 0:
        result = x
        step_logic = [
            f"Step 1: Check if x > 0.\n   {x} is positive.",
            "Step 2: Apply Positive Rule.\n   Return x unchanged.",
            f"Step 3: Final Result.\n   {result}"
        ]
    else:
        result = alpha * x
        step_logic = [
            f"Step 1: Check if x > 0.\n   {x} is negative.",
            f"Step 2: Apply Negative Rule.\n   Multiply x by alpha ({alpha}).",
            f"   Calculation: {alpha} * {x} = {result}",
            f"Step 3: Final Result.\n   {result}"
        ]

    if not show_steps:
        return result

    return Solution(
        given=f"x = {x}, alpha (leak slope) = {alpha}",
        to_find="Leaky ReLU Output",
        equation="f(x) = x (if x>0) | αx (if x≤0)",
        formula_name="Leaky ReLU",
        formula_used="max(αx, x)",
        formula_reason="Standard ReLU 'kills' negative neurons completely. Leaky ReLU allows a small 'trickle' of information to flow back, which helps learning.",
        explanation="We apply a linear function. If positive, slope is 1. If negative, slope is alpha (usually 0.01).",
        steps=step_logic,
        answer=result
    )

# ==========================================================
# TANH
# ==========================================================

def tanh_activation(x: float, show_steps=False):
    _validate_number(x, "x")
    
    exp_pos = math.exp(x)
    exp_neg = math.exp(-x)
    numerator = exp_pos - exp_neg
    denominator = exp_pos + exp_neg
    result = numerator / denominator

    if not show_steps:
        return result

    return Solution(
        given=f"Input x = {x}",
        to_find="Hyperbolic Tangent tanh(x)",
        equation="tanh(x) = (eˣ - e⁻ˣ) / (eˣ + e⁻ˣ)",
        formula_name="Hyperbolic Tangent",
        formula_used="(eˣ - e⁻ˣ) / (eˣ + e⁻ˣ)",
        formula_reason="Unlike Sigmoid (0 to 1), Tanh outputs (-1 to 1), which centers the data around zero. This is often better for optimization.",
        explanation="It is the ratio of the difference between the growth and decay exponentials to their sum.",
        steps=[
            f"Step 1: Calculate Positive Exponential (e^x).\n   e^({x}) ≈ {exp_pos:.5f}",
            f"Step 2: Calculate Negative Exponential (e^-x).\n   e^(-{x}) ≈ {exp_neg:.5f}",
            f"Step 3: Calculate the Numerator (Difference).\n   {exp_pos:.5f} - {exp_neg:.5f} = {numerator:.5f}",
            f"Step 4: Calculate the Denominator (Sum).\n   {exp_pos:.5f} + {exp_neg:.5f} = {denominator:.5f}",
            f"Step 5: Divide to find ratio.\n   {numerator:.5f} / {denominator:.5f} = {result:.6f}"
        ],
        answer=result
    )

# ==========================================================
# SOFTPLUS
# ==========================================================

def softplus(x: float, show_steps=False):
    _validate_number(x, "x")
    
    exp_val = math.exp(x)
    inner = 1 + exp_val
    result = math.log(inner)

    if not show_steps:
        return result

    return Solution(
        given=f"Input x = {x}",
        to_find="Softplus(x)",
        equation="y = ln(1 + eˣ)",
        formula_name="Softplus Function",
        formula_used="ln(1 + eˣ)",
        formula_reason="It is a smooth, differentiable approximation of ReLU. Useful when you need positive outputs but also need to calculate gradients everywhere.",
        explanation="We transform the input into a positive domain using exponentiation, add a bias of 1, and then revert the scale using the natural logarithm.",
        steps=[
            f"Step 1: Calculate e^x.\n   e^({x}) ≈ {exp_val:.5f}",
            f"Step 2: Add 1 to the result.\n   1 + {exp_val:.5f} = {inner:.5f}",
            f"Step 3: Take the Natural Logarithm (ln).\n   The natural log of {inner:.5f} is approximately {result:.6f}.",
            f"Step 4: Final Answer.\n   {result:.6f}"
        ],
        answer=result
    )

def softplus_stable(x: float, show_steps=False):
    _validate_number(x, "x")
    
    # Formula: max(x,0) + ln(1 + e^(-|x|))
    max_part = max(x, 0)
    abs_neg = -abs(x)
    exp_small = math.exp(abs_neg)
    log_part = math.log1p(exp_small) 
    result = max_part + log_part

    if not show_steps:
        return result

    return Solution(
        given=f"Input x = {x}",
        to_find="Stable Softplus(x)",
        equation="y ≈ max(x,0) + ln(1 + e^(-|x|))",
        formula_name="Numerically Stable Softplus",
        formula_used="max(x,0) + log1p(e^(-|x|))",
        formula_reason="Standard Softplus crashes if x is very large (e.g., x=1000) because e^1000 is too big for a computer.",
        explanation="We use a mathematical trick: separating the large linear part from the small decaying part.",
        steps=[
            f"Step 1: Identify the dominant linear part.\n   max({x}, 0) = {max_part}",
            f"Step 2: Calculate the correction term using negative absolute value.\n   -abs({x}) = {abs_neg}\n   e^({abs_neg}) ≈ {exp_small:.8f}",
            f"Step 3: Calculate log(1 + correction).\n   ln(1 + {exp_small:.8f}) ≈ {log_part:.8f}",
            f"Step 4: Add the parts together.\n   {max_part} + {log_part:.8f} = {result:.6f}"
        ],
        answer=result
    )

# ==========================================================
# SWISH
# ==========================================================

def swish(x: float, show_steps=False):
    _validate_number(x, "x")
    
    sig_val = sigmoid(x)
    result = x * sig_val

    if not show_steps:
        return result

    return Solution(
        given=f"Input x = {x}",
        to_find="Swish(x)",
        equation="y = x · σ(x)",
        formula_name="Swish Activation",
        formula_used="x * Sigmoid(x)",
        formula_reason="Swish is 'self-gated'. It allows large positive values to pass, sets large negative values to zero, but allows a small dip into negative values for small negative inputs.",
        explanation="We calculate the sigmoid of the input, and then multiply the original input by that sigmoid value.",
        steps=[
            f"Step 1: Calculate the Sigmoid of x.\n   σ({x}) ≈ {sig_val:.5f} (This acts as a 'gate' between 0 and 1)",
            f"Step 2: Multiply the original input by the gate.\n   Input ({x}) * Gate ({sig_val:.5f})",
            f"Step 3: Final Result.\n   {result:.6f}"
        ],
        answer=result
    )

def swish_stable(x: float, show_steps=False):
    _validate_number(x, "x")
    sig_val = sigmoid_stable(x)
    result = x * sig_val
    
    if not show_steps:
        return result
        
    return Solution(
        given=f"x = {x}",
        to_find="Stable Swish(x)",
        equation="y = x · σ_stable(x)",
        formula_name="Stable Swish",
        formula_used="x * Sigmoid_Stable(x)",
        formula_reason="Ensures the sigmoid component calculation is safe for all numbers.",
        steps=[
            "Step 1: Calculate Stable Sigmoid (see Sigmoid Stable logic).",
            f"   σ_stable({x}) = {sig_val:.5f}",
            f"Step 2: Multiply by x.\n   {x} * {sig_val:.5f} = {result:.6f}"
        ],
        answer=result
    )

# ==========================================================
# GELU
# ==========================================================

def gelu(x: float, show_steps=False):
    _validate_number(x, "x")
    
    # Constants
    SQRT_2_OVER_PI = 0.7978845608
    COEFF = 0.044715

    # Inner calc
    cubic = x ** 3
    inner_term = x + (COEFF * cubic)
    scaled_inner = SQRT_2_OVER_PI * inner_term
    tanh_val = math.tanh(scaled_inner)
    
    result = 0.5 * x * (1 + tanh_val)

    if not show_steps:
        return result

    return Solution(
        given=f"x = {x}",
        to_find="GELU Output",
        equation="GELU(x) ≈ 0.5x(1 + tanh(√2/π * (x + 0.044715x³)))",
        formula_name="Gaussian Error Linear Unit (Tanh Approximation)",
        formula_used="Standard Approximation used in BERT/GPT",
        formula_reason="GELU weights inputs by their position in a Gaussian distribution. It is smoother than ReLU and often yields better accuracy in Transformers.",
        explanation="We use a high-precision polynomial approximation involving tanh to estimate the Gaussian Cumulative Distribution Function (CDF).",
        steps=[
            f"Step 1: Calculate the cubic term.\n   x³ = {x} * {x} * {x} = {cubic:.4f}",
            f"Step 2: Add linear and cubic terms with coefficient.\n   {x} + (0.044715 * {cubic:.4f}) = {inner_term:.4f}",
            f"Step 3: Scale by √(2/π) (approx 0.79788).\n   0.79788 * {inner_term:.4f} = {scaled_inner:.4f}",
            f"Step 4: Apply Hyperbolic Tangent.\n   tanh({scaled_inner:.4f}) = {tanh_val:.5f}",
            f"Step 5: Final combination.\n   0.5 * {x} * (1 + {tanh_val:.5f}) = {result:.6f}"
        ],
        answer=result
    )

def gelu_stable(x: float, show_steps=False):
    _validate_number(x, "x")
    
    # In many libraries, the "stable" version simply refers to using the 
    # Tanh approximation instead of the expensive and potentially unstable 
    # exact Erf() calculation.
    
    # We will use the same calculation but with a specific note on stability.
    SQRT_2_OVER_PI = 0.7978845608
    COEFF = 0.044715
    
    cubic = x ** 3
    inner_term = x + (COEFF * cubic)
    scaled_inner = SQRT_2_OVER_PI * inner_term
    tanh_val = math.tanh(scaled_inner)
    result = 0.5 * x * (1 + tanh_val)

    if not show_steps:
        return result

    return Solution(
        given=f"x = {x}",
        to_find="Stable GELU Output",
        equation="GELU(x) ≈ 0.5x(1 + tanh(...))",
        formula_name="Stable GELU (Tanh Approximation)",
        formula_used="Tanh Approximation",
        formula_reason="The exact GELU definition uses the Error Function 'erf(x)', which is computationally expensive. This Tanh approximation is the standard 'stable' and fast alternative used in practice.",
        explanation="We use the exact same Tanh formula as standard GELU here, because this approximation IS the stability fix for the original Erf-based definition.",
        steps=[
            "Step 1: Acknowledge Method.\n   Using Tanh approximation instead of Erf for stability and speed.",
            f"Step 2: Calculate Polynomial term.\n   x + 0.044715x³ = {inner_term:.4f}",
            f"Step 3: Scale and Tanh.\n   tanh({scaled_inner:.4f}) = {tanh_val:.5f}",
            f"Step 4: Final Calculation.\n   0.5 * {x} * (1 + {tanh_val:.5f}) = {result:.6f}"
        ],
        answer=result
    )


# ==========================================================
# SOFTMAX
# ==========================================================

def softmax(values: List[float], show_steps=False):
    _validate_list(values, "Input values")
    
    exp_vals = [math.exp(v) for v in values]
    total_sum = sum(exp_vals)
    probs = [v / total_sum for v in exp_vals]

    if not show_steps:
        return probs

    steps = [
        f"Step 1: Inspect Input Vector.\n   We have {len(values)} scores: {values}",
        "Step 2: Exponentiate each element (e^x). This makes everything positive and exaggerates large values."
    ]
    
    # Detailed list step
    for i, (val, exp_v) in enumerate(zip(values, exp_vals)):
        steps.append(f"   Item {i}: e^({val}) ≈ {exp_v:.4f}")

    steps.append(f"Step 3: Sum of Exponentials (The Normalizer).\n   Sum = {' + '.join([f'{e:.2f}' for e in exp_vals])} = {total_sum:.4f}")
    steps.append("Step 4: Divide each exponential by the Sum to get Probabilities.")
    
    for i, p in enumerate(probs):
        steps.append(f"   Probability {i}: {exp_vals[i]:.4f} / {total_sum:.4f} = {p:.4f} ({p*100:.1f}%)")
    
    steps.append("   (Notice that all probabilities now sum to exactly 1.0)")

    return Solution(
        given=f"Score Vector = {values}",
        to_find="Softmax Probabilities",
        equation="p_i = e^(x_i) / Σ e^(x_j)",
        formula_name="Softmax Function",
        formula_used="e^x / Sum(e^x)",
        formula_reason="Used in the final layer of classifiers to turn raw scores (logits) into a valid probability distribution.",
        explanation="1. Make everything positive (exp). 2. Sum them up. 3. Divide by sum to normalize.",
        steps=steps,
        answer=probs
    )

def softmax_stable(values: List[float], show_steps=False):
    _validate_list(values, "Input values")
    
    # Shift invariance trick
    max_val = max(values)
    shifted_values = [v - max_val for v in values]
    
    exp_vals = [math.exp(v) for v in shifted_values]
    total_sum = sum(exp_vals)
    probs = [v / total_sum for v in exp_vals]

    if not show_steps:
        return probs

    steps = [
        f"Step 1: Find the Maximum Score.\n   Max({values}) = {max_val}",
        "Step 2: Shift (Subtract Max from every score). This ensures the largest exponent is e^0=1, preventing overflow.",
        f"   Shifted Values: {shifted_values}",
        "Step 3: Exponentiate the Shifted values."
    ]
    
    for i, (sv, ev) in enumerate(zip(shifted_values, exp_vals)):
        steps.append(f"   e^({sv}) = {ev:.4f}")

    steps.append(f"Step 4: Sum of Exponentials.\n   Total = {total_sum:.4f}")
    steps.append("Step 5: Normalize (Divide by Sum).")
    
    for i, p in enumerate(probs):
        steps.append(f"   Probability {i}: {exp_vals[i]:.4f} / {total_sum:.4f} = {p:.4f}")

    return Solution(
        given=f"Score Vector = {values}",
        to_find="Stable Softmax Probabilities",
        equation="p_i = e^(x_i - max) / Σ e^(x_j - max)",
        formula_name="Numerically Stable Softmax",
        formula_used="Shift-Invariance Property",
        formula_reason="The probabilities remain mathematically identical to standard Softmax, but this method is safe for any input magnitude.",
        explanation="We shift the entire curve left so the highest peak hits 0, keeping exponentials within a safe range.",
        steps=steps,
        answer=probs
    )


# ==========================================================
# ALIASES
# ==========================================================

# Critical alias for test compatibility
tanh = tanh_activation


# ==========================================================
# EXPORT
# ==========================================================

__all__ = [
    "sigmoid", "sigmoid_stable",
    "relu", "leaky_relu", "tanh_activation",
    "softplus", "softplus_stable",
    "swish", "swish_stable",
    "gelu", "gelu_stable",
    "softmax", "softmax_stable",
]
