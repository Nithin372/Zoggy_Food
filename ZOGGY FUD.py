from tkinter import *
from tkinter import ttk, messagebox
import csv

pro = Tk()
pro.state("zoomed")
pro.title("RND")
pro.rowconfigure(0, weight=1)
pro.columnconfigure(0, weight=1)
frame1 = Frame(pro)
frame2 = Frame(pro)
frame3 = Frame(pro)
frame4 = Frame(pro)
frame5 = Frame(pro)
frame6 = Frame(pro)
frame7 = Frame(pro)
frame8 = Frame(pro)
frame9 = Frame(pro)
frame10 = Frame(pro)
frame11 = Frame(pro)
frame12 = Frame(pro)
frame13 = Frame(pro)
frame14 = Frame(pro)
frame15 = Frame(pro)
frame16 = Frame(pro)
frame17 = Frame(pro)
frame18 = Frame(pro)
for frame in (
        frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12, frame13,
        frame14, frame15, frame16, frame17, frame18):
    frame.grid(row=0, column=0, sticky='nsew')

frame6.configure(bg='aqua')

uid=''
#  To Switch to a Particular Frame
def show_frame(frame_faces):
    frame_faces.tkraise()


# Opening Frame User Interface ( Frame - 1 )

frame1_title = Label(frame1, text='** Choose The User **', fg='green',
                     font=("Baskerville Old Face", 30, "bold")).place(x=510, y=75)
frame1_btn1 = Button(frame1, text=" CUSTOMER ", font=("Algerian", 30, "bold"), bg='gold',
                     command=lambda: show_frame(frame2)).place(
    x=590, y=200)
frame1_btn2 = Button(frame1, text=" RESTAURANT ", font=("Algerian", 30, "bold"), bg='gold',
                     command=lambda: show_frame(frame3)).place(x=560, y=400)
frame1_btn3 = Button(frame1, text=" EXIT ", font=("Algerian", 30, "bold"), bg='gold', command=exit).place(x=655, y=600)

show_frame(frame1)

#  Customer Sign_in ( Frame - 2)

custid = ''
holt = []
restid = ''

def ex_sinfo(a, b):
    global custid
    f = open('Customers.csv', 'r')
    reading = csv.reader(f)
    for word in reading:
        if a == word[0] and b == word[2]:
            custid = a
            frame2_stu_id.delete(0, END)
            frame2_stu_pass.delete(0, END)
            show_frame(frame6)
            break
    else:
        messagebox.showerror('Warning', 'In-Correct Credentials')
        frame2_stu_id.delete(0, END)
        frame2_stu_pass.delete(0, END)

get_aspirant_id = ''
# Creating Functionality Keys For User Interface:
def get_sinfo():
    global get_aspirant_id
    set_info = f"{frame2_p.get()}"
    get_aspirant_id = set_info
    set_password = f"{frame2_i.get()}"
    ex_sinfo(set_info, set_password)


frame2_title = Label(frame2, text=" Welcome ", fg="white", bg="green", font=("Algerian", 30),
                     width=40).place(x=370, y=50)

frame2_Id = Label(frame2, text=" Enter Your ID ", fg="black", bg="pink", relief="solid",
                  font=("Arial", 25, "bold")).place(x=500, y=150)
frame2_password = Label(frame2, text=" Enter Password ", fg="black", bg="pink", relief="solid",
                        font=("Arial", 25, "bold")).place(x=500, y=300)
frame2_signup = Label(frame2, text=" Don't have an Account ? Register Now", fg="black",
                      font=("calibri", 12)).place(x=540, y=550)
frame2_signup_btn = Button(frame2, text="Sign up", fg="red", bg="grey", font=("Baskerville Old Face", 14, "bold"),
                           width=15,
                           command=lambda: show_frame(frame4)).place(x=825, y=540)
# The Variables we require to Get Student details(initialization):

