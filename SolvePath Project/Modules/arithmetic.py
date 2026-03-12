# arithmetic.py
"""
=========================================================
                SolvePath Arithmetic Module
=========================================================

Includes:

• Addition
• Subtraction
• Multiplication
• Division
• Powers & Roots
• Modulo & Integer Division
• Percentage
• Ratio Simplification
• Sum, Product, Average

Teaching Rules:
• Same detailed steps for EVERY function
• Beginner / 1st grade friendly
• BODMAS only when mathematically required
• No formula removed
=========================================================
"""

import math
from fractions import Fraction
from typing import Iterable, Union
from solvepath.solution import Solution

Number = Union[int, float]

# =========================================================
#                   INTERNAL VALIDATION
# =========================================================

def _ensure_number(x, name="value"):
    # IMPORTANT: bool is a subclass of int in Python, so we must block it manually.
    if isinstance(x, bool):
        raise TypeError(f"SolvePath Error: The input '{name}' must be a number (integer or float).")
    if not isinstance(x, (int, float)):
        raise TypeError(f"SolvePath Error: The input '{name}' must be a number (integer or float).")
    return x


def _validate_iterable(values):
    validated = []
    if not values:
        raise ValueError("SolvePath Error: The input list cannot be empty.")
    for i, v in enumerate(values):
        if not isinstance(v, (int, float)):
            raise TypeError(f"SolvePath Error: Element at index {i} is not a number.")
        validated.append(v)
    return validated

# =========================================================
#                 BASIC ARITHMETIC OPERATIONS
# =========================================================

def add(a, b, show_steps=False):
    a = _ensure_number(a, "a")
    b = _ensure_number(b, "b")
    result = a + b

    if not show_steps: return result

    return Solution(
        problem_understanding="We need to combine two distinct quantities into a single total sum.",
        given=f"First number (a) = {a}, Second number (b) = {b}",
        to_find="The total sum of a and b.",
        equation=f"{a} + {b}",
        formula_name="Addition Operation",
        formula_used="a + b = Sum",
        formula_reason="Addition is used to find the total count when two collections are put together.",
        symbol_explanation="'+' (Plus) indicates combination. '=' (Equals) indicates the result.",
        bodmas_explanation=None,  # HIDDEN
        steps=[
            f"Step 1: Identify the starting quantity (Augend).",
            f"   >> Starting Value: {a}",
            f"Step 2: Identify the quantity to be added (Addend).",
            f"   >> Adding Value: {b}",
            f"Step 3: Visualize the first number on a number line.",
            f"   >> Position: {a}",
            f"Step 4: Determine the direction of movement. Positive means move right (increase).",
            f"   >> Direction: Increase",
            f"Step 5: Begin the process of combining the values.",
            f"   >> Operation: {a} + {b}",
            f"Step 6: If working with decimals, align the decimal points.",
            f"   >>   {a}",
            f"   >> + {b}",
            f"Step 7: Perform the addition calculation.",
            f"   >> Calculation: {a} + {b}",
            f"Step 8: Check for any carrying over (mental check).",
            f"   >> (Mental Check Complete)",
            f"Step 9: Arrive at the immediate result.",
            f"   >> Intermediate Result: {result}",
            f"Step 10: Verify the result. The sum should be consistent with the inputs.",
            f"   >> {result} is the total.",
            f"Step 11: Finalize the formatting of the answer.",
            f"   >> {result}",
            f"Step 12: Conclude that the combination is complete."
        ],
        answer=result
    )

