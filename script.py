from PIL import Image


def create_collage_with_percentage_padding(image_files, collage_width, collage_height, padding_percent=0.05):
    # Вычисляем отступ в пикселях
    padding = int(min(collage_width, collage_height) * padding_percent)

    # Загружаем все изображения
    images = []
    for img_file in image_files:
        try:
            img = Image.open(img_file)
            images.append(img)
        except Exception as e:
            print(f"Error loading image {img_file}: {e}")

    # Определяем размер каждого изображения в коллаже
    num_images = len(images)
    grid_size = int(num_images ** 0.5) + 1  # Определяем размер сетки
    img_width = (collage_width - padding * (grid_size + 1)) // grid_size
    img_height = (collage_height - padding * (grid_size + 1)) // grid_size

    # Создаем пустое изображение для коллажа
    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))

    # Вставляем каждое изображение в коллаж
    x_offset = padding
    y_offset = padding
    for img in images:
        # Изменяем размер изображения, сохраняя пропорции
        img.thumbnail((img_width, img_height))

        # Вставляем изображение в коллаж
        collage.paste(img, (x_offset, y_offset))

        x_offset += img_width + padding
        if x_offset + img_width + padding > collage_width:
            x_offset = padding
            y_offset += img_height + padding

    return collage
