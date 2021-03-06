import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from widgetStyles.styles import color, mode, default, light_blue

# #bbb grey
# #66e purple
# #bbf light purple
# #55f dark purple
HSlider = f"""
    QSlider::groove:horizontal {{
    border: 1px solid #bbb;
    background: white;
    height: 10px;
    border-radius: 4px;
    }}

    QSlider::sub-page:horizontal {{
        background: {light_blue};
        background: {light_blue};
        border: 1px solid #777;
        height: 10px;
        border-radius: 4px;
    }}

    QSlider::add-page:horizontal {{
        background: #fff;
        border: 1px solid #777;
        height: 10px;
        border-radius: 4px;
    }}

    QSlider::handle:horizontal {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #eee, stop:1 #ccc);
        border: 1px solid #777;
        width: 13px;
        margin-top: -2px;
        margin-bottom: -2px;
        border-radius: 4px;
    }}

    QSlider::handle:horizontal:hover {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #fff, stop:1 #ddd);
        border: 1px solid #444;
        border-radius: 4px;
    }}

    QSlider::sub-page:horizontal:disabled {{
        background: #bbb;
        border-color: #999;
    }}

    QSlider::add-page:horizontal:disabled {{
        background: #eee;
        border-color: #999;
    }}

    QSlider::handle:horizontal:disabled {{
        background: #eee;
        border: 1px solid #aaa;
        border-radius: 4px;
}}
    """