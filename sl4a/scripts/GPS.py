import android, time

droid = android.Android()
droid.startLocating(0,0)
droid.vibrate()
print "GPS started...."
time.sleep(10)
while 1:
	l=droid.readLocation()
	#loc= "Latitude:" + str(l[1]['gps']['latitude']) + "Longitude:" + str(l[1]['gps']['longitude'])
 	print l
	time.sleep(1)
