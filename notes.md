1) Change hostname by replacing 'raspberrypi' in /etc/hosts and /etc/hostname
2) Update OS wiht 'sudo apt-get update'
3) Install Chromium with 'sudo apt-get install chromium'
4) Install Python GPIO libraries from https://pypi.python.org/pypi/RPi.GPIO
	1) Install python-dev with 'sudo apt-get install python-dev'
	2) Download the tar ball
	3) Extract with 'tar zxvf R*.gz'
	4) Cd to new dir
	5) Install library with 'sudo python setup.py install'
5) If mouse is sluggish, add the following to end of the line in /boot/cmdline.txt: 'usbhid.mousepoll=0'
