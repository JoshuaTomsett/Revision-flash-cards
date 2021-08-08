import tkinter as  tk
import csv
import random

root = tk.Tk()
root.geometry("1920x1080")
root.config(bg="#121212")
root.attributes('-fullscreen', True)

def randomList(theme_list):
    copy = theme_list[:-1]
    random.shuffle(copy)
    copy.append(theme_list[-1])
    return(copy)


def add(number):        # number is current
    global current
    global theme_list
    global Question_state
    global page_label
    global text_box
    global end
    global wrong_list
    global ISWRONG

    if number == len(theme_list) - 1:

        if ISWRONG:
            pass

        elif end:
            wrong_list.append(["the end"])
            flash_card.Place(wrong=True,wrongList=wrong_list)

        else:
            end = True

    elif Question_state == True:  # currently on a question
        Question_state = False

    elif Question_state == False:
        current = number + 1
        Question_state = True
        page_label.config(text=(current+1 , "/" , len(theme_list)))
        text_box.delete('1.0', 'end')

def subtract(number):
    global current
    global Question_state
    global page_label

    if number == 0 and Question_state == True:
        pass

    elif Question_state == True:  # currently on a question
        current = number - 1
        Question_state = False
        page_label.config(text=(current+1 , "/" , len(theme_list)))

    elif Question_state == False:
        Question_state = True

def Next_Card(number):
    global card
    global theme_list
    global Question_state

    if Question_state == True:       # Question
        global card_img
        card.config(image=card_img)
        card.config(text=(str((theme_list[number])[0])))

    else:                            #Answer
        answer = list(str((theme_list[number])[1]))

        if answer[0] == 'A':
            card.config(image=card_img)
            card.config(text=(str((theme_list[number])[1])))
        else:
            card.config(text="")
            new_img = tk.PhotoImage(file=(str((theme_list[number])[1])))
            card.config(image=(new_img))
            card.photo = new_img

class Flash_Cards(object):

    def Place(self,subject=0,theme=0,wrong=False,wrongList=[]):                     #          even = Question

        menu_frame = tk.Frame(root,height = 1080,width=1920,bg="#121212")
        menu_frame.place(x=0,y=0)
        
        global theme_list
        global current
        global card
        global Question_state
        global text_box
        global end
        global ISWRONG
        end = False
        current = 0
        Question_state = True   # True if a question 

        if wrong:
            ISWRONG = True
            theme_list = wrongList
        
        else:
            ISWRONG = False
            directory = "Excel/"+subject+"/"+theme+".csv"
            theme_list = []
            with open(directory, 'rt') as text_file:
                reader = csv.reader(text_file)
                theme_list = list(reader)

        # theme_list = randomList(theme_list)     # Randomize list

        topic_banner_img = tk.PhotoImage(file="Images/topic_banner.gif")
        topic_banner = tk.Label(menu_frame,image=topic_banner_img,text=theme,font=("Helvetica",50,"bold"),fg='#84c9fb',compound='center')
        topic_banner.photo = topic_banner_img
        topic_banner.place(x=402,y=40)

        global card_img
        card_img = tk.PhotoImage(file="Images/card.gif")
        card = tk.Label(menu_frame,image=card_img,text=str((theme_list[current])[0]),font=("Helvetica",30,"bold"),wraplength=900,compound='center')
        card.photo = card_img
        card.place(x=402,y=192)

        text_box = tk.Text(menu_frame,font=("Helvetica",20,"bold"),height=19,width=21,fg='#84c9fb',bg='#121212')
        text_box.place(x=1560,y=192)

        next_img = tk.PhotoImage(file="Images/next.gif")
        next_button = tk.Button(menu_frame,image=next_img,font=("",30),command=lambda: [add(current) , Next_Card(current)])
        next_button.photo = next_img
        next_button.place(x=1287,y=834)

        back_img = tk.PhotoImage(file="Images/back.gif")
        last_button = tk.Button(menu_frame,image=back_img,font=("",30),command=lambda: [subtract(current) , Next_Card(current)])
        last_button.photo = back_img
        last_button.place(x=402,y=834)

        back_button_img = tk.PhotoImage(file="Images/back_menu.gif")
        back_button = tk.Button(menu_frame,image=back_button_img,command=lambda: [menu_frame.destroy() , topic.Place_buttons(subject)])
        back_button.photo = back_button_img
        back_button.place(x=35,y=35)

        global page_label
        page_img = tk.PhotoImage(file="Images/blank.gif")
        page_label = tk.Label(menu_frame,image=page_img,text=(current+1 , "/" , len(theme_list)),fg='#84c9fb',compound='center',font=("",30))
        page_label.photo = page_img
        page_label.place(x=992,y=834)

        def addWrong():
            if theme_list[current] not in wrong_list:
                wrong_list.append(theme_list[current])
        
        global wrong_list
        wrong_list = []

        wrong_img = tk.PhotoImage(file="Images/wrong.gif")
        wrong_button = tk.Button(menu_frame,image=wrong_img,command=lambda: [addWrong()])
        wrong_button.photo = wrong_img
        wrong_button.place(x=697,y=834)

        def next_bind(placeholder):
            next_button.invoke()

        def last_bind(placeholder):
            last_button.invoke()

        root.bind('<Right>',next_bind)
        root.bind('<Left>',last_bind)

