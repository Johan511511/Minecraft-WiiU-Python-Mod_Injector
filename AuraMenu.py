#===== Imports =====

from tkinter import *
import tkinter as tkinter
from TCP.tcpgecko import TCPGecko
import sys
import os
from IP import IP_Addr

#===== Imports End =====


#===== Main Window =====

window = Tk()
window.title('Aura Menu')
window.geometry('550x110')

# Print Logo
print("""

    █████╗ ██╗   ██╗██████╗  █████╗      ██████╗ ██████╗ ██████╗ ███████╗███████╗
   ██╔══██╗██║   ██║██╔══██╗██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
   ███████║██║   ██║██████╔╝███████║    ██║     ██║   ██║██║  ██║█████╗  ███████╗
   ██╔══██║██║   ██║██╔══██╗██╔══██║    ██║     ██║   ██║██║  ██║██╔══╝  ╚════██║
   ██║  ██║╚██████╔╝██║  ██║██║  ██║    ╚██████╗╚██████╔╝██████╔╝███████╗███████║
   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝
        
""")


#===== Main Window End =====


#===== Section: Defined Functions =====

def lvl1():
    if cg.get() == 1:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F100000)
        tcp.s.close()
        print("Aura Lvl 1 is now active")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cg.get() == 0:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.s.close()
        print("Aura reset!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def lvl2():
    if cg.get() == 2:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F200000)
        tcp.s.close()
        print("Aura Lvl 2 is now active")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cg.get() == 3:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.s.close()
        print("Aura reset!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def lvl3():
    if cg.get() == 4:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F300000)
        tcp.s.close()
        print("Aura Lvl 3 is now active")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cg.get() == 5:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.s.close()
        print("Aura reset!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def lvl4():
    if cg.get() == 6:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F400000)
        tcp.s.close()
        print("Aura Lvl 4 is now active")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cg.get() == 7:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.s.close()
        print("Aura reset!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def lvl5():
    if cg.get() == 8:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F500000)
        tcp.s.close()
        print("Aura Lvl 5 is now active")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cg.get() == 9:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.s.close()
        print("Aura reset!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def lvl6():
    if cg.get() == 10:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F600000)
        tcp.s.close()
        print("Aura Lvl 6 is now active")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cg.get() == 11:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.s.close()
        print("Aura reset!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def lvl7():
    if cg.get() == 12:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F700000)
        tcp.s.close()
        print("Aura Lvl 7 is now active")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cg.get() == 13:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.s.close()
        print("Aura reset!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def lvl8():
    if cg.get() == 14:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F800000)
        tcp.s.close()
        print("Aura Lvl 8 is now active")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cg.get() == 15:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.s.close()
        print("Aura reset!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def lvl9():
    if cg.get() == 16:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3FF00000)
        tcp.s.close()
        print("In the words of 9 year olds: You're a hackowr")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cg.get() == 17:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.s.close()
        print("Aura reset!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def lvl10():
    if cg.get() == 18:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x41099999)
        tcp.s.close()
        print("I think you just became god")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cg.get() == 19:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.s.close()
        print("Aura reset!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
#===== Section: Defined Functions End =====


#===== Section: Check Boxes =====

cg = IntVar()

c = Checkbutton(window, text="Level One", variable=cg, onvalue=1, offvalue=0, command=lvl1)
c.grid(column=0, row=0)

c = Checkbutton(window, text="Level Two", variable=cg, onvalue=2, offvalue=3, command=lvl2)
c.grid(column=1, row=0)

c = Checkbutton(window, text="Level Three", variable=cg, onvalue=4, offvalue=5, command=lvl3)
c.grid(column=2, row=0)

c = Checkbutton(window, text="Level Four", variable=cg, onvalue=6, offvalue=7, command=lvl4)
c.grid(column=3, row=0)

c = Checkbutton(window, text="Level Five", variable=cg, onvalue=8, offvalue=9, command=lvl5)
c.grid(column=4, row=0)

c = Checkbutton(window, text="Level Six", variable=cg, onvalue=10, offvalue=11, command=lvl6)
c.grid(column=0, row=1)

c = Checkbutton(window, text="Level Seven", variable=cg, onvalue=12, offvalue=13, command=lvl7)
c.grid(column=1, row=1)

c = Checkbutton(window, text="Level Eight", variable=cg, onvalue=14, offvalue=15, command=lvl8)
c.grid(column=2, row=1)

c = Checkbutton(window, text="Blatamt", variable=cg, onvalue=16, offvalue=17, command=lvl9)
c.grid(column=3, row=1)

c = Checkbutton(window, text="Absurdly Blatamt", variable=cg, onvalue=18, offvalue=19, command=lvl10)
c.grid(column=4, row=1)

btn = Button(window, text="Close", bd='2', bg="silver", fg="black",command=window.destroy)
btn.grid(column=4, row=5)

window.mainloop()
