#!/usr/bin/python
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import random
import time
from random import randrange, randint
class ROBO:
   def __init__(self,ht,wt,sz,nd):
          self.xposn=2
          self.yposn=2
          self.size=sz
          self.score=0
          self.defuses=[]
          self.noofdefuses=nd
          self.bombPos=[]
          self.height=ht
          self.width=wt
          self.h=[]
          self.m=[wt/4,(wt/4)+1,3*wt/4,(3*wt/4)+1]
          for i in range(ht/4,(3*ht/4)+1):
             self.h.append(i)
          self.robo=[["^^","||"],["~0~"," | ","^^^"],["-  -"," ** "," || ","----"],["  |  ","- 0 -","  |  "," / \ ","  0  "]]
   def printrobo(self,win):
       for i in range(self.size):
          for j in range(self.size):
              win.addch(self.yposn+i,self.xposn+j,(self.robo[self.size-2])[i][j],curses.color_pair((i+j)%4))
   def setdefuses(self):
     while len(self.defuses) < self.noofdefuses + 1:     # Randomly calculating the coordinates of defuse codes along with the last posn for bombposn
        (self.defuses).extend([n for n in [[randint(1, (self.height)-2), randint(1, (self.width)-2)] for x in range(20)] if (n[0] < self.yposn or n[0] > self.yposn + self.size) and (n[1] < self.xposn or n[1] > self.xposn + self.size)]) 
     for i in range(len(self.h)):
         for j in range(len(self.m)):
             for d in self.defuses:
                 if d[0]==self.h[i] and d[1]==self.m[j]:
                    (self.defuses).remove(d)
     self.bombPos = self.defuses[len(self.defuses) - 1]    # Position of bomb is the last coordinate calculated    
     self.defuses = self.defuses[:self.noofdefuses]    
   def checkdefuses(self):
     for d in self.defuses:
         if d[0]<self.yposn+self.size and d[0]>=self.yposn and d[1]<self.xposn+self.size and d[1]>=self.xposn:
             return d
     return []
   def remdef(self,d):
        (self.defuses).remove(d)
   def checkbomb(self):
     if self.bombPos[0]<self.yposn+self.size and self.bombPos[0]>=self.yposn and self.bombPos[1]<self.xposn+self.size and self.bombPos[1]>=self.xposn:
        return 1
     return 0
   def endgame_win(self):
	 curses.flash()
	 win = curses.newwin(5,30,1,1)
	 win.border(0)
	 win.addstr(1,1,"BOMB DEFUSED",curses.color_pair(3))
	 pos = 17
	 for i in range(10):
          win.addstr(1,pos,".",curses.color_pair(2))
          win.refresh()
          time.sleep(0.05)
          pos += 1
	 win.addstr(2,1,"YOU PROCEED TO NEXT LEVEL !!",curses.color_pair(2))
	 win.refresh()
	 time.sleep(1)
         win=curses.newwin(5,30,1,1)
         win.refresh()
         
   def show_progress(self):
         c=self.score
	 win = curses.newwin(3,40,1,1)
	 win.border(0)
	 win.addstr(1,1,"Codes collected ",curses.color_pair(2))
	 pos = 17
	 for i in range(15):
            win.addstr(1,pos,".",curses.color_pair(2))
            win.refresh()
            time.sleep(0.01)
            pos += 1
	 win.addstr(1,35,str(c),curses.color_pair(2))
	 win.refresh()
	 time.sleep(0.5)
	 win=curses.newwin(3,40,1,1)
	 win.refresh()
   def endgame_lose(self):
	 curses.flash()
	 win = curses.newwin(5,40,1,1)
	 win.border()
	 win.addstr(1,1,"EXPLOSION",curses.color_pair(3))
	 pos = 17
	 for i in range(15):
          win.addstr(1,pos,".",curses.color_pair(2))
          win.refresh()
          time.sleep(0.05)
          pos += 1
	 win.addstr(2,10,"YOU LOSE :-( !!",curses.color_pair(2))
	 win.refresh()
	 time.sleep(1)

   def incscore(self):
      self.score+=1
   def gyvscore(self):
      return self.score
   def printdef(self,win):
     for d in self.defuses:
        win.addch(d[0],d[1],'D',curses.color_pair(2))
   def printbomb(self,win):
     win.addch(self.bombPos[0],self.bombPos[1],'B',curses.color_pair(1))
   def checkposn(self):
     if self.xposn <= 0 or self.yposn <=0 or self.xposn + self.size >= self.width or self.yposn + self.size >= self.height:
        return 1
     return 0
   def checkposn2(self):
     flag=0
     if self.xposn <= 0 or self.yposn <=0 or self.xposn + self.size >= self.width or self.yposn + self.size >= self.height : 
          return 1
     else:
        for i in range(len(self.h)):
         for j in range(len(self.m)):
             if self.yposn==self.h[i] and self.xposn==self.m[j]:
                 flag=1
                 return 1
        return 0    
   def inxpos(self):
       self.xposn+=1
   def ndefu(self):
        return self.noofdefuses
   def dexpos(self):
       self.xposn-=1
   def inypos(self):
       self.yposn+=1
   def deypos(self):
       self.yposn-=1
   def setwalls(self,win):
       flag=0
       #m=[self.width/4,(self.width/4)+1,3*self.width/4,(3*self.width/4)+1]
       for i in range(self.height/4,(3*self.height/4)+1):
           for j in range(len(self.m)):
              #flag=0
              #for k in range(len(self.defuses)):
               #   if (self.defuses[k][0]==i and (self.defuses)[k][1]==self.m[j]):
                #      flag=1
                #r      break
              #if flag==0 and self.bombPos[0]==i and self.bombPos[1]==self.m[j]:
              #       flag=1
              #if flag==0:
               win.addch(i,self.m[j],'|',curses.color_pair((i+j)%4))
              # (self.wall).append([i,j])
   def end(self,status,lel2):
     curses.endwin()
     print("\nYour Score - " + str(self.score))
     if status == 1 and lel2==1:
         print("\nCongratulations!!Both level cleared!!!!\n")
     elif status==1 and lel2==0:
         print("\nCongratulations!!Level 1 cleared....2 lost!!!!\n")

     else:
         print("\nGAME OVER.....YOU LOSE\n")
     exit(0)


