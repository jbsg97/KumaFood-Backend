from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Product"],
)

@router.get("/")
async def show_products():
    return [{"id":1,"product": "Korean Soup"}, {"id":2,"product": "Korean Candy"}]
