# solvepath/transforms.py
"""
==========================================================
              SolvePath Transforms Module
==========================================================

Includes HIGHLY DETAILED step-by-step solutions for:
• Fourier Transform (Symbolic)
• Discrete Fourier Transform (DFT)
• Inverse Discrete Fourier Transform (IDFT)
• Laplace Transform (Symbolic & Power)
• Inverse Laplace Transform
• Z-Transform
• Inverse Z-Transform
• Discrete-Time Fourier Transform (DTFT)
• Discrete Cosine Transform (DCT-II)

Returns:
• Solution object when show_steps=True
• Final result when show_steps=False
==========================================================
"""

import math
import cmath
from typing import List, Union
from solvepath.solution import Solution

# ==========================================================
# INTERNAL VALIDATION
# ==========================================================

def _ensure_sequence(x, name="sequence"):
    if not isinstance(x, (list, tuple)):
        raise TypeError(f"{name} must be a list or tuple")
    if len(x) == 0:
        raise ValueError(f"{name} cannot be empty")
    for i, val in enumerate(x):
        if not isinstance(val, (int, float, complex)):
            raise TypeError(f"{name}[{i}] must be numeric")
    return x

# ==========================================================
# FOURIER TRANSFORM (SYMBOLIC – CONTINUOUS)
# ==========================================================

def fourier_transform_symbolic(expr: str, show_steps=False):
    result = f"F(ω) = ∫ {expr} · e^(−iωt) dt"

    if not show_steps:
        return result

    return Solution(
        given=f"f(t) = {expr}",
        to_find="The Fourier Transform F(ω)",
        equation="F(ω) = ∫₋∞⁺∞ f(t)e^(−iωt) dt",
        formula_name="Continuous Fourier Transform Definition",
        formula_used="F(ω) = ∫ f(t)e^(−iωt) dt",
        formula_reason="We use this to decompose a time-based signal into its frequency ingredients.",
        symbol_explanation=(
            "• f(t) is the signal in time.\n"
            "• ω (omega) is the angular frequency.\n"
            "• e^(−iωt) wraps the signal around the complex unit circle."
        ),
        explanation="The integral calculates the 'center of mass' of the signal when wrapped around the origin at frequency ω.",
        steps=[
            f"Step 1: Identify the input function.\n   f(t) = {expr}",
            "Step 2: Set up the Fourier Integral.\n   F(ω) = ∫₋∞⁺∞ f(t) · e^(−iωt) dt",
            f"Step 3: Substitute our specific function into the integral.\n   F(ω) = ∫ ({expr}) · e^(−iωt) dt",
            "Step 4: Evaluate the integral limits (usually -∞ to +∞).",
            f"Step 5: The symbolic solution is:\n   {result}"
        ],
        answer=result
    )

# ==========================================================
# DISCRETE FOURIER TRANSFORM (DFT)
# ==========================================================

def dft(x: List[complex], show_steps=False):
    x = _ensure_sequence(x, "input sequence")
    N = len(x)
    result = []
    
    steps = [
        f"--- Starting DFT Calculation ---",
        f"Step 1: Analyze the Input.\n   Sequence x[n] = {x}\n   Total samples (N) = {N}",
        "Step 2: Identify the DFT Formula.\n   X[k] = Σ (from n=0 to N-1) of x[n] · e^(−i · 2π · k · n / N)",
        "   (This formula compares the signal against rotating frequencies.)",
        "Step 3: Begin calculating X[k] for each frequency bin k."
    ]

    for k in range(N):
        s = 0
        steps.append(f"\n--- Calculating Frequency Bin k = {k} ---")
        
        iteration_details = []
        for n in range(N):
            # Detailed breakdown
            theta = -2 * math.pi * k * n / N
            complex_term = cmath.exp(1j * theta)
            term_value = x[n] * complex_term
            s += term_value
            
            # SHOW THE WORKING
            euler_desc = f"cos({theta:.2f}) + i·sin({theta:.2f})"
            
            iteration_details.append(
                f"   n={n}: Substitute into formula:\n"
                f"          x[{n}] · e^(-i·2π·{k}·{n}/{N})\n"
                f"          = {x[n]} · e^(i · {theta:.2f})\n"
                f"          = {x[n]} · [{euler_desc}]\n"
                f"          = {term_value.real:.2f} + {term_value.imag:.2f}j"
            )

        result.append(s)
        
        steps.append("   Summing contributions from all time points n:")
        steps.extend(iteration_details)
        steps.append(f"   Total Sum for X[{k}] = {s.real:.3f} + {s.imag:.3f}j")

    if not show_steps:
        return result

    return Solution(
        given=f"x[n] = {x}",
        to_find="Discrete Fourier Transform X[k]",
        equation="X[k] = Σ x[n] · W_N^(kn)",
        formula_name="DFT Summation",
        formula_used="X[k] = Σ x[n]e^(−i2πnk/N)",
        formula_reason="To convert discrete time samples into frequency domain coefficients.",
        symbol_explanation="W_N is the 'twiddle factor' e^(-i2π/N).",
        explanation="We project the signal onto N orthogonal basis vectors (complex sinusoids).",
        steps=steps,
        answer=[f"{v.real:.2f} + {v.imag:.2f}j" for v in result]
    )