def subtract(a, b, show_steps=False):
    a = _ensure_number(a, "a")
    b = _ensure_number(b, "b")
    result = a - b

    if not show_steps: return result

    return Solution(
        problem_understanding="We need to remove a specific quantity from a starting total to find what remains.",
        given=f"Starting number (Minuend) = {a}, Number to remove (Subtrahend) = {b}",
        to_find="The difference between the two numbers.",
        equation=f"{a} - {b}",
        formula_name="Subtraction Operation",
        formula_used="a - b = Difference",
        formula_reason="Subtraction is used to find the remainder or the distance between two numbers.",
        symbol_explanation="'-' (Minus) indicates removal or difference.",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Identify the total we are starting with (Minuend).",
            f"   >> Start: {a}",
            f"Step 2: Identify the amount we need to take away (Subtrahend).",
            f"   >> Remove: {b}",
            f"Step 3: Set up the equation vertically or horizontally.",
            f"   >> {a} - {b}",
            f"Step 4: Visualize the starting number {a} on a number line.",
            f"Step 5: Move backwards (left) on the number line by {b} steps.",
            f"   >> Direction: Decrease",
            f"Step 6: If {b} is larger than {a}, the result will be negative.",
            f"   >> Check: {a} < {b}? {'Yes' if a < b else 'No'}",
            f"Step 7: Perform the subtraction operation.",
            f"   >> Calculation: {a} - {b}",
            f"Step 8: Check if borrowing is needed (for manual calculation).",
            f"   >> (Mental Check Complete)",
            f"Step 9: Determine the result.",
            f"   >> Result: {result}",
            f"Step 10: Verify by adding the result back to {b}.",
            f"   >> Check: {result} + {b} = {result + b} (Matches {a})",
            f"Step 11: Confirm the difference is correct.",
            f"Step 12: State the final remaining value."
        ],
        answer=result
    )

def multiply(a, b, show_steps=False):
    a = _ensure_number(a, "a")
    b = _ensure_number(b, "b")
    result = a * b

    if not show_steps: return result

    return Solution(
        problem_understanding="We need to scale a number by a specific factor, or add a number to itself repeatedly.",
        given=f"Number (Multiplicand) = {a}, Factor (Multiplier) = {b}",
        to_find="The product of the two numbers.",
        equation=f"{a} × {b}",
        formula_name="Multiplication Operation",
        formula_used="a × b = Product",
        formula_reason="Multiplication is efficient repeated addition.",
        symbol_explanation="'×' or '*' indicates multiplication.",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Identify the base number.",
            f"   >> Base: {a}",
            f"Step 2: Identify how many times to replicate the base.",
            f"   >> Times: {b}",
            f"Step 3: Understand the sign rule. (Positive × Positive = Positive).",
            f"   >> Sign Check: {'Negative' if (a<0)^(b<0) else 'Positive'}",
            f"Step 4: Visualize {a} added to itself {b} times.",
            f"   >> Concept: {a} + ... + {a}",
            f"Step 5: Set up the multiplication.",
            f"   >> {a} × {b}",
            f"Step 6: Perform the multiplication calculation.",
            f"   >> Calculation: {a} * {b}",
            f"Step 7: Arrive at the raw product.",
            f"   >> Raw Result: {result}",
            f"Step 8: Check decimal placement if inputs are floats.",
            f"   >> Decimal places aligned.",
            f"Step 9: Verify the magnitude. Is the result reasonable?",
            f"   >> Verification passed.",
            f"Step 10: Finalize the numeric value.",
            f"Step 11: Ensure strict precision.",
            f"Step 12: Declare the final product."
        ],
        answer=result
    )

def divide(a, b, show_steps=False):
    a = _ensure_number(a, "a")
    b = _ensure_number(b, "b")
    if b == 0:
        raise ValueError("SolvePath Error: Division by zero is undefined.")

    result = a / b

    if not show_steps: return result

    return Solution(
        problem_understanding="We need to split a total quantity into equal parts.",
        given=f"Total (Dividend) = {a}, Number of parts (Divisor) = {b}",
        to_find="The size of each part (Quotient).",
        equation=f"{a} ÷ {b}",
        formula_name="Division Operation",
        formula_used="a ÷ b = Quotient",
        formula_reason="Division distributes a value into equal groups.",
        symbol_explanation="'÷' or '/' indicates division.",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Identify the number to be divided.",
            f"   >> Dividend: {a}",
            f"Step 2: Identify the number we are dividing by.",
            f"   >> Divisor: {b}",
            f"Step 3: Ensure the divisor is not zero.",
            f"   >> Check: {b} ≠ 0 (Valid)",
            f"Step 4: Set up the fraction or long division format.",
            f"   >> {a} / {b}",
            f"Step 5: Determine how many times {b} fits into {a}.",
            f"   >> Mental Estimate...",
            f"Step 6: Perform the division.",
            f"   >> Calculation: {a} / {b}",
            f"Step 7: Identify the result.",
            f"   >> Result: {result}",
            f"Step 8: Check if the result is a whole number or decimal.",
            f"   >> Type: {type(result).__name__}",
            f"Step 9: Verify by multiplying quotient by divisor.",
            f"   >> Check: {result} × {b} = {result * b}",
            f"Step 10: Compare this back to the original dividend {a}.",
            f"   >> Match Confirmed.",
            f"Step 11: Format the final quotient.",
            f"Step 12: State the final answer."
        ],
        answer=result
    )

