import curses
import curses.textpad
import time
import _thread
import sys
import datetime
from collections import OrderedDict
#from time import gmtime, strftime

def redraw(dic, links, rechts):
    links.erase()
    rechts.erase()
    links.box()
    rechts.box()
    links.refresh()
    rechts.refresh()
    draw_graph_1(rechts, top_five, get_top_five_keys(dic, top_five))
    draw_graph_2(links, top_five, get_top_five_keys(dic, top_five))
    
    curses.echo()

def read_in_file(readable_file, dic):
    lines=readable_file.readlines()
    if lines==[]:
        return

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
    #print(dic)

def draw_graph_1(win, arr, keys):
    win.erase()
    win.box()
    maxy,maxx=win.getmaxyx()
    abstand=maxx/(len(arr)*2+1)
    scale=(0.75*maxy)/arr[0]
    for i,j in enumerate(arr):
        for k in range((int)(abstand)):
            for l in range((int)(scale*j)):
                win.addch(maxy-2-l,k+(i*2*(int)(abstand)+1+(int)(abstand)),curses.ACS_BLOCK, curses.color_pair(2))
                
    
    thingi='     '
    offset=(int)(maxx*0.65)
    for i,j in enumerate(reversed(keys)):
        thingi=thingi[:(5-len(str(arr[i])))]
        win.addstr(2*i+2,offset+13-(len(j)),j+":"+thingi+(str)(arr[i])+"s")
        thingi='     '
    #win.refresh()
    #win = curses.newwin(height, width, begin_y, begin_x)
    
    win.refresh()

    small_win=curses.newwin(20,(int)(maxx*0.2),maxy+5,maxx+(int)(maxx*0.75))
    small_win.box()
    small_win.refresh()
    for i,j in enumerate(keys):
        small_win.addstr(i*2+1,2,j)
    small_win.refresh()

def draw_graph_2(win, arr, keys):
    win.erase()
    win.box()
    maxx,maxy=win.getmaxyx()
    abstand=maxx/(len(arr)*2+1)
    scale=(0.75*maxy)/arr[0]
    for i,j in enumerate(arr):
        for k in range((int)(abstand)):
            for l in range((int)(scale*j)):
                #win.addch(maxy-2-l,k+(i*2*(int)(abstand)+1+(int)(abstand)),curses.ACS_BLOCK, curses.color_pair(2))
                win.addch(k+(i*2*(int)(abstand)+1+(int)(abstand)),l+1,curses.ACS_BLOCK,curses.color_pair(1))
    win.refresh()

def wrapper_read_in_file(readable_file, dic, delay, win):
    while True:
        read_in_file(readable_file, dic)
        draw_graph_2(win, get_top_five(dic, 0))
        actual_leiste.refresh()
        time.sleep(delay)
        
def get_top_five(dic, offset):
    return sorted(dic.values(),reverse=True)[offset:5+offset]

def get_top_five_keys(dic, top_five):
    return_arr=[]
    for i in top_five:
        for j in list(dic.keys()):
            if dic[j]==i:
                return_arr.append(j)
    return list(reversed(return_arr))


stdscr = curses.initscr()

curses.curs_set(0)

curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)


curses.noecho()
#curses.echo()

y,x=stdscr.getmaxyx()
links=curses.newwin(y-3, (int)(x/2), 0, 0)
rechts=curses.newwin(y-3, (int)(x/2)+1, 0, (int)(x/2))
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


curses.echo()



cur_date=datetime.datetime.now().strftime('%Y %m %d').split(' ')
cur_day=datetime.date((int)(cur_date[0]), (int)(cur_date[1]), (int)(cur_date[2])).strftime('%s')

cur_file="/home/confringe/Hackatum/"+cur_day
readable_file=open(cur_file)
dic={}
read_in_file(readable_file, dic)
#file.close()
#top_five=sorted(dic.values(),reverse=True)[:6]
top_five=get_top_five(dic, 0)
#print(top_five)
#_thread.start_new_thread(wrapper_read_in_file, (readable_file, dic, 5, links, ))


draw_graph_1(rechts, top_five, get_top_five_keys(dic, top_five))
draw_graph_2(links, top_five, get_top_five_keys(dic, top_five))

global_l_offset=0
global_r_offset=0
global_vis_offset=0

#text=(str)(actual_leiste.getstr(0,0, x).decode("UTF-8"))
#while text!='quit' or text!='q' or text!=':q':
#while bytes(":q") not in text and bytes("quit") not in text:
curses.noecho()
#new_chr=actual_leiste.getch()
while True:
    curses.curs_set(0)
    curses.noecho()
    new_chr=actual_leiste.getch()
    if new_chr is ord(':'):
        actual_leiste.addch(0,0,':')
        curses.echo()
        curses.curs_set(1)
        text=(str)(actual_leiste.getstr(0,1, 15).decode("UTF-8"))
        if text=="":
            continue
        elif text[0] is "q" or "quit" in text:
            readable_file.close()
            curses.endwin()
            sys.exit()
        elif "refresh" in text:
            curses.echo()
            actual_leiste.erase()
            read_in_file(readable_file, dic)
            top_five=get_top_five(dic, 0)
            draw_graph_1(rechts, top_five, get_top_five_keys(dic, top_five))
            draw_graph_2(links, top_five, get_top_five_keys(dic, top_five))
            actual_leiste.refresh()
        else:
            actual_leiste.erase()
            append_file=open(cur_file, 'a');
            append_file.write(datetime.datetime.now().strftime('%s')+" "+text+"\n")
            actual_leiste.refresh()
            append_file.close()
            #text=(str)(actual_leiste.getstr(0,0, 15))
    #elif new_chr is "l":# in text:
    elif new_chr is ord('l'):
        lx=links.getmaxyx()[1]
        rx=rechts.getmaxyx()[1]
        links=curses.newwin(y-3, lx+1, 0, 0)
        rechts=curses.newwin(y-3, (int)(x/2)-global_r_offset, 0, (int)(x/2)+global_r_offset+1)
        global_r_offset+=1
        redraw(dic, links, rechts)
    elif new_chr is ord('h'):
        lx=links.getmaxyx()[1]
        rx=rechts.getmaxyx()[1]
        links=curses.newwin(y-3, lx-1, 0, 0)
        rechts=curses.newwin(y-3, rx+1, 0, (int)(x/2)+global_r_offset-1)
        global_r_offset-=1
        redraw(dic, links, rechts)
    elif new_chr is ord('j'):
        curses.echo()
        actual_leiste.erase()
        read_in_file(readable_file, dic)
        #actual_leiste.addstr(0,0,str(len(list(dic.keys()))))
        if global_vis_offset<len(list(dic.keys()))-6:
            global_vis_offset+=1
        top_five=get_top_five(dic, global_vis_offset)
        draw_graph_1(rechts, top_five, get_top_five_keys(dic, top_five))
        draw_graph_2(links, top_five, get_top_five_keys(dic, top_five))
        actual_leiste.refresh()
    elif new_chr is ord('k'):
        curses.echo()
        actual_leiste.erase()
        read_in_file(readable_file, dic)
        if global_vis_offset>0:
            global_vis_offset-=1
        else:
            continue
        top_five=get_top_five(dic, global_vis_offset)
        draw_graph_1(rechts, top_five, get_top_five_keys(dic, top_five))
        draw_graph_2(links, top_five, get_top_five_keys(dic, top_five))
        actual_leiste.refresh()
    elif new_chr is "q":# in text:
        break

#curses.addstr(4,1,text.encode('utf_8'))
readable_file.close()
curses.endwin()
