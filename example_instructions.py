"""
Original example instructions for BigCodeLLM-FT-Proj.

This file is original to this project and does not reproduce the
copyrighted example_instructions.py from meta-llama/codellama
(Copyright Meta Platforms, Inc., Llama 2 Community License).
To view that upstream file, see:
https://github.com/meta-llama/codellama/blob/main/example_instructions.py
Use that original only in accordance with its license terms.
"""

EXAMPLE_INSTRUCTIONS = [
    {"role": "user", "content": "Write a Python function that returns the sum of a list of numbers."},
    {"role": "user", "content": "Explain how to list files in a directory using Python standard library functions."},
]


def main():
    for instruction in EXAMPLE_INSTRUCTIONS:
        print(f"{instruction[role]}: {instruction[content]}")


if __name__ == "__main__":
    main()