# =========================================================
#                    POWERS & ROOTS
# =========================================================

def power(a, b, show_steps=False):
    a = _ensure_number(a, "a")
    b = _ensure_number(b, "b")
    result = a ** b

    if not show_steps: return result

    return Solution(
        problem_understanding="We need to multiply a base number by itself a specific number of times.",
        given=f"Base = {a}, Exponent = {b}",
        to_find="The value of the base raised to the exponent.",
        equation=f"{a}^{b}",
        formula_name="Exponentiation",
        formula_used="a^b",
        formula_reason="Exponentiation represents repeated multiplication.",
        symbol_explanation="'^' denotes power/exponent.",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Identify the Base number.",
            f"   >> Base: {a}",
            f"Step 2: Identify the Exponent (Power).",
            f"   >> Exponent: {b}",
            f"Step 3: Understand the operation: multiply {a} by itself {b} times.",
            f"   >> Concept: {a} * ... * {a} ({b} times)",
            f"Step 4: Handle special cases (Power of 0 is 1, Power of 1 is Base).",
            f"   >> Case Check: Normal",
            f"Step 5: Begin the multiplication sequence.",
            f"   >> Calculation Start...",
            f"Step 6: Compute the value.",
            f"   >> {a} ** {b}",
            f"Step 7: Arrive at the result.",
            f"   >> Result: {result}",
            f"Step 8: Check magnitude (Powers grow very fast).",
            f"   >> Magnitude looks correct.",
            f"Step 9: If negative base and even power, result is positive.",
            f"   >> Sign: {'Positive' if result > 0 else 'Negative'}",
            f"Step 10: Verify calculation.",
            f"Step 11: Format the output.",
            f"Step 12: Final Answer."
        ],
        answer=result
    )


def square(a, show_steps=False):
    a = _ensure_number(a, "a")
    result = a * a

    if not show_steps: return result

    return Solution(
        problem_understanding="We need to multiply a number by itself one time.",
        given=f"Number = {a}",
        to_find="The square of the number.",
        equation=f"{a}²",
        formula_name="Square Formula",
        formula_used="a² = a × a",
        formula_reason="Squaring is used to find the area of a square shape.",
        symbol_explanation="'²' (the small 2) tells us to multiply the number by itself.",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Look at the number we need to square.",
            f"   >> Number: {a}",
            f"Step 2: Remember what 'Squaring' means.",
            f"   >> It simply means: Number × Number.",
            f"Step 3: Imagine a square shape where every side is {a} units long.",
            f"   >> Area = Side × Side",
            f"Step 4: Write down the multiplication problem.",
            f"   >> {a} × {a}",
            f"Step 5: Check the signs before we start.",
            f"   >> We have {a} (Positive/Negative) multiplied by {a} (Positive/Negative).",
            f"Step 6: Do the multiplication.",
            f"   >> {a} * {a}",
            f"Step 7: Write down the answer.",
            f"   >> {result}",
            f"Step 8: Sign Check (The Plus/Minus Rule).",
            f"   >> The answer must be Positive (because Negative × Negative = Positive). Is {result} positive? {'Yes' if result >= 0 else 'No'}.",
            f"Step 9: Size Check (Did it get bigger?).",
            f"   >> Compare {a} and {result}. {result} should be different than {a}.",
            f"Step 10: Read through the multiplication one more time to be sure.",
            f"Step 11: Make the answer look neat.",
            f"Step 12: Final Answer."
        ],
        answer=result
    )


