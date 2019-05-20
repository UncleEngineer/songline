## Songline Library:

วิธีใช้งานทำตามนี้เลย เปิด *cmd* แล้ว

* ไลบรารี่ใช้ส่งไลน์
* ดาวโหลดตารางสติกเกอร์: <http://cons-robotics.com/LINEAPI/sticker.pdf>
* ออก token ในเว็บ: <https://notify-bot.line.me/my/>
  * Log In ด้วยรหัสไลน์ -->
  * เลื่อนลงไปล่างสุดแล้วกด -->
  * กดปุ่ม generate token (ออก token)) -->
  * ตั้งชื่อ Bot -->
  * หากลุ่มที่ต้องการส่งแล้วคลิกให้ขึ้นอักษรสีเขียว -->

ติดตั้งไลบรารี่ผ่าน CMD:
```
pip install songline
```

วิธีใช้งานประมาณนี้จร้าาา...

```
from songline import Sendline

token = 'xdkakfdjksjdfayfdyaodf'
messenger = Sendline(token)

#send message
messenger.sendtext('Hello world')

#send sticker
messenger.sticker(1,1)

#send image
messenger.sendimage('https://img.pngio.com/python-logo-python-logo-png-268_300.png')
```

 อย่าลืมกดไลค์เพจ **"ลุงวิศวกร สอนคำนวณ"** ด้วย
Page: <https://www.facebook.com/UncleEngineer/>.