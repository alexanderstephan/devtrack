import curses

stdscr = curses.initscr();

curses.noecho()

stdscr.keypad(True)

y,x = stdscr.getmaxyx();
win = curses.newwin(y-1, x-1,0,0)
stdscr.getkey();
std.box(0)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