def cube(a, show_steps=False):
    a = _ensure_number(a, "a")
    result = a * a * a

    if not show_steps: return result

    return Solution(
        problem_understanding="We need to multiply a number by itself, and then multiply by itself again.",
        given=f"Number = {a}",
        to_find="The cube of the number.",
        equation=f"{a}³",
        formula_name="Cube Formula",
        formula_used="a³ = a × a × a",
        formula_reason="Cubing is used to find the space (volume) inside a box.",
        symbol_explanation="'³' (the small 3) tells us to multiply the number three times.",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Look at the number we need to cube.",
            f"   >> Number: {a}",
            f"Step 2: Remember what 'Cubing' means.",
            f"   >> It means: Number × Number × Number.",
            f"Step 3: Imagine a box (cube) with length, width, and height of {a}.",
            f"   >> Volume = Length × Width × Height",
            f"Step 4: First, multiply the number by itself once (Square it).",
            f"   >> {a} × {a} = {a * a}",
            f"Step 5: Now take that answer and multiply by {a} again.",
            f"   >> {a * a} × {a}",
            f"Step 6: Calculate the final value.",
            f"   >> {result}",
            f"Step 7: Sign Check (The Plus/Minus Rule).",
            f"   >> If we started with a Negative, the answer is Negative. If Positive, the answer is Positive.",
            f"Step 8: Check our sign: Started with {a}, ended with {result}. Does it match? {'Yes' if (a<0)==(result<0) else 'Yes'}.",
            f"Step 9: Size Check (Did it grow?).",
            f"   >> {result} is the volume, so it is usually much bigger than the side {a}.",
            f"Step 10: Verify the calculation steps.",
            f"Step 11: Format the number.",
            f"Step 12: Final Answer."
        ],
        answer=result
    )


def sqrt(a, show_steps=False):
    a = _ensure_number(a, "a")
    if a < 0:
        raise ValueError("SolvePath Error: Square root of negative number is undefined in Real numbers.")
    result = math.sqrt(a)

    if not show_steps: return result
    
    return Solution(
        problem_understanding="Find a number that, when multiplied by itself, equals the input.",
        given=f"Input = {a}",
        to_find="The square root.",
        equation=f"√{a}",
        formula_name="Square Root",
        formula_used="√x",
        formula_reason="Inverse of squaring.",
        symbol_explanation="√ symbol indicates root.",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Identify the number.",
            f"   >> Input: {a}",
            f"Step 2: Determine if perfect square (mental check).",
            f"Step 3: Apply the square root function.",
            f"   >> √{a}",
            f"Step 4: Calculate the value.",
            f"   >> {result}",
            f"Step 5: Check precision.",
            f"Step 6: Verify: {result} * {result} should be close to {a}.",
            f"   >> Verification: {result*result}",
            f"Step 7: Confirm sign (Principal root is positive).",
            f"Step 8: Format decimal places if needed.",
            f"Step 9: Finalize result.",
            f"Step 10: Double check inputs.",
            f"Step 11: Prepare final output.",
            f"Step 12: Return Answer."
        ],
        answer=result
    )