frame2_p = StringVar()
frame2_i = StringVar()
#  Details Required From the User:
frame2_stu_id = Entry(frame2, textvariable=frame2_p, bg="white", font=("Arial", 25), width=12)
frame2_stu_id.pack()
frame2_stu_id.place(x=850, y=150)
frame2_stu_pass = Entry(frame2, show='*', textvariable=frame2_i, bg="white", font=("Arial", 25), width=12)
frame2_stu_pass.pack()
frame2_stu_pass.place(x=850, y=300)
frame2_browse = Button(frame2, text=" Login ", fg="white", bg="red", font=("Baskerville Old Face", 14, "bold"),
                       width=15,
                       command=get_sinfo).place(x=650, y=450)
frame2_ext_but = Button(frame2, text=" Exit ", fg="white", bg="black", font=("caliber", 14, "bold"), width=15,
                        command=exit).place(x=760, y=650)
frame2_back2 = Button(frame2, text="Go Back ", fg="white", bg="black", font=("caliber", 14, "bold"), width=15,
                      command=lambda: show_frame(frame1)).place(x=560, y=650)

#  Company Login Interface ( Frame -2 )

frame3_company_id = ''


def clicked():
    Label(frame5, text="** Thank You **", font=("Algerian", 10)).place(x=200, y=700)


frame3_hotel_name = ''


def ex_adinfo(q1, q2):
    g = open('Restaurant.csv', 'r')
    reading = csv.reader(g)
    global frame3_hotel_name
    for word in reading:
        if q1 == word[0] and q2 == word[3]:
            frame3_hotel_name = word[1]
            frame3_stu_id.delete(0, END)
            frame3_stu_pass.delete(0, END)
            show_frame(frame7)
            break
    else:
        messagebox.showerror('Warning', 'In-Correct Credentials')
        frame3_stu_id.delete(0, END)
        frame3_stu_pass.delete(0, END)


# Creating Functionality Keys For User Interface:
def get_adinfo():
    global frame3_company_id
    set_info = f"{frame3_p.get()}"
    set_password = f"{frame3_i.get()}"
    frame3_company_id = set_info
    ex_adinfo(set_info, set_password)


frame3_title = Label(frame3, text=" Welcome", fg="white", bg="green", font=("Algerian", 20),
                     width=35).place(x=370, y=50)
frame3_Id = Label(frame3, text=" Enter Your ID ", fg="black", bg="pink", relief="solid",
                  font=("Arial", 25, "bold")).place(x=450, y=200)
frame3_password = Label(frame3, text=" Enter Password ", fg="black", bg="pink", relief="solid",
                        font=("Arial", 25, "bold")).place(x=450, y=300)
frame3_signup = Label(frame3, text=" Don't have an Account ? Register Now", fg="black",
                      font=("calibri", 12)).place(x=540, y=570)
frame3_signup_btn = Button(frame3, text="Sign up", fg="red", bg="grey", font=("Baskerville Old Face", 12, "bold"),
                           width=15,
                           command=lambda: show_frame(frame5)).place(x=825, y=570)
# The Variables we require to Get Student details(initialization):
frame3_p = StringVar()
frame3_i = StringVar()
#  Details Required From the User:
frame3_stu_id = Entry(frame3, textvariable=frame3_p, bg="white", font=("Arial", 25), width=15)
frame3_stu_id.pack()
frame3_stu_id.place(x=850, y=200)
frame3_stu_pass = Entry(frame3, show='*', textvariable=frame3_i, bg="white", font=("Arial", 25), width=15)
frame3_stu_pass.pack()
frame3_stu_pass.place(x=850, y=300)
frame3_browse = Button(frame3, text=" Login ", fg="white", bg="sky blue", font=("Baskerville Old Face", 15, "bold"),
                       width=10,
                       command=get_adinfo).place(x=680, y=500)
frame3_ext_but = Button(frame3, text=" Exit ", fg="white", bg="green", font=("caliber", 10, "bold"), width=15,
                        command=exit).place(x=800, y=650)
