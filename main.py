import os
from script import create_collage_with_percentage_padding

from dotenv import load_dotenv

load_dotenv()
path_to_folder = os.getenv("path_to_folder")
collage_width = int(os.getenv("collage_width"))
collage_height = int(os.getenv("collage_height"))
all_formats_image = {"JPEG": "JPEG", "PNG": "PNG", "TIFF": "TIFF", "SVG": "SVG"}


class ListPath:
    def __init__(self) -> None:
        self.ls = set()

    def walk_file(self, path) -> set:
        for i in os.listdir(path):
            point_index = f'{path}/{i}'.find(".")
            if os.path.isdir(f'{path}/{i}'):
                self.walk_file(f'{path}/{i}')
            elif f'{path}/{i}'.upper()[point_index + 1:] in all_formats_image:
                self.ls.add(f'{path}/{i}')
        return self.ls


if __name__ == "__main__":
    make_ls = ListPath()
    image_files = make_ls.walk_file(path=path_to_folder)
    collage = create_collage_with_percentage_padding(image_files, collage_width,
                                                     collage_height)
    collage.save(os.path.join(path_to_folder, 'collage.jpg'))