class Topics(object):

    def Place_buttons(self,subject):

        menu_frame = tk.Frame(root,height = 1080,width=1920,bg="#121212")
        menu_frame.place(x=0,y=0)

        if subject == "Further":

            core_1_img = tk.PhotoImage(file="Images/Further/core_1.gif")
            core_1_button = tk.Button(menu_frame,image=core_1_img,command=lambda: [flash_card.Place("Further","Core_1"),menu_frame.destroy()])
            core_1_button.photo = core_1_img
            core_1_button.place(x=345,y=470)

            core_2_img = tk.PhotoImage(file="Images/Further/core_2.gif")
            core_2_button = tk.Button(menu_frame,image=core_2_img,command=lambda: [flash_card.Place("Further","Core_2"),menu_frame.destroy()])
            core_2_button.photo = core_2_img
            core_2_button.place(x=678,y=470)

            # core_1_img = tk.PhotoImage(file="Images/Further/core_1.gif")
            # core_1_button = tk.Button(menu_frame,image=core_1_img,command=lambda: [flash_card.Place("Further","Core_1"),menu_frame.destroy()])
            # core_1_button.photo = core_1_img
            # core_1_button.place(x=1011,y=470)

            # core_1_img = tk.PhotoImage(file="Images/Further/core_1.gif")
            # core_1_button = tk.Button(menu_frame,image=core_1_img,command=lambda: [flash_card.Place("Further","Core_1"),menu_frame.destroy()])
            # core_1_button.photo = core_1_img
            # core_1_button.place(x=1344,y=470)

        elif subject == "Maths":

            maths_1_img = tk.PhotoImage(file="Images/Maths/maths_1.gif")
            maths_1_button = tk.Button(menu_frame,image=maths_1_img,command=lambda: [flash_card.Place("Maths","Year_1"),menu_frame.destroy()])
            maths_1_button.photo = maths_1_img
            maths_1_button.place(x=583,y=231)

            stats_1_img = tk.PhotoImage(file="Images/Maths/stats.gif")
            stats_1_button = tk.Button(menu_frame,image=stats_1_img,command=lambda: [flash_card.Place("Maths","stats_1"),menu_frame.destroy()])
            stats_1_button.photo = stats_1_img
            stats_1_button.place(x=583,y=470)

            mechanics_1_img = tk.PhotoImage(file="Images/Maths/mechanics.gif")
            mechanics_1_button = tk.Button(menu_frame,image=mechanics_1_img,command=lambda: [flash_card.Place("Maths","mech_1"),menu_frame.destroy()])
            mechanics_1_button.photo = mechanics_1_img
            mechanics_1_button.place(x=583,y=709)

        elif subject == "CompSci":

            compsci_img_1_1 = tk.PhotoImage(file="Images/CompSci/1.1.gif")
            compsci_button_1_1 = tk.Button(menu_frame,image=compsci_img_1_1,command=lambda: [flash_card.Place("CompSci","1.1"),menu_frame.destroy()])
            compsci_button_1_1.photo = compsci_img_1_1
            compsci_button_1_1.place(x=153,y=317)

            compsci_img_1_2 = tk.PhotoImage(file="Images/CompSci/1.2.gif")
            compsci_button_1_2 = tk.Button(menu_frame,image=compsci_img_1_2,command=lambda: [flash_card.Place("CompSci","1.2"),menu_frame.destroy()])
            compsci_button_1_2.photo = compsci_img_1_2
            compsci_button_1_2.place(x=499,y=317)

            compsci_img_1_3 = tk.PhotoImage(file="Images/CompSci/1.3.gif")
            compsci_button_1_3 = tk.Button(menu_frame,image=compsci_img_1_3,command=lambda: [flash_card.Place("CompSci","1.3"),menu_frame.destroy()])
            compsci_button_1_3.photo = compsci_img_1_3
            compsci_button_1_3.place(x=845,y=317)

            compsci_img_1_4 = tk.PhotoImage(file="Images/CompSci/1.4.gif")
            compsci_button_1_4 = tk.Button(menu_frame,image=compsci_img_1_4,command=lambda: [flash_card.Place("CompSci","1.4"),menu_frame.destroy()])
            compsci_button_1_4.photo = compsci_img_1_4
            compsci_button_1_4.place(x=1191,y=317)

            compsci_img_1_5 = tk.PhotoImage(file="Images/CompSci/1.5.gif")
            compsci_button_1_5 = tk.Button(menu_frame,image=compsci_img_1_5,command=lambda: [flash_card.Place("CompSci","1.5"),menu_frame.destroy()])
            compsci_button_1_5.photo = compsci_img_1_5
            compsci_button_1_5.place(x=1537,y=317)

            compsci_img_2_1 = tk.PhotoImage(file="Images/CompSci/2.1.gif")
            compsci_button_2_1 = tk.Button(menu_frame,image=compsci_img_2_1,command=lambda: [flash_card.Place("CompSci","2.1"),menu_frame.destroy()])
            compsci_button_2_1.photo = compsci_img_2_1
            compsci_button_2_1.place(x=499,y=622)

            compsci_img_2_2 = tk.PhotoImage(file="Images/CompSci/2.2.gif")
            compsci_button_2_2 = tk.Button(menu_frame,image=compsci_img_2_2,command=lambda: [flash_card.Place("CompSci","2.2"),menu_frame.destroy()])
            compsci_button_2_2.photo = compsci_img_2_2
            compsci_button_2_2.place(x=845,y=622)

            compsci_img_2_3 = tk.PhotoImage(file="Images/CompSci/2.3.gif")
            compsci_button_2_3 = tk.Button(menu_frame,image=compsci_img_2_3,command=lambda: [flash_card.Place("CompSci","2.3"),menu_frame.destroy()])
            compsci_button_2_3.photo = compsci_img_2_3
            compsci_button_2_3.place(x=1191,y=622)

        elif subject == "Economics":
            
            theme_1_img = tk.PhotoImage(file="Images/Economics/theme_1.gif")
            theme_1_button = tk.Button(menu_frame,image=theme_1_img,command=lambda: [flash_card.Place("Economics","Theme_1"),menu_frame.destroy()])
            theme_1_button.photo = theme_1_img
            theme_1_button.place(x=345,y=470)

            theme_2_img = tk.PhotoImage(file="Images/Economics/theme_2.gif")
            theme_2_button = tk.Button(menu_frame,image=theme_2_img,command=lambda: [flash_card.Place("Economics","Theme_2"),menu_frame.destroy()])
            theme_2_button.photo = theme_2_img
            theme_2_button.place(x=678,y=470)

            theme_3_img = tk.PhotoImage(file="Images/Economics/theme_3.gif")
            theme_3_button = tk.Button(menu_frame,image=theme_3_img,command=lambda: [flash_card.Place("Economics","Theme_3"),menu_frame.destroy()])
            theme_3_button.photo = theme_3_img
            theme_3_button.place(x=1011,y=470)

            theme_4_img = tk.PhotoImage(file="Images/Economics/theme_4.gif")
            theme_4_button = tk.Button(menu_frame,image=theme_4_img,command=lambda: [flash_card.Place("Economics","Theme_4"),menu_frame.destroy()])
            theme_4_button.photo = theme_4_img
            theme_4_button.place(x=1344,y=470)

        back_button_img = tk.PhotoImage(file="Images/back_menu.gif")
        back_button = tk.Button(menu_frame,image=back_button_img,command=lambda: [menu_frame.destroy() , menu.Place_buttons()])
        back_button.photo = back_button_img
        back_button.place(x=35,y=35)

class Menu(object):

    def Place_buttons(self):

        menu_frame = tk.Frame(root,height = 1080,width=1920,bg="#121212")
        menu_frame.place(x=0,y=0)

        quit_img = tk.PhotoImage(file="Images/quit.gif")
        quit_button = tk.Button(menu_frame,image=quit_img,command=lambda: root.destroy())
        quit_button.photo = quit_img
        quit_button.place(x=35,y=35)

        further_img = tk.PhotoImage(file="Images/Further/further_maths.gif")
        further_button = tk.Button(menu_frame,image=further_img,command=lambda: [topic.Place_buttons("Further"),menu_frame.destroy()])
        further_button.photo = further_img
        further_button.place(x=345,y=470)

        maths_img = tk.PhotoImage(file="Images/Maths/maths.gif")
        maths_button = tk.Button(menu_frame,image=maths_img,command=lambda: [topic.Place_buttons("Maths"),menu_frame.destroy()])
        maths_button.photo = maths_img
        maths_button.place(x=678,y=470)

        computing_img = tk.PhotoImage(file="Images/CompSci/computer_science.gif")
        computing_button = tk.Button(menu_frame,image=computing_img,command=lambda: [topic.Place_buttons("CompSci"),menu_frame.destroy()])
        computing_button.photo = computing_img
        computing_button.place(x=1011,y=470)

        economics_img = tk.PhotoImage(file="Images/Economics/economics.gif")
        economics_button = tk.Button(menu_frame,image=economics_img,command=lambda: [topic.Place_buttons("Economics"),menu_frame.destroy()])
        economics_button.photo = economics_img
        economics_button.place(x=1344,y=470)

menu = Menu()
topic = Topics()
flash_card = Flash_Cards()

menu.Place_buttons()

def exit_fullscreen(placeholder):
    root.attributes('-fullscreen', False)
    root.state('zoomed')
root.bind('<Escape>',exit_fullscreen)

def fullscreen(placeholder):
    root.attributes('-fullscreen', True)
root.bind('<F11>',fullscreen)

root.mainloop()