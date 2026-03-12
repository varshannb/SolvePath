# solvepath/__init__.py

"""
SolvePath package initializer.

Automatically imports public symbols from all SolvePath modules
based on their __all__ definitions.

Defensive importing ensures:
- missing modules do not break the package
- partially implemented modules are ignored safely
"""

from __future__ import annotations

import importlib

__version__ = "0.1.0"
__author__ = "Varshan"

# List of all modules to attempt importing
_expected_submodules = [
    "utils",
    "arithmetic",
    "algebra",
    "geometry",
    "trigonometry",
    "calculus",
    "linear_algebra",
    "vectors",
    "probability",
    "statistics",
    "number_theory",
    "complex_numbers",
    "transforms",
    "differential_equations",
    "discrete_math",
    "set_theory",
    "theorems",
    "expression_solver",
    "activation",
]

# ✅ IMPORTANT FIX:
# When `importlib.reload(solvepath)` runs, Python re-executes this file
# but does NOT automatically remove old attributes from the module.
# So we must manually delete previously exported symbols.
_old_exports = globals().get("__all__", [])
if isinstance(_old_exports, list):
    for _name in list(_old_exports):
        if _name in globals():
            del globals()[_name]

# Fresh public export list
__all__ = []

# Dynamic import loop
for mod_name in _expected_submodules:
    try:
        # Import using relative path (e.g., .arithmetic) relative to 'solvepath'
        mod = importlib.import_module(f".{mod_name}", package=__name__)

        # If the module defines __all__, expose those symbols
        module_all = getattr(mod, "__all__", None)
        if not module_all:
            continue

        for symbol in module_all:
            # Avoid overwriting existing symbols
            if symbol in globals():
                continue

            # Bring the symbol into the package namespace
            try:
                val = getattr(mod, symbol)
            except AttributeError:
                # Symbol listed in __all__ but not actually defined
                continue

            globals()[symbol] = val
            __all__.append(symbol)

    except (ImportError, ModuleNotFoundError):
        # Module doesn't exist yet or has an error; skip it gracefully
        continue
