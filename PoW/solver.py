#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: supsuge (Evan Pardon)
import hashlib
import random
import string
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from dataclasses import dataclass

@dataclass
class COLOR:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    END = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"


class ProofOfWorkSolver:
    def __init__(self, chars=None, num_threads=8, pow_difficulty=4):
        self.chars = chars or string.ascii_lowercase + string.digits
        self.num_threads = num_threads
        self.pow_difficulty = pow_difficulty

    def _sha256_hex(self, s: str, token: bytes) -> str:
        """Compute SHA-256 hash of the input string concatenated with the token."""
        return hashlib.sha256(s.encode('utf-8') + token).hexdigest()

    def _worker(self, token: bytes, difficulty: int, found_solution, stop_event):
        """Worker function to find a solution meeting the difficulty requirement."""
        target = '0' * difficulty
        while not stop_event.is_set():
            length = random.randint(1, 10)  # Random lengths from 1 to 10
            guess = ''.join(random.choice(self.chars) for _ in range(length))
            h = self._sha256_hex(guess, token)
            if h.startswith(target):
                print(f"{COLOR.GREEN}Found solution:{COLOR.END}{COLOR.BOLD} {guess} (Hash: {h}){COLOR.END}")
                found_solution["value"] = guess
                stop_event.set()
                return

    def solve(self, token_hex: str, difficulty=None) -> str:
        """Solve the proof-of-work challenge given a token."""
        token = bytes.fromhex(token_hex)  
        difficulty = difficulty or self.pow_difficulty
        found_solution = {"value": None}
        stop_event = threading.Event()

        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = []
            for _ in range(self.num_threads):
                futures.append(executor.submit(self._worker, token, difficulty, found_solution, stop_event))

            for fut in as_completed(futures):
                if found_solution["value"] is not None:
                    return found_solution["value"]

        return None


# Example usage as a script
'''
from .solver import ProofOfWorkSolver
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{COLOR.RED}Usage: python3 {sys.argv[0]} <token_hex>{COLOR.END}")
        sys.exit(1)

    token_hex = sys.argv[1]
    start = time.perf_counter()
    pow_solver = ProofOfWorkSolver(num_threads=8, pow_difficulty=4)
    solution = pow_solver.solve(token_hex, difficulty=4)
    end = time.perf_counter()

    if solution:
        print(f"{COLOR.GREEN}Solution:{COLOR.END}{COLOR.BOLD} {solution}{COLOR.END}")
    else:
        print(f"{COLOR.RED}No solution found.{COLOR.END}")
    print(f"{COLOR.YELLOW}Time taken: {end - start:.2f} seconds{COLOR.END}")
'''