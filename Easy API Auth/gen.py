from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ApprovalRequest(BaseModel):
    status: str

@app.post("/check-approval/")
async def check_approval(request: ApprovalRequest):
    if request.status.lower() == "15":
        return {"message": "Sim bonitão, o você está aprovado"}
    return {"message": "Negado"}


#uvicorn script_geradora:app --reload