frame3_back = Button(frame3, text="Go Back ", fg="white", bg="green", font=("caliber", 10, "bold"), width=15,
                     command=lambda: show_frame(frame1)).place(x=540, y=650)


# For Customer Sign_Up Frame ( Frame - 4):


def register_info():
    dict_data = []
    dz = []
    dz = dz + [frame4_x1.get()]
    dz = dz + [frame4_y1.get()]
    dz = dz + [frame4_a1.get()]
    dict_data = dict_data + [dz]
    print(dict_data)
    f = open("Customers.csv", "a", newline="")
    wr = csv.writer(f)
    for word in dict_data:
        wr.writerow(word)
        messagebox.showinfo("Updated Result", " You have Registered Successfully ")
    frame4_e1.delete(0, END)
    frame4_e2.delete(0, END)
    frame4_e3.delete(0, END)


frame4_title = Label(frame4, text=" Welcome ", fg="yellow", bg="black",
                     font=("Algerian", 20),
                     width=50).place(x=350, y=50)
l1 = Label(frame4, text=" Enter Your Customer ID : ", fg="blue", bg="orange", relief="solid",
           font=("Arial", 18, "bold")).place(x=450, y=150)
frame4_x1 = StringVar()
frame4_e1 = Entry(frame4, textvariable=frame4_x1, bg="white", font=("Arial", 15, "bold"), width=18)
frame4_e1.pack()
frame4_e1.place(x=850, y=150)
l2 = Label(frame4, text=" Enter Your Name ", fg="blue", bg="orange", relief="solid",
           font=("Arial", 18, "bold")).place(x=450, y=250)
frame4_y1 = StringVar()
frame4_e2 = Entry(frame4, textvariable=frame4_y1, bg="white", font=("Arial", 15, "bold"), width=18)
frame4_e2.pack()
frame4_e2.place(x=850, y=250)
l3 = Label(frame4, text=" Create Your Password ", fg="blue", bg="orange", relief="solid",
           font=("Arial", 18, "bold")).place(x=450, y=350)
frame4_a1 = StringVar()
frame4_e3 = Entry(frame4, show='*', textvariable=frame4_a1, bg="white", font=("Arial", 15, "bold"), width=18)
frame4_e3.pack()
frame4_e3.place(x=850, y=350)

frame4_browse = Button(frame4, text=" Register ", fg="white", bg="red", font=("Baskerville Old Face", 14, "bold"),
                       width=15,
                       command=register_info).place(x=650, y=580)
frame4_ext_but = Button(frame4, text=" Exit ", fg="pink", bg="grey", font=("caliber", 14, "bold"), width=15,
                        command=exit).place(x=760, y=700)
frame4_back = Button(frame4, text="Go Back ", fg="pink", bg="grey", font=("caliber", 14, "bold"), width=15,
                     command=lambda: show_frame(frame2)).place(x=560, y=700)


# Restaurant Sign Up Form ( Frame -5 ):


def up_info():
    dict_data = []
    dz = []
    dz = dz + [x1.get()]
    dz = dz + [y1.get()]
    dz = dz + [c1.get()]
    dz = dz + [b1.get()]
    dz = dz + ['']
    dz = dz + ['']
    dict_data = dict_data + [dz]
    f = open("Restaurant.csv", "a", newline="")
    wr = csv.writer(f)
    for word in dict_data:
        wr.writerow(word)
        messagebox.showinfo("Updated Result", " You have Registered Successfully ")
    e1.delete(0, END)
    e2.delete(0, END)
    e4.delete(0, END)
    c1.set('')


frame5_title = Label(frame5, text=' Provide the Details Below ', font=("Algerian", 25, "bold"), bg='red',
                     fg='gold').place(x=500, y=10)
