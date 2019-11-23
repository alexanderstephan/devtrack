#include <iostream>
#include <ncurses.h>

WINDOW* window = NULL;

int main() {
    initscreen();
    noecho();
    window = initWin();
    keypad(window, true);
    wprintw(window, s.c_str());
    wrefresh(window);

    return 0;
}
