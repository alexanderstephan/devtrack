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
    maxy,maxx=win.getmaxyx()
    abstand=maxx/(len(arr)*2+1)
    scale=(0.75*maxy)/arr[0]
    for i,j in enumerate(arr):
        for k in range((int)(abstand)):
            for l in range((int)(scale*j)):
                win.addch(maxy-2-l,k+(i*2*(int)(abstand)+1+(int)(abstand)),curses.ACS_BLOCK, curses.color_pair(2))
    win.refresh()

def draw_graph_2(win, arr):
    maxx,maxy=win.getmaxyx()
    abstand=maxy/(len(arr)*2+1)
    scale=(0.75*maxx)/arr[0]
    for i,j in enumerate(arr):
        for k in range((int)(abstand)):
            for l in range((int)(scale*j)):
                    win.addch(k+(i*2*(int)(abstand)+1+(int)(abstand)),l+1,curses.ACS_BLOCK,curses.color_pair(1))
    win.refresh()


file=open("/home/alex/devtrack/frontend/data")
#lines=file.readlines()
#print(lines)
#time.sleep(10)
#lines=file.readlines()
#print(lines)
dic={}
read_in_file(file, dic)
file.close()
top_five=sorted(dic.values(),reverse=True)[:5]
print(top_five)

#time.sleep(5)

stdscr = curses.initscr()

curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)


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
draw_graph_2(links, top_five)
tb = curses.textpad.Textbox(actual_leiste)
text = tb.edit()


#rechts.refresh()

stdscr.getch()
#curses.addstr(4,1,text.encode('utf_8'))
curses.endwin()
