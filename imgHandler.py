from PIL import Image

class ImgHandler():
    def __init__(self, image_path):
        self.image = self.open("/img/test.jpg")
        self.width, self.height = self.image.size