# ==========================================================
# INVERSE DISCRETE FOURIER TRANSFORM (IDFT)
# ==========================================================

def idft(X: List[complex], show_steps=False):
    X = _ensure_sequence(X, "frequency sequence")
    N = len(X)
    result = []
    
    steps = [
        f"--- Starting Inverse DFT Calculation ---",
        f"Step 1: Input Frequency Bins.\n   X[k] = {X}\n   Count N = {N}",
        "Step 2: Identify the IDFT Formula.\n   x[n] = (1/N) · Σ X[k] · e^(+i · 2π · k · n / N)",
        "   (Note the POSITIVE exponent and the 1/N scaling factor!)"
    ]

    for n in range(N):
        s = 0
        steps.append(f"\n--- Reconstructing Time Sample n = {n} ---")
        
        for k in range(N):
            theta = 2 * math.pi * k * n / N
            term = X[k] * cmath.exp(1j * theta)
            s += term
            steps.append(
                f"   k={k}: Substitute X[{k}] into formula:\n"
                f"          {X[k]} · e^(i · {theta:.2f})\n"
                f"          = {term.real:.2f} + {term.imag:.2f}j"
            )
            
        final_val = s / N
        result.append(final_val)
        steps.append(f"   Sum of terms = {s.real:.2f} + {s.imag:.2f}j")
        steps.append(f"   Divide by N ({N}): Final x[{n}] = {final_val.real:.3f} + {final_val.imag:.3f}j")

    if not show_steps:
        return result

    return Solution(
        given=f"X[k] = {X}",
        to_find="Time Domain Signal x[n]",
        equation="x[n] = (1/N) Σ X[k]W_N^(-kn)",
        formula_name="Inverse DFT",
        formula_used="x[n] = (1/N) Σ X[k]e^(i2πnk/N)",
        formula_reason="To synthesize the original signal by adding up its frequency waves.",
        symbol_explanation="The 1/N term averages the energy to return to the correct amplitude.",
        explanation="Each sample x[n] is a weighted sum of all frequency components.",
        steps=steps,
        answer=[f"{v.real:.2f} + {v.imag:.2f}j" for v in result]
    )

# ==========================================================
# LAPLACE TRANSFORM (SYMBOLIC & POWER)
# ==========================================================

def laplace_transform(expr: Union[str, int], show_steps=False):
    """
    Computes Laplace transform.
    - If expr is int 'n', computes L{t^n}
    - If expr is str, uses lookup table.
    """
    
    # CASE A: Power Function t^n (Integer Input)
    if isinstance(expr, int):
        n = expr
        numerator = math.factorial(n)
        power_s = n + 1
        result = f"{numerator}/s^{power_s}"

        if not show_steps: return result

        return Solution(
            given=f"f(t) = t^{n}",
            to_find="Laplace Transform L{f(t)}",
            equation="L{t^n} = n! / s^(n+1)",
            formula_name="Laplace Transform (Power Rule)",
            formula_used="n! / s^(n+1)",
            explanation="The Laplace transform converts a time-domain power function into an s-domain rational function.",
            steps=[
                f"Step 1: Identify power n = {n}.",
                f"Step 2: Calculate factorial n! = {numerator}.",
                f"Step 3: Calculate power of s: n+1 = {power_s}.",
                f"Step 4: Combine: {result}."
            ],
            answer=result
        )

    # CASE B: Symbolic Lookup (String Input)
    table = {
        "1": "1/s",
        "t": "1/s^2",
        "e^(at)": "1/(s−a)",
        "sin(bt)": "b/(s² + b²)",
        "cos(bt)": "s/(s² + b²)"
    }

    result = table.get(expr, f"L{{{expr}}} (symbolic)")

    if not show_steps:
        return result
    
    steps = [
        f"Step 1: Analyze the time-domain function.\n   f(t) = {expr}",
        "Step 2: Recall the Definition of Laplace Transform.\n   L{f(t)} = ∫₀^∞ f(t)e^(-st) dt",
        "Step 3: Compare f(t) with standard Laplace Table entries.",
    ]

    if expr in table:
        steps.append(f"   Found match! The transform pair for '{expr}' is known.")
        steps.append(f"Step 4: Write the result from the table.\n   F(s) = {result}")
        steps.append("Step 5: Determine Region of Convergence (ROC).\n   Valid where Real(s) > pole location.")
    else:
        steps.append("   No direct match found in the basic table.")
        steps.append(f"Step 4: Apply the definition or properties of linearity.\n   Result: {result}")

    return Solution(
        given=f"f(t) = {expr}",
        to_find="Laplace Transform F(s)",
        equation="L{f(t)} = F(s)",
        formula_name="Laplace Table Lookup",
        formula_used="Standard Transform Pairs",
        explanation="We map the function to the S-plane to analyze stability and transient response.",
        steps=steps,
        answer=result
    )

