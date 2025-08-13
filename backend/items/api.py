class ItemSchema(Schema):
    id: int
    title: str
    description: str
    status: str
    location: str
    latitude: float | None
    longitude: float | None


@api.post("/items/", response=ItemSchema)
def create_item(
    request,
    title: str,
    description: str,
    status: str,
    location: str,
    latitude: float = None,
    longitude: float = None,
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
