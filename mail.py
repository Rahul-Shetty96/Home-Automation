import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from email.Utils import COMMASPACE, formatdate
from email import Encoders


filePath = "attach.jpg"#your file name

From = 'rajeev11430@gmail.com'
To = 'rahul.shetty@ves.ac.in'

msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = 'Automated Home'

msg.attach(MIMEText('Someone is waiting'))

try:
    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.starttls()
    smtp.login('rajeev11430@gmail.com', 'rajiv9230')
except:
    i = 1
else:
    i = 0

  
if i == 0:
    ctype, encoding = mimetypes.guess_type(filePath)
    if ctype is None or encoding is not None:
        # No guess could be made, or the file is encoded (compressed), so
        # use a generic bag-of-bits type.
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    if maintype == 'text':
        fp = open(filePath)
        # Note: we should handle calculating the charset
        part = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'image':
        fp = open(filePath, 'rb')
        part = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'audio':
        fp = open(filePath, 'rb')
        part = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(filePath, 'rb')
        part = MIMEBase(maintype, subtype)
        part.set_payload(fp.read())
        fp.close()
        # Encode the payload using Base64
        Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % filePath)
    msg.attach(part)
    try:
        smtp.sendmail(From, To, msg.as_string())
    except:
        print "Mail not sent"
    else:
        print "Mail sent"
    smtp.close()
else:
    print "Connection failed"