# Alias for compatibility
laplace = laplace_transform
laplace_t = laplace_transform

# ==========================================================
# INVERSE LAPLACE TRANSFORM
# ==========================================================

def inverse_laplace(expr: str, show_steps=False):
    table = {
        "1/s": "1",
        "1/s^2": "t",
        "1/(s-a)": "e^(at)",
        "b/(s^2 + b^2)": "sin(bt)",
        "s/(s^2 + b^2)": "cos(bt)"
    }
    result = table.get(expr, f"L⁻¹{{{expr}}}")

    if not show_steps:
        return result

    return Solution(
        given=f"F(s) = {expr}",
        to_find="Time Domain Function f(t)",
        equation="L⁻¹{F(s)} = f(t)",
        formula_name="Inverse Laplace Lookup",
        formula_used="Standard Inverse Pairs",
        formula_reason="To convert the solved algebraic equation back into a physical time signal.",
        symbol_explanation="L⁻¹ is the inverse operator.",
        explanation="We look for a pattern in F(s) that matches a known time function.",
        steps=[
            f"Step 1: Identify the s-domain expression.\n   F(s) = {expr}",
            "Step 2: Check the denominator to identify the type of function (pole location).",
            f"Step 3: Match found in table.\n   Expression matches the form for: {result}",
            f"Step 4: Final Answer.\n   f(t) = {result}"
        ],
        answer=result
    )

# ==========================================================
# Z-TRANSFORM
# ==========================================================

def z_transform(x: List[float], show_steps=False):
    x = _ensure_sequence(x, "input sequence")
    
    terms_str = []
    for n, val in enumerate(x):
        if val != 0:
            power = "" if n == 0 else f"z^(−{n})"
            terms_str.append(f"{val}{power}")
    result = " + ".join(terms_str) if terms_str else "0"

    if not show_steps:
        return result

    steps = [
        f"Step 1: Input Sequence.\n   x[n] = {x}",
        "Step 2: Identify Z-Transform Definition.\n   X(z) = Σ (from n=-∞ to +∞) x[n] · z⁻ⁿ",
        "   Since our sequence starts at n=0, we sum from n=0.",
        "Step 3: Expand the summation term by term."
    ]

    for n, val in enumerate(x):
        if val != 0:
            term_desc = f"{val} · z⁻{n}" if n > 0 else f"{val} · z⁰"
            steps.append(f"   n={n}: Substitute x[{n}]={val} into formula -> {term_desc}")
        else:
            steps.append(f"   n={n}: Value is 0. Term is 0 (ignored).")

    steps.append(f"Step 4: Combine all non-zero terms into a polynomial.\n   X(z) = {result}")

    return Solution(
        given=f"x[n] = {x}",
        to_find="Z-Transform X(z)",
        equation="X(z) = Σ x[n]z⁻ⁿ",
        formula_name="Unilateral Z-Transform",
        formula_used="X(z) = Σ x[n]z⁻ⁿ",
        formula_reason="To analyze discrete-time control systems and filters.",
        symbol_explanation="z represents a complex frequency shift operator.",
        explanation="The Z-transform converts a sequence of numbers into a polynomial in z.",
        steps=steps,
        answer=result
    )

# ==========================================================
# INVERSE Z-TRANSFORM
# ==========================================================

def inverse_z_transform(expr: str, show_steps=False):
    table = {
        "1/(1-az^-1)": "a^n u[n]",
        "1/(1-z^-1)": "u[n] (Unit Step)",
        "z/(z-1)^2": "n u[n] (Ramp)"
    }
    result = table.get(expr, f"Z⁻¹{{{expr}}}")

    if not show_steps:
        return result

    return Solution(
        given=f"X(z) = {expr}",
        to_find="Discrete Sequence x[n]",
        equation="Z⁻¹{X(z)} = x[n]",
        formula_name="Inverse Z-Transform Table",
        formula_used="Partial Fraction / Table Lookup",
        formula_reason="To recover the time sequence from the z-domain function.",
        symbol_explanation="u[n] is the unit step function (1 for n>=0, 0 otherwise).",
        explanation="We match the rational function in z to known sequence patterns.",
        steps=[
            f"Step 1: Given z-domain function.\n   X(z) = {expr}",
            "Step 2: Recognize the form.",
            "   (Is it a geometric series? 1/(1-r)? Is it a ramp?)",
            f"Step 3: Match found in table.\n   Corresponds to: {result}",
            f"Step 4: Final Sequence.\n   x[n] = {result}"
        ],
        answer=result
    )

