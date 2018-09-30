import win32file
import os
import subprocess
import time

while True:
	usb = False;

	drive_list = []
	drivebits=win32file.GetLogicalDrives()
	for d in range(1,26):
		mask=1 << d
		if drivebits & mask:
				# here if the drive is at least there
			drname='%c:\\' % chr(ord('A')+d)
			t=win32file.GetDriveType(drname)
			if t == win32file.DRIVE_REMOVABLE:
				drive_list.append(drname)
				usb = True
				drlist = ''.join(drive_list)

	if usb == True:
		print("I see there is a external storage device conntected")
		# print(drive_list)
		# os.chdir(drlist)
		# print(drlist)
		# user = os.environ.get('USERNAME')
		# #gets username
		# file = open("openme.txt","w") 
	
		# file.write("I love you " + user) 
		# file.close() 
		# subprocess.Popen(r'explorer')
		#writes file on USB
	else:
		# print("you don't have a external storage device connected")
		pass
	time.sleep(2)




