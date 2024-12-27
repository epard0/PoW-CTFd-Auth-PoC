# Proof of Work Authentication Proof of Concept

> Project Status: *Beta*

This project was inspired by a similar project from another CTF I had played in a while ago, I simply took the concept/idea and implemented it for my needs. I plan to further develop this project and make it more robust and secure. Hopefully one day even integrating directly into the CTFd platform via a plugin.

I don't remember which CTF it was specifically, but when I do I'll update this README to give proper credit where it's due.

## Installation

1. Clone the repository

```bash
git clone https://github.com/supasuge/PoW-CTFd-Auth-PoC.git
```

2. Install the package + Dependencies

```bash
cd PoW-CTFd-Auth-PoC
pip install .
```

3. For newer versions of python, you may need to first create a virtual environment and install the dependencies in there to keep it isolated from your system installation.

```bash
python -m venv env
source env/bin/activate
pip install .
# OR for windows
python -m venv env
env\Scripts\activate
pip install .
```

---

## Usage

```python
from PoW.solver import ProofOfWorkSolver
solver = ProofOfWorkSolver(num_threads=8, pow_difficulty=4)
token_hex = "abc123"
solution = solver.solve(token_hex, pow_difficulty=4)
if solution:
    print(solution)
else:
    print("No solution found")
```

---

### How it works

In a Proof-of-Work (PoW) challenge, the server generates a **16-character hexadecimal string** (`token`) and specifies a **difficulty** level, which determines the number of leading `0`s required in the hash. The user must find an **alphanumeric string** (`[a-z0-9]`) such that the SHA-256 hash of `alphanum + token` satisfies the condition:

```
sha256(alphanum + token).hexdigest() == 0000.... (number of leading 0's based on difficulty)
```

The user solves the challenge by brute-forcing potential `alphanum` strings until a valid hash is found. Once found, the solution is submitted to the server for verification.

---

#### Step-By-Step Overview

- **Server:**
  - Generates a random 16-character `token`.
  - Specifies the number of leading `0`s required in the hash (e.g., `difficulty = 4`).
- **User:**
  - Brute-forces alphanumeric strings.
  - Computes `sha256(alphanum + token).hexdigest()` for each string.
  - Submits a solution when the hash meets the required difficulty.
- **Server:**
  - Verifies the submitted solution by recomputing the hash.

---

##### TODO

- [ ] Add a CLI Interface to the module
- [ ] Add a simplified interface to use with pwntools.
- [ ] Add a properly formatted plugin for CTFd.
- [ ] Add a plugin to use with Flask.


---
