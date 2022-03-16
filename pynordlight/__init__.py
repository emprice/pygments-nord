from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

import colorsys
import webcolors
from pynord import colors

def scale_lightness(rgb, scale):
    ''' https://stackoverflow.com/a/60562502/1552418 '''
    # convert rgb to hls
    h, l, s = colorsys.rgb_to_hls(*rgb)
    # manipulate h, l, s values and return as rgb
    return colorsys.hls_to_rgb(h, min(1, l * scale), s=s)

def hexscale(hexcode, scale):
    rgb = webcolors.hex_to_rgb(hexcode)
    rgb = tuple(map(lambda x: x / 255, rgb))
    scaled = scale_lightness(rgb, scale)
    scaled = tuple(map(lambda x: int(x * 255), scaled))
    return webcolors.rgb_to_hex(scaled)

lighten = lambda hx: hexscale(hx, 1.1)
darken  = lambda hx: hexscale(hx, 0.7)

def hexalpha(hexcode, alpha):
    r, g, b = webcolors.hex_to_rgb(hexcode)
    return f'rgba({r}, {g}, {b}, {alpha})'

class NordLight(Style):
    default_style = ''
    background_color = colors.snow_storm.lightest
    highlight_color = hexalpha(lighten(colors.aurora.yellow), 0.5)
    styles = {
        Generic :                colors.polar_night.darkest,
        Comment :                'italic ' + colors.polar_night.med,
        Comment.Preproc :        'noitalic ' + colors.polar_night.darkest,
        Comment.PreprocFile :    'noitalic ' + colors.polar_night.darkest,
        Keyword :                colors.frost.dark,
        Operator.Word :          colors.frost.dark,
        Name.Builtin :           colors.frost.dark,
        Number :                 darken(colors.aurora.purple),
        Name.Constant :          colors.aurora.red,
        Name.Function :          colors.frost.med,
        Name.Class :             colors.frost.med,
        Name.Namespace :         colors.frost.med,
        String :                 darken(colors.aurora.green),
        String.Escape :          darken(colors.aurora.orange),
    }

# vim: set ft=python:
