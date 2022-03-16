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

lighten = lambda hx: hexscale(hx, 1.2)
darken  = lambda hx: hexscale(hx, 0.9)

def hexalpha(hexcode, alpha):
    r, g, b = webcolors.hex_to_rgb(hexcode)
    return f'rgba({r}, {g}, {b}, {alpha})'

class NordDark(Style):
    default_style = ''
    background_color = colors.polar_night.darker
    highlight_color = lighten(colors.polar_night.dark)
    styles = {
        Generic :                colors.snow_storm.lightest,
        Punctuation :            colors.snow_storm.lightest,
        Operator :               colors.snow_storm.lightest,
        Comment :                'italic ' + colors.snow_storm.light,
        Comment.Preproc :        'noitalic ' + colors.snow_storm.lightest,
        Comment.PreprocFile :    'noitalic ' + colors.snow_storm.lightest,
        Keyword :                'bold ' + colors.frost.light,
        Operator.Word :          colors.frost.light,
        Number :                 darken(colors.aurora.purple),
        Name :                   colors.snow_storm.lightest,
        Name.Builtin :           'bold ' + colors.frost.light,
        Name.Constant :          colors.aurora.red,
        Name.Function :          colors.frost.greenish,
        Name.Class :             colors.frost.greenish,
        Name.Namespace :         colors.aurora.yellow,
        String :                 darken(colors.aurora.green),
        String.Escape :          darken(colors.aurora.orange),
    }

# vim: set ft=python:
