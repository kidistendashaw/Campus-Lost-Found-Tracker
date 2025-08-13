from ninja import NinjaAPI, Schema, File
from ninja.files import UploadedFile
from .models import Item, ItemImage

api = NinjaAPI()


class ItemSchema(Schema):
    id: int
    title: str
    description: str
    status: str
    location: str


@api.post("/items/", response=ItemSchema)
def create_item(
    request,
    title: str,
    description: str,
    status: str,
    location: str,
    image: UploadedFile = File(...),
):
    item = Item.objects.create(
        title=title, description=description, status=status, location=location
    )
    ItemImage.objects.create(item=item, image=image)
    return item
