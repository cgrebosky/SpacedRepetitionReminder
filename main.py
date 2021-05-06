import datetime
import os

# From https://www.quora.com/Whats-the-best-spaced-repetition-schedule.  Not really scientific, but it seems decent.
schedule = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

if __name__ == '__main__':
    today = datetime.date.today()
    schedule_days = [today - datetime.timedelta(days=i) for i in schedule]

    schedule_days = [i.strftime("%m/%d") for i in schedule_days]
    output_string = ", ".join(schedule_days)

    # God, applescript is literally the worst :'(.  Why does this exist?  Who thought this was a good idea?
    # Also, you'll have to change this for a different OS, but this should work on pretty much all OSX versions
    os.system("osascript -e 'display notification \"%s\" with title \"Spaced Repetition Reminder\"\'" % output_string)
