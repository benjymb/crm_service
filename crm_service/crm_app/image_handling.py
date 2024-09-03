import base64
from PIL import Image
from io import BytesIO
from .exceptions import ImageHandlingError
from django.core.files.base import ContentFile as DjangoFile

def process_image(data, filename):
    try:
        im = Image.open(BytesIO(base64.b64decode(data)))
        return DjangoFile(im.tobytes(), f'{filename}.{im.format.lower()}')
    except Exception as e:
        raise ImageHandlingError(str(e))