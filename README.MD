# Data Structures with Python

A collection of beginner-to-intermediate Python exercises focused on **variables, input/output, conditionals, loops, and basic algorithms**. Each file `ex1.py` ... `ex10.py` is a small standalone program that solves one specific problem.

This repository is part of my learning journey ("ENSETM - Data Structures") and is also a template for how I organize and publish future Python projects.

---

## Project Structure

```
Data_Structures_Python/
│
├── README.MD        # This documentation file
│
├── ex1.py           # User profile — reads name, surname, age, city and prints a greeting
├── ex2.py           # Simple calculator — +, -, *, / using a menu loop and match/case
├── ex3.py           # Time converter — converts a number of days into years, weeks and days
├── ex4.py           # Square root — computes the square root of a float (rejects negatives)
├── ex5.py           # BMI calculator — computes IMC and interprets the result
├── ex6.py           # Pressure/Volume monitor — checks sensors against thresholds
├── ex7.py           # for loop — prints numbers from 0 to 15 with a step of 3
├── ex8.py           # for loop with continue — skips the value 5
├── ex9.py           # Integer square root — finds the largest integer whose square root is whole
└── ex10.py          # while loops — counts up and down with conditions
```

---

## File Descriptions

| File | Concept practiced | Description |
|------|-------------------|-------------|
| `ex1.py` | `input`, `int`, f-strings | Asks for personal information and prints a formatted introduction. |
| `ex2.py` | `while`, `match/case` | Menu-driven calculator for the four basic operations. |
| `ex3.py` | Integer division `//`, modulo `%` | Converts a total number of days into years, weeks and days. |
| `ex4.py` | `if/else`, exponent `**` | Computes the square root of a number, handling negatives. |
| `ex5.py` | `if/elif/else` | Body Mass Index (IMC) with health interpretation. |
| `ex6.py` | Boolean conditions (`and`) | Checks pressure and volume against safety thresholds. |
| `ex7.py` | `for` with `range(start, stop, step)` | Iterates with a custom step. |
| `ex8.py` | `for` with `continue` | Skips one iteration inside a loop. |
| `ex9.py` | `while` | Finds a whole-number square root by decrementing. |
| `ex10.py` | `while` | Counts up and down using loop conditions. |

---

## Requirements

- **Python 3.10+** is required because `ex2.py` uses the `match/case` statement.
- No external libraries are needed — everything uses the **standard library**.

---

## How to Run

1. Make sure Python is installed:
   ```bash
   python --version
   ```

2. Run any exercise from the project folder:
   ```bash
   python ex1.py
   ```
   On Windows you may need:
   ```bash
   py ex1.py
   ```

3. Follow the on-screen prompts (each program asks for input).

---

## Optional: Virtual Environment

Although these exercises need no dependencies, using a virtual environment is good practice for future projects:

```bash
pip install virtualenv
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux
```

---

## Learning Goals

- Reading user input and converting types
- Making decisions with `if / elif / else` and `match`
- Repeating actions with `for` and `while`
- Writing clear, formatted output with f-strings
- Solving small algorithmic problems

---

## Notes

- Google Classroom code: `ftaf2uzs`
- Each file is independent and can be run on its own.
- This README doubles as a reusable template for future Python projects.

---

## Author

Personal learning repository. Feel free to explore and learn from the exercises.
