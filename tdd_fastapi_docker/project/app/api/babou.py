from fastapi import APIRouter

from pydantic import BaseModel

router = APIRouter()


class BabouPayloadSchema(BaseModel):
    message: str

class BabouResponseSchema(BaseModel):
    response: str


@router.post("/", response_model=BabouResponseSchema)
async def respond_to_babou(payload: BabouPayloadSchema) -> BabouResponseSchema:
    """
    Secret babou endpoint
    """
    msg = payload.message
    if not msg:
        raise HTTPException(status_code=404, detail="Oh noes, no message was found babou!")
    return {
        "response": (
            f"Hello babou, I received your message: '{msg}'"
            f"It had {len(msg.split(' '))} words. Love you very much!"
        )
    }