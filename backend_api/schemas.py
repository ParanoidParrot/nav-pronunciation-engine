from pydantic import BaseModel

class Instruction(BaseModel):
    instruction: str