l1 = Label(frame5, text=" Enter Your ID : ", font=("Arial", 20, "bold")).place(x=400, y=100)
x1 = StringVar()
e1 = Entry(frame5, textvariable=x1, bg="white", font=("Arial", 20, "bold"), width=18)
e1.pack()
e1.place(x=850, y=100)
l2 = Label(frame5, text=" Enter Your Restaurant  Name :", font=("Arial", 20, "bold")).place(x=400, y=200)
y1 = StringVar()
e2 = Entry(frame5, textvariable=y1, bg="white", font=("Arial", 20, "bold"), width=18)
e2.pack()
e2.place(x=850, y=200)
l5 = Label(frame5, text="Enter Restaurant Location :", font=("Arial", 20, "bold")).place(x=400, y=300)
c1 = StringVar()
location_list = ['Anantapur', 'Kurnool', 'Vijayawada', 'Hindupur', 'Chitoor']
company_info = ttk.Combobox(frame5, values=location_list, textvariable=c1, font=("Arial", 18, "bold")).place(x=850,
                                                                                                             y=300)
c1.set("Select Location")
l4 = Label(frame5, text=" Set Password :", font=("Arial", 20, "bold")).place(x=400, y=400)
b1 = StringVar()
e4 = Entry(frame5, show='*', textvariable=b1, bg="white", font=("Arial", 20, "bold"), width=18)
e4.pack()
e4.place(x=850, y=400)

frame5_update = Button(frame5, text=" Register ", fg="white", bg="sky blue",
                       font=("Baskerville Old Face", 14, "bold"),
                       width=15,
                       command=up_info).place(x=640, y=550)
frame5_back10 = Button(frame5, text=" Go Back ", fg="blue", bg="white", font=("caliber", 14, "bold"), width=15,
                       command=lambda: show_frame(frame3)).place(x=630, y=650)

# For Customer Page ( Frame - 6) :
locs = ['ANANTAPUR', 'KURNOOL', 'NELLORE']
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
lbd = []
datal = []
plor = []
ordt = []
def add_info():
    gh = 0
    n = []
    for lk in ordt:
        pd = lk.split('₹')
        gh = gh+int(pd[1])
    messagebox.showinfo('Order','Order costs ₹'+str(gh)+' has been placed successfully')
    df = ordt[0].split('-')[0]
    for lk in ordt[1:]:
        df = df+'_'+lk.split('-')[0]
    f = open('Restaurant.csv', 'r')
    reader = csv.reader(f)
    found = 0
    n = []
    for i in reader:
        if restid == i[1]:
            i[7] = i[7] + '_' + df
            found = 1
            messagebox.showinfo("Items", "Placed Order")
        n.append(i)
    if found == 0:
        messagebox.showinfo('Restaurants', " Restaurant  Not Found")
    else:
        g = open("Restaurant.csv", "w", newline='')
        csvw = csv.writer(g)
        csvw.writerows(n)
        g.close()


olt1 = Label(frame10, text='Items in your Cart, Confirm Order', fg="blue", font=("calibri", 18, "bold"))
obt1 = Button(frame10, text='PLACE ORDER', fg="green", bg="wheat", font=("caliber", 16, "bold"), width=15, command=add_info)
obt3 = Button(frame10, text='Back', fg='red', bg='orange', font=('arial', 16, 'bold'), width=8,
              command=lambda: show_frame(frame8))


def plord():
    show_frame(frame10)
    st = ''
    for j in ordt:
        st = st + j + '\n'
    olt2 = Label(frame10, text=st, fg="red", font=("calibri", 18, "bold"))
    olt1.place(x=200, y=150)
    obt1.place(x=450, y=520)
    olt2.place(x=450, y=220)
    obt3.place(x=500, y=600)


def addt():
    messagebox.showinfo('Cart', 'Item Added to Cart Successfully')
    vl = v4.get()
    ordt.append(vl)


