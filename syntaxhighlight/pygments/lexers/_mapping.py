# -*- coding: utf-8 -*-
"""
    plushcms.syntaxhighlight.pygments.lexers._mapping
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer mapping defintions. This file is generated by itself. Everytime
    you change something on a builtin lexer defintion, run this script from
    the lexers folder to update it.

    Do not alter the LEXERS dictionary by hand.

    :copyright: Copyright 2006-2010 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

LEXERS = {
    'ABAPLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'ABAP', ('abap',), ('*.abap',), ('text/x-abap',)),
    'ActionScript3Lexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'ActionScript 3', ('as3', 'actionscript3'), ('*.as',), ('application/x-actionscript', 'text/x-actionscript', 'text/actionscript')),
    'ActionScriptLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'ActionScript', ('as', 'actionscript'), ('*.as',), ('application/x-actionscript', 'text/x-actionscript', 'text/actionscript')),
    'AdaLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Ada', ('ada', 'ada95ada2005'), ('*.adb', '*.ads', '*.ada'), ('text/x-ada',)),
    'AntlrActionScriptLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'ANTLR With ActionScript Target', ('antlr-as', 'antlr-actionscript'), ('*.G', '*.g'), ()),
    'AntlrCSharpLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'ANTLR With C# Target', ('antlr-csharp', 'antlr-c#'), ('*.G', '*.g'), ()),
    'AntlrCppLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'ANTLR With CPP Target', ('antlr-cpp',), ('*.G', '*.g'), ()),
    'AntlrJavaLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'ANTLR With Java Target', ('antlr-java',), ('*.G', '*.g'), ()),
    'AntlrLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'ANTLR', ('antlr',), (), ()),
    'AntlrObjectiveCLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'ANTLR With ObjectiveC Target', ('antlr-objc',), ('*.G', '*.g'), ()),
    'AntlrPerlLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'ANTLR With Perl Target', ('antlr-perl',), ('*.G', '*.g'), ()),
    'AntlrPythonLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'ANTLR With Python Target', ('antlr-python',), ('*.G', '*.g'), ()),
    'AntlrRubyLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'ANTLR With Ruby Target', ('antlr-ruby', 'antlr-rb'), ('*.G', '*.g'), ()),
    'ApacheConfLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'ApacheConf', ('apacheconf', 'aconf', 'apache'), ('.htaccess', 'apache.conf', 'apache2.conf'), ('text/x-apacheconf',)),
    'AppleScriptLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'AppleScript', ('applescript',), ('*.applescript',), ()),
    'AsymptoteLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Asymptote', ('asy', 'asymptote'), ('*.asy',), ('text/x-asymptote',)),
    'AutohotkeyLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'autohotkey', ('ahk',), ('*.ahk', '*.ahkl'), ('text/x-autohotkey',)),
    'AwkLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Awk', ('awk', 'gawk', 'mawk', 'nawk'), ('*.awk',), ('application/x-awk')),
    'BBCodeLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'BBCode', ('bbcode',), (), ('text/x-bbcode',)),
    'BaseMakefileLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Makefile', ('basemake',), (), ()),
    'BashLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Bash', ('bash', 'sh', 'ksh'), ('*.sh', '*.ksh', '*.bash', '*.ebuild', '*.eclass'), ('application/x-sh', 'application/x-shellscript')),
    'BashSessionLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Bash Session', ('console',), ('*.sh-session',), ('application/x-shell-session',)),
    'BatchLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Batchfile', ('bat',), ('*.bat', '*.cmd'), ('application/x-dos-batch',)),
    'BefungeLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Befunge', ('befunge',), ('*.befunge',), ('application/x-befunge',)),
    'BlitzMaxLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'BlitzMax', ('blitzmax', 'bmax'), ('*.bmx',), ('text/x-bmx',)),
    'BooLexer': ('plushcms.syntaxhighlight.pygments.lexers.dotnet', 'Boo', ('boo',), ('*.boo',), ('text/x-boo',)),
    'BrainfuckLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Brainfuck', ('brainfuck', 'bf'), ('*.bf', '*.b'), ('application/x-brainfuck',)),
    'CLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'C', ('c',), ('*.c', '*.h'), ('text/x-chdr', 'text/x-csrc')),
    'CMakeLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'CMake', ('cmake',), ('*.cmake', 'CMakeLists.txt'), ('text/x-cmake',)),
    'CObjdumpLexer': ('plushcms.syntaxhighlight.pygments.lexers.asm', 'c-objdump', ('c-objdump',), ('*.c-objdump',), ('text/x-c-objdump',)),
    'CSharpAspxLexer': ('plushcms.syntaxhighlight.pygments.lexers.dotnet', 'aspx-cs', ('aspx-cs',), ('*.aspx', '*.asax', '*.ascx', '*.ashx', '*.asmx', '*.axd'), ()),
    'CSharpLexer': ('plushcms.syntaxhighlight.pygments.lexers.dotnet', 'C#', ('csharp', 'c#'), ('*.cs',), ('text/x-csharp',)),
    'CheetahHtmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'HTML+Cheetah', ('html+cheetah', 'html+spitfire'), (), ('text/html+cheetah', 'text/html+spitfire')),
    'CheetahJavascriptLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'JavaScript+Cheetah', ('js+cheetah', 'javascript+cheetah', 'js+spitfire', 'javascript+spitfire'), (), ('application/x-javascript+cheetah', 'text/x-javascript+cheetah', 'text/javascript+cheetah', 'application/x-javascript+spitfire', 'text/x-javascript+spitfire', 'text/javascript+spitfire')),
    'CheetahLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Cheetah', ('cheetah', 'spitfire'), ('*.tmpl', '*.spt'), ('application/x-cheetah', 'application/x-spitfire')),
    'CheetahXmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'XML+Cheetah', ('xml+cheetah', 'xml+spitfire'), (), ('application/xml+cheetah', 'application/xml+spitfire')),
    'ClojureLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Clojure', ('clojure', 'clj'), ('*.clj',), ('text/x-clojure', 'application/x-clojure')),
    'CoffeeScriptLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'CoffeeScript', ('coffee-script', 'coffeescript'), ('*.coffee',), ('text/coffeescript',)),
    'ColdfusionHtmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Coldfusion HTML', ('cfm',), ('*.cfm', '*.cfml', '*.cfc'), ('application/x-coldfusion',)),
    'ColdfusionLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'cfstatement', ('cfs',), (), ()),
    'CommonLispLexer': ('plushcms.syntaxhighlight.pygments.lexers.functional', 'Common Lisp', ('common-lisp', 'cl'), ('*.cl', '*.lisp', '*.el'), ('text/x-common-lisp',)),
    'CppLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'C++', ('cpp', 'c++'), ('*.cpp', '*.hpp', '*.c++', '*.h++', '*.cc', '*.hh', '*.cxx', '*.hxx'), ('text/x-c++hdr', 'text/x-c++src')),
    'CppObjdumpLexer': ('plushcms.syntaxhighlight.pygments.lexers.asm', 'cpp-objdump', ('cpp-objdump', 'c++-objdumb', 'cxx-objdump'), ('*.cpp-objdump', '*.c++-objdump', '*.cxx-objdump'), ('text/x-cpp-objdump',)),
    'CssDjangoLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'CSS+Django/Jinja', ('css+django', 'css+jinja'), (), ('text/css+django', 'text/css+jinja')),
    'CssErbLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'CSS+Ruby', ('css+erb', 'css+ruby'), (), ('text/css+ruby',)),
    'CssGenshiLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'CSS+Genshi Text', ('css+genshitext', 'css+genshi'), (), ('text/css+genshi',)),
    'CssLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'CSS', ('css',), ('*.css',), ('text/css',)),
    'CssPhpLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'CSS+PHP', ('css+php',), (), ('text/css+php',)),
    'CssSmartyLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'CSS+Smarty', ('css+smarty',), (), ('text/css+smarty',)),
    'CythonLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Cython', ('cython', 'pyx'), ('*.pyx', '*.pxd', '*.pxi'), ('text/x-cython', 'application/x-cython')),
    'DLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'D', ('d',), ('*.d', '*.di'), ('text/x-dsrc',)),
    'DObjdumpLexer': ('plushcms.syntaxhighlight.pygments.lexers.asm', 'd-objdump', ('d-objdump',), ('*.d-objdump',), ('text/x-d-objdump',)),
    'DarcsPatchLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Darcs Patch', ('dpatch',), ('*.dpatch', '*.darcspatch'), ()),
    'DebianControlLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Debian Control file', ('control',), ('control',), ()),
    'DelphiLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Delphi', ('delphi', 'pas', 'pascal', 'objectpascal'), ('*.pas',), ('text/x-pascal',)),
    'DiffLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Diff', ('diff', 'udiff'), ('*.diff', '*.patch'), ('text/x-diff', 'text/x-patch')),
    'DjangoLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Django/Jinja', ('django', 'jinja'), (), ('application/x-django-templating', 'application/x-jinja')),
    'DuelLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'Duel', ('duel', 'Duel Engine', 'Duel View', 'JBST', 'jbst', 'JsonML+BST'), ('*.duel', '*.jbst'), ('text/x-duel', 'text/x-jbst')),
    'DylanLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Dylan', ('dylan',), ('*.dylan', '*.dyl'), ('text/x-dylan',)),
    'ErbLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'ERB', ('erb',), (), ('application/x-ruby-templating',)),
    'ErlangLexer': ('plushcms.syntaxhighlight.pygments.lexers.functional', 'Erlang', ('erlang',), ('*.erl', '*.hrl'), ('text/x-erlang',)),
    'ErlangShellLexer': ('plushcms.syntaxhighlight.pygments.lexers.functional', 'Erlang erl session', ('erl',), ('*.erl-sh',), ('text/x-erl-shellsession',)),
    'EvoqueHtmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'HTML+Evoque', ('html+evoque',), ('*.html',), ('text/html+evoque',)),
    'EvoqueLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Evoque', ('evoque',), ('*.evoque',), ('application/x-evoque',)),
    'EvoqueXmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'XML+Evoque', ('xml+evoque',), ('*.xml',), ('application/xml+evoque',)),
    'FactorLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Factor', ('factor',), ('*.factor',), ('text/x-factor',)),
    'FancyLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Fancy', ('fancy', 'fy'), ('*.fy', '*.fancypack'), ('text/x-fancysrc',)),
    'FelixLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Felix', ('felix', 'flx'), ('*.flx', '*.flxh'), ('text/x-felix',)),
    'FortranLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Fortran', ('fortran',), ('*.f', '*.f90'), ('text/x-fortran',)),
    'GLShaderLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'GLSL', ('glsl',), ('*.vert', '*.frag', '*.geo'), ('text/x-glslsrc',)),
    'GasLexer': ('plushcms.syntaxhighlight.pygments.lexers.asm', 'GAS', ('gas',), ('*.s', '*.S'), ('text/x-gas',)),
    'GenshiLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Genshi', ('genshi', 'kid', 'xml+genshi', 'xml+kid'), ('*.kid',), ('application/x-genshi', 'application/x-kid')),
    'GenshiTextLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Genshi Text', ('genshitext',), (), ('application/x-genshi-text', 'text/x-genshi')),
    'GettextLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Gettext Catalog', ('pot', 'po'), ('*.pot', '*.po'), ('application/x-gettext', 'text/x-gettext', 'text/gettext')),
    'GherkinLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Gherkin', ('Cucumber', 'cucumber', 'Gherkin', 'gherkin'), ('*.feature',), ('text/x-gherkin',)),
    'GnuplotLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Gnuplot', ('gnuplot',), ('*.plot', '*.plt'), ('text/x-gnuplot',)),
    'GoLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Go', ('go',), ('*.go',), ('text/x-gosrc',)),
    'GoodDataCLLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'GoodData-CL', ('gooddata-cl',), ('*.gdc',), ('text/x-gooddata-cl',)),
    'GroffLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Groff', ('groff', 'nroff', 'man'), ('*.[1234567]', '*.man'), ('application/x-troff', 'text/troff')),
    'HamlLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'Haml', ('haml', 'HAML'), ('*.haml',), ('text/x-haml',)),
    'HaskellLexer': ('plushcms.syntaxhighlight.pygments.lexers.functional', 'Haskell', ('haskell', 'hs'), ('*.hs',), ('text/x-haskell',)),
    'HaxeLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'haXe', ('hx', 'haXe'), ('*.hx',), ('text/haxe',)),
    'HtmlDjangoLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'HTML+Django/Jinja', ('html+django', 'html+jinja'), (), ('text/html+django', 'text/html+jinja')),
    'HtmlGenshiLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'HTML+Genshi', ('html+genshi', 'html+kid'), (), ('text/html+genshi',)),
    'HtmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'HTML', ('html',), ('*.html', '*.htm', '*.xhtml', '*.xslt'), ('text/html', 'application/xhtml+xml')),
    'HtmlPhpLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'HTML+PHP', ('html+php',), ('*.phtml',), ('application/x-php', 'application/x-httpd-php', 'application/x-httpd-php3', 'application/x-httpd-php4', 'application/x-httpd-php5')),
    'HtmlSmartyLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'HTML+Smarty', ('html+smarty',), (), ('text/html+smarty',)),
    'HybrisLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Hybris', ('hybris', 'hy'), ('*.hy', '*.hyb'), ('text/x-hybris', 'application/x-hybris')),
    'IniLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'INI', ('ini', 'cfg'), ('*.ini', '*.cfg'), ('text/x-ini',)),
    'IoLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Io', ('io',), ('*.io',), ('text/x-iosrc',)),
    'IokeLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Ioke', ('ioke', 'ik'), ('*.ik',), ('text/x-iokesrc',)),
    'IrcLogsLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'IRC logs', ('irc',), ('*.weechatlog',), ('text/x-irclog',)),
    'JadeLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'Jade', ('jade', 'JADE'), ('*.jade',), ('text/x-jade',)),
    'JavaLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Java', ('java',), ('*.java',), ('text/x-java',)),
    'JavascriptDjangoLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'JavaScript+Django/Jinja', ('js+django', 'javascript+django', 'js+jinja', 'javascript+jinja'), (), ('application/x-javascript+django', 'application/x-javascript+jinja', 'text/x-javascript+django', 'text/x-javascript+jinja', 'text/javascript+django', 'text/javascript+jinja')),
    'JavascriptErbLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'JavaScript+Ruby', ('js+erb', 'javascript+erb', 'js+ruby', 'javascript+ruby'), (), ('application/x-javascript+ruby', 'text/x-javascript+ruby', 'text/javascript+ruby')),
    'JavascriptGenshiLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'JavaScript+Genshi Text', ('js+genshitext', 'js+genshi', 'javascript+genshitext', 'javascript+genshi'), (), ('application/x-javascript+genshi', 'text/x-javascript+genshi', 'text/javascript+genshi')),
    'JavascriptLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'JavaScript', ('js', 'javascript'), ('*.js',), ('application/javascript', 'application/x-javascript', 'text/x-javascript', 'text/javascript')),
    'JavascriptPhpLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'JavaScript+PHP', ('js+php', 'javascript+php'), (), ('application/x-javascript+php', 'text/x-javascript+php', 'text/javascript+php')),
    'JavascriptSmartyLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'JavaScript+Smarty', ('js+smarty', 'javascript+smarty'), (), ('application/x-javascript+smarty', 'text/x-javascript+smarty', 'text/javascript+smarty')),
    'JspLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Java Server Page', ('jsp',), ('*.jsp',), ('application/x-jsp',)),
    'LighttpdConfLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Lighttpd configuration file', ('lighty', 'lighttpd'), (), ('text/x-lighttpd-conf',)),
    'LiterateHaskellLexer': ('plushcms.syntaxhighlight.pygments.lexers.functional', 'Literate Haskell', ('lhs', 'literate-haskell'), ('*.lhs',), ('text/x-literate-haskell',)),
    'LlvmLexer': ('plushcms.syntaxhighlight.pygments.lexers.asm', 'LLVM', ('llvm',), ('*.ll',), ('text/x-llvm',)),
    'LogtalkLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Logtalk', ('logtalk',), ('*.lgt',), ('text/x-logtalk',)),
    'LuaLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Lua', ('lua',), ('*.lua', '*.wlua'), ('text/x-lua', 'application/x-lua')),
    'MOOCodeLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'MOOCode', ('moocode',), ('*.moo',), ('text/x-moocode',)),
    'MakefileLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Makefile', ('make', 'makefile', 'mf', 'bsdmake'), ('*.mak', 'Makefile', 'makefile', 'Makefile.*', 'GNUmakefile'), ('text/x-makefile',)),
    'MakoCssLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'CSS+Mako', ('css+mako',), (), ('text/css+mako',)),
    'MakoHtmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'HTML+Mako', ('html+mako',), (), ('text/html+mako',)),
    'MakoJavascriptLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'JavaScript+Mako', ('js+mako', 'javascript+mako'), (), ('application/x-javascript+mako', 'text/x-javascript+mako', 'text/javascript+mako')),
    'MakoLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Mako', ('mako',), ('*.mao',), ('application/x-mako',)),
    'MakoXmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'XML+Mako', ('xml+mako',), (), ('application/xml+mako',)),
    'MaqlLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'MAQL', ('maql',), ('*.maql',), ('text/x-gooddata-maql', 'application/x-gooddata-maql')),
    'MasonLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Mason', ('mason',), ('*.m', '*.mhtml', '*.mc', '*.mi', 'autohandler', 'dhandler'), ('application/x-mason',)),
    'MatlabLexer': ('plushcms.syntaxhighlight.pygments.lexers.math', 'Matlab', ('matlab', 'octave'), ('*.m',), ('text/matlab',)),
    'MatlabSessionLexer': ('plushcms.syntaxhighlight.pygments.lexers.math', 'Matlab session', ('matlabsession',), (), ()),
    'MiniDLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'MiniD', ('minid',), ('*.md',), ('text/x-minidsrc',)),
    'ModelicaLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Modelica', ('modelica',), ('*.mo',), ('text/x-modelica',)),
    'Modula2Lexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Modula-2', ('selectedModulea2', 'm2'), ('*.def', '*.mod'), ('text/x-selectedModulea2',)),
    'MoinWikiLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'MoinMoin/Trac Wiki markup', ('trac-wiki', 'moin'), (), ('text/x-trac-wiki',)),
    'MuPADLexer': ('plushcms.syntaxhighlight.pygments.lexers.math', 'MuPAD', ('mupad',), ('*.mu',), ()),
    'MxmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'MXML', ('mxml',), ('*.mxml',), ()),
    'MySqlLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'MySQL', ('mysql',), (), ('text/x-mysql',)),
    'MyghtyCssLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'CSS+Myghty', ('css+myghty',), (), ('text/css+myghty',)),
    'MyghtyHtmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'HTML+Myghty', ('html+myghty',), (), ('text/html+myghty',)),
    'MyghtyJavascriptLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'JavaScript+Myghty', ('js+myghty', 'javascript+myghty'), (), ('application/x-javascript+myghty', 'text/x-javascript+myghty', 'text/javascript+mygthy')),
    'MyghtyLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Myghty', ('myghty',), ('*.myt', 'autodelegate'), ('application/x-myghty',)),
    'MyghtyXmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'XML+Myghty', ('xml+myghty',), (), ('application/xml+myghty',)),
    'NasmLexer': ('plushcms.syntaxhighlight.pygments.lexers.asm', 'NASM', ('nasm',), ('*.asm', '*.ASM'), ('text/x-nasm',)),
    'NewspeakLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Newspeak', ('newspeak',), ('*.ns2',), ('text/x-newspeak',)),
    'NginxConfLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Nginx configuration file', ('nginx',), (), ('text/x-nginx-conf',)),
    'NumPyLexer': ('plushcms.syntaxhighlight.pygments.lexers.math', 'NumPy', ('numpy',), (), ()),
    'ObjdumpLexer': ('plushcms.syntaxhighlight.pygments.lexers.asm', 'objdump', ('objdump',), ('*.objdump',), ('text/x-objdump',)),
    'ObjectiveCLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Objective-C', ('objective-c', 'objectivec', 'obj-c', 'objc'), ('*.m',), ('text/x-objective-c',)),
    'ObjectiveJLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'Objective-J', ('objective-j', 'objectivej', 'obj-j', 'objj'), ('*.j',), ('text/x-objective-j',)),
    'OcamlLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'OCaml', ('ocaml',), ('*.ml', '*.mli', '*.mll', '*.mly'), ('text/x-ocaml',)),
    'OcamlLexer': ('plushcms.syntaxhighlight.pygments.lexers.functional', 'OCaml', ('ocaml',), ('*.ml', '*.mli', '*.mll', '*.mly'), ('text/x-ocaml',)),
    'OocLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Ooc', ('ooc',), ('*.ooc',), ('text/x-ooc',)),
    'PerlLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Perl', ('perl', 'pl'), ('*.pl', '*.pm'), ('text/x-perl', 'application/x-perl')),
    'PhpLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'PHP', ('php', 'php3', 'php4', 'php5'), ('*.php', '*.php[345]'), ('text/x-php',)),
    'PostScriptLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'PostScript', ('postscript',), ('*.ps', '*.eps'), ('application/postscript',)),
    'PovrayLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'POVRay', ('pov',), ('*.pov', '*.inc'), ('text/x-povray',)),
    'PrologLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Prolog', ('prolog',), ('*.prolog', '*.pro', '*.pl'), ('text/x-prolog',)),
    'PropertiesLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Properties', ('properties',), ('*.properties',), ('text/x-java-properties',)),
    'ProtoBufLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Protocol Buffer', ('protobuf',), ('*.proto',), ()),
    'Python3Lexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Python 3', ('python3', 'py3'), (), ('text/x-python3', 'application/x-python3')),
    'Python3TracebackLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Python 3.0 Traceback', ('py3tb',), ('*.py3tb',), ('text/x-python3-traceback',)),
    'PythonConsoleLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Python console session', ('pycon',), (), ('text/x-python-doctest',)),
    'PythonLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Python', ('python', 'py'), ('*.py', '*.pyw', '*.sc', 'SConstruct', 'SConscript', '*.tac'), ('text/x-python', 'application/x-python')),
    'PythonTracebackLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Python Traceback', ('pytb',), ('*.pytb',), ('text/x-python-traceback',)),
    'RConsoleLexer': ('plushcms.syntaxhighlight.pygments.lexers.math', 'RConsole', ('rconsole', 'rout'), ('*.Rout',), ()),
    'RagelCLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'Ragel in C Host', ('ragel-c',), ('*.rl',), ()),
    'RagelCppLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'Ragel in CPP Host', ('ragel-cpp',), ('*.rl',), ()),
    'RagelDLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'Ragel in D Host', ('ragel-d',), ('*.rl',), ()),
    'RagelEmbeddedLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'Embedded Ragel', ('ragel-em',), ('*.rl',), ()),
    'RagelJavaLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'Ragel in Java Host', ('ragel-java',), ('*.rl',), ()),
    'RagelLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'Ragel', ('ragel',), (), ()),
    'RagelObjectiveCLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'Ragel in Objective C Host', ('ragel-objc',), ('*.rl',), ()),
    'RagelRubyLexer': ('plushcms.syntaxhighlight.pygments.lexers.parsers', 'Ragel in Ruby Host', ('ragel-ruby', 'ragel-rb'), ('*.rl',), ()),
    'RawTokenLexer': ('plushcms.syntaxhighlight.pygments.lexers.special', 'Raw token data', ('raw',), (), ('application/x-plushcms.syntaxhighlight.pygments-tokens',)),
    'RebolLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'REBOL', ('rebol',), ('*.r', '*.r3'), ('text/x-rebol',)),
    'RedcodeLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Redcode', ('redcode',), ('*.cw',), ()),
    'RhtmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'RHTML', ('rhtml', 'html+erb', 'html+ruby'), ('*.rhtml',), ('text/html+ruby',)),
    'RstLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'reStructuredText', ('rst', 'rest', 'restructuredtext'), ('*.rst', '*.rest'), ('text/x-rst', 'text/prs.fallenstein.rst')),
    'RubyConsoleLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Ruby irb session', ('rbcon', 'irb'), (), ('text/x-ruby-shellsession',)),
    'RubyLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Ruby', ('rb', 'ruby', 'duby'), ('*.rb', '*.rbw', 'Rakefile', '*.rake', '*.gemspec', '*.rbx', '*.duby'), ('text/x-ruby', 'application/x-ruby')),
    'SLexer': ('plushcms.syntaxhighlight.pygments.lexers.math', 'S', ('splus', 's', 'r'), ('*.S', '*.R'), ('text/S-plus', 'text/S', 'text/R')),
    'SassLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'Sass', ('sass', 'SASS'), ('*.sass',), ('text/x-sass',)),
    'ScalaLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Scala', ('scala',), ('*.scala',), ('text/x-scala',)),
    'ScamlLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'Scaml', ('scaml', 'SCAML'), ('*.scaml',), ('text/x-scaml',)),
    'SchemeLexer': ('plushcms.syntaxhighlight.pygments.lexers.functional', 'Scheme', ('scheme', 'scm'), ('*.scm',), ('text/x-scheme', 'application/x-scheme')),
    'ScssLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'SCSS', ('scss',), ('*.scss',), ('text/x-scss',)),
    'SmalltalkLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Smalltalk', ('smalltalk', 'squeak'), ('*.st',), ('text/x-smalltalk',)),
    'SmartyLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Smarty', ('smarty',), ('*.tpl',), ('application/x-smarty',)),
    'SourcesListLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'Debian Sourcelist', ('sourceslist', 'sources.list'), ('sources.list',), ()),
    'SqlLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'SQL', ('sql',), ('*.sql',), ('text/x-sql',)),
    'SqliteConsoleLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'sqlite3con', ('sqlite3',), ('*.sqlite3-console',), ('text/x-sqlite3-console',)),
    'SquidConfLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'SquidConf', ('squidconf', 'squid.conf', 'squid'), ('squid.conf',), ('text/x-squidconf',)),
    'SspLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Scalate Server Page', ('ssp',), ('*.ssp',), ('application/x-ssp',)),
    'TclLexer': ('plushcms.syntaxhighlight.pygments.lexers.agile', 'Tcl', ('tcl',), ('*.tcl',), ('text/x-tcl', 'text/x-script.tcl', 'application/x-tcl')),
    'TcshLexer': ('plushcms.syntaxhighlight.pygments.lexers.other', 'Tcsh', ('tcsh', 'csh'), ('*.tcsh', '*.csh'), ('application/x-csh',)),
    'TexLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'TeX', ('tex', 'latex'), ('*.tex', '*.aux', '*.toc'), ('text/x-tex', 'text/x-latex')),
    'TextLexer': ('plushcms.syntaxhighlight.pygments.lexers.special', 'Text only', ('text',), ('*.txt',), ('text/plain',)),
    'ValaLexer': ('plushcms.syntaxhighlight.pygments.lexers.compiled', 'Vala', ('vala', 'vapi'), ('*.vala', '*.vapi'), ('text/x-vala',)),
    'VbNetAspxLexer': ('plushcms.syntaxhighlight.pygments.lexers.dotnet', 'aspx-vb', ('aspx-vb',), ('*.aspx', '*.asax', '*.ascx', '*.ashx', '*.asmx', '*.axd'), ()),
    'VbNetLexer': ('plushcms.syntaxhighlight.pygments.lexers.dotnet', 'VB.net', ('vb.net', 'vbnet'), ('*.vb', '*.bas'), ('text/x-vbnet', 'text/x-vba')),
    'VelocityHtmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'HTML+Velocity', ('html+velocity',), (), ('text/html+velocity',)),
    'VelocityLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'Velocity', ('velocity',), ('*.vm', '*.fhtml'), ()),
    'VelocityXmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'XML+Velocity', ('xml+velocity',), (), ('application/xml+velocity',)),
    'VerilogLexer': ('plushcms.syntaxhighlight.pygments.lexers.hdl', 'verilog', ('v',), ('*.v', '*.sv'), ('text/x-verilog',)),
    'VimLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'VimL', ('vim',), ('*.vim', '.vimrc'), ('text/x-vim',)),
    'XQueryLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'XQuery', ('xquery', 'xqy'), ('*.xqy', '*.xquery'), ('text/xquery', 'application/xquery')),
    'XmlDjangoLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'XML+Django/Jinja', ('xml+django', 'xml+jinja'), (), ('application/xml+django', 'application/xml+jinja')),
    'XmlErbLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'XML+Ruby', ('xml+erb', 'xml+ruby'), (), ('application/xml+ruby',)),
    'XmlLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'XML', ('xml',), ('*.xml', '*.xsl', '*.rss', '*.xslt', '*.xsd', '*.wsdl'), ('text/xml', 'application/xml', 'image/svg+xml', 'application/rss+xml', 'application/atom+xml', 'application/xsl+xml', 'application/xslt+xml')),
    'XmlPhpLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'XML+PHP', ('xml+php',), (), ('application/xml+php',)),
    'XmlSmartyLexer': ('plushcms.syntaxhighlight.pygments.lexers.templates', 'XML+Smarty', ('xml+smarty',), (), ('application/xml+smarty',)),
    'XsltLexer': ('plushcms.syntaxhighlight.pygments.lexers.web', 'XSLT', ('xslt',), ('*.xsl', '*.xslt'), ('text/xml', 'application/xml', 'image/svg+xml', 'application/rss+xml', 'application/atom+xml', 'application/xsl+xml', 'application/xslt+xml')),
    'YamlLexer': ('plushcms.syntaxhighlight.pygments.lexers.text', 'YAML', ('yaml',), ('*.yaml', '*.yml'), ('text/x-yaml',))
}

if __name__ == '__main__':
    import sys
    import os

    # lookup lexers
    found_lexers = []
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
    for filename in os.listdir('.'):
        if filename.endswith('.py') and not filename.startswith('_'):
            selectedModulee_name = 'plushcms.syntaxhighlight.pygments.lexers.%s' % filename[:-3]
            print selectedModulee_name
            selectedModulee = __import__(selectedModulee_name, None, None, [''])
            for lexer_name in selectedModulee.__all__:
                lexer = getattr(selectedModulee, lexer_name)
                found_lexers.append(
                    '%r: %r' % (lexer_name,
                                (selectedModulee_name,
                                 lexer.name,
                                 tuple(lexer.aliases),
                                 tuple(lexer.filenames),
                                 tuple(lexer.mimetypes))))
    # sort them, that should make the diff files for svn smaller
    found_lexers.sort()

    # extract useful sourcecode from this file
    f = open(__file__)
    try:
        content = f.read()
    finally:
        f.close()
    header = content[:content.find('LEXERS = {')]
    footer = content[content.find("if __name__ == '__main__':"):]

    # write new file
    f = open(__file__, 'w')
    f.write(header)
    f.write('LEXERS = {\n    %s\n}\n\n' % ',\n    '.join(found_lexers))
    f.write(footer)
    f.close()
