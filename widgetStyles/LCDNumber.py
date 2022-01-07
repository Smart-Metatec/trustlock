import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from widgetStyles.styles import color, mode, default

LCDNumber = f"""

    QLCDNumber{{
    background-color: {mode};
    border: 2px solid {color};
    border-width: 2px;
    border-radius: 10px;
    color: {color};
    }}
"""