Requirements

	-Terminal Emulator App
	-ADB installed in PC
	-Check 'Install from Unknown Sources'



Open Terminal Emulator in Android

Type the following commands

	su
	setprop service.adb.tcp.port 5555
	stop adbd
	start adbd
	
Connect your phone to PC through WiFi
	
Open Terminal Window in Linux
Type the command 

	adb connect YOUR_PHONE_IP    (The IP address of your phone can be found in Wifi->Advanced)
	
You must receive the confirmation "Connected to YOUR_PHONE_IP"

Navigate to /rospy_android folder
Type the Command

	sh install.sh 
	
Now open Py4A from your phone and click install
Wait till it downloads and extracts scripts
When it's done, run the following command in the linux terminal

	sh ros_setup.sh

Now wait till the installation is complete.

IMPORTANT_NOTE:
	Currently rospy.loginfo() is not working due to native library problems. You could use rostopic echo /topic to see the data instead
