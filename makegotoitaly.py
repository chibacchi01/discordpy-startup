# coding: utf-8
from PIL import Image, ImageFont, ImageDraw
#import cv2
import numpy as np
import sys

# 画像に文字を入れる関数
def img_add_msg(img, message, fontcolor = "#FF5555", fontsize = 30, isShadow = False):
    shadowcolor = '#222222'
    font_path = './fonts/Noto.otf' # Windowsのフォントファイルへのパス
    font_size = fontsize    # フォントサイズ
    fontcustom = ImageFont.truetype(font_path, font_size, 0, encoding='utf-8') # PILでフォントを定義
    # mask = Image.open("./images/ejimasu_stamp_alpha.png")
    img = Image.open(img)
    bg = Image.new("RGBA", (320,320), (0,0,0,0))
    # bg.paste(img,(0,0),mask.split()[0])
    # textch = Image.new("RGBA", img.size,(0,0,0,0))
    draw = ImageDraw.Draw(bg) # 描画用のDraw関数を用意
    w , h = draw.textsize(message, font=fontcustom)
    # テキストを描画（位置、文章、フォント、文字色（BGR+α）を指定）
    x = (320 - w)/2
    y = 250
    if (isShadow):
        draw.text((x+1, y+1), message, font=fontcustom, fill=shadowcolor)
        draw.text((x-1, y-1), message, font=fontcustom, fill=shadowcolor)
        draw.text((x+1, y-1), message, font=fontcustom, fill=shadowcolor)
        draw.text((x-1, y+1), message, font=fontcustom, fill=shadowcolor)
    draw.text((x, y), message, font=fontcustom, fill=fontcolor)
    bg.paste(img,(0,0),img)
    # textch = np.array(textch) # PIL型の画像をcv2(NumPy)型に変換
    return bg # 文字入りの画像をリターン