# Spaced Repetition Reminder
This software is a bare-bones tool to help remind me what I'm supposed to study each day.  I'm designing this 
purposefully to be as simple as possible.  This is built for OSX, although it's fairly trivial to modify it 
to work on whatever system you'd like.  

![image](SRR%20Screenshot.png)

## Setup
This script only takes care of calculating and displaying a notification.  You will have to set up _when_ you want to
run this script on your own.  That being said, I use `cron`, with this command(s):
```shell
crontab -e
30 8 * * * python3 ~/path/to/this/script/main.py
```
Note that on OSX, at least, you will have to give cron permissions (a short explanation is 
[here](https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/)), and schedule a start-up time for
your computer.

An alternative is to use `launchd`, but cron seems a lot easier and more universal.  