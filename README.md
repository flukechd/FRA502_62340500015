# FRA502_62340500015
Miniproject for Fra502


# Prerequistes
Ubuntu 20.04.3 LTS
ROS: Noetic
Gazebo: version 11.5.1


# Installation
Build package from source: navigate to the source folder of your catkin workspace and build this package using: 
$ git clone 
$ cd ..
$ catkin_make


# Run gazebo and teleop keyboard
$ roslaunch diff_drive_bot gazebo.launch 
$ roslaunch  diff_drive_bot teleop_Rb.launch 


# Simultaneous Localization And Mapping (SLAM)
1.Move the robot in your environment till a satisfactory map is created.
2.Save map with map saver
$ rosrun map_server map_saver -f mymap


# Navigation robot
$ roslaunch diff_drive_bot gazebo.launch 
$ roslaunch diff_drive_bot amcl_move_base.launch


# Speech and Target
$ rosrun diff_drive_bot move.py

# Summary 
Phase1 กระบวนการทำโปรเจคนี้เริ่มต้นจากการสร้าง World จาก Gazebo หลังจากนั้นทำการสร้างไฟล์หุ่นยนต์ ด้วย URDF ขั้นตอนถัดไป คือการนำหุ่นยนต์มา Spawn ใน World ที่สร้างไว้ ขั้นตอนถัดไปคือการนำ Plug in ต่างๆ เช่น Diff_Drive เเละ Lidar หรือCamera มาใส่ใน URDF เเล้วนำไปใช้งานบน RVIZ
Phase2 คือการนำ Package Gmapping มาใช้งานรับ input จาก Lidar เพื่อนำไปสร้างไฟล์ map .yaml เเละ .pgm หลังจากได้ไฟล์map เเล้ว เราจะนำไปใช้งานกับ Package Movebase เพื่อให้หุ่นยนต์เคลื่อนที่ไปยังจุดที่เราต้องการได้อย่างอัตโนมัติ โดยต้องเคลื่อนที่อยู่บน map ที่ถูกนำมาใช้เท่านั้นโดยทำให้หุ่นยนต์รับรู้ได้ว่าพื้นที่ไหนสามรถเคลื่อนที่ไปได้
Phase3 คือการนำตำเเหน่งที่ต้องการไปเขียนเป็นฟังก์ชั่นเเละเขียน Condition เพื่อรองรับการทำงาน อย่างมีระบบ เเละ install speech recognition มาใช้งานผ่าน Python 3 เเละนำไปสู่การใช้งานสั่งการหุ่นยนต์ด้วยคำสั่งเสียงได้ในท้ายที่สุด


# Problem
จากปัญหาที่พบคือการ Tranformation ของตัวหุ่นยนต์เเละParameter ของMovebase นั้นยังถูกตั้งค่าได้ไม่เหมาะสมเพียงพอจึงทำให้บางครั้งหุ่นยนต์สามารถเคลื่อนที่ไปยังเป้าหมายได้ เเต่ขณะเดินทางกลับมาจุดเริ่มต้นเกิดความผิดพลาดในบางครั้ง เเละ ปัญหาที่สำคัญของโปรเจคครั้งนี้ คือการออกเเบบ World ที่มีความยากเกินไปสำหรับหุ่นยนต์ ในการเคลื่อนที่ เช่น มีทางเข้าห้องที่เล็กมากๆ จึงเป็นสาเหตุสำคัญในการทำโปรเจคครั้งนี้


# Feedback
1.ปรับจูนค่า Parameter ของ Movebase ให้มีค่าที่เหมาะสมมากกว่านี้ ซึ่งต้องใช้เวลาในการศึกษาทำความเข้าใจว่า Parameter ต่างๆมีผลอย่างไร
2.การออกเเบบ World ควรคำนึงถึงระบบการเคลื่อนที่เป็นสำคัญ ควรออกเเบบให้เหมาะสม ซึ่งจะรู้ได้หลังจากได้ทำโปรเจคนี้


# Ref
https://github.com/devanshdhrafani/diff_drive_bot?fbclid=IwAR3N2APZTE-HXOEWXhWh5xzVII6Mn7pezyJTzT2U0C___wmdRpeC-7f2wt0
https://github.com/PranaliDesai/robomechtrix_ws?fbclid=IwAR27oeugVkK5uaJnxyCQA32NV1ZKy4TawzGOPontq4tsmq7tROVr8LVM--k

