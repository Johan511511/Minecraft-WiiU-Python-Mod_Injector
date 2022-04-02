#===== Imports =====

from tkinter import *
import tkinter as tkinter
from TCP.tcpgecko import TCPGecko
from IP import IP_Addr
import sys
import os

#===== Imports End =====


#===== Main Window =====

window = Tk()
window.title('Korozin RTM V2')
window.geometry('580x110')

# Print Logo
print("""

   ██╗  ██╗ ██████╗ ██████╗  ██████╗ ███████╗██╗███╗   ██╗    ██████╗ ████████╗███╗   ███╗    ██╗   ██╗██████╗ 
   ██║ ██╔╝██╔═══██╗██╔══██╗██╔═══██╗╚══███╔╝██║████╗  ██║    ██╔══██╗╚══██╔══╝████╗ ████║    ██║   ██║╚════██╗
   █████╔╝ ██║   ██║██████╔╝██║   ██║  ███╔╝ ██║██╔██╗ ██║    ██████╔╝   ██║   ██╔████╔██║    ██║   ██║ █████╔╝
   ██╔═██╗ ██║   ██║██╔══██╗██║   ██║ ███╔╝  ██║██║╚██╗██║    ██╔══██╗   ██║   ██║╚██╔╝██║    ╚██╗ ██╔╝██╔═══╝ 
   ██║  ██╗╚██████╔╝██║  ██║╚██████╔╝███████╗██║██║ ╚████║    ██║  ██║   ██║   ██║ ╚═╝ ██║     ╚████╔╝ ███████╗
   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝      ╚═══╝  ╚══════╝             
""")

#===== Main Window End =====


#===== Section: Defined Functions =====

