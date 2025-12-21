# \# bip2-primitive

# 

# \[!\[DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18004196.svg)](https://doi.org/10.5281/zenodo.18004196)

# 

# \## 🔒 Status: Frozen Primitive (v1.0)

# 

# This repository contains the \*\*frozen reference implementation\*\* of the BIP-2

# deterministic receipt primitive.

# 

# The primitive is \*\*immutable\*\*, \*\*content-agnostic\*\*, and \*\*deterministic\*\*.

# It performs no interpretation, policy enforcement, or platform logic.

# 

# Any system-level behavior must be layered \*outside\* this repository.

# 

# ---

# 

# \## What This Is

# 

# \- A deterministic computation primitive

# \- Content-agnostic

# \- Reproducible across environments

# \- Suitable for cryptographic verification and audit trails

# 

# ---

# 

# \## What This Is Not

# 

# \- Not a policy engine

# \- Not an authority

# \- Not a platform

# \- Not mutable after v1.0

# 

# ---

# 

# \## Verification

# 

# Independent verification instructions are provided in \[`VERIFY.md`](VERIFY.md).

# 

# Determinism has been empirically verified using repeated execution with identical

# inputs producing identical outputs.

# 

# ---

# 

# \## Frozen Primitive Methodology (FPM)

# 

# This repository follows the Frozen Primitive Methodology:

# 

# \- Immutable computation core

# \- No side effects

# \- No external state

# \- No interpretation layer

# 

# Extensions must import this primitive without modification.

# 

# ---

# 

# \## Citation

# 

# Vallejos, D. (2025).  

# \*The Frozen Primitive Methodology: Deterministic Computation via Immutable Primitives\*.  

# Zenodo.  

# https://doi.org/10.5281/zenodo.18004196

# 

# ---

# 

# \## License

# 

# MIT License. See \[`LICENSE`](LICENSE).



