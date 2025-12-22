from PIL import Image, ImageChops, ImageColor


face_state = {
    "face_shape": "oval_01",
    "features" : {
        "eyes": {"id": "eye_01", "x": 250, "y": 200, "scale_x": 1.0, "scale_y": 1.0},
        "nose": {"id": "nose_01", "x": 250, "y": 300, "scale": 1.0},
        "mouth" : {"id": "mouth_01", "x": 250, "y": 400, "scale": 1.0},

        "hair" : {
            "id": "hair_01",
            "colour": "brown",
            "colour_rgb" : (60, 40, 30),
            "scale": 1.0,
            "layer_order" : 10
        }
    }
}

def apply_hair_colour(hair, colour_rgb):
    colour_layer = Image.new("RGBA", hair.size, colour_rgb + (255,))
    #Fill inside sketch lines with colour
    tinted_hair = ImageChops.multiply(hair, colour_layer)
    #Restore original transparent(alpha) mask
    tinted_hair.putalpha(hair.getchannel('A'))

    return tinted_hair

def draw_face(state, asset_path):
    canvas = Image.new("RGBA", (800, 800), (255, 255, 255, 255))

    face_shape = Image.open(f"{asset_path}/faces/{state['face_shape_id']}.png").convert("RGBA")
    canvas.paste(face_shape, (0, 0), face_shape)

    eye_data = state['features']['eyes']
    eye = Image.open(f"{asset_path}/eyes/{eye_data['id']}.png").convert("RGBA")
    eye_pos = (eye_data['x'], eye_data['y'])
    canvas.paste(eye, eye_pos, eye)

    mouth_data = state['features']['mouth']
    mouth = Image.open(f"{asset_path}/mouth/{mouth_data['id']}.png").convert("RGBA")
    mouth_pos = (mouth_data['x'], mouth_data['y'])
    canvas.paste(mouth, mouth_pos, mouth)

    nose_data = state['features']['nose']
    nose = Image.open(f"{asset_path}/nose/{nose_data['id']}.png").convert("RGBA")
    nose_pos = (nose_data['x'], nose_data['y'])
    canvas.paste(nose, nose_pos, nose)

    hair_data = state['features']['hair']
    hair = Image.open(f"{asset_path}/hair/{hair_data['id']}.png").convert("RGBA")
    coloured_hair = apply_hair_colour(hair, hair_data['colour_rgb'])

    #resize hair if needed
    if hair_data['scale'] != 1.0:
        new_size = (int(coloured_hair.width * hair_data['scale']), int(coloured_hair.height * hair_data['scale']))
        coloured_hair = coloured_hair.resize(new_size, Image.LANCZOS)

    canvas.paste(coloured_hair, (0,0), coloured_hair)

    return canvas

