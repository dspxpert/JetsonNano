#! /usr/bin/python

import curses

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # print numeric value
            stdscr.clear()  # clear screen
            stdscr.addstr(0,0, str(c) + ' ')
            stdscr.refresh()
            stdscr.move(0,0)
            # return curser to start position
            if c == ord('w'):
                #print("hello")
                stdscr.addstr(1,0, "hello")
                stdscr.refresh()
                stdscr.move(0,0)
            if c == 3 or c == ord('q') or c == ord(' '):
                break

if __name__ == '__main__':
    curses.wrapper(main)
