import ftplib
import io

session = ftplib.FTP('host','user','pass')

imageUrl = 'https://avatars1.githubusercontent.com/u/9145304?s=460&u=1126a26b2ffac6187f655816e5eb0ffcb55c429b&v=4'

image = '<img src="' + imageUrl + '"/>'

HTMLPart1 = """<!DOCTYPE html>
<html>
  <head>
    <title>test</title>
  </head>
  <body>
"""

HTMLPart2 = """
  </body>
</html>"""

HTMLFinal = bytes((HTMLPart1 + image + HTMLPart2), encoding= 'utf-8')
HTMLFinal = io.BytesIO(HTMLFinal)
session.storbinary('STOR test.php', HTMLFinal)
