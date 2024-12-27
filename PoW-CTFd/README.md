# Beta Proof of Work Authentication Proof of Concept

This project was inspired by a similar project from another CTF I had played in a while ago, I simply took the concept/idea and implemented it for my needs. I plan to further develop this project and make it more robust and secure. Hopefully one day even integrating directly into the CTFd platform via a plugin.

I don't remember which CTF it was specifically, but when I do I'll update this README to give proper credit where it's due.

## Installation

1. Clone the repository

```bash
git clone https://github.com/supasuge/ProofOfWorkAuthenticator-Beta.git
```

2. Install the package + Dependencies

```bash
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

## TODO

- [ ] Add a CLI Interface to the module
- [ ] Add a simplified interface to use with pwntools.
- [ ] Add a properly formatted plugin for CTFd.
- [ ] Add a plugin to use with Flask.


