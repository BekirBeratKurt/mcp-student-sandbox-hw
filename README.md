# Mystery Module - Quadratic Equation Solver

## Overview
The `mystery_module.py` file contains a function that solves quadratic equations using the **quadratic formula**. This module is designed as a homework assignment to demonstrate understanding of mathematical problem-solving and Python implementation.

## Mathematical Background

A quadratic equation has the standard form:
```
ax² + bx + c = 0
```

Where:
- **a**, **b**, and **c** are coefficients (constants)
- **x** is the variable we're solving for

### The Quadratic Formula

The solutions to a quadratic equation are found using:

```
x = (-b ± √(b² - 4ac)) / 2a
```

The expression under the square root, **b² - 4ac**, is called the **discriminant** (Δ):
- If Δ > 0: Two distinct real solutions
- If Δ = 0: One repeated real solution
- If Δ < 0: No real solutions (complex solutions exist)

## Function Description

### `fn_x(a, b, c)`

Solves the quadratic equation ax² + bx + c = 0

**Parameters:**
- `a` (float): Coefficient of x²
- `b` (float): Coefficient of x
- `c` (float): Constant term

**Returns:**
- Tuple of two floats: The two solutions (x₁, x₂)
- `None`: If the discriminant is negative (no real solutions)

## Usage Examples

```python
from mystery_module import fn_x

# Example 1: Equation with two distinct solutions
# x² - 5x + 6 = 0  →  (x-2)(x-3) = 0
result = fn_x(1, -5, 6)
print(result)  # Output: (3.0, 2.0)

# Example 2: Equation with one solution (perfect square)
# x² - 4x + 4 = 0  →  (x-2)² = 0
result = fn_x(1, -4, 4)
print(result)  # Output: (2.0, 2.0)

# Example 3: Equation with no real solutions
# x² + 1 = 0
result = fn_x(1, 0, 1)
print(result)  # Output: None

# Example 4: Standard form equation
# 2x² + 3x - 2 = 0
result = fn_x(2, 3, -2)
print(result)  # Output: (0.5, -2.0)
```

## Key Features

- ✅ Handles all three cases of the discriminant
- ✅ Accurate mathematical computation using Python's math library
- ✅ Simple and straightforward API
- ✅ Educational resource for learning the quadratic formula

## Notes

- Ensure that coefficient **a ≠ 0** (otherwise it's not a quadratic equation)
- The function returns solutions in numerical form
- For equations with no real solutions (negative discriminant), the function returns `None`

---

*This module is part of the mcp-student-sandbox-hw assignment.*
