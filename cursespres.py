#DONT ZOOM TOO MUCH !! chars shouldn't
#   get out of screens' space !!


import curses
from time import sleep
import random

attrs = [curses.A_REVERSE, curses.A_BOLD, curses.A_DIM, curses.A_BLINK]

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)

maxy, maxx = stdscr.getmaxyx()

def main():

    stdscr.refresh()

    win = curses.newwin(maxy - 1, maxx - 1, 1, 1)
    winmaxy, winmaxx = win.getmaxyx()
    win.addstr(0, 1, "press CTRL+C to quit")
    win.refresh()

    draw_line_filled_square(win, 5, winmaxx // 2 - 8)

    while True:
        key = stdscr.getch()

        if key == ord('q'):
            curses.endwin
            break

        if key == ord(' '):
            add_prestring(win)

def relaunch():
    main()

def draw_line_filled_square(win, posy, posx):
    winmaxy, winmaxx = win.getmaxyx()
    chars = "@-_#!*m~"
    block_len = 30
    for i, line in enumerate(range(block_len)):
        if posy <= winmaxy - 5:
            if i <= block_len - 2:
                char = random.choice(chars)
                random_factor = random.randint(-block_len * 2, block_len)
                win.hline(posy, posx - block_len // 2, char, int(block_len * 1.5), random.choice(attrs))
                sleep(0.1)
                win.vline(posy - 2, posx - block_len // 2- random_factor, char, block_len // int(i + 2), random.choice(attrs))
                sleep(0.01)
                win.vline(posy - 2, posx - block_len // 2- random_factor, char, block_len // int(i + 2), random.choice(attrs))
                sleep(0.01)
                win.vline(posy - 2, posx - block_len // 2- random_factor, char, block_len // int(i + 2), random.choice(attrs))
                sleep(0.01)
                win.hline(posy, posx - block_len // 2- random_factor, char, block_len // int(i + 2), random.choice(attrs))
                sleep(0.01)
                win.hline(posy, posx - block_len // 2- random_factor, char, block_len // int(i + 2), random.choice(attrs))
                sleep(0.01)
                win.hline(posy, posx - block_len // 2- random_factor, char, block_len // int(i + 2), random.choice(attrs))
                posy += 1
                win.refresh()
            elif i >= block_len -1:
                draw_line_filled_square(win, posy, posx)
    else:
        relaunch()

def add_prestring(win):
    win.clear()
    scnd_prestring = "enjoy reading :)"
    posy = maxy // 4 - 2
    posy_scnd = maxy // 2 + maxy % 4 
    for i, char in enumerate(scnd_prestring):
        if i != int(len(scnd_prestring) - 2):
            win.addstr(posy, maxx // 2, char, random.choice(attrs))
            posy += 1
            win.addstr(posy_scnd, maxx // 2, char, random.choice(attrs))
            posy_scnd += 1
            sleep(0.1)
            win.refresh()
        else:
            stdscr.clear()
            add_prestring(win)
        
   
main()
