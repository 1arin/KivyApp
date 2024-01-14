main_app.kv
  ไฟล์นี้ใช้ภาษา KV กำหนด UI โดยใช้ KivyMD และทำ Layout ของ ToDo list พร้อมทั้งกล่องใส่ข้อความและปุ่มสำหรับเพิ่ม task นอกจากนี้ยังมีการใช้ checkbox เพื่อ mark ว่าเสร็จสิ้นและเลือกวันที่ครบกำหนดโดยใช้ date picker

database.py
  ไฟล์ Python นี้ประกอบด้วยคลาส Database ที่ดำเนินการฐานข้อมูล SQLite รวมถึงการสร้างตาราง/เพิ่ม task / ดึงข้อมูล / อัปเดตสถานะการเสร็จสิ้น / และลบ tasks

main_app.py
  เป็นส่วนหลักและกำหนด (MainApp) มี medthode สำหรับแสดง dialog / ปิด dialog และเพิ่ม task connect กับฐานข้อมูล SQLite ที่กำหนดไว้ใน database.py

How to use the app
- กดปุ่ม + เพื่อกดเพิ่ม task
- ใส่ชื่อ task และกำหยดวัน
- mark ว่า task เสร็จ โดยการกดปุ่ม checkbox
- ลบ task ได้ โดยกดที่ปุ่ม ถังขยะ


การทำงานของโค้ดนี้
1. KV Language (main_app.kv):
  MDFloatLayout
 -MDLabel: แสดง topic "To Do" แบบใหญ่ ๆ โดยใช้ Markdown markup
 -ScrollView: ใช้เลื่อนบนหน้าจอ
 -MDList: ใช้เพื่อเก็บ list
 -MDFloatingActionButton ปุ่มลัดสำหรับเรียกหน้าต่างในการ add task

2. Dialog and Content (DialogContent class):
 -MDBoxLayout: ใช้เป็นหน้าต่างแสดงผลของ Dialog ใน add task
 -MDTextField: ช่องใส่ text สำหรับ add task
 -MDIconButton: ไอคอนปฏิทินที่ให้ user เลือกวันที่
 -MDLabel: แสดงวันที่ที่เลือกจากปฏิทิน
 -BoxLayout: ปุ่ม "SAVE" และ "CANCEL" สำหรับการบันทึกและยกเลิก
 
3. List Item (ListItemWithCheckbox class):
 -TwoLineAvatarIconListItem: รายการที่ปรับแต่งสำหรับแสดงงานพร้อมกับ checkbox และไอคอนถังขยะ
 -LeftCheckbox: ช่อง check box ที่ปรับแต่งสำหรับทำเครื่องหมาย task ว่าเสร็จหรือยังไม่เสร็จ
 -IconRightWidget: ไอคอนถังขยะที่ให้ผู้ใช้ลบ task
 
 4. Main App (MainApp class):
  MDApp main class
 -build method: การตั้งค่าธีมและการแสดงหน้าต่างหลัก
 -show_task_dialog method เปิดหน้าต่าง Dialog สำหรับ add task
 -on_start method: โหลด task ที่บันทึกไว้และเพิ่มลงใน MDList เมื่อแอปพลิเคชัน start
 -close_dialog method: ปิด Dialog
 -add_task method: เพิ่ม task ลงใน MDList และบันทึกลงใน database

5. Database Operations (Database class):
 -init method: การเชื่อมต่อกับ SQLite database 
 -create_task_table method: สร้างตารางงาน
 -create_task method: เพิ่ม task ลงในฐานข้อมูล
 -get_tasks method: ดึงข้อมูล task
 -mark_task_as_complete method: อัปเดตสถานะ task เป็นเสร็จสิ้น
 -mark_task_as_incomplete method: อัปเดตสถานะ task เป็นยังไม่เสร็จสิ้น
 -delete_task method: ลบ task
 -close_db_connection method: ปิดการเชื่อมต่อกับฐานข้อมูล