def armorHud():
    if cb.get() == 2:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02E9B1B0, 0x7FE4FB78)
        tcp.s.close()
        print("You can now see the armor hud like in mini-games!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 3:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02E9B1B0, 0x7FC4F378)
        tcp.s.close()
        print("Armor Hud Disabled")
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
        
def megaCode():
    if cb.get() == 1:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02F88110, 0x39400002)
        tcp.pokemem(0x02FAF4F0, 0x39400002)
        tcp.pokemem(0x02FAF560, 0x39400002)
        tcp.pokemem(0x02FAF5DC, 0x39400002)
        tcp.pokemem(0x02FAF64C, 0x39400002)
        tcp.pokemem(0x030FA014, 0x2C090001)
        tcp.pokemem(0x030F9D38, 0xFC605018)
        tcp.pokemem(0x030F9D3C, 0xFC20A018)
        tcp.pokemem(0x030F9D40, 0xFC005018)
        tcp.pokemem(0x030F9D30, 0xFC405018)
        tcp.pokemem(0x030F9D10, 0xFD69482A)
        tcp.pokemem(0x030F9D20, 0xFD494828)
        tcp.pokemem(0x030F9C50, 0x7F24CB78)
        tcp.pokemem(0x11120008, 0x000006D5)
        tcp.pokemem(0x02D5731C, 0x38600001)
        tcp.pokemem(0x02D57320, 0x4E800020)
        tcp.pokemem(0x02F70970, 0x38600001)
        tcp.pokemem(0x032283CC, 0x38800000)
        tcp.pokemem(0x02F59534, 0x480002E8)
        tcp.pokemem(0x02DEC0B4, 0x38600001)
        tcp.pokemem(0x10997EA8, 0x30000000)
        tcp.pokemem(0x02E9B1B0, 0x7FE4FB78)
        tcp.pokemem(0x030FA0C8, 0x616500FF)
        tcp.pokemem(0x0384CD3C, 0x60000000)
        tcp.pokemem(0x0384CD40, 0x3D804100)
        tcp.pokemem(0x0384CD44, 0x618C0003)
        tcp.pokemem(0x0384CD48, 0x80AC0000)
        tcp.pokemem(0x0384CD4C, 0x4B8AD380)
        tcp.pokemem(0x108C7C2C, 0x60000000)
        tcp.pokemem(0x0205C430, 0x38600000)
        tcp.pokemem(0x031B2B4C, 0x38600001)
        tcp.pokemem(0x02F5C874, 0x38600001)
        tcp.pokemem(0x105DD948, 0x3F100000)
        tcp.s.close()
        print("Mega code is now activated!")
    elif cb.get() == 0:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x105DD948, 0x3F000000)
        tcp.pokemem(0x02F70970, 0x38600000)
        tcp.pokemem(0x032283CC, 0x38800001)
        tcp.pokemem(0x02F59534, 0x7C0802A6)
        tcp.pokemem(0x02DEC0B4, 0x57E3063E)
        tcp.pokemem(0x02F88110, 0x39400003)
        tcp.pokemem(0x02FAF4F0, 0x39400003)
        tcp.pokemem(0x02FAF560, 0x39400003)
        tcp.pokemem(0x02FAF5DC, 0x39400003)
        tcp.pokemem(0x02FAF64C, 0x39400003)
        tcp.pokemem(0x10997EA8, 0x3F000000)
        tcp.pokemem(0x02E9B1B0, 0x7FC4F378)
        tcp.pokemem(0x108C7C2C, 0x3CF5C28F)
        tcp.pokemem(0x0205C430, 0x3860FFFF)
        tcp.pokemem(0x030EA1C8, 0x6CC08000)
        tcp.pokemem(0x02F5C874, 0x38600000)
        tcp.pokemem(0x02D5731C, 0x7C0802A6)
        tcp.pokemem(0x02D57320, 0x9421FFF0)
        tcp.pokemem(0x030F9D38, 0xFC405018)
        tcp.pokemem(0x030F9D3C, 0xFC604018)
        tcp.pokemem(0x030F9D40, 0xFC205818)
        tcp.pokemem(0x030F9D30, 0xFD1D682A)
        tcp.pokemem(0x030F9D10, 0xFD6D682A)
        tcp.pokemem(0x030F9D20, 0xFD49582A)
        tcp.pokemem(0x030FA0C8, 0x38A5FFFF)
        tcp.pokemem(0x030FA014, 0x2C090000)
        tcp.pokemem(0x030F9C50, 0x388000FF)
        tcp.pokemem(0x108C9C20, 0x40080000)
        tcp.pokemem(0x0232F3A0, 0x38800000)
        tcp.s.close()
        print("Codes Disabled!")
        canv = Tk()
        canv.title('Code Disabled!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                      fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def craftAll():
    if cb.get() == 3:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02F70970, 0x38600001)
        tcp.pokemem(0x032283CC, 0x38800001)
        tcp.pokemem(0x02F59534, 0x7C0802A6)
        tcp.s.close()
        print("Craft all now disabled!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 4:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02F70970, 0x38600000)
        tcp.s.close()
        print("Armor Hud Disabled")
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
        
def fly():
    if cb.get() == 5:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x0271AA74, 0x38600001)
        tcp.s.close()
        print("You can now fly!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 6:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x0271AA74, 0x38600000)
        tcp.s.close()
        print("Fly disabled!")
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
        
def FOFbypass():
    if cb.get() == 7:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02D5731C, 0x38600001)
        tcp.pokemem(0x02D57320, 0x4E800020)
        tcp.s.close()
        print("You can now bypass Friends of Friends!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 8:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02D5731C, 0x7C0802A6)
        tcp.pokemem(0x02D57320, 0x9421FFF0)
        tcp.s.close()
        print("FOF Disabled")
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
        
def host():
    if cb.get() == 9:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02F17B30, 0x38807D00)
        tcp.s.close()
        print("You can now use host options anywhere!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 10:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02D5731C, 0x7C0802A6)
        tcp.pokemem(0x02D57320, 0x9421FFF0)
        tcp.s.close()
        print("Host options disabled!")
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
        
def multiJump():
    if cb.get() == 11:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x0232F3A0, 0x38800001)
        tcp.s.close()
        print("Multi-Jump is now active!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 12:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x0232F3A0, 0x38800000)
        tcp.s.close()
        print("Multi-Jump disabled!")
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
        
def muteMic():
    if cb.get() == 13:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x10997EA8, 0x30000000)
        tcp.s.close()
        print("Your mic is now muted!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 14:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x10997EA8, 0x3F000000)
        tcp.s.close()
        print("Mute mic disabled!")
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
        
def reach():
    if cb.get() == 15:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x108C9C20, 0x50090000)
        tcp.s.close()
        print("Reach = 3 blocks")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 16:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x108C9C20, 0x40080000)
        tcp.s.close()
        print("reach disabled")
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
        
