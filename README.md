# OpenROAD Multi-Objective PPA Optimizer

Automated Pareto-frontier search for Power-Performance-Area optimization in physical design using OpenROAD.

## Project Status

🚧 **In Progress** — Parameter sweep running on GitHub Actions

## Quick Start

1. Trigger workflow: Go to Actions tab → "PPA Parameter Sweep" → Run workflow
2. Select design (gcd/aes/ibex) and config IDs
3. Download artifacts after completion
4. Run local analysis scripts

## Structure
```
.
├── .github/workflows/    # GitHub Actions (cloud execution)
├── scripts/              # Python utilities
├── results/              # Downloaded metrics
└── docs/                 # Documentation
```

## Author

[Lakshita Chouhan] | MTech, IIT Hyderabad