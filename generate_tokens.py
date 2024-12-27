import os
import json

def generate_challenge(prefix_length: int = 8, pow_difficulty: int = 4):
    token = os.urandom(prefix_length).hex()
    return {
        "token": token,
        "difficulty": pow_difficulty
    }

if __name__ == "__main__":
    os.makedirs("test_data", exist_ok=True)
    
    for difficulty, filename in [(4, "challenge_4.json"), (6, "challenge_6.json"), (8, "challenge_8.json")]:
        challenges = [generate_challenge(prefix_length=8, pow_difficulty=difficulty) for _ in range(101)]
        with open(f"test_data/{filename}", "w") as f:
            json.dump(challenges, f, indent=4)