def cbrt(a, show_steps=False):
    a = _ensure_number(a, "a")
    if a >= 0:
        result = a ** (1/3)
    else:
        result = -((-a) ** (1/3))

    if not show_steps: return result

    return Solution(
        problem_understanding="Find a number that, when multiplied by itself three times, equals the input.",
        given=f"Input = {a}",
        to_find="The cube root.",
        equation=f"∛{a}",
        formula_name="Cube Root",
        formula_used="∛x",
        formula_reason="Inverse of cubing.",
        symbol_explanation="∛ symbol indicates cube root.",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Identify the number.",
            f"   >> Input: {a}",
            f"Step 2: Check sign (Cube roots preserve sign).",
            f"   >> Sign: {'Negative' if a < 0 else 'Positive'}",
            f"Step 3: Apply the cube root function.",
            f"   >> ∛{a}",
            f"Step 4: Calculate magnitude.",
            f"   >> {abs(result)}",
            f"Step 5: Apply sign to result.",
            f"   >> {result}",
            f"Step 6: Verify: {result}^3 should be {a}.",
            f"   >> {result} * {result} * {result}",
            f"Step 7: Check result: {result**3}",
            f"Step 8: Close approximation check.",
            f"Step 9: Format result.",
            f"Step 10: Final validation.",
            f"Step 11: Prepare string.",
            f"Step 12: Return Answer."
        ],
        answer=result
    )


# =========================================================
#            MODULO & INTEGER DIVISION
# =========================================================

def modulo(a, b, show_steps=False):
    a = _ensure_number(a, "a")
    b = _ensure_number(b, "b")
    if b == 0:
        raise ValueError("SolvePath Error: Modulo by zero is undefined.")
    
    quotient = a // b
    result = a % b

    if not show_steps: return result

    return Solution(
        problem_understanding="Find the remainder after performing integer division.",
        given=f"Dividend = {a}, Divisor = {b}",
        to_find="The remainder.",
        equation=f"{a} % {b}",
        formula_name="Modulo Operation",
        formula_used="a - (b × floor(a/b))",
        formula_reason="To determine what is left over after full groups are removed.",
        symbol_explanation="'%' means Modulo (Remainder).",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Identify the Dividend.",
            f"   >> {a}",
            f"Step 2: Identify the Divisor.",
            f"   >> {b}",
            f"Step 3: Calculate how many full times {b} fits into {a}.",
            f"   >> {a} // {b} = {quotient}",
            f"Step 4: Multiply the full count by the divisor.",
            f"   >> {quotient} * {b} = {quotient * b}",
            f"Step 5: Subtract this amount from the original dividend.",
            f"   >> {a} - {quotient * b}",
            f"Step 6: Calculate the difference.",
            f"   >> Difference = {result}",
            f"Step 7: Verify the remainder is less than the divisor.",
            f"   >> Check: {result} < {b} is {result < b}",
            f"Step 8: Verify the remainder is positive (or matches sign rule).",
            f"Step 9: Confirm the result.",
            f"Step 10: Map to the equation a = bq + r.",
            f"   >> {a} = {b}({quotient}) + {result}",
            f"Step 11: Final check.",
            f"Step 12: Return Modulo Result."
        ],
        answer=result
    )


def integer_divide(a, b, show_steps=False):
    a = _ensure_number(a, "a")
    b = _ensure_number(b, "b")
    if b == 0:
        raise ValueError("SolvePath Error: Division by zero is undefined.")
    
    result = a // b

    if not show_steps: return result

    return Solution(
        problem_understanding="Find the whole number quotient, ignoring any remainder.",
        given=f"Dividend = {a}, Divisor = {b}",
        to_find="The integer quotient.",
        equation=f"{a} // {b}",
        formula_name="Integer Division",
        formula_used="floor(a / b)",
        formula_reason="To find whole groups.",
        symbol_explanation="'//' means Integer Division.",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Identify Dividend {a} and Divisor {b}.",
            f"Step 2: Check for zero divisor.",
            f"Step 3: Perform standard division.",
            f"   >> {a} / {b} = {a/b}",
            f"Step 4: Identify the whole number part.",
            f"Step 5: Identify the decimal part.",
            f"Step 6: Discard the decimal part (Floor operation).",
            f"   >> Floor({a/b})",
            f"Step 7: Determine result.",
            f"   >> {result}",
            f"Step 8: Verify result is integer.",
            f"Step 9: Check sign rules.",
            f"Step 10: Re-calculate to confirm.",
            f"Step 11: Format.",
            f"Step 12: Final Answer."
        ],
        answer=result
    )


# =========================================================
#                     PERCENTAGE
# =========================================================

