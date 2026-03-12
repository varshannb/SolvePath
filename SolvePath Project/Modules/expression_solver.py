# solvepath/expression_solver.py
"""
=========================================================
              SolvePath Expression Solver Module
=========================================================

Secure, AST-based arithmetic expression solver with
HIGHLY DETAILED, TUTOR-STYLE step-by-step explanations.

Supports:
• Basic Ops: +, -, *, /, //, %, **
• Exponents: ^ (converted to **)
• Grouping: ( ) brackets
• Unary Ops: -5, +3

Features:
• Enforces BODMAS/PEMDAS automatically via AST
• Secure (No eval())
• Detailed breakdown of calculation order

Returns:
• Solution object when show_steps=True
• Final result when show_steps=False

=========================================================
"""

from __future__ import annotations
import ast
import operator
from typing import List, Union
from solvepath.solution import Solution

Number = Union[int, float]

# =========================================================
# OPERATOR MAPS
# =========================================================

_BIN_OPS = {
    ast.Add: (operator.add, "+", "Addition"),
    ast.Sub: (operator.sub, "-", "Subtraction"),
    ast.Mult: (operator.mul, "*", "Multiplication"),
    ast.Div: (operator.truediv, "/", "Division"),
    ast.FloorDiv: (operator.floordiv, "//", "Floor Division"),
    ast.Mod: (operator.mod, "%", "Modulus"),
    ast.Pow: (operator.pow, "^", "Exponentiation"),
}

_UNARY_OPS = {
    ast.UAdd: (operator.pos, "+", "Unary Plus"),
    ast.USub: (operator.neg, "-", "Unary Negation"),
}

_ALLOWED_NODES = (
    ast.Expression,
    ast.BinOp,
    ast.UnaryOp,
    ast.Constant,
)

# =========================================================
# CUSTOM ERROR
# =========================================================

class UnsafeExpressionError(ValueError):
    pass

# =========================================================
# PREPARE EXPRESSION
# =========================================================

def _prepare_expression(expr: str) -> str:
    """
    Replace ^ with ** so Python AST understands exponentiation.
    """
    return expr.replace("^", "**").strip()

# =========================================================
# AST SAFETY CHECK
# =========================================================

def _check_ast(node: ast.AST):
    """
    Ensure only safe mathematical nodes are used.
    """
    if isinstance(node, _ALLOWED_NODES):
        pass
    elif isinstance(node, (
        ast.Add, ast.Sub, ast.Mult, ast.Div,
        ast.FloorDiv, ast.Mod, ast.Pow,
        ast.UAdd, ast.USub
    )):
        pass
    else:
        raise UnsafeExpressionError(
            f"Disallowed syntax: {node.__class__.__name__}"
        )

    for child in ast.iter_child_nodes(node):
        if isinstance(child, (
            ast.Name, ast.Call, ast.Attribute,
            ast.Subscript, ast.Lambda,
            ast.ListComp, ast.DictComp,
            ast.SetComp, ast.GeneratorExp
        )):
            raise UnsafeExpressionError(
                f"Disallowed construct: {child.__class__.__name__}"
            )
        _check_ast(child)

# =========================================================
# AST EVALUATION (RECURSIVE, STEP-BY-STEP)
# =========================================================

def _eval_node(node: ast.AST, steps: List[str], counter: List[int]) -> Number:
    """
    Recursively evaluate AST nodes following BODMAS.
    The recursion inherently respects the order of operations.
    """

    # ------------------------------
    # NUMBER (Leaf Node)
    # ------------------------------
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise UnsafeExpressionError("Only numeric values are allowed")

    # ------------------------------
    # UNARY OPERATION (-5)
    # ------------------------------
    if isinstance(node, ast.UnaryOp):
        func, sym, name = _UNARY_OPS[type(node.op)]
        
        # Evaluate operand first
        value = _eval_node(node.operand, steps, counter)
        
        # Calculate result
        result = func(value)

        counter[0] += 1
        steps.append(
            f"Step {counter[0]}: Perform {name}.\n"
            f"   Operation: {sym}({value})\n"
            f"   Result: {result}"
        )
        return result

    # ------------------------------
    # BINARY OPERATION (5 + 3)
    # ------------------------------
    if isinstance(node, ast.BinOp):
        func, sym, name = _BIN_OPS[type(node.op)]

        # The AST structure ensures BODMAS.
        # We must evaluate children before the current node.
        
        # 1. Evaluate Left Child
        left = _eval_node(node.left, steps, counter)
        
        # 2. Evaluate Right Child
        right = _eval_node(node.right, steps, counter)

        # Safety Check for Division
        if sym in ("/", "//", "%") and right == 0:
            raise ZeroDivisionError("Division by zero is undefined.")

        # 3. Calculate Result
        result = func(left, right)

        counter[0] += 1
        steps.append(
            f"Step {counter[0]}: Perform {name}.\n"
            f"   Equation: {left} {sym} {right}\n"
            f"   Result: {result}"
        )
        return result

    raise UnsafeExpressionError(
        f"Unsupported AST node: {node.__class__.__name__}"
    )

# =========================================================
# PUBLIC API
# =========================================================

def solve_expression(expr: str, show_steps: bool = False):
    """
    Safely evaluate a mathematical expression
    using AST and BODMAS order.
    """

    if not isinstance(expr, str):
        raise TypeError("Expression must be a string")

    prepared = _prepare_expression(expr)

    # Block variables explicitly (security layer)
    for ch in prepared:
        if ch.isalpha():
            raise UnsafeExpressionError("Variables (letters) are not allowed. Only numbers.")

    try:
        tree = ast.parse(prepared, mode="eval")
    except SyntaxError as e:
        raise ValueError(f"Invalid expression syntax: {e}")

    # Validate AST structure
    _check_ast(tree)

    # Initialize tracking
    steps: List[str] = [
        f"Problem: Evaluate '{expr}'",
        "Strategy: We use the Abstract Syntax Tree (AST) to enforce BODMAS logic.",
        "   1. Brackets ( )",
        "   2. Orders (Exponents ^)",
        "   3. Division / Multiplication",
        "   4. Addition / Subtraction"
    ]

    counter = [0]

    # Perform Evaluation
    result = _eval_node(tree.body, steps, counter)

    if not show_steps:
        return result

    return Solution(
        given=expr,
        to_find="Final Value",
        equation=expr,
        formula_name="Order of Operations (BODMAS)",
        formula_used="B -> O -> D/M -> A/S",
        formula_reason="Calculations must be performed in a specific hierarchy to be correct.",
        explanation="We decompose the expression into a tree structure where higher-priority operations (like *) are closer to the bottom (leaves) and solved first.",
        steps=steps,
        answer=result
    )

# =========================================================
# EXPORT
# =========================================================

__all__ = ["solve_expression"]