if __name__=='__main__':
   ht=int(raw_input("Enter height of window:"));
   wt=int(raw_input("Enter width of window:"));
   sz=int(raw_input("Enter size of robo:"));
   nd=int(raw_input("Enter no of defuses:"));
   mode=raw_input("Enter mode:\nEASY(e)     MEDIUM(m)     INSANE(i)\n");
   if mode=='e':
       x=100
   if mode=='m':
       x=60
   if mode=='i':
      x=40
   l=1
   r=ROBO(ht,wt,sz,nd)
   curses.initscr()
   curses.curs_set(0)
   curses.start_color()
   #curses.init_pair(0, curses.COLOR_GREEN, curses.COLOR_BLACK)
   curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
   curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
   curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
   curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
   #time.sleep(3)
   #curses.endwin()
   #width=50   #of screen
   #height=30      #of scr
   win=curses.newwin(ht,wt,0,0)
   win.keypad(1)
   win.border(0)
   win.nodelay(1)
   curses.noecho()
   key=-1
   defaultkey=KEY_RIGHT
   r.setdefuses()

   while key!=27:      #jab tak ecp key nae aata
     win.clear()
     win.border(0)
     if r.checkposn()==1:
            r.end(0,0)
     r.printrobo(win)
     t=r.checkdefuses()
     if t:
        r.remdef(t)
        r.incscore()
        r.show_progress()
     if r.checkbomb():
         if r.gyvscore()==r.ndefu():
              r.endgame_win()
              win.addstr(ht/2,2,"LEVEL 1..CLEARED..",curses.color_pair(3))
              win.addstr(ht/2+1,2,"press 1 for next level",curses.color_pair(3))
           
              l+=1
              #key=defaultkey
              while 1>0:
                  key=win.getch()
                  key=key if key==-1 else key  
                  if key==ord('1'):                     
                     #curses.endwin()
                     r2=ROBO(ht,wt,sz,nd)
                     curses.initscr()
                     curses.curs_set(0)
                     curses.start_color()
                     win=curses.newwin(ht,wt,0,0)
                     win.keypad(1)
                     win.border(0)
                     win.nodelay(1)
                     curses.noecho()
                     #win.addstr(ht/2,2,"welcome")
                     #win.refresh()
                     key=-1
                     defaultkey=KEY_RIGHT
                     r2.setdefuses()
                     cleared=0
                     #r2.setwalls(win)
                     #win.addstr(20,1,"....")
                     while key!=27:      #jab tak ecp key nae aata
                           win.clear()
                           win.border(0)
                           #r2.setwalls(win)
                           if r2.checkposn2()==1:
                             # cleared=0
                              break
                           r2.printrobo(win)
                           t=r2.checkdefuses()
                           if t:
                              r2.remdef(t)
                              r2.incscore()
                              r2.show_progress()
                           if r2.checkbomb():
                                 if r2.gyvscore()==r2.ndefu():
                                     cleared=1
				     break
                                 else:
				     cleared=0
				     break
                           r2.printdef(win)
                           r2.printbomb(win)
                           r2.setwalls(win)
                           win.addstr(0,2,'Codes Taken='+str(r2.gyvscore())+'..')
                           win.addstr(0,16,'Level:'+str(l))
                           win.timeout(x-20)
                           key=win.getch()
                           key = defaultkey if key==-1 else key
                           if key==27:
                                curses.endwin()
                                break
                                #print "LOSER"
                                #exit(0)
                           if key==ord('p') or key==ord('P'):
                                     while 1>0:
                                       key=win.getch()
                                       if key==ord('p') or key==ord('P'):
                                             break
                                     key=win.getch()   
                                     key = defaultkey if key==-1 else key
                           if key==KEY_RIGHT:
                                 r2.inxpos()
	                         defaultkey=KEY_RIGHT
                           elif key==KEY_LEFT:
                                 r2.dexpos()
	                         defaultkey=KEY_LEFT
                           elif key==KEY_UP:
                                r2.deypos()
	                        defaultkey=KEY_UP
                           elif key==KEY_DOWN:
                                 r2.inypos()
	                         defaultkey=KEY_DOWN
                     #key=win.getch()
                     #while 1>0:
                     #    key=win.getch()
                     #    defaultkey=key
                     #    key=defaultkey if key==-1 else key
                     #    if key==ord('2'):
                     #       curses.endwin()
                     #       break
                     break
              if cleared==1:
                r.end(1,1)
                r2.printwall()
              else:
                r.end(1,0)
         else:
           r.endgame_lose()
           r.end(0,0)
     r.printdef(win)
     r.printbomb(win)
     win.addstr(0,2,'Codes Taken='+str(r.gyvscore())+'..')
     win.addstr(0,16,'Level:'+str(l))
     win.timeout(x)
     key=win.getch()
     key = defaultkey if key==-1 else key
     if key==27:
       curses.endwin()
       print "LOSER"
       exit(0)
     if key==ord('p') or key==ord('P'):
       while 1>0:
          key=win.getch()
          if key==ord('p') or key==ord('P'):
             break
       key=win.getch()   
       key = defaultkey if key==-1 else key
     if key==KEY_RIGHT:
        r.inxpos()
	defaultkey=KEY_RIGHT
     elif key==KEY_LEFT:
        r.dexpos()
	defaultkey=KEY_LEFT
     elif key==KEY_UP:
        r.deypos()
	defaultkey=KEY_UP
     elif key==KEY_DOWN:
        r.inypos()
	defaultkey=KEY_DOWN
        win.clearok(1)
        win.refresh()
 #finally:
  #  curses.nocbreak()
  #  stdscr.keypad(0)
  #  curses.echo()
  #  curses.endwin()

