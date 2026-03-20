from pydantic import BaseModel

class Instruction(BaseModel):
    instruction: str

class DemoCompareResponse(BaseModel):
    original_text: str
    normalized_text: str
    original_audio_url: str
    normalized_audio_url: str
    