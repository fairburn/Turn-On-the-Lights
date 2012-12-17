## Brandon Fairburn
#### Intro to Unix
#### December 16, 2012 

For my "Make an Assignment" suggestion, I've decided to choose something that
I did this semester after installing Linux on my computer, in my spare time.

When I first installed Linux (my choice being Linux Mint rather than Ubuntu), I
noticed that the screen brighten/dim buttons on my laptop were not functional.
These have always been very convenient for me, and after searching for a
solution it became clear that it would be just as easy for me to write a couple
of Python scripts to handle these features and assign them to a shortcut key as
it would be to make a forum post asking for help. A [little research][1] showed
me that a simple text file in the /sys branch of the filesystem controlled the 
screen's brightness. Writing the scripts to interact and set this file really
drove home the point that *everything* is a file in Unix and Linux, and helped
me realize that Linux's hood is pretty transparent; controlling hardware (in
this case at least) can be as simple as changing an integer in a text file.

---

## Grading Distribution
* Code is readable and well commented: 30%
* Script properly alters screen brightness: 70%

---

If the scripts fail to run, the full 30% could still be given for comments and
readability. Partial credit for the remaining 70% should be given based on an
educated attempt at reading in the brightness integer from the file, changing
it, and writing back to the file.

As a note, I don't know if you remember this, but near the beginning of the
semester I came to you and asked why my backlight was turned off until I logged
in. I finally solved that problem by setting my `bright.py` script to run when
the system booted up.




[1]: https://wiki.archlinux.org/index.php/Backlight "Arch Linux Wiki"