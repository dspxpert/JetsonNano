#! /usr/bin/python

import curses

# curses key code definition
# https://www.gnu.org/software/guile-ncurses/manual/html_node/Getting-characters-from-the-keyboard.html

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # print numeric value
            stdscr.clear()
            stdscr.addstr(0,0, str(c) + ' ')
            stdscr.refresh()
            stdscr.move(0,0)
            # return curser to start position
            if c == ord('w'):
                #print("hello")
                stdscr.addstr(1,0, "hello")
                stdscr.refresh()
                stdscr.move(0,0)
            if c == curses.KEY_UP:
                #print("hello")
                stdscr.addstr(1,0, "up")
                stdscr.refresh()
                stdscr.move(0,0)
            if c == curses.KEY_DOWN:
                #print("hello")
                stdscr.addstr(1,0, "down")
                stdscr.refresh()
                stdscr.move(0,0)
            if c == curses.KEY_LEFT:
                #print("hello")
                stdscr.addstr(1,0, "left")
                stdscr.refresh()
                stdscr.move(0,0)
            if c == curses.KEY_RIGHT:
                #print("hello")
                stdscr.addstr(1,0, "right")
                stdscr.refresh()
                stdscr.move(0,0)
            if c == 3 or c == ord('q') or c == ord(' '):
                break

if __name__ == '__main__':
    curses.wrapper(main)
