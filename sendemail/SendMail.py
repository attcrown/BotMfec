import smtplib
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

current_date = date.today()

# ข้อมูลการเข้าสู่ระบบ Outlook
outlook_email = "vongvaris@mfec.co.th"
outlook_password = "rgnhqkrrdgxnfszp"

# สร้างอีเมล
sender_email = outlook_email
receiver_email = "ittatting@gmail.com"
subject = f"[Monitor] Infrastructure status checklist as of {current_date}"
body = f"""
<pre>
Dear All,

        Please be aware of the Infrastructure readiness checklist for {current_date}.
        
        EMCC
        - Host
        <img src="cid:image1">
        
        <img src="cid:image1">
        
        <img src="cid:image1">
        
        <img src="cid:image1">

Best Regards


<img src="cid:image2"> <small>Vongvaris Chawawiwat( Att ) | ITOMS |
                 Tel : +66(0)99-454-1525 | Email : vongvaris@mfec.co.th</small>
<img src="cid:image3">


<small>DISCLAIMER: This e-mail and any attachments may contain confidential or legally privileged information for use of 

MFEC Public Company Limited only.  If you are not the intended recipient, you are not authorized to copy or disclose 

all or any part of it without the prior written consent of the company.  Refer to https://www.mfec.co.th/en/privacy-policy/ </small> 
</pre>
"""

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# แนบข้อความลงในอีเมล
message.attach(MIMEText(body, "html"))


# กำหนดค่า script_directory
image_path = os.path.join(os.getcwd(), "test.jpeg")
image_pathBar = os.path.join(os.getcwd(), "thumbnail_image.png")
image_pathBar2 = os.path.join(os.getcwd(), "thumbnail_image_2.png")
# แนบรูปภาพ
with open(image_path, "rb") as image_file:
    image_data = image_file.read()
    image = MIMEImage(image_data, name="test.jpeg")
    image.add_header('Content-ID', '<image1>')
    message.attach(image)

with open(image_pathBar, "rb") as image_file:
    image_data = image_file.read()
    image_bar = MIMEImage(image_data, name="thumbnail_image.png")
    image_bar.add_header('Content-ID', '<image2>')
    message.attach(image_bar)
    
with open(image_pathBar2, "rb") as image_file:
    image_data = image_file.read()
    image_bar2 = MIMEImage(image_data, name="thumbnail_image_2.png")
    image_bar2.add_header('Content-ID', '<image3>')
    message.attach(image_bar2)

def sendMail():
    print("SendMail")
    # เชื่อมต่อกับเซิร์ฟเวอร์ Outlook
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(outlook_email, outlook_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        
    print("Email sent successfully!")

sendMail()