def keyboard():
    if cb.get() == 17:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02F88110, 0x39400002)
        tcp.pokemem(0x02FAF4F0, 0x39400002)
        tcp.pokemem(0x02FAF560, 0x39400002)
        tcp.pokemem(0x02FAF5DC, 0x39400002)
        tcp.pokemem(0x02FAF64C, 0x39400002)
        tcp.s.close()
        print("The entire keyboard is now unlocked!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 18:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02F88110, 0x39400003)
        tcp.pokemem(0x02FAF4F0, 0x39400003)
        tcp.pokemem(0x02FAF560, 0x39400003)
        tcp.pokemem(0x02FAF5DC, 0x39400003)
        tcp.pokemem(0x02FAF64C, 0x39400003)
        tcp.s.close()
        print("Keyboard locked!")
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
        
def FOV():
    if cb.get() == 19:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x1088EDA8, 0x3F800000)
        tcp.s.close()
        print("FOV Enhanced")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 20:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x1088EDA8, 0x3F000000)
        tcp.s.close()
        print("FOV Reset")
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
        
def Hitbox():
    if cb.get() == 21:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x030FA0C8, 0xFFFFFFFF)
        tcp.pokemem(0x030FA014, 0x2C090001)
        tcp.pokemem(0x030F9C50, 0xFFFFFFFF)
        tcp.s.close()
        print("Hitbox now shown!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 22:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x030FA0C8, 0xFFFFFFFF)
        tcp.pokemem(0x030FA014, 0x2C090001)
        tcp.pokemem(0x030F9C50, 0xFFFFFFFF)
        tcp.s.close()
        print("Hitbox now shown!")
        canv = Tk()
        canv.title('Disabling for this code has not yet been added.')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def itemJava():
    if cb.get() == 23:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x0316760C, 0x60000000)
        tcp.pokemem(0x0316762C, 0xFC80F090)
        tcp.pokemem(0x03168DCC, 0xEC4F6BFA)
        tcp.pokemem(0x0384CEBC, 0x3D801002)
        tcp.pokemem(0x0384CEC0, 0x3C40433A)
        tcp.pokemem(0x0384CEC4, 0x904C0110)
        tcp.pokemem(0x0384CEC8, 0xC02C0110)
        tcp.pokemem(0x0384CECC, 0x4B91A770)
        tcp.pokemem(0x03167638, 0x486E5884)
        tcp.s.close()
        print("Item Drop animation has now been modified!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 24:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x0316760C, 0x60000000)
        tcp.pokemem(0x0316762C, 0xFC80F090)
        tcp.pokemem(0x03168DCC, 0xEC4F6BFA)
        tcp.pokemem(0x0384CEBC, 0x3D801002)
        tcp.pokemem(0x0384CEC0, 0x3C40433A)
        tcp.pokemem(0x0384CEC4, 0x904C0110)
        tcp.pokemem(0x0384CEC8, 0xC02C0110)
        tcp.pokemem(0x0384CECC, 0x4B91A770)
        tcp.pokemem(0x03167638, 0x486E5884)
        tcp.s.close()
        print("Disabling for this code has not yet been added.")
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
        
def offhand():
    if cb.get() == 25:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x024FD7F4, 0x38600001)
        tcp.pokemem(0x0207F604, 0x38600001)
        tcp.s.close()
        print("All item slots have been unlocked! (eg offhand and body slots)")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 26:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x024FD7F4, 0x38600000)
        tcp.pokemem(0x0207F604, 0x38600000)
        tcp.s.close()
        print("Item slots back to normal")
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
        