def menu(idx):
    global plor, restid
    restid =  idx
    for i in datal:
        if idx == i[0]:
            plor.clear()
            items = i[3].split('_')
            prices = i[4].split('_')
            lbl1 = Label(frame8, text='Select the Items into Cart :', fg="green", bg="violet",
                         font=("caliber", 18, "bold"))
            btn1 = Button(frame8, text='View Cart->', fg="green", bg="wheat", font=("caliber", 16, "bold"), width=10,
                          command=plord)
            btn2 = Button(frame8, text='<-BACK', fg="red", bg="wheat", font=("caliber", 16, "bold"),
                          command=lambda: show_frame(frame6))
            btn3 = Button(frame8, text='Add to Cart', fg="red", bg="wheat", font=("caliber", 16, "bold"), command=addt)

            show_frame(frame8)
            for u in range(len(items)):
                plor.append(items[u] + ' - ₹' + prices[u])
            lbl1.place(x=300, y=120)
            cb2['values'] = plor
            cb2.place(x=500, y=220)
            btn3.place(x=500, y=300)
            btn1.place(x=500, y=400)
            btn2.place(x=500, y=500)


def res():
    if lbd != [] or datal != []:
        for i in lbd:
            i.place_forget()
        lbd.clear()
        datal.clear()
    a = ''
    a = v1.get()
    f = open('Restaurant.csv', 'r')
    data = csv.reader(f)
    for i in data:
        if a == i[2]:
            datal.append(i[1:])
    for i in range(len(datal)):
        lab = Button(frame6, text=datal[i][0] + '\n' + a, bg='tan', font=('arial', 11, 'bold'), width=27,
                     command=lambda idx=datal[i][0]: menu(idx))
        holt.append(datal[i][0])
        lbd.append(lab)
    p, q = 650, 200
    for i in range(len(datal)):
        lbd[i].place(x=p, y=q)
        q = q + 100


def chp():
    show_frame(frame9)
    lb4.place(x=150, y=150)
    lb5.place(x=150, y=220)
    en1.place(x=450, y=150)
    en2.place(x=450, y=220)
    bt3.place(x=350, y=300)
    bt4.place(x=350, y=400)


def pas():
    a = v2.get()
    b = v3.get()
    rowlt = []
    cnt = 0
    with open('Customers.csv', 'r') as f:
        dt = csv.reader(f)
        for i in dt:
            if i[0] == custid and i[2] == a:
                cnt = 1
                i[2] = b
                messagebox.showinfo('Credentials','Password Changed Successfully')
                show_frame(frame2)
            rowlt.append(i)
        else :
            if cnt==0:
                messagebox.showerror('ERROR','Incorrect Password Entered')
    g = open("Customers.csv", "w", newline='')
    csvw = csv.writer(g)
    csvw.writerows(rowlt)


# To change password for Customer
bt1 = Button(frame6, text="Change Password", fg='red', bg='wheat', font=("Baskerville Old Face", 14, "bold"),
             command=chp)
bt2 = Button(frame6, text='GO', fg='brown', bg='wheat', font=("Baskerville Old Face", 12, "bold"), command=res)
bt3 = Button(frame9, text='SET', fg='brown', bg='wheat', font=("Baskerville Old Face", 15, "bold"), command=pas)
bt4 = Button(frame9, text='Back', fg='red', bg='wheat', font=("Baskerville Old Face", 15, "bold"),
             command=lambda: show_frame(frame6))
bt5 = Button(frame6, text='Log Out', fg='red', bg='wheat', font=("Baskerville Old Face", 12, "bold"),
             command=lambda: show_frame(frame2))

cb1 = ttk.Combobox(frame6, width=15, textvariable=v1, font=('Arial', 15))
cb2 = ttk.Combobox(frame8, width=24, textvariable=v4, font=('Arial', 15))
cb1['values'] = locs

