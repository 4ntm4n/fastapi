from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_items():
    return [{"item_id": "1", "item_name": "Item 1"}, {"item_id": "2", "item_name": "Item 2"}]