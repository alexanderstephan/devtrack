import curses
import curses.textpad
import time

def read_in_file(file, dic):
    lines=file.readlines()
    #ts=(int)lines[0].split(" ")[0]
    #act=i.split(" ")[1:]

    # number, item
    s=" "
    for i,j in enumerate(lines[:-1]):
        split=j.split(" ")
        act=s.join(split[1:])[:-1]
        ts=(int)(split[0])
        next_split=lines[i+1].split(" ")
        if act in list(dic.keys()):
            dic[act]+=(int)(next_split[0])-ts
        else:
            dic[act]=(int)(next_split[0])-ts
    print(dic)

def draw_graph_1(win, arr):
    #rechts.addstr(4,4,"TEST")
    #rechts.addch(4,4,curses.ACS_BLOCK)
    #rechts.addch(4,5,curses.ACS_BLOCK)
    #rechts.addch(5,4,curses.ACS_BLOCK)
    #rechts.addch(5,5,curses.ACS_BLOCK)

    maxy,maxx=win.getmaxyx()
    abstand=maxx/(len(arr)*2+1)
    scale=arr[0]/(0.75*maxy)
    win.addstr(3,20,(str)(scale))
    win.addstr(4,20,(str)(abstand))
    win.addstr(5,20,(str)(maxx))
    win.addstr(6,20,(str)(maxy))
    #win.addch(3,3,curses.ACS_BLOCK)
    #win.addch(5,5,curses.ACS_BLOCK)
    for i in range(len(arr)):
        for j in range((int)(scale*i)):
            for k in range()
            win.addch(j+1,(int)(i*abstand),curses.ACS_BLOCK)
    win.refresh()

file=open("/home/alex/devtrack/frontend/data")
dic={}
read_in_file(file, dic)
file.close()
top_five=sorted(dic.values(),reverse=True)[:5]
print(top_five)

#time.sleep(2)

stdscr = curses.initscr()

curses.noecho()
#curses.echo()

y,x=stdscr.getmaxyx()
links=curses.newwin(y-3, (int)(x/2), 0, 0)
rechts=curses.newwin(y-3, (int)(x/2), 0, (int)(x/2))
leiste=curses.newwin(3,x-1,y-3,0)
actual_leiste=curses.newwin(1,x-4,y-2,2)
#win = curses.newwin(height, width, begin_y, begin_x)
#win.box()
links.box()
rechts.box()
leiste.box()
#stdscr.refresh()
links.refresh()
rechts.refresh()
leiste.refresh()
draw_graph_1(rechts, top_five)
tb = curses.textpad.Textbox(actual_leiste)
text = tb.edit()


#rechts.refresh()

stdscr.getch()
#curses.addstr(4,1,text.encode('utf_8'))
curses.endwin()
