# Turn On the Lights
**"Everything is a file"** is a fundamental feature of Unix-like operating
systems. This assignment will help to familiarize you with this concept by
allowing you to change a simple hardware property, the brightness of your
laptop screen, by accessing and modifying a system file which contains a
single integer describing the screen brightness. The integer ranges between 0
(off) and some maximum value, usually 15. Read [this entry][1] of the Arch Linux
Wiki for more information about the files you'll need to access (the paths in
Ubuntu are the same as shown there).

You can find the maximum brightness value of your backlight by running

		cat /sys/class/backlight/acpi_video0/max_brightness

To complete this assignment, write two short Python scripts, `bright.py` and
`dim.py`, which modify your system's brightness file.

##`bright.py`

* This script should read in the current screen brightness, increment it by one,
and write it back to the file. Note that this will *not* come from the same file
listed in the command above. When you write back to the file, be sure to
overwrite its contents rather than appending to it.
* The script should exit without doing anything if the brightness is already set
to the maximum value.

##`dim.py`
* This script should follow the same specifications for `bright.py`, except
instead of incrementing the brightness value, it should decrement the value by
one and write it back to the file.
* The script should exit without doing anything if the brightness is set to 1,
as setting it to 0 will turn off your backlight (if this happens accidentally,
running `bright.py` or rebooting your computer will fix it; no changes made to
the brightness file are permanent).

## Testing and Submission
You may want to test your scripts on a dummy text file before running them on
the system's actual brightness file to ensure they work properly. The only
contents of the file should be a single integer on one line, with an empty line
following it. Also note that when accessing the system brightness file, you may
need to run the script as root:

		sudo bright.py

As an example, let's assume you are testing your `bright.py` script on a dummy
file in the current directory called `test.txt`:

		% cat ./test.txt
		6
		% ./bright.py
		% cat ./test.txt
		7

When your scripts work properly you will see the brightness on your screen
change slightly each time you run them. Make sure that your code is clearly
commented and readable before submitting.

[1]: https://wiki.archlinux.org/index.php/Backlight "Arch Linux Wiki"