lb1 = Label(frame6, text='Welcome to ZOGGY', font=('Cansolas', 32), fg='red', bg='aqua')
lb2 = Label(frame6, text='Hey User! Hungry? Get the food delivered in no time...', font=('Arial', 15), bg='aqua')
lb3 = Label(frame6, text='Enter the location : ', fg='blue', bg='aqua', font=('calibri', 25, 'bold'))
lb4 = Label(frame9, text='Enter Old Password :', fg='blue', bg='aqua', font=('calibri', 22, 'bold'))
lb5 = Label(frame9, text='Enter New Password:', fg='blue', bg='aqua', font=('calibri', 22, 'bold'))

en1 = Entry(frame9, textvariable=v2, width=20, font=('calibri', 15), show='*')
en2 = Entry(frame9, textvariable=v3, width=20, font=('calibri', 15), show='*')

bt1.place(x=1350, y=20)
lb1.place(x=580, y=20)
lb2.place(x=550, y=75)
lb3.place(x=450, y=110)
cb1.place(x=750, y=125)
bt2.place(x=950, y=120)
bt5.place(x=1400, y=70)

a1 = StringVar()
c1 = StringVar()


def autoc(e):
    v = e.widget.get()
    if v == '':
        cb1['values'] = locs
    else:
        d = []
        for i in locs:
            if v.lower() in i.lower():
                d.append(i)
        cb1['values'] = d


cb1.bind('<KeyRelease>', autoc)

#  Restaurants after Login ( Frame - 7)
hotel_item = ''


def get_hotel_info():
    found = 0
    l = []
    global hotel_item, frame3_hotel_name
    x = a1.get()
    y = c1.get()
    hotel_item = x
    f = open('Restaurant.csv', 'r')
    reader = csv.reader(f)
    for i in reader:
        if frame3_hotel_name == i[1]:
            i[4] = i[4] + '_' + x
            i[5] = i[5] + '_' + y
            a1.set('')
            c1.set('')
            found = 1
            messagebox.showinfo("Items", "Items Added Successfully")
        l.append(i)
    if found == 0:
        messagebox.showinfo('Restaurants', " Restaurant  Not Found")
    else:
        g = open("Restaurant.csv", "w", newline='')
        csvw = csv.writer(g)
        csvw.writerows(l)
        g.close()


def frame7_change_pass(w, r):
    g = open("Restaurant.csv", 'r')
    reading = csv.reader(g)
    found = 0
    global frame3_hotel_name
    m = []
    for info in reading:
        if info[1] == frame3_hotel_name and info[3] == w:
            print(info[3])
            info[3] = r
            print(info[3])
            found = 1
        m.append(info)
    g.close()
    if found == 0:
        messagebox.showwarning('Password Change', 'Check your old and New Password')
    else:
        f = open("officer.csv", "w", newline='')
        messagebox.showinfo('Password Change', 'Your Password Changed Successfully')
        csvw = csv.writer(f)
        csvw.writerows(m)
        f.close()
    frame7_old_pass1.delete(0, END)
    frame7_new_pass1.delete(0, END)


def frame7_m_pass():
    frame7_set_old_pass = frame7_o_pass.get()
    frame7_set_pass = frame7_c_pass.get()
    frame7_change_pass(frame7_set_old_pass, frame7_set_pass)


frame7_item_label = Label(frame7, text=" Enter Food Item ", font=('Cansolas', 20), fg='black', bg='green')
frame7_item_entry = Entry(frame7, textvariable=a1, bg="skyblue", font=("Arial", 20, "bold"), width=28)
frame7_item_price = Label(frame7, text=" Enter Food Item Price ", font=('Cansolas', 20), fg='black', bg='green')
frame7_price_entry = Entry(frame7, textvariable=c1, bg="skyblue", font=("Arial", 20, "bold"), width=18)
frame7_add_btn = Button(frame7, text='Add', bg="black", fg='skyblue', font=("Arial", 20, "bold"), width=7,
                        command=get_hotel_info)
frame7_label_v_order = Label(frame7, text='The Ordered Customer ID ', fg="white", bg="black",
                             font=("Baskerville Old Face", 30, "bold"))