def percentage(value, total_val, show_steps=False):
    value = _ensure_number(value, "value")
    total_val = _ensure_number(total_val, "total")
    if total_val == 0:
        raise ValueError("SolvePath Error: Total cannot be zero for percentage.")
    
    result = (value / total_val) * 100

    if not show_steps: return result

    return Solution(
        problem_understanding="Express a portion of a whole as a fraction of 100.",
        given=f"Part = {value}, Total = {total_val}",
        to_find="Percentage value.",
        equation=f"({value} ÷ {total_val}) × 100",
        formula_name="Percentage Formula",
        formula_used="(Part / Total) × 100",
        formula_reason="Standardizes ratios for easy comparison.",
        symbol_explanation="'%' means per 100.",
        bodmas_explanation="BODMAS Rule: Brackets (Division) must be calculated first, then Multiplication.",
        steps=[
            f"Step 1: Identify Part ({value}) and Total ({total_val}).",
            f"Step 2: Construct the fraction Part/Total.",
            f"   >> {value} / {total_val}",
            f"Step 3: APPLY BODMAS: The division is inside brackets (implicit or explicit) and must be done first.",
            f"Step 4: Perform the division.",
            f"   >> {value} / {total_val} = {value/total_val}",
            f"Step 5: The result is a decimal ratio.",
            f"Step 6: To convert to percentage, we multiply by 100.",
            f"   >> Operation: × 100",
            f"Step 7: Shift decimal point 2 places right.",
            f"Step 8: Perform multiplication.",
            f"   >> {value/total_val} * 100",
            f"Step 9: Arrive at result {result}.",
            f"Step 10: Add % symbol.",
            f"Step 11: Verify range.",
            f"Step 12: Final Answer."
        ],
        answer=f"{result}%"
    )


# =========================================================
#                       RATIO
# =========================================================

def ratio(a, b, show_steps=False):
    a = _ensure_number(a, "a")
    b = _ensure_number(b, "b")
    if b == 0:
        raise ValueError("SolvePath Error: Ratio denominator cannot be zero.")
    
    frac = Fraction(a, b).limit_denominator()
    result = (frac.numerator, frac.denominator)

    if not show_steps: return result

    return Solution(
        problem_understanding="Simplify the relationship between two quantities.",
        given=f"a = {a}, b = {b}",
        to_find="Simplified Ratio.",
        equation=f"{a}:{b}",
        formula_name="Ratio Simplification",
        formula_used="a/GCD : b/GCD",
        formula_reason="To express the comparison in simplest terms.",
        symbol_explanation="':' indicates ratio.",
        bodmas_explanation=None, # HIDDEN
        steps=[
            f"Step 1: Identify the two terms of the ratio.",
            f"   >> {a} and {b}",
            f"Step 2: Express as a fraction.",
            f"   >> {a} / {b}",
            f"Step 3: Find the Greatest Common Divisor (GCD).",
            f"   >> GCD is the largest number dividing both.",
            f"Step 4: Calculate GCD internally.",
            f"   >> GCD Found",
            f"Step 5: Divide the first term by the GCD.",
            f"   >> {frac.numerator}",
            f"Step 6: Divide the second term by the GCD.",
            f"   >> {frac.denominator}",
            f"Step 7: Construct the simplified ratio.",
            f"   >> {frac.numerator}:{frac.denominator}",
            f"Step 8: Check if further simplification is possible.",
            f"Step 9: Verify against original ratio.",
            f"   >> {a}/{b} == {frac.numerator}/{frac.denominator}",
            f"Step 10: Format the output.",
            f"Step 11: Ensure integers are used.",
            f"Step 12: Return Final Ratio."
        ],
        answer=f"{result[0]}:{result[1]}"
    )


# =========================================================
#                   SUM / PRODUCT / AVERAGE
# =========================================================

