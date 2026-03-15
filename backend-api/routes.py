from fastapi import APIRouter
from schemas import Instruction
from pronunciation_engine.normalizer import normalize_instruction

router = APIRouter()

@router.post("/normalize")
def normalize(data: Instruction):
    result = normalize_instruction(data.instruction)
    return {"normalized": result}