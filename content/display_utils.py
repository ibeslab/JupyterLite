# -*- coding: utf-8 -*-
"""
Shared display helper used by the const_coeff_* / ode_solvers modules to
mimic Maple's `print(a, b, c, ...)` style of mixing text and math on one
line.

Uses IPython's rich display (so SymPy objects render as typeset math in
Jupyter/Spyder with init_printing() active) when available, and falls
back to plain print() so the same code also runs as a bare script or
anywhere IPython isn't present.
"""

try:
    from IPython.display import display
    _HAVE_IPYTHON_DISPLAY = True
except ImportError:
    _HAVE_IPYTHON_DISPLAY = False


def mprint(*args):
    """Mixed print/display: renders each argument with IPython's display()
    when available, otherwise falls back to print()."""
    if _HAVE_IPYTHON_DISPLAY:
        for a in args:
            display(a)
    else:
        print(*args)
