from pronunciation_engine.instruction_generator import generate_instruction
from pronunciation_engine.normalizer import normalize_instruction

for _ in range(5):

    instruction = generate_instruction()

    normalized = normalize_instruction(instruction)

    print("RAW:        ", instruction)
    print("NORMALIZED: ", normalized)
    print()