lab = Button(frame7)
frame7_old_pass = Label(frame7, text="Enter Old Password", fg="black", bg="pink", relief="solid",
                        font=("Arial", 20, "bold"))
frame7_new_pass = Label(frame7, text="Enter New Password", fg="black", bg="pink", relief="solid",
                        font=("Arial", 20, "bold"))

frame7_o_pass = StringVar()
frame7_c_pass = StringVar()
frame7_old_pass1 = Entry(frame7, show="*", textvariable=frame7_o_pass, bg="white", font=("Arial", 15), width=10)
frame7_new_pass1 = Entry(frame7, show="*", textvariable=frame7_c_pass, bg="white", font=("Arial", 15), width=10)
frame7_change = Button(frame7, text="Change", fg="white", bg="sky blue", font=("Baskerville Old Face", 10, "bold"),
                       width=15, command=frame7_m_pass)


def add_food_clear():
    frame7_item_label.place_forget()
    frame7_item_entry.place_forget()
    frame7_item_price.place_forget()
    frame7_price_entry.place_forget()
    frame7_add_btn.place_forget()


def password_clear():
    frame7_old_pass.place_forget()
    frame7_new_pass.place_forget()
    frame7_old_pass1.place_forget()
    frame7_new_pass1.place_forget()
    frame7_change.place_forget()


def add_food_item():
    frame7_label_v_order.place_forget()
    lab.place_forget()
    password_clear()
    a = frame3_hotel_name
    frame7_item_label.place(x=400, y=380)
    frame7_item_price.place(x=400, y=480)
    frame7_item_entry.place(x=900, y=380)
    frame7_price_entry.place(x=900, y=480)
    frame7_add_btn.place(x=650, y=600)


def restaurant_password_change():
    add_food_clear()
    frame7_label_v_order.place_forget()
    lab.place_forget()
    frame7_old_pass.place(x=420, y=400)
    frame7_new_pass.place(x=420, y=600)
    frame7_old_pass1.place(x=900, y=400)
    frame7_new_pass1.place(x=900, y=600)
    frame7_change.place(x=600, y=700)
    frame7_m_pass()


def view_food_orders():
    add_food_clear()
    password_clear()
    datal = []
    if lbd != [] or datal != []:
        for i in lbd:
            i.place_forget()
        lbd.clear()
        datal.clear()
    a = ''
    a = v1.get()
    frame3_hotel_name
    f = open('Restaurant.csv', 'r')
    data = csv.reader(f)
    for i in data:
        if frame3_hotel_name == i[1]:
            frame7_label_v_order.place(x=285, y=350)
            datal = i[6].split('_')
    for i in range(len(datal)):
        lab = Button(frame7, text=datal[i] + '\n' + a, bg='tan', font=('arial', 10, 'bold'), width=10,
                     command=lambda idx=datal[i][0]: menu(idx))
        lbd.append(lab)
    p, q = 350, 450
    for i in range(len(datal)):
        lbd[i].place(x=p, y=q)
        p = p + 150


frame7_label1 = Label(frame7, text=" Welcome ", font=('Cansolas', 30), fg='black', bg='green').place(x=650, y=30)
frame7_btn1 = Button(frame7, text=" Add Food Items ", fg='brown', bg='wheat',
                     font=("Baskerville Old Face", 16, "bold"), command=add_food_item).place(x=200, y=200)
frame7_btn2 = Button(frame7, text=" View Orders ", fg='brown', bg='wheat',
                     font=("Baskerville Old Face", 16, "bold"), command=view_food_orders).place(x=650, y=200)
frame7_btn3 = Button(frame7, text=" Change Password ", fg='brown', bg='wheat',
                     font=("Baskerville Old Face", 16, "bold"), command=restaurant_password_change).place(x=1100, y=200)
frame7_btn4 = Button(frame7, text=" Log Out ", fg='black', bg='white', font=("Baskerville Old Face", 8, "bold"),
                     command=lambda: show_frame(frame3)).place(x=1300, y=50)

pro.mainloop()
