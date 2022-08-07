from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Punctuation, Generic

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
        Punctuation :            colors.polar_night.darkest,
        Operator :               colors.polar_night.darkest,
        Comment :                'italic ' + colors.polar_night.med,
        Comment.Preproc :        'bold noitalic ' + darken(colors.aurora.purple),
        Comment.PreprocFile :    'nobold noitalic ' + darken(colors.aurora.purple),
        Keyword :                colors.frost.dark,
        Operator.Word :          colors.frost.dark,
        Number :                 darken(colors.aurora.purple),
        Name :                   colors.polar_night.darkest,
        Name.Builtin :           'bold  ' + colors.frost.dark,
        Name.Constant :          colors.aurora.red,
        Name.Function :          colors.frost.greenish,
        Name.Class :             colors.frost.greenish,
        Name.Namespace :         darken(colors.aurora.yellow),
        String :                 darken(colors.aurora.green),
        String.Escape :          darken(colors.aurora.orange),
    }

# vim: set ft=python:
