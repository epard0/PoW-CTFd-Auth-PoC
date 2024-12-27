import unittest
import json
import hashlib
import os
from PoW.solver import ProofOfWorkSolver


class TestProofOfWorkSolver(unittest.TestCase):
    @staticmethod
    def _verify_solution(solution: str, token_hex: str, difficulty: int) -> bool:
        """
        Verifies if the solution concatenated with the token produces
        a hash starting with the required number of leading zeroes.
        """
        token = bytes.fromhex(token_hex)
        hash_result = hashlib.sha256(solution.encode('utf-8') + token).hexdigest()
        return hash_result.startswith('0' * difficulty)

    def _load_test_data(self, file_path: str):
        """
        Loads test data from a JSON file containing a JSON array of challenges.
        """
        with open(file_path, 'r') as f:
            return json.load(f)  # Load the entire JSON array


    def test_solver_challenge_4(self):
        """
        Test ProofOfWorkSolver against difficulty 4 challenges.
        """
        solver = ProofOfWorkSolver()
        file_path = os.path.join("test_data", "challenge_4.json")
        test_cases = self._load_test_data(file_path)

        for case in test_cases:
            token = case["token"]
            difficulty = case["difficulty"]
            solution = solver.solve(token, difficulty=difficulty)
            self.assertIsNotNone(solution, "Solver did not find a solution")
            self.assertTrue(
                self._verify_solution(solution, token, difficulty),
                f"Solution {solution} for token {token} did not meet difficulty {difficulty}"
            )

    def test_solver_challenge_6(self):
        """
        Test ProofOfWorkSolver against difficulty 6 challenges.
        """
        solver = ProofOfWorkSolver()
        file_path = os.path.join("test_data", "challenge_6.json")
        test_cases = self._load_test_data(file_path)

        for case in test_cases:
            token = case["token"]
            difficulty = case["difficulty"]
            solution = solver.solve(token, difficulty=difficulty)
            self.assertIsNotNone(solution, "Solver did not find a solution")
            self.assertTrue(
                self._verify_solution(solution, token, difficulty),
                f"Solution {solution} for token {token} did not meet difficulty {difficulty}"
            )

    def test_solver_challenge_8(self):
        """
        Test ProofOfWorkSolver against difficulty 8 challenges.
        """
        solver = ProofOfWorkSolver()
        file_path = os.path.join("test_data", "challenge_8.json")
        test_cases = self._load_test_data(file_path)

        for case in test_cases:
            token = case["token"]
            difficulty = case["difficulty"]
            solution = solver.solve(token, difficulty=difficulty)
            self.assertIsNotNone(solution, "Solver did not find a solution")
            self.assertTrue(
                self._verify_solution(solution, token, difficulty),
                f"Solution {solution} for token {token} did not meet difficulty {difficulty}"
            )


if __name__ == "__main__":
    unittest.main()