# ==========================================================
# DISCRETE-TIME FOURIER TRANSFORM (DTFT)
# ==========================================================

def dtft(x: List[float], omega: float, show_steps=False):
    x = _ensure_sequence(x)
    result = 0
    
    steps = [
        f"Step 1: Inputs.\n   Sequence x[n] = {x}\n   Target Frequency ω = {omega} rad/sample",
        "Step 2: DTFT Formula.\n   X(ω) = Σ x[n] · e^(−i · ω · n)",
        "Step 3: Sum the contribution of each sample."
    ]
    
    for n, val in enumerate(x):
        angle = -omega * n
        term = val * cmath.exp(1j * angle)
        result += term
        
        # SHOW THE WORKING
        steps.append(
            f"   n={n}: Substitute into formula:\n"
            f"          {val} · e^(−i·{omega}·{n})\n"
            f"          = {val} · e^(i · {angle:.2f})\n"
            f"          = {val} · [cos({angle:.2f}) + i·sin({angle:.2f})]\n"
            f"          = {term.real:.3f} + {term.imag:.3f}j"
        )

    steps.append(f"Step 4: Final Summation.\n   X({omega}) = {result.real:.4f} + {result.imag:.4f}j")

    if not show_steps:
        return result

    return Solution(
        given=f"x[n] = {x}, ω = {omega}",
        to_find="DTFT Value X(ω)",
        equation="X(ω) = Σ x[n]e^(−iωn)",
        formula_name="DTFT Summation",
        formula_used="X(ω) = Σ x[n]e^(−iωn)",
        formula_reason="To find the frequency response of a non-periodic discrete signal.",
        symbol_explanation="ω is continuous frequency from -π to +π.",
        explanation="We are calculating the value of the spectrum at one specific frequency point.",
        steps=steps,
        answer=f"{result.real:.4f} + {result.imag:.4f}j"
    )

# ==========================================================
# DISCRETE COSINE TRANSFORM (DCT-II)
# ==========================================================

def dct_ii(x: List[float], show_steps=False):
    x = _ensure_sequence(x)
    N = len(x)
    result = []
    
    steps = [
        f"--- Starting DCT-II Calculation ---",
        f"Step 1: Inputs.\n   Sequence x[n] = {x}\n   Length N = {N}",
        "Step 2: DCT-II Formula.\n   X[k] = Σ x[n] · cos[ π · k · (2n + 1) / (2N) ]",
        "Step 3: Compute coefficients for k = 0 to N-1."
    ]

    for k in range(N):
        s = 0
        steps.append(f"\n--- Coefficient k = {k} ---")
        
        term_details = []
        for n in range(N):
            argument = math.pi * k * (2*n + 1) / (2*N)
            cos_val = math.cos(argument)
            term_val = x[n] * cos_val
            s += term_val
            
            # SHOW THE WORKING
            term_details.append(
                f"   n={n}: Substitute into Cosine term:\n"
                f"          π · {k} · ({2*n+1}) / {2*N} = {argument:.3f} rad\n"
                f"          cos({argument:.3f}) = {cos_val:.3f}\n"
                f"          Multiply by x[{n}]: {x[n]} * {cos_val:.3f} = {term_val:.3f}"
            )
            
        result.append(s)
        steps.extend(term_details)
        steps.append(f"   Sum for X[{k}] = {s:.4f}")

    if not show_steps:
        return result

    return Solution(
        given=f"x[n] = {x}",
        to_find="DCT Coefficients",
        equation="X[k] = Σ x[n] cos(...)",
        formula_name="DCT-II Definition",
        formula_used="X[k] = Σ x[n] cos(πk(2n+1)/(2N))",
        formula_reason="Commonly used in JPEG image compression to concentrate energy.",
        symbol_explanation="Uses real-valued cosine functions instead of complex exponentials.",
        explanation="We decompose the signal into a sum of cosine waves oscillating at different frequencies.",
        steps=steps,
        answer=[f"{v:.4f}" for v in result]
    )

# ==========================================================
# EXPORT
# ==========================================================

__all__ = [
    "fourier_transform_symbolic",
    "dft",
    "idft",
    "laplace_transform",
    "laplace",
    "laplace_t",
    "inverse_laplace",
    "z_transform",
    "inverse_z_transform",
    "dtft",
    "dct_ii",
]
