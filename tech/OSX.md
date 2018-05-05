# OSX

- [How To Stop CalendarAgent From Eating CPU](https://robert.accettura.com/blog/2012/08/19/how-to-stop-calendaragent-from-eating-cpu/)
  - Remove the Calendar from “Mail, Contacts & Calendars” pref panel (just uncheck from the account). Then go into Calendar and make sure the account is removed. If it’s not, remove it.
  - Delete ~/Library/Calendars/
  - Delete ~/Library/Preferences/com.apple.iCal.plist
  - Go back into the “Mail, Contacts & Calendars” pref panel, put the calendar back. Give it some time to download.
