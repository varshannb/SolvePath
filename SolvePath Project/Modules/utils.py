# solvepath/utils.py
"""
=========================================================
                    SolvePath Utils
=========================================================

Purpose:
• Lightweight helper utilities
• Backward compatibility for old modules
• NO printing
• NO evaluation logic
• NO formatting logic

NOTE:
New modules should use solvepath.solution.Solution directly.
"""

from typing import List, Tuple, Union

Number = Union[int, float]


# =========================================================
# LEGACY RESULT WRAPPER (BACKWARD COMPATIBILITY)
# =========================================================

def _with_steps(result, steps: List[str], show_steps: bool):
    """
    Legacy helper.

    If show_steps=True:
        returns (result, steps)
    else:
        return result

    NOTE:
    New SolvePath modules should NOT use this.
    """
    return (result, steps) if show_steps else result


# =========================================================
# EXPORT
# =========================================================

__all__ = ["_with_steps"]
