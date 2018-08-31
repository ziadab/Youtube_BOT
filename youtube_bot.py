import webbrowser
import platform
import time
import os

url = str(input('Enter your youtube video URL : '))
browser = str(input("Enter the browser that you want use : ")).lower()
repeat_time = int(input("How many view you wanna add : "))
delail = 10

for i in range(repeat_time):
	b = webbrowser.get(browser)
	b.open(url)
	time.sleep(delail)
	if platform.system() == 'Linux':
		os.system(" killall -9 " + str(b))
		print('View added')
	elif platform.system() == "Windows":
		os.system("TASKKILL /F /IM " + str(b) + ".exe")
		print('View added')