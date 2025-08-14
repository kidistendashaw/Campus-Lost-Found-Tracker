from ninja import Router, File, Schema, UploadedFile
from typing import Optional
from .models import Item, ItemImage

api = Router()


class ItemSchema(Schema):
    id: int
    title: str
    description: str
    status: str
    location: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None


@api.post("/items/", response=ItemSchema)
def create_item(
    request,
    title: str,
    description: str,
    status: str,
    location: str,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    image: UploadedFile = File(...),
):
    item = Item.objects.create(
        title=title,
        description=description,
        status=status,
        location=location,
        latitude=latitude,
        longitude=longitude,
    )
    ItemImage.objects.create(item=item, image=image)
    return item
