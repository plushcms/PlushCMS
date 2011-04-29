# -*- coding: utf-8 -*-

# Used by contact form
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import parseaddr
from email.Utils import formataddr

# Used for scaling image
from PIL import Image

# Used for generate captcha
import ImageDraw
import ImageFont
import cStringIO
import hashlib
import string
from random import choice
from random import randint
from settings import MEDIA_FONT

from os.path import getsize

# Used by pygments
from plushcms.syntaxhighlight.BeautifulSoup import BeautifulSoup
import plushcms.syntaxhighlight.pygments
from plushcms.syntaxhighlight.pygments import lexers
from plushcms.syntaxhighlight.pygments import formatters
from plushcms.syntaxhighlight.pygments import highlight

def sendEmail(server, port, login, password, sender, recipient, subject, body):
    """Send e-mail function with unicode support"""
    headerCharset = "ISO-8859-1"

    for bodyCharset in ("US-ASCII", "ISO-8859-1", "UTF-8"):
        try:
            body.encode(bodyCharset)

        except UnicodeError:
            pass

        else:
            break

    senderName, senderAddr = parseaddr(sender)
    recipientName, recipientAddr = parseaddr(recipient)

    senderName = str(Header(unicode(senderName), headerCharset))
    recipientName = str(Header(unicode(recipientName), headerCharset))

    senderAddr = senderAddr.encode("ascii")
    recipientAddr = recipientAddr.encode("ascii")

    msg = MIMEText(body.encode(bodyCharset), "html", bodyCharset)
    msg["From"] = formataddr((senderName, senderAddr))
    msg["To"] = formataddr((recipientName, recipientAddr))
    msg["Subject"] = Header(unicode(subject), headerCharset)

    server = smtplib.SMTP(server, port)
    server.login(login, password)
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()

def scaleImage(logo, width = 200, showPhotoMin = 0):
    """Change the logoSize of an image"""
    logoIn = Image.open(logo)
    logoSize = logoIn.size

    # Scaling it if necessary
    if logoSize[0] > width:
        logoIn.thumbnail((width, logoSize[1]), Image.ANTIALIAS)

        # Used by gallery application for creating thumbnails
        if showPhotoMin:
            logoIn.save("%s-min.%s" % tuple(logo.split(".")))
        else:
            logoIn.save(logo)
    elif showPhotoMin:
        logoIn.save("%s-min.%s" % tuple(logo.split(".")))

def renderCapchaImage(width, height, length, fontSize):
    """Captcha image generator"""
    imgtext = "".join([choice(string.ascii_letters + string.digits + "-+!@%?&#$=") for x in xrange(length)])
    imghash = hashlib.sha1(imgtext).hexdigest()
    img = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    dr = (randint(0, 255) - r) / 300
    dg = (randint(0, 255) - g) / 300
    db = (randint(0, 255) - b) / 300

    for x in xrange(300):
        r, g, b = r + dr, g + dg, b + db
        draw.line((x, 0, x, 300), fill = (r, g, b))

    font = ImageFont.truetype(MEDIA_FONT, fontSize)
    draw.text(((width / 11) - length, height / 4), imgtext, font = font, fill = (255, 255, 255))

    captchaFile = cStringIO.StringIO()
    img.save(captchaFile, "PNG")
    captchaFile.seek(0)
    data = {"imghash" : imghash, "picture" : captchaFile.read()}

    return data

def getFileSize(pathFile):
    """Return file size in MB"""
    return str(getsize(pathFile) / (1024 * 1024.0))

def highlightCode(html):
    """Highlight the source code shown in an HTML"""
    soup = BeautifulSoup(html)
    preBlocks = soup.findAll("pre")

    for pre in preBlocks:
        if pre.has_key("class"):
            try:
                code = "".join([unicode(item) for item in pre.contents])
                code = code.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
                lexer = lexers.get_lexer_by_name(pre["class"])
                formatter = formatters.HtmlFormatter()
                codeHl = highlight(code, lexer, formatter)
                pre.replaceWith(BeautifulSoup(codeHl))
            except:
                pass

    return unicode(soup)
