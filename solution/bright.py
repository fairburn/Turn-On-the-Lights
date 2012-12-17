#!/usr/bin/env python

# read in the current screen brightness
f = open('/sys/class/backlight/acpi_video0/brightness', 'r')
brightness = int(f.readline())
f.close()

# exit if brightness is higher than the max
# mine was shown to be 10 instead of 15
if brightness+1 > 10:
	quit()
	
# set the new brightness
new_brightness = str(brightness+1)
f = open('/sys/class/backlight/acpi_video0/brightness', 'w')
f.write(new_brightness + '\n') # keep the newline at end of file
f.close()