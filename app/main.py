from fastapi import FastAPI, APIRouter, Depends
from starlette.requests import Request
from .api.models import Word
from .api.jumble import jumble_word

app = FastAPI()
api_router = APIRouter()

audit_queue = []

@api_router.get("/")
async def root():
    return {"message": "Welcome to Tim's Glia API"}

@api_router.post("/jumble")
async def jumble(word: Word):
    return jumble_word(word)

@api_router.get("/audit")
async def audit():
    return audit_queue

async def log_json(request: Request):
    if len(audit_queue) >= 10:
        audit_queue.pop(0)
    endpoint = request.url.path
    if request.method == "POST":
        payload = await request.json()
    else:
        payload = request.query_params
    audit_queue.append({"endpoint": endpoint, "payload": payload})

def reset_audit_queue():
    global audit_queue
    audit_queue = []
    return

app.include_router(api_router, dependencies=[Depends(log_json)])