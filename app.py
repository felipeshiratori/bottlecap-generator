import sys
import os
import io

from flask import Flask, send_file, request
from flask_restful import Resource, Api
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

app = Flask(__name__)
api = Api(app)

class Bottlecap(Resource):
    def get(self):
        return self.generate()

    def generate(self):
        pincode = request.args.get("pincode")
        img = Image.open("bottlecap_white_template.jpg")
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype("font.ttf", 32)
        draw.text((225, 356), pincode[:7], (55,70,47),font=font)
        draw.text((225, 386), pincode[7:], (55,70,47),font=font)

        imgIO = io.BytesIO()
        img.save(imgIO, 'JPEG', quality=100)
        imgIO.seek(0)
        return send_file(imgIO, mimetype='image/jpeg')

api.add_resource(Bottlecap, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=42000)
