#include <iostream>
#include <ncurses.h>

WINDOW* titlebar = nullptr;
WINDOW* primary = nullptr;
WINDOW* secondary = nullptr;
WINDOW* command = nullptr;


int main() {
    std::string s= "Hello World \n";

    initscr();
    noecho();

    //enable keylistener
    keypad(stdscr, true);

    titlebar = newwin(1,COLS-2,1,1);
    box(stdscr, ACS_VLINE, ACS_HLINE);
//    wrefresh(stdscr);
//    wprintw(window, s.c_str());
//    wrefresh(window);
    for(;;);
    return 0;
}
