#include <ncurses.h>
#include <stdio.h>

int main() {
    char* s = "Hello World\n";
    initscr();
    noecho();

   //enable keylistener
    keypad(stdscr, true);

    WINDOW* titlebar = newwin(1,COLS-2,1,1);
    WINDOW* primary = newwin(2, COLS/2-2, 2,1);
    WINDOW* secondary = newwin(2, COLS/2+1, 1, 1);
    WINDOW* command = newwin(LINES-1, COLS-2, LINES-1,1);

    box(stdscr, ACS_VLINE, ACS_HLINE);
    box(titlebar, ACS_VLINE, ACS_HLINE);
    box(primary, ACS_VLINE, ACS_HLINE);
    box(secondary, ACS_VLINE, ACS_HLINE);
    box(command, ACS_VLINE, ACS_HLINE);

    wrefresh(stdscr);
    wrefresh(primary);
    wrefresh(secondary);
    wrefresh(command);
    wrefresh(titlebar);
    wprintw(primary,s);

    getch();

    endwin();
}
