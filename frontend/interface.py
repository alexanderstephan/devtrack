import curses
import curses.textpad
import time
import _thread
import datetime
from collections import OrderedDict
#from time import gmtime, strftime


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
                
    
    offset=(int)(maxx*0.75)
    for i,j in enumerate(reversed(keys)):
        win.addstr(2*i+2,offset,j)
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
        draw_graph_2(win, get_top_five(dic))
        actual_leiste.refresh()
        time.sleep(delay)
        
def get_top_five(dic):
    return sorted(dic.values(),reverse=True)[:5]

def get_top_five_keys(dic, top_five):
    # sorted_dict=OrderedDict(sorted(dic.items()))
    # sorted_keys=list(reversed(sorted_dict.keys()))
    # print(dic.items())
    # print(sorted(dic.items()))
    # print(dic)
    # print(sorted_dict)
    # print(sorted_keys)
    # return sorted_keys[:5]
    return_arr=[]
    for i in top_five:
        for j in list(dic.keys()):
            if dic[j]==i:
                return_arr.append(j)
    return list(reversed(return_arr))



cur_date=datetime.datetime.now().strftime('%Y %m %d').split(' ')
cur_day=datetime.date((int)(cur_date[0]), (int)(cur_date[1]), (int)(cur_date[2])).strftime('%s')

cur_file="/home/confringe/Hackatum/"+cur_day
readable_file=open(cur_file)
dic={}
read_in_file(readable_file, dic)
#file.close()
#top_five=sorted(dic.values(),reverse=True)[:6]
top_five=get_top_five(dic)
#print(top_five)
#_thread.start_new_thread(wrapper_read_in_file, (readable_file, dic, 5, links, ))
get_top_five_keys(dic,top_five)

#time.sleep(10)


stdscr = curses.initscr()

curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)


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


cur_date=datetime.datetime.now().strftime('%Y %m %d').split(' ')
cur_day=datetime.date((int)(cur_date[0]), (int)(cur_date[1]), (int)(cur_date[2])).strftime('%s')

cur_file="/home/confringe/Hackatum/"+cur_day
readable_file=open(cur_file)
dic={}
read_in_file(readable_file, dic)
#file.close()
#top_five=sorted(dic.values(),reverse=True)[:6]
top_five=get_top_five(dic)
#print(top_five)
#_thread.start_new_thread(wrapper_read_in_file, (readable_file, dic, 5, links, ))



draw_graph_1(rechts, top_five, get_top_five_keys(dic, top_five))
draw_graph_2(links, top_five, get_top_five_keys(dic, top_five))

curses.echo()
text=actual_leiste.getstr(0,0, x).decode()
#while text!='quit' or text!='q' or text!=':q':
#while bytes(":q") not in text and bytes("quit") not in text:
while ":q" not in (str)(text) and "quit" not in str(text):
    actual_leiste.erase()
    append_file=open(cur_file, 'a');
    append_file.write(datetime.datetime.now().strftime('%s')+" "+(str)(text)+"\n")
    actual_leiste.refresh()
    append_file.close()
    text=actual_leiste.getstr(0,0, 15)

#curses.addstr(4,1,text.encode('utf_8'))
readable_file.close()
curses.endwin()
