import re
import mechanize


br = mechanize.Browser(factory=mechanize.RobustFactory())
url='http://www.ugelcajamarca.gob.pe/institucional/directorio'

r = br.open(url)
respuesta1=br.response().read()
mailsrch = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')

xd = mailsrch.findall(respuesta1)
print ''.join(xd)
