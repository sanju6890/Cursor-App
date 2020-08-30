import time
import curses
from curses import textpad
import webbrowser

# function for date and time
def time_date():
    import datetime
    now = datetime.datetime.now()
    date_time ='DATE: 'f'{now:%d-%m-%Y | %H:%M }'
    return date_time

# function for speech
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

menu = ['newspaper','instagram','facebook','blogger','youtube','github','exit']

# function to print menu
def print_menu(stdscr,selected_row_idx):
    for idx,row in enumerate(menu):
        h, w = stdscr.getmaxyx()
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(3))
        else:
            stdscr.attron(curses.color_pair(5))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(5))
    stdscr.refresh()
            
# main display function
def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_YELLOW)
    current_row_idx = 0
    # defining color pairs
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_PAIRS)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    title="<<<<< WELCOME >>>>>"
    h,w = stdscr.getmaxyx()
    x = w//2 - len(title)//2
    y = 0

    print_menu(stdscr,current_row_idx)
    while 1:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(y, x, title)
        stdscr.attroff(curses.color_pair(1))
        stdscr.addstr(2, 4,time_date())
        #constructing a box 
        box = [[3,3], [h-3,w-3]]
        stdscr.attron(curses.color_pair(2))
        textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
        stdscr.attroff(curses.color_pair(2))
        stdscr.refresh()
        print_menu(stdscr,current_row_idx)
        key=stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx = current_row_idx-1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx = current_row_idx+1
        elif key == curses.KEY_ENTER or key in [10,13]:
            stdscr.attron(curses.color_pair(2))
            textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
            stdscr.attroff(curses.color_pair(2))
            stdscr.refresh()
            stdscr.attron(curses.color_pair(4))
            stdscr.addstr(h//2, w//2 - len(f"You selected {menu[current_row_idx]}")//2,f"You selected {menu[current_row_idx]}")
            stdscr.attroff(curses.color_pair(4))
            stdscr.refresh()
            time.sleep(2)
            if 'facebook' in menu[current_row_idx]:
                url='https://facebook.com/'
                webbrowser.get().open(url)
                speak('opening facebook')
            elif menu[current_row_idx]=='blogger':
                url='https://techdeet.blogspot.com/'
                webbrowser.get().open(url)
                speak('opening blogger')
            elif menu[current_row_idx]=='instagram':
                url='https://instagram.com/'
                webbrowser.get().open(url)
                speak('opening instagram')
            elif menu[current_row_idx]=='github':
                url='https://github.com/'
                webbrowser.get().open(url)
                speak('opening Github')
            elif menu[current_row_idx]=='newspaper':
                url='https://epaper.hindustantimes.com/Home/ArticleView'
                webbrowser.get().open(url)
                speak('opening Hindustan Times e-newspaper')
            elif menu[current_row_idx]=='youtube':
                url='https://www.youtube.com/'
                webbrowser.get().open(url)
                speak('opening youtube')
            elif menu[current_row_idx] == 'exit':
                speak('good bye')
                exit()
        stdscr.clear()
        print_menu(stdscr,current_row_idx)
        stdscr.refresh()
curses.wrapper(main)