def takeAll():
    if cb.get() == 27:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02DEC0B4, 0x38600001)
        tcp.s.close()
        print("You can now take everything from chests!")
        canv = Tk()
        canv.title('Codes Sent!')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
    elif cb.get() == 28:
        tcp = TCPGecko(IP_Addr)
        tcp.pokemem(0x02DEC0B4, 0x57E3063E)
        tcp.s.close()
        print("You can no longer take everything")
        canv = Tk()
        canv.title('Code Disabled')
        canv.geometry('200x40')
        btn = Button(canv, text="                           OK!                           ", bd='5', bg="black",                         fg="white",command=canv.destroy)
        btn.pack(side='top')
        canv.mainloop()
    else:
        canv = Tk()
        canv.title('Error!')
        canv.geometry('200x40')
        btn = Button(canv, text = "ERROR!", bd='5', bg="black",                      fg="white",command=canv.destroy)
        
def auraMenu():
    os.system("python AuraMenu.py")
        
#===== Section: Defined Functions End =====


#===== Section: Check Boxes =====

cb = IntVar()

c = Checkbutton(window, text="Mega-Code", variable=cb, onvalue=1, offvalue=0, command=megaCode)
c.grid(column=0, row=0)

c = Checkbutton(window, text="Armor Hud", variable=cb, onvalue=2, offvalue=3, command=armorHud)
c.grid(column=1, row=0)

c = Checkbutton(window, text="Craft All", variable=cb, onvalue=3, offvalue=4, command=craftAll)
c.grid(column=2, row=0)

c = Checkbutton(window, text="Fly", variable=cb, onvalue=5, offvalue=6, command=fly)
c.grid(column=3, row=0)

c = Checkbutton(window, text="FOF Bypass", variable=cb, onvalue=7, offvalue=8, command=FOFbypass)
c.grid(column=4, row=0)

c = Checkbutton(window, text="Host Options", variable=cb, onvalue=9, offvalue=10, command=host)
c.grid(column=0, row=1)

c = Checkbutton(window, text="Multi-Jump", variable=cb, onvalue=11, offvalue=12, command=multiJump)
c.grid(column=1, row=1)

c = Checkbutton(window, text="Mute Mic", variable=cb, onvalue=13, offvalue=14, command=muteMic)
c.grid(column=2, row=1)

c = Checkbutton(window, text="Reach", variable=cb, onvalue=15, offvalue=16, command=reach)
c.grid(column=3, row=1)

c = Checkbutton(window, text="Unlock Keyboard", variable=cb, onvalue=17, offvalue=18, command=keyboard)
c.grid(column=4, row=1)

c = Checkbutton(window, text="FOV", variable=cb, onvalue=19, offvalue=20, command=FOV)
c.grid(column=0, row=2)

c = Checkbutton(window, text="Draw Hitbox", variable=cb, onvalue=21, offvalue=22, command=Hitbox)
c.grid(column=1, row=2)

c = Checkbutton(window, text="Item Drop", variable=cb, onvalue=23, offvalue=24, command=itemJava)
c.grid(column=2, row=2)

c = Checkbutton(window, text="Unlock Offhand", variable=cb, onvalue=25, offvalue=26, command=offhand)
c.grid(column=3, row=2)

c = Checkbutton(window, text="Take All", variable=cb, onvalue=27, offvalue=28, command=takeAll)
c.grid(column=4, row=2)

btn = Button(window, text="Aura Menu", bd='2', bg="silver", fg="black",command=auraMenu)
btn.grid(column=4, row=5)

window.mainloop()
