# BigCodeLLM-FT-Proj - Example Instructions
# This is an original file created for the fine-tuning framework.
# For reference, see the original example from meta-llama/codellama:
# https://github.com/meta-llama/codellama/blob/main/example_instructions.py
# The original is licensed under the Llama 2 Community License.
# https://github.com/facebookresearch/llama/blob/main/LICENSE

from typing import List, Dict

def get_example_instructions() -> List[List[Dict[str, str]]]:
    """Return example instructions for fine-tuning."""
    return [
        [{"role": "user", "content": "Explain how to fine-tune a code LLM."}],
        [{"role": "user", "content": "Write a Python function to sort a list."}],
    ]

if __name__ == "__main__":
    for instr in get_example_instructions():
        print(instr)
