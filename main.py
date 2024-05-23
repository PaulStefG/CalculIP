import math
from tkinter import *
from tkinter.ttk import *

def calculIPuri(p):
    in1 = int(E1.get())
    in2 = int(E2.get())
    in3 = int(E3.get())
    in4 = int(E4.get())

    in1b = bin(in1)[2:].zfill(8)
    in2b = bin(in2)[2:].zfill(8)
    in3b = bin(in3)[2:].zfill(8)
    in4b = bin(in4)[2:].zfill(8)

    prefix = p
    pf = '1' * prefix
    pf += '0' * (32 - prefix)

    ipBin = [in1b, in2b, in3b, in4b]
    ipB = ipBin[0] + ipBin[1] + ipBin[2] + ipBin[3]
    ipB_int = int(ipB, 2)

    result = ipB_int & int(pf, 2)
    result_bin = bin(result)[2:].zfill(32)
    Network = [int(result_bin[0:8], 2), int(result_bin[8:16], 2), int(result_bin[16:24], 2), int(result_bin[24:32], 2)]
    SubnetMask = [int(pf[0:8], 2), int(pf[8:16], 2), int(pf[16:24], 2), int(pf[24:32], 2)]

    pc = '0' * prefix
    pc += '1' * (32 - prefix)
    BCast = ipB_int | int(pc, 2)
    BCast_bin = bin(BCast)[2:].zfill(32)
    Broadcast = [int(BCast_bin[0:8], 2), int(BCast_bin[8:16], 2), int(BCast_bin[16:24], 2), int(BCast_bin[24:32], 2)]

    gr = ""
    if SubnetMask[0] == 255:
        if SubnetMask[1] == 255:
            if SubnetMask[2] == 255:
                gr = "D"
            else:
                gr = "C"
        else:
            gr = "B"
    else:
        gr = "A"

    F_IP_Util = [int(result_bin[0:8], 2), int(result_bin[8:16], 2), int(result_bin[16:24], 2),
                 int(result_bin[24:32], 2) + 1]
    L_IP_Util = [int(BCast_bin[0:8], 2), int(BCast_bin[8:16], 2), int(BCast_bin[16:24], 2),
                 int(BCast_bin[24:32], 2) - 1]

    NrTotClase = pow(2, (32 - prefix))
    NrClaseUtile = pow(2, (32 - prefix)) - 2

    rez = ("Adresa de Retea (Network): " + ".".join(map(str, Network)) + "\n"
           + "Broadcast: " + ".".join(map(str, Broadcast)) + "\n"
           + "Primul IP util:" + ".".join(map(str, F_IP_Util)) + "\n"
           + "Ultimul IP Util: " + ".".join(map(str, L_IP_Util)) + "\n"
           + "Subnet Mask: " + ".".join(map(str, SubnetMask)) + "\n"
           + "Nr. total de adrese in clasa: " + str(NrTotClase) + "\n"
           + "Nr. de adrese utile in clasa: " + str(NrClaseUtile) + "\n"
           + "Grupa IP: " + str(gr)
           )

    T1.config(text=".".join(map(str, SubnetMask)))
    T2.config(text=".".join(map(str, Network)))
    T3.config(text=".".join(map(str, Broadcast)))
    T4.config(text=".".join(map(str, F_IP_Util)))
    T5.config(text=".".join(map(str, L_IP_Util)))
    T6.config(text=str(NrTotClase))
    T7.config(text=str(NrClaseUtile))
    T8.config(text=str(gr))
    T9.config(text=str(prefix))

def calculPrcuUtile(u):
    IPutil = u + 2
    NrDr = int(math.log(IPutil, 2))
    prefix = 32 - NrDr
    return prefix

def calculPrcuMasca(m1, m2, m3, m4):
    ma1 = m1
    ma2 = m2
    ma3 = m3
    ma4 = m4

    ma1b = bin(ma1)[2:].zfill(8)
    ma2b = bin(ma2)[2:].zfill(8)
    ma3b = bin(ma3)[2:].zfill(8)
    ma4b = bin(ma4)[2:].zfill(8)

    maBin = [ma1b, ma2b, ma3b, ma4b]
    prefix = maBin[0].count('1') + maBin[1].count('1') + maBin[2].count('1') + maBin[3].count('1')
    return prefix

