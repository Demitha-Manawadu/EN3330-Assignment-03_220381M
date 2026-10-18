# EN3330 Assignment 03 - Source Code

**Module:** EN3330 - Introduction to Engineering Optimization  
**Student:** Manawadu M.D  
**Index Number:** 220381M

This repository contains the Python code used to generate the plots included in Assignment 03.

## Contents

- `generate_plots.py` - generates all figures in one run.
- `source/q1a_lagrangian.py` - Q1(a): Lagrangian curves for mu = 0, 1, 2, 3.
- `source/q1b_dual.py` - Q1(b): dual function and dual optimum.
- `source/q1c_primal.py` - Q1(c): extended-valued primal function.
- `source/q2a_saddle.py` - Q2(a): saddle-point plots.
- `source/q3b_lower_envelope.py` - Q3(b): lower-envelope illustration and exact dual function.
- `plots/` - the generated PNG figures used in the report.

The PNG plots are already included in this package. Running the Python code again will regenerate and overwrite the corresponding files inside `plots/`.

## Requirements

```bash
pip install -r requirements.txt
```

## Generate all plots

From the repository root, run:

```bash
python generate_plots.py
```

All five figures will be saved automatically in the `plots/` folder.

## Generate a single plot

For example:

```bash
python source/q1a_lagrangian.py
```

The individual scripts also save their output to the same `plots/` folder.
