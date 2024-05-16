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

window = Tk()
window.geometry('500x600')
option = IntVar()
L1 = Label(window, width=10, text="IP", anchor='w')
E1 = Entry(window, width=10)
E2 = Entry(window, width=10)
E3 = Entry(window, width=10)
E4 = Entry(window, width=10)
R1 = Radiobutton(window, text="Prefix", variable=option, value=1, command=sel)
R2 = Radiobutton(window, text="IP urile", variable=option, value=2, command=sel)
R3 = Radiobutton(window, text="Masca", variable=option, value=3, command=sel)

T1 = Label(window, width=40,text="", anchor='w')
T2 = Label(window, width=40,text="", anchor='w')
T3 = Label(window, width=40,text="", anchor='w')
T4 = Label(window, width=40,text="", anchor='w')
T5 = Label(window, width=40,text="", anchor='w')
T6 = Label(window, width=40,text="", anchor='w')
T7 = Label(window, width=40,text="", anchor='w')
T8 = Label(window, width=40,text="", anchor='w')
T9 = Label(window, width=40,text="", anchor='w')

L2 = Label(window, width=20, text="Masca", anchor='e')
L3 = Label(window, width=20, text="Network", anchor='e')
L4 = Label(window, width=20, text="Broadcast", anchor='e')
L5 = Label(window, width=20, text="Primul IP util", anchor='e')
L6 = Label(window, width=20, text="Ultimul IP util", anchor='e')
L7 = Label(window, width=20, text="Total IP-uri", anchor='e')
L8 = Label(window, width=20, text="Total IP-uri utile", anchor='e')
L9 = Label(window, width=20, text="Grupa", anchor='e')
L10 = Label(window, width=20, text="Prefix", anchor='e')


#prefix
E5 = Entry(window, width=10)
#utile
E6 = Entry(window, width=10)
#masca
E7 = Entry(window, width=10)
E8 = Entry(window, width=10)
E9 = Entry(window, width=10)
E10 = Entry(window, width=10)

B1 = Button(window, text="Calculate", command=calcul)

E5.config(state=DISABLED)
E6.config(state=DISABLED)
E7.config(state=DISABLED)
E8.config(state=DISABLED)
E9.config(state=DISABLED)
E10.config(state=DISABLED)

L1.grid(row=0, column=0, pady=10, padx=5)
E1.grid(row=0, column=1, pady=5)
E2.grid(row=0, column=2, pady=5)
E3.grid(row=0, column=3, pady=5)
E4.grid(row=0, column=4, pady=5)
R1.grid(row=1, column=0, pady=5, padx=10, sticky=W)
R2.grid(row=2, column=0, pady=5, padx=10, sticky=W)
R3.grid(row=3, column=0, pady=5, padx=10, sticky=W)
E5.grid(row=1, column=1, pady=5)
E6.grid(row=2, column=1, pady=5)
E7.grid(row=3, column=1, pady=5)
E8.grid(row=3, column=2, pady=5)
E9.grid(row=3, column=3, pady=5)
E10.grid(row=3, column=4, pady=5)
B1.grid(row=4, column=0, pady=5, padx=10)

T1.grid(row=6, column=1, pady=5, padx=10, columnspan=5, sticky=W)
L2.grid(row=6, column=0, pady=10, padx=5)

T2.grid(row=7, column=1, pady=5, padx=10, columnspan=5, sticky=W)
L3.grid(row=7, column=0, pady=10, padx=5)

T3.grid(row=8, column=1, pady=5, padx=10, columnspan=5, sticky=W)
L4.grid(row=8, column=0, pady=10, padx=5)

T4.grid(row=9, column=1, pady=5, padx=10, columnspan=5, sticky=W)
L5.grid(row=9, column=0, pady=10, padx=5)

T5.grid(row=10, column=1, pady=5, padx=10, columnspan=5, sticky=W)
L6.grid(row=10, column=0, pady=10, padx=5)

T6.grid(row=11, column=1, pady=5, padx=10, columnspan=5, sticky=W)
L7.grid(row=11, column=0, pady=10, padx=5)

T7.grid(row=12, column=1, pady=5, padx=10, columnspan=5, sticky=W)
L8.grid(row=12, column=0, pady=10, padx=5)

T8.grid(row=13, column=1, pady=5, padx=10, columnspan=5, sticky=W)
L9.grid(row=13, column=0, pady=10, padx=5)

T9.grid(row=14, column=1, pady=5, padx=10, columnspan=5, sticky=W)
L10.grid(row=14, column=0, pady=10, padx=5)

window.mainloop()
