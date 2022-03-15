from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic
from pynord import colors

class NordLight(Style):
    default_style = ''
    background_color = colors.snow_storm.lightest
    highlight_color = colors.aurora.yellow
    styles = {
        Generic :                colors.polar_night.darkest,
        Comment :                'italic ' + colors.polar_night.med,
        Keyword :                colors.frost.dark,
        Operator.Word :          colors.frost.dark,
        Name.Builtin :           colors.frost.dark,
        Number :                 colors.aurora.purple,
        Name.Constant :          colors.aurora.red,
        Name.Function :          colors.frost.med,
        Name.Class :             colors.frost.med,
        Name.Namespace :         colors.frost.med,
        String :                 colors.aurora.green,
        String.Escape :          colors.aurora.orange
    }

# vim: set ft=python:
