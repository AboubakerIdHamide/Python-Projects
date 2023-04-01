from ast import Pass
from tkinter import *
from tkinter.font import Font


app=Tk()
app.geometry("1000x600")
app.title("X_O")
app.minsize(300,600)
app.iconbitmap("D:\wallpaper\XO.ico")
turn=0
def replay_all():
    # ========================================= inputs ==========================================
    name1= Entry(app, bg="black", fg="#ffcc00", justify="center")
    name1.place(x=820, y=85, width=250, height=40)
    name2= Entry(app, bg="black", fg="#ffcc00", justify="center")
    name2.place(x=820, y=140, width=250, height=40)
    # =========================================functions=========================================
    #                      ================== VARIABLES ================
    b1_txt= StringVar()
    b2_txt= StringVar()
    b3_txt= StringVar()
    b4_txt= StringVar()
    b5_txt= StringVar()
    b6_txt= StringVar()
    b7_txt= StringVar()
    b8_txt= StringVar()
    b9_txt= StringVar()


    #                       ================== button functions ================
    def start_f():
        if name1.get() != "" and name2.get() != "":
            b1.config(text=" ", font= Font( size= 80, weight= "bold"), command=b1_f, bg="#ffcc00", state="normal")
            b2.config(text=" ", font= Font( size= 80, weight= "bold"), command=b2_f, bg="#ffcc00", state="normal")
            b3.config(text=" ", font= Font( size= 80, weight= "bold"), command=b3_f, bg="#ffcc00", state="normal")
            b4.config(text=" ", font= Font( size= 80, weight= "bold"), command=b4_f, bg="#ffcc00", state="normal")
            b5.config(text=" ", font= Font( size= 80, weight= "bold"), command=b5_f, bg="#ffcc00", state="normal")
            b6.config(text=" ", font= Font( size= 80, weight= "bold"), command=b6_f, bg="#ffcc00", state="normal")
            b7.config(text=" ", font= Font( size= 80, weight= "bold"), command=b7_f, bg="#ffcc00", state="normal")
            b8.config(text=" ", font= Font( size= 80, weight= "bold"), command=b8_f, bg="#ffcc00", state="normal")
            b9.config(text=" ", font= Font( size= 80, weight= "bold"), command=b9_f, bg="#ffcc00", state="normal")
            if turn%2==0:
                message.set(f"IT'S {name1.get().upper()}'S TURN")
            else:
                message.set(f"IT'S {name2.get().upper()}'S TURN")
            start.config(state="disabled")
            global var_n2
            global var_n1
            var_n1=name1.get()
            var_n2=name2.get()
            name1.delete(0,50)
            name2.delete(0,50)
    def b1_f():
        global turn
        turn+=1
        
        if turn%2==0:
            b1_txt.set("O")
            b1.config(textvariable=b1_txt, bg="black", fg="white",state="disabled")
            message.set(f"IT'S {var_n1.upper()}'S TURN")
            winnner()
        else:
            b1_txt.set("X")
            b1.config(textvariable=b1_txt, bg="black",fg="white",state="disabled")
            message.set(f"IT'S {var_n2.upper()}'S TURN")
            winnner()
        

    def b2_f():
        global turn
        turn+=1
        if turn%2==0:
            b2_txt.set("O")
            b2.config(textvariable=b2_txt, bg="black", fg="white",state="disabled")
            message.set(f"IT'S {var_n1.upper()}'S TURN")
            winnner()
        else:
            b2_txt.set("X")
            b2.config(textvariable=b2_txt, bg="black",fg="white",state="disabled")
            message.set(f"IT'S {var_n2.upper()}'S TURN")
            winnner()
        
    def b3_f():
        global turn
        turn+=1
        if turn%2==0:
            b3_txt.set("O")
            b3.config(textvariable=b3_txt, bg="black", fg="white",state="disabled")
            message.set(f"IT'S {var_n1.upper()}'S TURN")
            winnner()
        else:
            b3_txt.set("X")
            b3.config(textvariable=b3_txt, bg="black",fg="white",state="disabled")
            message.set(f"IT'S {var_n2.upper()}'S TURN")
            winnner()
        
    def b4_f():
        global turn
        turn+=1
        if turn%2==0:
            b4_txt.set("O")
            b4.config(textvariable=b4_txt, bg="black", fg="white",state="disabled")
            message.set(f"IT'S {var_n1.upper()}'S TURN")
            winnner()
        else:
            b4_txt.set("X")
            b4.config(textvariable=b4_txt, bg="black",fg="white",state="disabled")
            message.set(f"IT'S {var_n2.upper()}'S TURN")
            winnner()
        
    def b5_f():
        global turn
        turn+=1
        if turn%2==0:
            b5_txt.set("O")
            b5.config(textvariable=b5_txt, bg="black", fg="white",state="disabled")
            message.set(f"IT'S {var_n1.upper()}'S TURN")
            winnner()
        else:
            b5_txt.set("X")
            b5.config(textvariable=b5_txt, bg="black",fg="white",state="disabled")
            message.set(f"IT'S {var_n2.upper()}'S TURN")
            winnner()
        
    def b6_f():
        global turn
        turn+=1
        if turn%2==0:
            b6_txt.set("O")
            b6.config(textvariable=b6_txt, bg="black", fg="white",state="disabled")
            message.set(f"IT'S {var_n1.upper()}'S TURN")
            winnner()
        else:
            b6_txt.set("X")
            b6.config(textvariable=b6_txt, bg="black",fg="white",state="disabled")
            message.set(f"IT'S {var_n2.upper()}'S TURN")
            winnner()
        
    def b7_f():
        global turn
        turn+=1
        if turn%2==0:
            b7_txt.set("O")
            b7.config(textvariable=b7_txt, bg="black", fg="white",state="disabled")
            message.set(f"IT'S {var_n1.upper()}'S TURN")
            winnner()
        else:
            b7_txt.set("X")
            b7.config(textvariable=b7_txt, bg="black",fg="white",state="disabled")
            message.set(f"IT'S {var_n2.upper()}'S TURN")
            winnner()
        
    def b8_f():
        global turn
        turn+=1
        if turn%2==0:
            b8_txt.set("O")
            b8.config(textvariable=b8_txt, bg="black", fg="white",state="disabled")
            message.set(f"IT'S {var_n1.upper()}'S TURN")
            winnner()
        else:
            b8_txt.set("X")
            b8.config(textvariable=b8_txt, bg="black",fg="white",state="disabled")
            message.set(f"IT'S {var_n2.upper()}'S TURN")
            winnner()
        
    def b9_f():
        global turn
        turn+=1
        if turn%2==0:
            b9_txt.set("O")
            b9.config(textvariable=b9_txt, bg="black", fg="white",state="disabled")
            message.set(f"IT'S {var_n1.upper()}'S TURN")
            winnner()
        else:
            b9_txt.set("X")
            b9.config(textvariable=b9_txt, bg="black",fg="white",state="disabled")
            message.set(f"IT'S {var_n2.upper()}'S TURN")
            winnner()



    # ========================================= buttons ==========================================

    b1=Button(app,text=" ", bg="#ffcc00", state="disabled")
    b1.place(x=50, y=30, width=200, height=200)
    b2=Button(app,text=" ", bg="#ffcc00", state="disabled")
    b2.place(x=50, y=230, width=200, height=200) 
    b3=Button(app,text=" ", bg="#ffcc00", state="disabled")
    b3.place(x=50, y=430, width=200, height=200) 
    b4=Button(app,text=" ", bg="#ffcc00", state="disabled")
    b4.place(x=250, y=30, width=200, height=200) 
    b5=Button(app,text=" ", bg="#ffcc00", state="disabled")
    b5.place(x=250, y=230, width=200, height=200) 
    b6=Button(app,text=" ", bg="#ffcc00", state="disabled")
    b6.place(x=250, y=430, width=200, height=200) 
    b7=Button(app,text=" ", bg="#ffcc00", state="disabled")
    b7.place(x=450, y=30, width=200, height=200) 
    b8=Button(app,text=" ", bg="#ffcc00", state="disabled")
    b8.place(x=450, y=230, width=200, height=200) 
    b9=Button(app,text=" ", bg="#ffcc00", state="disabled")
    b9.place(x=450, y=430, width=200, height=200)

    start=Button(app,text=" START ", font= Font( size= 9, weight= "bold"), fg="#ffcc00", bg="black", command=start_f, activebackground="#ffcc00", activeforeground="black")
    start.place(x=800, y=230, width=80, height=35)
    replay_b=Button(app,text=" REPLAY ", font= Font( size= 9, weight= "bold"), fg="#ffcc00", bg="black", command=replay_all, activebackground="#ffcc00", activeforeground="black")
    replay_b.place(x=900, y=230, width=80, height=35)
    
    get_out=Button(app,text=" GET OUT ", font= Font( size= 9, weight= "bold"), fg="white", bg="red", command=quit, activebackground="#ffcc00", activeforeground="black")
    get_out.place(x=1000, y=230, width=80, height=35)
    # ======================================= labels ================================================

    player1 = Label(app, text="Player 1 Name", bg="#ffcc00", fg="black", font= Font( size= 9, weight= "bold"))
    player1.place(x=710, y=85, width=90, height=40)

    player2 = Label(app, text="Player 2 Name", bg="#ffcc00", fg="black", font= Font( size= 9, weight= "bold"))
    player2.place(x=710, y=140, width=90, height=40)


    message=StringVar()
    genereal_msg = Label(app, textvariable=message, bg="#ffcc00", fg="black", font= Font( size= 14, weight= "bold"))
    genereal_msg.place(x=720, y=310, width=400, height=100)

    # ======================================== conditions =======================================
    def winnner():
        if turn%2==0:
            real_name=var_n2
        else:
            real_name=var_n1

        if b1_txt.get()==b2_txt.get()==b3_txt.get()=="X" or b1_txt.get()==b2_txt.get()==b3_txt.get()=="O":
            b1.config(fg="black", bg="white", state="disabled")
            b2.config(fg="black", bg="white", state="disabled")
            b3.config(fg="black", bg="white", state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
            message.set(f"THE WINNER IS {real_name.upper()}")


        elif  b1_txt.get()==b4_txt.get()==b7_txt.get()=="X" or b1_txt.get()==b4_txt.get()==b7_txt.get()=="O":
            b1.config(fg="black", bg="white", state="disabled")
            b4.config(fg="black", bg="white", state="disabled")
            b7.config(fg="black", bg="white", state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
            message.set(f"THE WINNER IS {real_name.upper()}")


        elif  b1_txt.get()==b5_txt.get()==b9_txt.get()=="X" or b1_txt.get()==b5_txt.get()==b9_txt.get()=="O":
            b1.config(fg="black", bg="white", state="disabled")
            b5.config(fg="black", bg="white", state="disabled")
            b9.config(fg="black", bg="white", state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b6.config(state="disabled")
            b8.config(state="disabled")
            b7.config(state="disabled")
            message.set(f"THE WINNER IS {real_name.upper()}")


        elif  b2_txt.get()==b5_txt.get()==b8_txt.get()=="X" or b2_txt.get()==b5_txt.get()==b8_txt.get()=="O":
            b2.config(fg="black", bg="white", state="disabled")
            b5.config(fg="black", bg="white", state="disabled")
            b8.config(fg="black", bg="white", state="disabled")
            b1.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b6.config(state="disabled")
            b9.config(state="disabled")
            b7.config(state="disabled")
            message.set(f"THE WINNER IS {real_name.upper()}")


        elif  b3_txt.get()==b5_txt.get()==b7_txt.get()=="X" or b3_txt.get()==b5_txt.get()==b7_txt.get()=="O" :
            b3.config(fg="black", bg="white", state="disabled")
            b5.config(fg="black", bg="white", state="disabled")
            b7.config(fg="black", bg="white", state="disabled")
            b1.config(state="disabled")
            b2.config(state="disabled")
            b4.config(state="disabled")
            b6.config(state="disabled")
            b9.config(state="disabled")
            b8.config(state="disabled")
            message.set(f"THE WINNER IS {real_name.upper()}")


        elif  b3_txt.get()==b6_txt.get()==b9_txt.get()=="X" or b3_txt.get()==b6_txt.get()==b9_txt.get()=="O"  :
            b3.config(fg="black", bg="white", state="disabled")
            b6.config(fg="black", bg="white", state="disabled")
            b9.config(fg="black", bg="white", state="disabled")
            b1.config(state="disabled")
            b2.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            message.set(f"THE WINNER IS {real_name.upper()}")


        elif  b4_txt.get()==b5_txt.get()==b6_txt.get()=="X" or b4_txt.get()==b5_txt.get()==b6_txt.get()=="O" :
            b4.config(fg="black", bg="white", state="disabled")
            b6.config(fg="black", bg="white", state="disabled")
            b5.config(fg="black", bg="white", state="disabled")
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b9.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            message.set(f"THE WINNER IS {real_name.upper()}")

            
        elif  b7_txt.get()==b8_txt.get()==b9_txt.get()=="X" or b7_txt.get()==b8_txt.get()==b9_txt.get()=="O":
            b7.config(fg="black", bg="white", state="disabled")
            b8.config(fg="black", bg="white", state="disabled")
            b9.config(fg="black", bg="white", state="disabled")
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            message.set(f"THE WINNER IS {real_name.upper()}")
        elif turn==9:
            message.set(f"THE GAME ENDED WITH A TIE")
    # ===============================================================================================
    app.config(bg="#ffcc00")
replay_all()
app.mainloop()