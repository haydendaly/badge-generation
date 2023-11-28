from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import numpy as np

df = pd.read_csv('badges.csv', sep=',')

def add_text_to_image(image_path, text, output_path):
    image = Image.open(image_path)
    back_image = Image.open('./templates/back.png')
    new_image = Image.new('RGB', (image.width + back_image.width, image.height), (0, 0, 0))
    new_image.paste(image, (0, 0))
    new_image.paste(back_image, (image.width, 0))
    draw = ImageDraw.Draw(new_image)

    font_large = ImageFont.truetype('OpenSans-Bold.ttf', size=80, layout_engine=ImageFont.LAYOUT_RAQM)
    font_small = ImageFont.truetype('OpenSans-Semibold.ttf', size=64, layout_engine=ImageFont.LAYOUT_RAQM)

    if pd.isnull(text):
        new_image.save(output_path)
        return
    else:
        name_parts = text.split(' ', 1)
        first_name = name_parts[0].capitalize()
        rest_of_name = "".join([sub for sub in name_parts[1:] if sub != ""]) if len(name_parts) > 1 else ''

        text_position_first_name = (80, 480)
        text_position_rest_of_name = (80, 570)

        draw.text(text_position_first_name, first_name, font=font_large, fill="white")
        draw.text(text_position_rest_of_name, rest_of_name, font=font_small, fill="white")

        new_image.save(output_path)

for index, row in df.iterrows():
    try:
        image_path = f"./templates/{row['Role'].lower()}.png"
        if pd.isnull(row['Name']):
            output_path = f"./output/{row['Role'].lower()}_blank_{index+1}.png"
        else:
            output_path = f"./output/{row['Role'].lower()}_{row['Name'].replace(' ', '_')}.png"
        add_text_to_image(image_path, row['Name'], output_path)
    except Exception as e:
        print(e)
        print(f"Failed to generate badge for {row['Name']}")