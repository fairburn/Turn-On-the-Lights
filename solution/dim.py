#!/usr/bin/env python

#read in the current brightness
f = open('/sys/class/backlight/acpi_video0/brightness', 'r')
brightness = int(f.readline())
f.close()

# don't allow brightness to drop below 1
if brightness-1 < 1:
	quit()
	
# set the new brightness
new_brightness = str(brightness-1)
f = open('/sys/class/backlight/acpi_video0/brightness', 'w')
f.write(new_brightness + '\n') # keep the newline at end of file
f.close()