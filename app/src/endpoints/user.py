from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["User"],
)

@router.get("/")
async def show_users():
    return [{"id": 1}, {"id": 2}]
