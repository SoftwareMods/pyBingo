from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json
from pathlib import Path

sessions_file = 'data/sessions.json'
game_types_file = 'data/game_types.json'
settings_file = 'data/settings.json'

def saveJSONToFile(json_file,json_obj):
    Path(json_file).write_text(json.dumps(json_obj))
    return True

def loadJSONFromFile(json_file):
    return json.loads(Path(json_file).read_text())

def getNewId(mylist):
    """ Get unused or new id """
    ids = []

    if len(mylist) == 0:
        return 1

    # Get all used ids
    for e in mylist:
        ids.append(e['id'])

    # Put them in order so we can get the last
    # one later if needed
    ids.sort()

    # Get list of missing ids within range of list
    missing_ids = [ele for ele in range(1,max(ids) + 1) if ele not in ids]

    # If there are missing ids, get the first one missing
    # else get the last used id and increase by 1
    if len(missing_ids) > 0:
        this_id = missing_ids[0]
    else:
        this_id = ids[-1] + 1

    return this_id

def mask_image(imgdata, imgtype="png", size=64):
        # Load image
        image = QImage.fromData(imgdata, imgtype)

        # convert image to 32-bit ARGB (adds an alpha
        # channel ie transparency factor):
        image.convertToFormat(QImage.Format_ARGB32)

        # Crop image to a square:
        imgsize = min(image.width(), image.height())
        rect = QRect(
            int((image.width() - imgsize) / 2),
            int((image.height() - imgsize) / 2),
            imgsize,
            imgsize,
        )

        image = image.copy(rect)

        # Create the output image with the same dimensions
        # and an alpha channel and make it completely transparent:
        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)

        # Create a texture brush and paint a circle
        # with the original image onto the output image:
        brush = QBrush(image)

        # Paint the output image
        painter = QPainter(out_img)
        painter.setBrush(brush)

        # Don't draw an outline
        painter.setPen(Qt.NoPen)

        # drawing circle
        painter.drawEllipse(0, 0, imgsize, imgsize)

        # closing painter event
        painter.end()

        # Convert the image to a pixmap and rescale it.
        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size *= pr
        size = int(size)
        pm = pm.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # return back the pixmap data
        return pm

def setPayoutText(txt):
    return f'Payout<br><span style="color: blue; font-weight: bold;">{txt}</span>'

def getNumbersCalledText(curr, max=None):
    show_max = ""
    if max:
        show_max = f"/{max}"
    return f'Numbers Called<br><span style="color: blue; font-weight: bold;">{curr}{show_max}</span>'

def setPreviousNumCalledText(num):
    return f'Previous Number<br><span style="color: blue; font-weight: bold; font-size: 16px;">{num}</span>'

def setGameNumberText(num, total=None):
    show_total = ""
    if total:
        show_total = f" / {total}"
    return f'Game Number<br><span style="color: blue; font-weight: bold;">{num}{show_total}</span>'

