import pygame


class MediaLoader:
    def __init__(self):
        ...

    def load_image(self, path: str) -> pygame.Surface:
        try:
            image = pygame.image.load(path)
        except FileNotFoundError:
            return None
        return image

    def crop_image_for_scaling(self, image: pygame.Surface, size: tuple[int, int]) -> pygame.Surface:
        w, h = size
        scale = w / h  # desired scale

        current_scale = image.get_width() / image.get_height()

        #rescales image to correct one
        if current_scale > scale:
            image = image.subsurface((
                (image.get_width() - int(image.get_height() * scale)) // 2,
                0,
                int(image.get_height() * scale),
                image.get_height()
            ))

        return image

    def load_image_to_size(self, path: str, size: tuple[int, int]) -> pygame.Surface:
        image = self.load_image(path)

        if image is None:
            return None

        image = self.crop_image_for_scaling(image, size)
        image = pygame.transform.smoothscale(image, size)
        return image
