import android
import os

droid = android.Android()

def getMasterDialog():

	ros_master_uri_dialog = droid.dialogGetInput("ROS on Android", "ROS_MASTER_URI:\n(Press cancel to use QR-code)")
	if repr(ros_master_uri_dialog.result) == 'None':
		code = droid.scanBarcode()
		ros_master_uri = code.result.get('extras').get('SCAN_RESULT')
	else:
		ros_master_uri = ros_master_uri_dialog.result

	droid.makeToast('ROS_MASTER_URI:\n' + ros_master_uri)
	print "ROS_MASTER_URI", ros_master_uri
	return ros_master_uri

def getDeviceIP():
	device_ip_dialog= droid.dialogGetInput("ROS on Android","Device IP:")
	if repr(device_ip_dialog.result)== 'None':
		print "Please enter device IP"
	else:
		device_ip=device_ip_dialog.result
	droid.makeToast('Device IP:\n'+device_ip)
	print "Device IP", device_ip
	return device_ip

def ENV_VAR_SET():

	print "ENV_VAR_SET()"

	os.environ["ROS_IP"] = getDeviceIP()
	os.environ["ROS_MASTER_URI"] = getMasterDialog()
	os.environ["ROS_LOG_DIR"] = "/mnt/sdcard/tmp/"
	os.environ["ROS_PACKAGE_PATH"]="/mnt/sdcard/com.googlecode.pythonforandroid/extras"

if __name__ == '__main__':
    try:
        ENV_VAR_SET()
    except rospy.ROSInterruptException: pass
