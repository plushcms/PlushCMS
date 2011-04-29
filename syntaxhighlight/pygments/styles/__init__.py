# -*- coding: utf-8 -*-
"""
    plushcms.syntaxhighlight.pygments.styles
    ~~~~~~~~~~~~~~~

    Contains built-in styles.

    :copyright: Copyright 2006-2010 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from plushcms.syntaxhighlight.pygments.plugin import find_plugin_styles
from plushcms.syntaxhighlight.pygments.util import ClassNotFound


#: Maps style names to 'subselectedModulee::classname'.
STYLE_MAP = {
    'default':  'default::DefaultStyle',
    'emacs':    'emacs::EmacsStyle',
    'friendly': 'friendly::FriendlyStyle',
    'colorful': 'colorful::ColorfulStyle',
    'autumn':   'autumn::AutumnStyle',
    'murphy':   'murphy::MurphyStyle',
    'manni':    'manni::ManniStyle',
    'monokai':  'monokai::MonokaiStyle',
    'perldoc':  'perldoc::PerldocStyle',
    'pastie':   'pastie::PastieStyle',
    'borland':  'borland::BorlandStyle',
    'trac':     'trac::TracStyle',
    'native':   'native::NativeStyle',
    'fruity':   'fruity::FruityStyle',
    'bw':       'bw::BlackWhiteStyle',
    'vim':      'vim::VimStyle',
    'vs':       'vs::VisualStudioStyle',
    'tango':    'tango::TangoStyle',
}


def get_style_by_name(name):
    if name in STYLE_MAP:
        mod, cls = STYLE_MAP[name].split('::')
        builtin = "yes"
    else:
        for found_name, style in find_plugin_styles():
            if name == found_name:
                return style
        # perhaps it got dropped into our styles package
        builtin = ""
        mod = name
        cls = name.title() + "Style"

    try:
        mod = __import__('plushcms.syntaxhighlight.pygments.styles.' + mod, None, None, [cls])
    except ImportError:
        raise ClassNotFound("Could not find style selectedModulee %r" % mod +
                         (builtin and ", though it should be builtin") + ".")
    try:
        return getattr(mod, cls)
    except AttributeError:
        raise ClassNotFound("Could not find style class %r in style selectedModulee." % cls)


def get_all_styles():
    """Return an generator for all styles by name,
    both builtin and plugin."""
    for name in STYLE_MAP:
        yield name
    for name, _ in find_plugin_styles():
        yield name