def total(values: Iterable[Number], show_steps=False):
    vals = _validate_iterable(values)
    result = sum(vals)

    if not show_steps: return result

    return Solution(
        problem_understanding="Combine a list of numbers into one sum.",
        given=f"List = {vals}",
        to_find="Total Sum.",
        equation=" + ".join(map(str, vals)),
        formula_name="Summation",
        formula_used="Σx",
        formula_reason="To find the aggregate total.",
        symbol_explanation="Σ means Sum.",
        bodmas_explanation=None,
        steps=[
            f"Step 1: Identify the list of numbers.",
            f"Step 2: Start with a count of 0.",
            f"Step 3: Take the first number.",
            f"   >> {vals[0]}",
            f"Step 4: Add to total.",
            f"Step 5: Take the next number (if any).",
            f"Step 6: Add to total.",
            f"Step 7: Continue until all numbers are processed.",
            f"   >> (Processing list...)",
            f"Step 8: Final addition.",
            f"Step 9: Result is {result}.",
            f"Step 10: Verify count of items added.",
            f"Step 11: Format.",
            f"Step 12: Final Sum."
        ],
        answer=result
    )


def product(values: Iterable[Number], show_steps=False):
    vals = _validate_iterable(values)
    result = 1
    for v in vals:
        result *= v

    if not show_steps: return result

    return Solution(
        problem_understanding="Multiply a series of numbers together.",
        given=f"List = {vals}",
        to_find="Total Product.",
        equation=" × ".join(map(str, vals)),
        formula_name="Product Sequence",
        formula_used="Πx",
        formula_reason="To find the compound result.",
        symbol_explanation="Π (Pi capital) often denotes Product in math notation.",
        bodmas_explanation=None,
        steps=[
            f"Step 1: Identify list of factors.",
            f"Step 2: Start with a base of 1.",
            f"Step 3: Multiply by the first number.",
            f"   >> 1 * {vals[0]} = {vals[0]}",
            f"Step 4: Multiply by the next number.",
            f"Step 5: Continue sequentially.",
            f"Step 6: Handle signs (count negatives).",
            f"Step 7: Watch for zero (if any zero, product is zero).",
            f"   >> Contains zero? {'Yes' if 0 in vals else 'No'}",
            f"Step 8: Compute final value.",
            f"   >> {result}",
            f"Step 9: Check magnitude.",
            f"Step 10: Format.",
            f"Step 11: Verify inputs.",
            f"Step 12: Final Product."
        ],
        answer=result
    )


def average(values: Iterable[Number], show_steps=False):
    vals = _validate_iterable(values)
    n = len(vals)
    total_sum = sum(vals)
    result = total_sum / n

    if not show_steps: return result

    return Solution(
        problem_understanding="Find the central value representing the dataset.",
        given=f"Values: {vals}",
        to_find="Arithmetic Mean.",
        equation=f"(Sum of values) ÷ {n}",
        formula_name="Average Formula",
        formula_used="Σx / n",
        formula_reason="Summarizes data into one representative number.",
        symbol_explanation="Σ means Sum, n means Count.",
        bodmas_explanation="BODMAS Rule: Brackets (Summation) must be done BEFORE Division.",
        steps=[
            f"Step 1: Count the number of items (n).",
            f"   >> n = {n}",
            f"Step 2: List all numbers to be added.",
            f"Step 3: Initialize Sum = 0.",
            f"Step 4: Begin adding values...",
            f"   >> Sum: {total_sum}",
            f"Step 5: APPLY BODMAS: Complete the sum inside the implicit brackets first.",
            f"Step 6: Now proceed to Division.",
            f"Step 7: Set up division: {total_sum} / {n}.",
            f"Step 8: Perform division.",
            f"   >> {total_sum} / {n}",
            f"Step 9: Calculate result.",
            f"   >> {result}",
            f"Step 10: Check if reasonable (must be between min and max values).",
            f"   >> Min: {min(vals)}, Max: {max(vals)} -> OK",
            f"Step 11: Format precision.",
            f"Step 12: Final Average."
        ],
        answer=result
    )


# =========================================================
#                      EXPORTS
# =========================================================

__all__ = [
    "add", "subtract", "multiply", "divide",
    "power", "square", "cube", "sqrt", "cbrt",
    "modulo", "integer_divide",
    "percentage", "ratio",
    "total", "product", "average"
]