def sel():
    selection = int(option.get())
    if selection == 1:
        E5.config(state=NORMAL)
        E6.config(state=DISABLED)
        E7.config(state=DISABLED)
        E8.config(state=DISABLED)
        E9.config(state=DISABLED)
        E10.config(state=DISABLED)

    elif selection == 2:
        E5.config(state=DISABLED)
        E6.config(state=NORMAL)
        E7.config(state=DISABLED)
        E8.config(state=DISABLED)
        E9.config(state=DISABLED)
        E10.config(state=DISABLED)
    elif selection == 3:
        E5.config(state=DISABLED)
        E6.config(state=DISABLED)
        E7.config(state=NORMAL)
        E8.config(state=NORMAL)
        E9.config(state=NORMAL)
        E10.config(state=NORMAL)
    return selection

def calcul():
    if sel() == 1:
        calculIPuri(int(E5.get()))
    elif sel() == 2:
        calculIPuri(calculPrcuUtile(int(E6.get())))
    elif sel() == 3:
        calculIPuri(calculPrcuMasca(int(E7.get()), int(E8.get()), int(E9.get()), int(E10.get())))


#Interfata
window = Tk()
window.geometry('1300x600')
option = IntVar()


def next():
    pass


E1 = Entry(window, width=10).grid(row=0, column=1, pady=5)
E2 = Entry(window, width=10).grid(row=0, column=2, pady=5)
E3 = Entry(window, width=10).grid(row=0, column=3, pady=5)
E4 = Entry(window, width=10).grid(row=0, column=4, pady=5)
#prefix
E5 = Entry(window, width=10)
E5.config(state=DISABLED)
E5.grid(row=1, column=1, pady=5)
#utile
E6 = Entry(window, width=10)
E6.config(state=DISABLED)
E6.grid(row=2, column=1, pady=5)
#masca
E7 = Entry(window, width=10)
E7.config(state=DISABLED)
E7.grid(row=3, column=1, pady=5)
E8 = Entry(window, width=10)
E8.config(state=DISABLED)
E8.grid(row=3, column=2, pady=5)
E9 = Entry(window, width=10)
E9.config(state=DISABLED)
E9.grid(row=3, column=3, pady=5)
E10 = Entry(window, width=10)
E10.config(state=DISABLED)
E10.grid(row=3, column=4, pady=5)
E11 = Entry(window, width=10).grid(row=0, column=6, pady=5)
E12 = Entry(window, width=10).grid(row=1, column=6, pady=5)

LAN1 = Entry(window, width=10).grid(row=0, column=8, padx=5, pady=5)
LAN2 = Entry(window, width=10).grid(row=0, column=9, padx=5, pady=5)
LAN3 = Entry(window, width=10).grid(row=0, column=10, padx=5, pady=5)
LAN4 = Entry(window, width=10).grid(row=0, column=11, padx=5, pady=5)
LAN5 = Entry(window, width=10).grid(row=0, column=12, padx=5, pady=5)

WAN1 = Entry(window, width=10).grid(row=1, column=8, padx=5, pady=5)
WAN2 = Entry(window, width=10).grid(row=1, column=9, padx=5, pady=5)
WAN3 = Entry(window, width=10).grid(row=1, column=10, padx=5, pady=5)
WAN4 = Entry(window, width=10).grid(row=1, column=11, padx=5, pady=5)
WAN5 = Entry(window, width=10).grid(row=1, column=12, padx=5, pady=5)

R1 = Radiobutton(window, text="Prefix", variable=option, value=1, command=sel).grid(row=1, column=0, pady=5, padx=10, sticky=W)
R2 = Radiobutton(window, text="IP urile", variable=option, value=2, command=sel).grid(row=2, column=0, pady=5, padx=10, sticky=W)
R3 = Radiobutton(window, text="Masca", variable=option, value=3, command=sel).grid(row=3, column=0, pady=5, padx=10, sticky=W)

T1 = Label(window, width=40,text="", anchor='w').grid(row=6, column=1, pady=5, padx=10, columnspan=5, sticky=W)
T2 = Label(window, width=40,text="", anchor='w').grid(row=7, column=1, pady=5, padx=10, columnspan=5, sticky=W)
T3 = Label(window, width=40,text="", anchor='w').grid(row=8, column=1, pady=5, padx=10, columnspan=5, sticky=W)
T4 = Label(window, width=40,text="", anchor='w').grid(row=9, column=1, pady=5, padx=10, columnspan=5, sticky=W)
T5 = Label(window, width=40,text="", anchor='w').grid(row=10, column=1, pady=5, padx=10, columnspan=5, sticky=W)
T6 = Label(window, width=40,text="", anchor='w').grid(row=11, column=1, pady=5, padx=10, columnspan=5, sticky=W)
T7 = Label(window, width=40,text="", anchor='w').grid(row=12, column=1, pady=5, padx=10, columnspan=5, sticky=W)
T8 = Label(window, width=40,text="", anchor='w').grid(row=13, column=1, pady=5, padx=10, columnspan=5, sticky=W)
T9 = Label(window, width=40,text="", anchor='w').grid(row=14, column=1, pady=5, padx=10, columnspan=5, sticky=W)

