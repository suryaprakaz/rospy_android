import android

droid = android.Android()
droid.startSensing()
while 1:
 acc=droid.sensorsGetLight().result
 #print "X:" ,acc[0], "Y:", acc[1], "Z:", acc[2]
 print acc