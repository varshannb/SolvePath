# solvepath/solution.py
"""
==========================================================
                    SolvePath Solution Object
==========================================================

Core container for step-by-step mathematical solutions.

Design goals:
• SAFE (no auto printing, no side effects)
• Human-readable
• Teacher-style explanation
• Backward compatible
• Future-proof

Supports:
• Problem Understanding
• Given Information
• What Needs to be Found
• Equation
• Formula Name
• Formula Used
• Formula Explanation
• Why the Formula is Used
• Symbol Meaning Explanation
• BODMAS Explanation
• Step-by-step Solution
• Final Answer
• Mathematical Constants (π support)

==========================================================
"""


# ==========================================================
# IMMUTABLE STEPS CONTAINER (CRITICAL FOR TESTS)
# ==========================================================

class _ImmutableSteps(tuple):
    """
    Immutable tuple-like container for solution steps.
    Any mutation attempt raises TypeError (NOT AttributeError).
    """

    def append(self, *_):
        raise TypeError("Solution steps are immutable and cannot be modified")

    def extend(self, *_):
        raise TypeError("Solution steps are immutable and cannot be modified")

    def insert(self, *_):
        raise TypeError("Solution steps are immutable and cannot be modified")

    def remove(self, *_):
        raise TypeError("Solution steps are immutable and cannot be modified")

    def pop(self, *_):
        raise TypeError("Solution steps are immutable and cannot be modified")


# ==========================================================
# SOLUTION OBJECT
# ==========================================================

class Solution:
    """
    Standard container for step-by-step math solutions.
    """

    def __init__(
        self,
        equation,
        formula=None,
        steps=None,
        answer=None,
        *,
        # --- Teaching blueprint (optional)
        problem_understanding=None,
        given=None,
        to_find=None,
        bodmas_explanation=None,

        # --- Formula intelligence
        formula_name=None,
        formula_used=None,
        explanation=None,
        symbol_explanation=None,
        formula_reason=None,

        # --- Mathematical constants
        constants_used=None,
    ):
        # --------------------------------------------------
        # Validation
        # --------------------------------------------------
        if not equation:
            raise ValueError("equation must be a non-empty value")

        # --------------------------------------------------
        # Teaching blueprint
        # --------------------------------------------------
        self.problem_understanding = problem_understanding
        self.given = given
        self.to_find = to_find
        self.bodmas_explanation = bodmas_explanation

        # --------------------------------------------------
        # Core information
        # --------------------------------------------------
        self.equation = equation

        # Backward compatibility
        self.formula_name = formula_name
        self.formula_used = formula_used or formula

        # --------------------------------------------------
        # Teaching explanations
        # --------------------------------------------------
        self.explanation = explanation
        self.formula_reason = formula_reason
        self.symbol_explanation = symbol_explanation

        # --------------------------------------------------
        # Constants
        # --------------------------------------------------
        self.constants_used = constants_used or {}

        # --------------------------------------------------
        # Steps & Answer (IMMUTABLE)
        # --------------------------------------------------
        self._steps = _ImmutableSteps(steps or [])
        self.answer = answer

    # --------------------------------------------------
    # Immutable steps access
    # --------------------------------------------------
    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):
        raise TypeError("Solution steps are immutable and cannot be reassigned")

    # --------------------------------------------------
    # Human-readable output
    # --------------------------------------------------
    def __str__(self):
        lines = []

        if self.problem_understanding:
            lines.append("Problem Understanding :")
            lines.append(f"  {self.problem_understanding}")

        if self.given:
            lines.append("Given :")
            lines.append(f"  {self.given}")

        if self.to_find:
            lines.append("To Find :")
            lines.append(f"  {self.to_find}")

        lines.append(f"Equation : {self.equation}")

        if self.formula_name:
            lines.append(f"Formula Name : {self.formula_name}")

        if self.formula_used:
            lines.append(f"Formula Used : {self.formula_used}")

        if self.formula_reason:
            lines.append(f"Why this formula is used : {self.formula_reason}")

        if self.symbol_explanation:
            lines.append("Symbols Meaning :")
            lines.append(f"  {self.symbol_explanation}")

        if self.explanation:
            lines.append("Formula Explanation :")
            lines.append(f"  {self.explanation}")

        if self.bodmas_explanation:
            lines.append("BODMAS Explanation :")
            lines.append(f"  {self.bodmas_explanation}")

        if self.constants_used:
            lines.append("Constants Used :")
            for k, v in self.constants_used.items():
                lines.append(f"  {k} : {v}")

        lines.append("Solution :")
        if self.steps:
            for step in self.steps:
                lines.append(f"  {step}")
        else:
            lines.append("  Step 1: (No steps provided)")

        if self.answer is not None:
            lines.append(f"Final Answer : {self.answer}")
        else:
            lines.append("Final Answer : (No final answer provided)")

        return "\n".join(lines)

    # --------------------------------------------------
    # Debug representation
    # --------------------------------------------------
    def __repr__(self):
        return (
            "Solution("
            f"equation={self.equation!r}, "
            f"formula_used={self.formula_used!r}, "
            f"steps={len(self.steps)} steps, "
            f"answer={self.answer!r})"
        )

    # --------------------------------------------------
    # Validation helper
    # --------------------------------------------------
    def validate(self):
        if not self.equation:
            raise ValueError("Equation is missing")
        if not self.steps:
            raise ValueError("Solution steps are missing")
        if self.answer is None:
            raise ValueError("Final answer is missing")
        return True

    # --------------------------------------------------
    # Summary (API / UI use)
    # --------------------------------------------------
    def summary(self):
        return {
            "equation": self.equation,
            "formula_used": self.formula_used,
            "answer": self.answer,
        }

    # --------------------------------------------------
    # Dictionary export
    # --------------------------------------------------
    def to_dict(self):
        return {
            "problem_understanding": self.problem_understanding,
            "given": self.given,
            "to_find": self.to_find,
            "equation": self.equation,
            "formula_name": self.formula_name,
            "formula_used": self.formula_used,
            "formula_reason": self.formula_reason,
            "symbol_explanation": self.symbol_explanation,
            "explanation": self.explanation,
            "bodmas_explanation": self.bodmas_explanation,
            "constants_used": self.constants_used,
            "steps": list(self.steps),
            "answer": self.answer,
        }


__all__ = ["Solution"]