L1 = Label(window, width=10, text="IP", anchor='w').grid(row=0, column=0, pady=10, padx=5)
L2 = Label(window, width=20, text="Masca", anchor='e').grid(row=6, column=0, pady=10, padx=5)
L3 = Label(window, width=20, text="Network", anchor='e').grid(row=7, column=0, pady=10, padx=5)
L4 = Label(window, width=20, text="Broadcast", anchor='e').grid(row=8, column=0, pady=10, padx=5)
L5 = Label(window, width=20, text="Primul IP util", anchor='e').grid(row=9, column=0, pady=10, padx=5)
L6 = Label(window, width=20, text="Ultimul IP util", anchor='e').grid(row=10, column=0, pady=10, padx=5)
L7 = Label(window, width=20, text="Total IP-uri", anchor='e').grid(row=11, column=0, pady=10, padx=5)
L8 = Label(window, width=20, text="Total IP-uri utile", anchor='e').grid(row=12, column=0, pady=10, padx=5)
L9 = Label(window, width=20, text="Grupa", anchor='e').grid(row=13, column=0, pady=10, padx=5)
L10 = Label(window, width=20, text="Prefix", anchor='e').grid(row=14, column=0, pady=10, padx=5)
L11 = Label(window, width=20, text="Nr. LAN-uri", anchor='e').grid(row=0, column=5, pady=10, padx=5)
L12 = Label(window, width=20, text="Nr. WAN-uri", anchor='e').grid(row=1, column=5, pady=10, padx=5)
L13 = Label(window, width=20, text="LAN H", anchor='center').grid(row=0, column=7, pady=10, padx=5)
L14 = Label(window, width=20, text="WAN H", anchor='center').grid(row=1, column=7, pady=10, padx=5)

L15 = Label(window, width=20, text="LAN1", anchor='center').grid(row=2, column=8, pady=10, padx=5)
L16 = Label(window, width=20, text="LAN2", anchor='center').grid(row=2, column=9, pady=10, padx=5)
L17 = Label(window, width=20, text="LAN3", anchor='center').grid(row=2, column=10, pady=10, padx=5)
L18 = Label(window, width=20, text="LAN4", anchor='center').grid(row=2, column=11, pady=10, padx=5)
L19 = Label(window, width=20, text="LAN5", anchor='center').grid(row=2, column=12, pady=10, padx=5)

L20 = Label(window, width=20, text="WAN1", anchor='center').grid(row=8, column=8, pady=10, padx=5)
L21 = Label(window, width=20, text="WAN2", anchor='center').grid(row=8, column=9, pady=10, padx=5)
L22 = Label(window, width=20, text="WAN3", anchor='center').grid(row=8, column=10, pady=10, padx=5)
L23 = Label(window, width=20, text="WAN4", anchor='center').grid(row=8, column=11, pady=10, padx=5)
L24 = Label(window, width=20, text="WAN5", anchor='center').grid(row=8, column=12, pady=10, padx=5)

L25 = Label(window, width=20, text="Adresa LAN", anchor='center').grid(row=3, column=7, pady=10, padx=5)
L26 = Label(window, width=20, text="Adresa NW", anchor='center').grid(row=4, column=7, pady=10, padx=5)
L27 = Label(window, width=20, text="Adresa BC", anchor='center').grid(row=5, column=7, pady=10, padx=5)
L28 = Label(window, width=20, text="1 IP util", anchor='center').grid(row=6, column=7, pady=10, padx=5)
L29 = Label(window, width=20, text="U IP util", anchor='center').grid(row=7, column=7, pady=10, padx=5)

L30 = Label(window, width=20, text="Adresa LAN", anchor='center').grid(row=9, column=7, pady=10, padx=5)
L31 = Label(window, width=20, text="Adresa NW", anchor='center').grid(row=10, column=7, pady=10, padx=5)
L32 = Label(window, width=20, text="Adresa BC", anchor='center').grid(row=11, column=7, pady=10, padx=5)
L33 = Label(window, width=20, text="1 IP util", anchor='center').grid(row=12, column=7, pady=10, padx=5)
L34 = Label(window, width=20, text="U IP util", anchor='center').grid(row=13, column=7, pady=10, padx=5)

B1 = Button(window, text="Calculate", command=calcul).grid(row=4, column=0, pady=5, padx=10)
B2 = Button(window, text="Submit", command=next).grid(row=2, column=5, pady=5, padx=10)

window.mainloop()
