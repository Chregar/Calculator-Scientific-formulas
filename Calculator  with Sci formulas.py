from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox




####################################################Start calculator########################################

root = Tk()
root.title('Calculator')
root.configure(background='gray38')


entry_text_1 = StringVar()
entry = Entry(root, fg="#00FF00", bg="black", textvariable = entry_text_1, width=30,borderwidth=30)
entry.grid(row = 0,column = 0,columnspan = 3, padx = 10,pady=10)
new_text = '     Welcome to the calculator!'
entry_text_1.set(new_text,)

##################################################Function for button_formulas#######################################

def button_formulas():
    top = Toplevel()
    top.title('Formulas')
    top.configure(background='black')


    entrytext = StringVar()
    entry2 = Entry(top, fg="#00FF00", bg="black", textvariable = entrytext, width=30,borderwidth=30)
    entry2.grid(row = 0,column = 0,columnspan = 3, padx = 10,pady=10)
    new_text = '     Pick any formula. Thank you!'
    entrytext.set(new_text)

    def popup_of_formulas():
        answer = messagebox.askyesno('Popup', 'Are you sure want to exit ?')
        if answer:
            top.destroy()
    btnclose = Button(top, bg = 'indian red',text='Close Window', width = 35, command=popup_of_formulas)
    btnclose.grid(row = 7,column = 0,columnspan = 3)


###################################################Define force#############################################################
    def button_force():
        global f_num
        global sec_num
        global first_value

        top_force_input = Toplevel()
        top_force_input.configure(background='gray38')
        top_force_input.title('Force_ input')

        labelText = StringVar()
        labelText.set("      Dear user, which variable of the equation would you like to calculate ?\nForce (F), mass (m) or acceleration (a) ? ")
        labelDir = Label(top_force_input, textvariable=labelText,
                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
        labelDir.grid(row=0, column=0)

        def popup_of_force():
            answer = messagebox.showinfo('Popup', 'You exited "Force" section')
            if answer:
                top_force_input.destroy()

        btnclose = Button(top_force_input, text='Close Window', font=('Times New Roman', 12),
                          bg='indian red', fg='black', command=popup_of_force)
        btnclose.grid(row=5, column=0, columnspan=3)

        ########Entry for force_mass##############
        entry_force_input = Entry(top_force_input, fg="#00FF00", bg="black", width=50, borderwidth=30)
        entry_force_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        def button_proceed1():
            global first_value
            first_choice = entry_force_input.get()
            first_value = str(first_choice)

            if entry_force_input.get() == 'M' or entry_force_input.get() == 'm':
                top_mass_force = Toplevel()
                top_mass_force.configure(background='gray38')
                top_mass_force.title('Mass__ force')

                labelText = DoubleVar()
                labelText.set("Enter the desired Force (Newtons):                                       ")
                labelDir = Label(top_mass_force, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_mass_force, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_mass_force.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                entry_mass_force = Entry(top_mass_force, fg="#00FF00", bg="black", width=50,
                                         borderwidth=30)
                entry_mass_force.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_mass_force():
                    first_num_force = entry_mass_force.get()
                    f_num = first_num_force

                    top_mass_acceleration = Toplevel()
                    top_mass_acceleration.configure(background='gray38')
                    top_mass_acceleration.title('Mass__ acceleration')

                    labelText = DoubleVar()
                    labelText.set("Enter the desired acceleration (m/s²):                                            ")
                    labelDir = Label(top_mass_acceleration, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_mass_acceleration, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_mass_acceleration.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_mass_acceleration = Entry(top_mass_acceleration, fg="#00FF00", bg="black", width=50,
                                                    borderwidth=30)
                    entry_mass_acceleration.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceedfinal_resultmass():
                        sec_num_acceleration = entry_mass_acceleration.get()
                        sec_num = sec_num_acceleration

                        top_result_mass = Toplevel()
                        top_result_mass.configure(background='gray38')
                        top_result_mass.title('Mass__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (kg):                                                                        ")
                        labelDir = Label(top_result_mass, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_mass, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_mass.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_mass = Entry(top_result_mass, font=('Times New Roman', 15),
                                                  fg="#00FF00", bg="black", width=50,
                                                  borderwidth=30)
                        entry_result_mass.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_mass.insert(0, float(f_num) / float(sec_num))

                    buttonproceed_mass = Button(top_mass_acceleration, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonproceedfinal_resultmass)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_mass_force, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_mass_force)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_force_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_force_input.get() == 'A' or entry_force_input.get() == 'a':
                top_acceleration_force = Toplevel()
                top_acceleration_force.configure(background='gray38')
                top_acceleration_force.title('Acceleration__ force')

                labelText = DoubleVar()
                labelText.set("Enter the desired Force (Newtons):                                       ")
                labelDir = Label(top_acceleration_force, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_acceleration_force, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_acceleration_force.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_acceleration_force = Entry(top_acceleration_force, fg="#00FF00", bg="black", width=50,
                                                 borderwidth=30)
                entry_acceleration_force.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_acceleration_force():
                    first_num_force = entry_acceleration_force.get()
                    f_num = first_num_force

                    top_acceleration_mass = Toplevel()
                    top_acceleration_mass.configure(background='gray38')
                    top_acceleration_mass.title('Acceleration__ mass')

                    labelText = DoubleVar()
                    labelText.set("Enter the desired mass (kg):                                            ")
                    labelDir = Label(top_acceleration_mass, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_acceleration_mass, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_acceleration_mass.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_acceleration_mass = Entry(top_acceleration_mass, fg="#00FF00", bg="black", width=50,
                                                    borderwidth=30)
                    entry_acceleration_mass.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceedfinal_resultacceleration():
                        sec_num_mass = entry_acceleration_mass.get()
                        sec_num = sec_num_mass

                        top_result_acceleration = Toplevel()
                        top_result_acceleration.configure(background='gray38')
                        top_result_acceleration.title('Acceleration__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (m/s²):                                                                        ")
                        labelDir = Label(top_result_acceleration, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_acceleration, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_acceleration.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_acceleration = Entry(top_result_acceleration, font=('Times New Roman', 15),
                                                          fg="#00FF00", bg="black", width=50,
                                                          borderwidth=30)
                        entry_result_acceleration.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_acceleration.insert(0, float(f_num) / float(sec_num))

                    buttonproceed_mass = Button(top_acceleration_mass, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonproceedfinal_resultacceleration)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_acceleration_force, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_acceleration_force)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_force_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_force_input.get() == 'F' or entry_force_input.get() == 'f':
                top_force_acceleration = Toplevel()
                top_force_acceleration.configure(background='gray38')
                top_force_acceleration.title('Force_ acceleration')

                labelText = DoubleVar()
                labelText.set("Enter the desired acceleration (m/s²):                                       ")
                labelDir = Label(top_force_acceleration, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_force_acceleration, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_force_acceleration.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_force_acceleration = Entry(top_force_acceleration, fg="#00FF00", bg="black", width=50,
                                                 borderwidth=30)
                entry_force_acceleration.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_force_acceleration():
                    first_num_acceleration = entry_force_acceleration.get()
                    f_num = first_num_acceleration

                    top_force_mass = Toplevel()
                    top_force_mass.configure(background='gray38')
                    top_force_mass.title('Force_ mass')

                    ###########Label close for force_mass##########
                    labelText = DoubleVar()
                    labelText.set("Enter the desired mass (kg):                                            ")
                    labelDir = Label(top_force_mass, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_force_mass, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_force_mass.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_force_mass = Entry(top_force_mass, fg="#00FF00", bg="black", width=50, borderwidth=30)
                    entry_force_mass.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceedfinal_resultforce():
                        sec_num_force = entry_force_mass.get()
                        sec_num = sec_num_force

                        top_result_force = Toplevel()
                        top_result_force.configure(background='gray38')
                        top_result_force.title('Force_ result')

                        ###########Label close for force_mass##########
                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (Newtons):                                                                        ")
                        labelDir = Label(top_result_force, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_force, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_force.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_force_result = Entry(top_result_force, font=('Times New Roman', 15),
                                                   fg="#00FF00", bg="black", width=50,
                                                   borderwidth=30)
                        entry_force_result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_force_result.insert(0, float(f_num) * float(sec_num))

                    buttonproceed_mass = Button(top_force_mass, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonproceedfinal_resultforce)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_force_acceleration, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_force_acceleration)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

        buttonproceed_input = Button(top_force_input, text='Continue', padx=90, pady=20,
                                     font=('Times New Roman', 10),
                                     command=button_proceed1)
        buttonproceed_input.grid(row=3, column=0, columnspan=3)

    ##################################################Define weight#############################################################

    def button_weight():
        global f_num
        global sec_num
        global first_value

        top_weight_input = Toplevel()
        top_weight_input.configure(background='gray38')
        top_weight_input.title('Weight_ input')

        labelText = StringVar()
        labelText.set("      Dear user, which variable of the equation would you like to calculate ?\nWeight (w), mass(m), or gravity (g) ? ")
        labelDir = Label(top_weight_input, textvariable=labelText,
                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
        labelDir.grid(row=0, column=0)

        def popup_of_weight():
            answer = messagebox.showinfo('Popup', 'You exited "Weight" section')
            if answer:
                top_weight_input.destroy()


        btnclose = Button(top_weight_input, text='Close Window', font=('Times New Roman', 12),
                          bg='indian red', fg='black', command=popup_of_weight)
        btnclose.grid(row=5, column=0, columnspan=3)

        ########Entry for force_mass##############
        entry_weight_input = Entry(top_weight_input, fg="#00FF00", bg="black", width=50, borderwidth=30)
        entry_weight_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        def button_proceed1():
            global first_value
            first_choice = entry_weight_input.get()
            first_value = str(first_choice)

            if entry_weight_input.get() == 'M' or entry_weight_input.get() == 'm':
                top_mass_weight = Toplevel()
                top_mass_weight.configure(background='gray38')
                top_mass_weight.title('Mass__ weight')

                labelText = DoubleVar()
                labelText.set("Enter the desired weight (Newtons):                                       ")
                labelDir = Label(top_mass_weight, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_mass_weight, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_mass_weight.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                entry_mass_weight = Entry(top_mass_weight, fg="#00FF00", bg="black", width=50,
                                          borderwidth=30)
                entry_mass_weight.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_mass_weight():
                    first_num_weight = entry_mass_weight.get()
                    f_num = first_num_weight

                    top_mass_gravity = Toplevel()
                    top_mass_gravity.configure(background='gray38')
                    top_mass_gravity.title('Mass__ acceleration')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired gravitational force magnitude (m/s²):                                            ")
                    labelDir = Label(top_mass_gravity, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_mass_gravity, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_mass_gravity.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_mass_gravity = Entry(top_mass_gravity, fg="#00FF00", bg="black", width=50,
                                               borderwidth=30)
                    entry_mass_gravity.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceedfinal_resultmass():
                        sec_num_gravity = entry_mass_gravity.get()
                        sec_num = sec_num_gravity

                        top_result_mass = Toplevel()
                        top_result_mass.configure(background='gray38')
                        top_result_mass.title('Mass__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (kg):                                                                        ")
                        labelDir = Label(top_result_mass, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_mass, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_mass.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_mass = Entry(top_result_mass, font=('Times New Roman', 15),
                                                  fg="#00FF00", bg="black", width=50,
                                                  borderwidth=30)
                        entry_result_mass.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_mass.insert(0, float(f_num) / float(sec_num))

                    buttonproceed_mass = Button(top_mass_gravity, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonproceedfinal_resultmass)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_mass_weight, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_mass_weight)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_weight_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_weight_input.get() == 'g' or entry_weight_input.get() == 'G':
                top_gravity_weight = Toplevel()
                top_gravity_weight.configure(background='gray38')
                top_gravity_weight.title('Gravity__ weight')

                labelText = DoubleVar()
                labelText.set("Enter the desired weight magnitude (Newtons):                                       ")
                labelDir = Label(top_gravity_weight, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_gravity_weight, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_gravity_weight.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_gravity_weight = Entry(top_gravity_weight, fg="#00FF00", bg="black", width=50,
                                             borderwidth=30)
                entry_gravity_weight.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_gravity_weight():
                    first_num_gravity = entry_gravity_weight.get()
                    f_num = first_num_gravity

                    top_gravity_mass = Toplevel()
                    top_gravity_mass.configure(background='gray38')
                    top_gravity_mass.title('Gravity__ mass')

                    labelText = DoubleVar()
                    labelText.set("Enter the desired mass (kg):                                            ")
                    labelDir = Label(top_gravity_mass, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_gravity_mass, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_gravity_mass.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_gravity_mass = Entry(top_gravity_mass, fg="#00FF00", bg="black", width=50, borderwidth=30)
                    entry_gravity_mass.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceedfinal_resultgravity():
                        sec_num_mass = entry_gravity_mass.get()
                        sec_num = sec_num_mass

                        top_result_gravity = Toplevel()
                        top_result_gravity.configure(background='gray38')
                        top_result_gravity.title('Gravity__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (m/s²):                                                                        ")
                        labelDir = Label(top_result_gravity, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_gravity, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_gravity.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_gravity = Entry(top_result_gravity, font=('Times New Roman', 15),
                                                     fg="#00FF00", bg="black", width=50,
                                                     borderwidth=30)
                        entry_result_gravity.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_gravity.insert(0, float(f_num) / float(sec_num))

                    buttonproceed_mass = Button(top_gravity_mass, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonproceedfinal_resultgravity)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_gravity_weight, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_gravity_weight)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_weight_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_weight_input.get() == 'W' or entry_weight_input.get() == 'w':
                top_weight_gravity = Toplevel()
                top_weight_gravity.configure(background='gray38')
                top_weight_gravity.title('Force_ acceleration')

                labelText = DoubleVar()
                labelText.set(
                    "Enter the desired gravitational force magnitude (m/s²):                                       ")
                labelDir = Label(top_weight_gravity, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_weight_gravity, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_weight_gravity.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_weight_gravity = Entry(top_weight_gravity, fg="#00FF00", bg="black", width=50,
                                             borderwidth=30)
                entry_weight_gravity.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_weight_gravity():
                    first_num_weight = entry_weight_gravity.get()
                    f_num = first_num_weight

                    top_weight_mass = Toplevel()
                    top_weight_mass.configure(background='gray38')
                    top_weight_mass.title('Weight__ mass')

                    ###########Label close for force_mass##########
                    labelText = DoubleVar()
                    labelText.set("Enter the desired mass (kg):                                            ")
                    labelDir = Label(top_weight_mass, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_weight_mass, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_weight_mass.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_weight_mass = Entry(top_weight_mass, fg="#00FF00", bg="black", width=50, borderwidth=30)
                    entry_weight_mass.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceedfinal_resultweight():
                        sec_num_mass = entry_weight_mass.get()
                        sec_num = sec_num_mass

                        top_result_weight = Toplevel()
                        top_result_weight.configure(background='gray38')
                        top_result_weight.title('Weight__ result')

                        ###########Label close for force_mass##########
                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (Newtons):                                                                        ")
                        labelDir = Label(top_result_weight, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_weight, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_weight.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_force_result = Entry(top_result_weight, font=('Times New Roman', 15),
                                                   fg="#00FF00", bg="black", width=50,
                                                   borderwidth=30)
                        entry_force_result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_force_result.insert(0, float(f_num) * float(sec_num))

                    buttonproceed_mass = Button(top_weight_mass, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonproceedfinal_resultweight)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_weight_gravity, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_weight_gravity)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

        buttonproceed_input = Button(top_weight_input, text='Continue', padx=90, pady=20,
                                     font=('Times New Roman', 10),
                                     command=button_proceed1)
        buttonproceed_input.grid(row=3, column=0, columnspan=3)

    ###################################################Define power#############################################################

    def buttonpower():
        global f_num
        global sec_num
        global first_value

        top_power_input = Toplevel()
        top_power_input.configure(background='gray38')
        top_power_input.title('Power input')

        labelText = StringVar()
        labelText.set("      Dear user, which variable of the equation would you like to calculate ?\nPower (P), work (w), time (t)? ")
        labelDir = Label(top_power_input, textvariable=labelText,
                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
        labelDir.grid(row=0, column=0)

        def popup_of_power():
            answer = messagebox.showinfo('Popup', 'You exited "Power" section')
            if answer:
                top_power_input.destroy()

        btnclose = Button(top_power_input, text='Close Window', font=('Times New Roman', 12),
                          bg='indian red', fg='black', command=popup_of_power)
        btnclose.grid(row=5, column=0, columnspan=3)

        ########Entry for force_mass##############
        entry_power_input = Entry(top_power_input, fg="#00FF00", bg="black", width=50, borderwidth=30)
        entry_power_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        def button_proceed1():
            global first_value
            first_choice = entry_power_input.get()
            first_value = str(first_choice)

            if entry_power_input.get() == 'P' or entry_power_input.get() == 'p':
                top_power_work = Toplevel()
                top_power_work.configure(background='gray38')
                top_power_work.title('Power__ work')

                labelText = DoubleVar()
                labelText.set("Enter the desired work magnitude (joules):                                       ")
                labelDir = Label(top_power_work, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_power_work, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_power_work.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                entry_power_work = Entry(top_power_work, fg="#00FF00", bg="black", width=50,
                                         borderwidth=30)
                entry_power_work.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def proceed_energy_work():
                    first_num = entry_power_work.get()
                    f_num = first_num

                    top_power_time = Toplevel()
                    top_power_time.configure(background='gray38')
                    top_power_time.title('Power__ time')

                    labelText = DoubleVar()
                    labelText.set("Enter the desired time (seconds):                                            ")
                    labelDir = Label(top_power_time, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_power_time, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_power_time.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_power_time = Entry(top_power_time, fg="#00FF00", bg="black", width=50,
                                             borderwidth=30)
                    entry_power_time.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonresult_power():
                        sec_num = entry_power_time.get()
                        sec_num = sec_num

                        top_result_power = Toplevel()
                        top_result_power.configure(background='gray38')
                        top_result_power.title('Power__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (watt):                                                                        ")
                        labelDir = Label(top_result_power, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_power, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_power.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_power = Entry(top_result_power, font=('Times New Roman', 15),
                                                   fg="#00FF00", bg="black", width=50,
                                                   borderwidth=30)
                        entry_result_power.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_power.insert(0, float(f_num) / float(sec_num))

                    buttonproceed3 = Button(top_power_time, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=buttonresult_power)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_power_work, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=proceed_energy_work)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_power_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_power_input.get() == 'W' or entry_power_input.get() == 'w':
                top_work_power = Toplevel()
                top_work_power.configure(background='gray38')
                top_work_power.title('Work__ power')

                labelText = DoubleVar()
                labelText.set("Enter the desired power magnitude (watt):                                       ")
                labelDir = Label(top_work_power, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_work_power, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_work_power.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_work_power = Entry(top_work_power, fg="#00FF00", bg="black", width=50,
                                         borderwidth=30)
                entry_work_power.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed3_energy():
                    first_num = entry_work_power.get()
                    f_num = first_num

                    top_work_time = Toplevel()
                    top_work_time.configure(background='gray38')
                    top_work_time.title('Work__ time')

                    labelText = DoubleVar()
                    labelText.set("Enter the desired time (seconds):                                            ")
                    labelDir = Label(top_work_time, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_work_time, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_work_time.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_work_time = Entry(top_work_time, fg="#00FF00", bg="black", width=50,
                                            borderwidth=30)
                    entry_work_time.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonresult_power():
                        sec_num = entry_work_time.get()
                        sec_num = sec_num

                        top_result_work = Toplevel()
                        top_result_work.configure(background='gray38')
                        top_result_work.title('Work__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (joules):                                                                        ")
                        labelDir = Label(top_result_work, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_work, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_work.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_work = Entry(top_result_work, font=('Times New Roman', 15),
                                                  fg="#00FF00", bg="black", width=50,
                                                  borderwidth=30)
                        entry_result_work.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_work.insert(0, float(f_num) * float(sec_num))

                    buttonproceed3 = Button(top_work_time, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=buttonresult_power)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_work_power, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed3_energy)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_power_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_power_input.get() == 'T' or entry_power_input.get() == 't':
                top_time_work = Toplevel()
                top_time_work.configure(background='gray38')
                top_time_work.title('Time__ work')

                labelText = DoubleVar()
                labelText.set("Enter the work magnitude (joules):                                       ")
                labelDir = Label(top_time_work, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_time_work, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_time_work.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_time_work = Entry(top_time_work, fg="#00FF00", bg="black", width=50,
                                        borderwidth=30)
                entry_time_work.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_time_work():
                    first_num_distance = entry_time_work.get()
                    f_num = first_num_distance

                    top_time_power = Toplevel()
                    top_time_power.configure(background='gray38')
                    top_time_power.title('Time__ power')

                    ###########Label close for force_mass##########
                    labelText = DoubleVar()
                    labelText.set("Enter the desired velocity (m/s):                                            ")
                    labelDir = Label(top_time_power, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_time_power, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_time_power.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_time_power = Entry(top_time_power, fg="#00FF00", bg="black", width=50, borderwidth=30)
                    entry_time_power.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonresult_time():
                        sec_number = entry_time_power.get()
                        sec_num = sec_number

                        top_result_time = Toplevel()
                        top_result_time.configure(background='gray38')
                        top_result_time.title('Time__ result')

                        ###########Label close for force_mass##########
                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (seconds):                                                                        ")
                        labelDir = Label(top_result_time, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_time, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_time.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_time_result = Entry(top_result_time, font=('Times New Roman', 15),
                                                  fg="#00FF00", bg="black", width=50,
                                                  borderwidth=30)
                        entry_time_result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_time_result.insert(0, float(f_num) / float(sec_num))

                    buttonproceed3 = Button(top_time_power, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=buttonresult_time)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_time_work, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed_time_work)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

        buttonproceed_input = Button(top_power_input, text='Continue', padx=90, pady=20,
                                     font=('Times New Roman', 10),
                                     command=button_proceed1)
        buttonproceed_input.grid(row=3, column=0, columnspan=3)

###################################################Define velocity#############################################################

    def button_velocity():
        global f_num
        global sec_num
        global first_value

        top_velocity_input = Toplevel()
        top_velocity_input.configure(background='gray38')
        top_velocity_input.title('Velocity input')

        labelText = StringVar()
        labelText.set("      Dear user, which variable of the equation would you like to calculate ?\nVelocity (v), distance (d), or time (t)")
        labelDir = Label(top_velocity_input, textvariable=labelText,
                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
        labelDir.grid(row=0, column=0)

        def popup_of_velocity():
            answer = messagebox.showinfo('Popup', 'You exited "Velocity" section')
            if answer:
                top_velocity_input.destroy()

        btnclose = Button(top_velocity_input, text='Close Window', font=('Times New Roman', 12),
                          bg='indian red', fg='black', command=popup_of_velocity)
        btnclose.grid(row=5, column=0, columnspan=3)

        ########Entry for force_mass##############
        entry_velocity_input = Entry(top_velocity_input, fg="#00FF00", bg="black", width=50, borderwidth=30)
        entry_velocity_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        def button_proceed1():
            global first_value
            first_choice = entry_velocity_input.get()
            first_value = str(first_choice)

            if entry_velocity_input.get() == 'd' or entry_velocity_input.get() == 'D':
                top_distance_velocity = Toplevel()
                top_distance_velocity.configure(background='gray38')
                top_distance_velocity.title('Distance__ velocity')

                labelText = DoubleVar()
                labelText.set("Enter the desired velocity (m/s):                                       ")
                labelDir = Label(top_distance_velocity, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_distance_velocity, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_distance_velocity.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                entry_distance_velocity = Entry(top_distance_velocity, fg="#00FF00", bg="black", width=50,
                                                borderwidth=30)
                entry_distance_velocity.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_distance_velocity():
                    first_num_distance = entry_distance_velocity.get()
                    f_num = first_num_distance

                    top_distance_time = Toplevel()
                    top_distance_time.configure(background='gray38')
                    top_distance_time.title('Distance__ time')

                    labelText = DoubleVar()
                    labelText.set("Enter the desired time (s):                                            ")
                    labelDir = Label(top_distance_time, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_distance_time, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_distance_time.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_distance_time = Entry(top_distance_time, fg="#00FF00", bg="black", width=50,
                                                borderwidth=30)
                    entry_distance_time.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceedfinal_resultdistance():
                        sec_num_time = entry_distance_time.get()
                        sec_num = sec_num_time

                        top_result_distance = Toplevel()
                        top_result_distance.configure(background='gray38')
                        top_result_distance.title('Distance__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (m):                                                                        ")
                        labelDir = Label(top_result_distance, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_distance, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_distance.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_distance = Entry(top_result_distance, font=('Times New Roman', 15),
                                                      fg="#00FF00", bg="black", width=50,
                                                      borderwidth=30)
                        entry_result_distance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_distance.insert(0, float(f_num) * float(sec_num))

                    buttonproceed_mass = Button(top_distance_time, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonproceedfinal_resultdistance)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_distance_velocity, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_distance_velocity)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_velocity_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_velocity_input.get() == 'v' or entry_velocity_input.get() == 'V':
                top_velocity_distance = Toplevel()
                top_velocity_distance.configure(background='gray38')
                top_velocity_distance.title('Velocity__ distance')

                labelText = DoubleVar()
                labelText.set("Enter the desired distance (meters):                                       ")
                labelDir = Label(top_velocity_distance, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_velocity_distance, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_velocity_distance.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_velocity_distance = Entry(top_velocity_distance, fg="#00FF00", bg="black", width=50,
                                                borderwidth=30)
                entry_velocity_distance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_velocity_distance():
                    first_num_distance = entry_velocity_distance.get()
                    f_num = first_num_distance

                    top_velocity_time = Toplevel()
                    top_velocity_time.configure(background='gray38')
                    top_velocity_time.title('Velocity__ time')

                    labelText = DoubleVar()
                    labelText.set("Enter the desired time (seconds):                                            ")
                    labelDir = Label(top_velocity_time, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_velocity_time, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_velocity_time.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_velocity_time = Entry(top_velocity_time, fg="#00FF00", bg="black", width=50,
                                                borderwidth=30)
                    entry_velocity_time.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceedfinal_resultacceleration():
                        sec_num_time = entry_velocity_time.get()
                        sec_num = sec_num_time

                        top_result_velocity = Toplevel()
                        top_result_velocity.configure(background='gray38')
                        top_result_velocity.title('Velocity__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (m/s²):                                                                        ")
                        labelDir = Label(top_result_velocity, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_velocity, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_velocity.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_velocity_result = Entry(top_result_velocity, font=('Times New Roman', 15),
                                                      fg="#00FF00", bg="black", width=50,
                                                      borderwidth=30)
                        entry_velocity_result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_velocity_result.insert(0, float(f_num) / float(sec_num))

                    buttonproceed_mass = Button(top_velocity_time, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonproceedfinal_resultacceleration)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_velocity_distance, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_velocity_distance)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_velocity_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_velocity_input.get() == 'T' or entry_velocity_input.get() == 't':
                top_time_distance = Toplevel()
                top_time_distance.configure(background='gray38')
                top_time_distance.title('Force_ acceleration')

                labelText = DoubleVar()
                labelText.set("Enter the desired acceleration (m/s²):                                       ")
                labelDir = Label(top_time_distance, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_time_distance, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_time_distance.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_time_distance = Entry(top_time_distance, fg="#00FF00", bg="black", width=50,
                                            borderwidth=30)
                entry_time_distance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_time_distance():
                    first_num_distance = entry_time_distance.get()
                    f_num = first_num_distance

                    top_time_velocity = Toplevel()
                    top_time_velocity.configure(background='gray38')
                    top_time_velocity.title('Time__ velocity')

                    ###########Label close for force_mass##########
                    labelText = DoubleVar()
                    labelText.set("Enter the desired velocity (m/s):                                            ")
                    labelDir = Label(top_time_velocity, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_time_velocity, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_time_velocity.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_time_velocity = Entry(top_time_velocity, fg="#00FF00", bg="black", width=50, borderwidth=30)
                    entry_time_velocity.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceedfinal_resulttime():
                        sec_num_velocity = entry_time_velocity.get()
                        sec_num = sec_num_velocity

                        top_result_time = Toplevel()
                        top_result_time.configure(background='gray38')
                        top_result_time.title('Time__ result')

                        ###########Label close for force_mass##########
                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (seconds):                                                                        ")
                        labelDir = Label(top_result_time, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_time, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_time.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_time_result = Entry(top_result_time, font=('Times New Roman', 15),
                                                  fg="#00FF00", bg="black", width=50,
                                                  borderwidth=30)
                        entry_time_result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_time_result.insert(0, float(f_num) * float(sec_num))

                    buttonproceed_mass = Button(top_time_velocity, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonproceedfinal_resulttime)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_time_distance, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_time_distance)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

        buttonproceed_input = Button(top_velocity_input, text='Continue', padx=90, pady=20,
                                     font=('Times New Roman', 10),
                                     command=button_proceed1)
        buttonproceed_input.grid(row=3, column=0, columnspan=3)

###################################################Define velocity from wave################################################

    def buttonvelocityfromwave():
        global f_num
        global sec_num
        global first_value

        top_fvelocity_input = Toplevel()
        top_fvelocity_input.configure(background='gray38')
        top_fvelocity_input.title('Velocity waves input')

        labelText = StringVar()
        labelText.set("      Dear user, which variable of the equation would you like to calculate ?\nVelocity (v), frequency (f), wavelength (w) ? ")
        labelDir = Label(top_fvelocity_input, textvariable=labelText,
                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
        labelDir.grid(row=0, column=0)

        def popup_of_fvelocity():
            answer = messagebox.showinfo('Popup', 'You exited "Velocity" section')
            if answer:
                top_fvelocity_input.destroy()

        btnclose = Button(top_fvelocity_input, text='Close Window', font=('Times New Roman', 12),
                          bg='indian red', fg='black', command=popup_of_fvelocity)
        btnclose.grid(row=5, column=0, columnspan=3)

        ########Entry for force_mass##############
        entry_fvelocity_input = Entry(top_fvelocity_input, fg="#00FF00", bg="black", width=50, borderwidth=30)
        entry_fvelocity_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        def button_proceed1():
            global first_value
            first_choice = entry_fvelocity_input.get()
            first_value = str(first_choice)

            if entry_fvelocity_input.get() == 'w' or entry_fvelocity_input.get() == 'W':
                top_wavelength_frequency = Toplevel()
                top_wavelength_frequency.configure(background='gray38')
                top_wavelength_frequency.title('Wavelength__ frequency')

                labelText = DoubleVar()
                labelText.set("Enter the desired frequency magnitude (Hertz):                                       ")
                labelDir = Label(top_wavelength_frequency, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_wavelength_frequency, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_wavelength_frequency.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                entry_wavelength_frequency = Entry(top_wavelength_frequency, fg="#00FF00", bg="black", width=50,
                                                   borderwidth=30)
                entry_wavelength_frequency.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def proceed_wavelength_frequency():
                    first_num = entry_wavelength_frequency.get()
                    f_num = first_num

                    top_wavelength_velocity = Toplevel()
                    top_wavelength_velocity.configure(background='gray38')
                    top_wavelength_velocity.title('Wavelength__ velocity')

                    labelText = DoubleVar()
                    labelText.set("Enter the velocity magnitude (m/s):                                            ")
                    labelDir = Label(top_wavelength_velocity, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_wavelength_velocity, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_wavelength_velocity.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_wavelength_velocity = Entry(top_wavelength_velocity, fg="#00FF00", bg="black", width=50,
                                                      borderwidth=30)
                    entry_wavelength_velocity.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonresult_power():
                        sec_num = entry_wavelength_velocity.get()
                        sec_num = sec_num

                        top_result_wavelength = Toplevel()
                        top_result_wavelength.configure(background='gray38')
                        top_result_wavelength.title('Wavelength__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (meters):                                                                        ")
                        labelDir = Label(top_result_wavelength, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_wavelength, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_wavelength.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_power = Entry(top_result_wavelength, font=('Times New Roman', 15),
                                                   fg="#00FF00", bg="black", width=50,
                                                   borderwidth=30)
                        entry_result_power.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_power.insert(0, float(f_num) / float(sec_num))

                    buttonproceed3 = Button(top_wavelength_velocity, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=buttonresult_power)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_wavelength_frequency, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=proceed_wavelength_frequency)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_fvelocity_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_fvelocity_input.get() == 'f' or entry_fvelocity_input.get() == 'F':
                top_frequency_velocity = Toplevel()
                top_frequency_velocity.configure(background='gray38')
                top_frequency_velocity.title('Frequency__ velocity')

                labelText = DoubleVar()
                labelText.set("Enter the desired velocity magnitude (m/s):                                       ")
                labelDir = Label(top_frequency_velocity, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_frequency_velocity, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_frequency_velocity.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_frequency_velocity = Entry(top_frequency_velocity, fg="#00FF00", bg="black", width=50,
                                                 borderwidth=30)
                entry_frequency_velocity.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_fvelocity():
                    first_num = entry_frequency_velocity.get()
                    f_num = first_num

                    top_frequency_wavelength = Toplevel()
                    top_frequency_wavelength.configure(background='gray38')
                    top_frequency_wavelength.title('Frequency__ wavelength')

                    labelText = DoubleVar()
                    labelText.set("Enter the wavelength (meters):                                            ")
                    labelDir = Label(top_frequency_wavelength, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_frequency_wavelength, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_frequency_wavelength.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_frequency_wavelength = Entry(top_frequency_wavelength, fg="#00FF00", bg="black", width=50,
                                                       borderwidth=30)
                    entry_frequency_wavelength.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonresult_power():
                        sec_num = entry_frequency_wavelength.get()
                        sec_num = sec_num

                        top_result_frequency = Toplevel()
                        top_result_frequency.configure(background='gray38')
                        top_result_frequency.title('Frequency__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (Hertz):                                                                        ")
                        labelDir = Label(top_result_frequency, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_frequency, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_frequency.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_frequency = Entry(top_result_frequency, font=('Times New Roman', 15),
                                                       fg="#00FF00", bg="black", width=50,
                                                       borderwidth=30)
                        entry_result_frequency.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_frequency.insert(0, float(f_num) * float(sec_num))

                    buttonproceed3 = Button(top_frequency_wavelength, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=buttonresult_power)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_frequency_velocity, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed_fvelocity)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_fvelocity_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_fvelocity_input.get() == 'V' or entry_fvelocity_input.get() == 'v':
                top_fvelocity_frequency = Toplevel()
                top_fvelocity_frequency.configure(background='gray38')
                top_fvelocity_frequency.title('Velocity__ frequency')

                labelText = DoubleVar()
                labelText.set("Enter the frequency magnitude (Hertz):                                       ")
                labelDir = Label(top_fvelocity_frequency, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_fvelocity_frequency, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_fvelocity_frequency.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_velocity_frequency = Entry(top_fvelocity_frequency, fg="#00FF00", bg="black", width=50,
                                                 borderwidth=30)
                entry_velocity_frequency.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_velocity_frequency():
                    first_num_distance = entry_velocity_frequency.get()
                    f_num = first_num_distance

                    top_velocity_wavelength = Toplevel()
                    top_velocity_wavelength.configure(background='gray38')
                    top_velocity_wavelength.title('Velocity__ wavelength')

                    ###########Label close for force_mass##########
                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired wavelegth magnitude (meters):                                            ")
                    labelDir = Label(top_velocity_wavelength, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_velocity_wavelength, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_velocity_wavelength.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_velocity_wavelength = Entry(top_velocity_wavelength, fg="#00FF00", bg="black", width=50,
                                                      borderwidth=30)
                    entry_velocity_wavelength.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonresult_velocity():
                        sec_number = entry_velocity_wavelength.get()
                        sec_num = sec_number

                        top_result_velocity = Toplevel()
                        top_result_velocity.configure(background='gray38')
                        top_result_velocity.title('Velocity__ result')

                        ###########Label close for force_mass##########
                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (m/s):                                                                        ")
                        labelDir = Label(top_result_velocity, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_velocity, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_velocity.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_fvelocity_result = Entry(top_result_velocity, font=('Times New Roman', 15),
                                                       fg="#00FF00", bg="black", width=50,
                                                       borderwidth=30)
                        entry_fvelocity_result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_fvelocity_result.insert(0, float(f_num) / float(sec_num))

                    buttonproceed3 = Button(top_velocity_wavelength, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=buttonresult_velocity)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_fvelocity_frequency, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed_velocity_frequency)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

        buttonproceed_input = Button(top_fvelocity_input, text='Continue', padx=90, pady=20,
                                     font=('Times New Roman', 10),
                                     command=button_proceed1)
        buttonproceed_input.grid(row=3, column=0, columnspan=3)

###################################################Define energy#############################################################

    def button_energy():
        global f_num
        global sec_num
        global first_value

        top_energy_input = Toplevel()
        top_energy_input.configure(background='gray38')
        top_energy_input.title('Energy input')

        labelText = StringVar()
        labelText.set("      Dear user, which variable of the equation would you like to calculate ? (c is constant)\nEnergy (E), or mass (m) ?")
        labelDir = Label(top_energy_input, textvariable=labelText,
                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
        labelDir.grid(row=0, column=0)

        def popup_of_energy():
            answer = messagebox.showinfo('Popup', 'You exited "Energy" section')
            if answer:
                top_energy_input.destroy()

        btnclose = Button(top_energy_input, text='Close Window', font=('Times New Roman', 12),
                          bg='indian red', fg='black', command=popup_of_energy())
        btnclose.grid(row=5, column=0, columnspan=3)

        ########Entry for force_mass##############
        entry_energy_input = Entry(top_energy_input, fg="#00FF00", bg="black", width=50, borderwidth=30)
        entry_energy_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        def button_proceed1():
            global first_value
            first_choice = entry_energy_input.get()
            first_value = str(first_choice)

            if entry_energy_input.get() == 'E' or entry_energy_input.get() == 'e':
                top_energy_mass = Toplevel()
                top_energy_mass.configure(background='gray38')
                top_energy_mass.title('Energy__ mass')

                labelText = DoubleVar()
                labelText.set("Enter the desired mass (kg):                                       ")
                labelDir = Label(top_energy_mass, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_energy_mass, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_energy_mass.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                entry_energy_mass = Entry(top_energy_mass, fg="#00FF00", bg="black", width=50,
                                          borderwidth=30)
                entry_energy_mass.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_energy_mass():
                    first_num = entry_energy_mass.get()
                    f_num = first_num

                    top_energy_lightspeed = Toplevel()
                    top_energy_lightspeed.configure(background='gray38')
                    top_energy_lightspeed.title('Distance__ time')

                    labelText = DoubleVar()
                    labelText.set("Enter the desired speed of light (m/s):                                            ")
                    labelDir = Label(top_energy_lightspeed, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_energy_lightspeed, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_energy_lightspeed.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_energy_lightspeed = Entry(top_energy_lightspeed, fg="#00FF00", bg="black", width=50,
                                                    borderwidth=30)
                    entry_energy_lightspeed.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonresult_energy():
                        sec_num = entry_energy_lightspeed.get()
                        sec_num = sec_num

                        top_result_energy = Toplevel()
                        top_result_energy.configure(background='gray38')
                        top_result_energy.title('Energy__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (joules):                                                                        ")
                        labelDir = Label(top_result_energy, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_energy, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_energy.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_energy = Entry(top_result_energy, font=('Times New Roman', 15),
                                                    fg="#00FF00", bg="black", width=50,
                                                    borderwidth=30)
                        entry_result_energy.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_energy.insert(0, float(f_num) * (float(sec_num) ** 2))

                    buttonproceed_mass = Button(top_energy_lightspeed, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonresult_energy)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_energy_mass, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_energy_mass)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_energy_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_energy_input.get() == 'm' or entry_energy_input.get() == 'M':
                top_mass_energy = Toplevel()
                top_mass_energy.configure(background='gray38')
                top_mass_energy.title('Velocity__ distance')

                labelText = DoubleVar()
                labelText.set("Enter the desired energy magnitude (joules):                                       ")
                labelDir = Label(top_mass_energy, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_mass_energy, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_mass_energy.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_mass_energy = Entry(top_mass_energy, fg="#00FF00", bg="black", width=50,
                                          borderwidth=30)
                entry_mass_energy.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_mass_energy():
                    first_num = entry_mass_energy.get()
                    f_num = first_num

                    top_mass_lightspeed = Toplevel()
                    top_mass_lightspeed.configure(background='gray38')
                    top_mass_lightspeed.title('Mass__ light-speed')

                    labelText = DoubleVar()
                    labelText.set("Enter the desired light speed (m/s):                                            ")
                    labelDir = Label(top_mass_lightspeed, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_mass_lightspeed, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_mass_lightspeed.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_mass_lightspeed = Entry(top_mass_lightspeed, fg="#00FF00", bg="black", width=50,
                                                  borderwidth=30)
                    entry_mass_lightspeed.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonresult_mass():
                        sec_num = entry_mass_lightspeed.get()
                        sec_num = sec_num

                        top_result_mass = Toplevel()
                        top_result_mass.configure(background='gray38')
                        top_result_mass.title('Mass__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (kg):                                                                        ")
                        labelDir = Label(top_result_mass, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_mass, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_mass.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_mass = Entry(top_result_mass, font=('Times New Roman', 15),
                                                  fg="#00FF00", bg="black", width=50,
                                                  borderwidth=30)
                        entry_result_mass.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_mass.insert(0, float(f_num) / (float(sec_num) ** 2))

                    buttonproceed_mass = Button(top_mass_lightspeed, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonresult_mass)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_mass_energy, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_mass_energy)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_energy_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_energy_input.get() == 'T' or entry_energy_input.get() == 't':
                top_time_distance = Toplevel()
                top_time_distance.configure(background='gray38')
                top_time_distance.title('Error')

                labelText = DoubleVar()
                labelText.set("                      Invalid input!                      ")
                labelDir = Label(top_time_distance, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_time_distance, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_time_distance.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_time_distance = Entry(top_time_distance, fg="#00FF00", bg="black", width=50,
                                            borderwidth=30)
                entry_time_distance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed_time_distance():
                    first_num_distance = entry_time_distance.get()
                    f_num = first_num_distance

                    top_time_velocity = Toplevel()
                    top_time_velocity.configure(background='gray38')
                    top_time_velocity.title('Error__')

                    ###########Label close for force_mass##########
                    labelText = DoubleVar()
                    labelText.set("                      Invalid input!                      ")
                    labelDir = Label(top_time_velocity, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_time_velocity, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_time_velocity.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_time_velocity = Entry(top_time_velocity, fg="#00FF00", bg="black", width=50, borderwidth=30)
                    entry_time_velocity.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceedfinal_resulttime():
                        sec_number = entry_time_velocity.get()
                        sec_num = sec_number

                        top_result_time = Toplevel()
                        top_result_time.configure(background='gray38')
                        top_result_time.title('Error__')

                        ###########Label close for force_mass##########
                        labelText = DoubleVar()
                        labelText.set("                      Invalid input!                      ")
                        labelDir = Label(top_result_time, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_time, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_time.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_time_result = Entry(top_result_time, font=('Times New Roman', 15),
                                                  fg="#00FF00", bg="black", width=50,
                                                  borderwidth=30)
                        entry_time_result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_time_result.insert(0, 'Error 404')

                    buttonproceed_mass = Button(top_time_velocity, text='Show result', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=buttonproceedfinal_resulttime)
                    buttonproceed_mass.grid(row=3, column=0, columnspan=3)

                buttonproceed_acceleration = Button(top_time_distance, text='Continue', padx=90, pady=20,
                                                    font=('Times New Roman', 10),
                                                    command=buttonproceed_time_distance)
                buttonproceed_acceleration.grid(row=3, column=0, columnspan=3)

        buttonproceed_input = Button(top_energy_input, text='Continue', padx=90, pady=20,
                                     font=('Times New Roman', 10),
                                     command=button_proceed1)
        buttonproceed_input.grid(row=3, column=0, columnspan=3)

    def button_voltage():
        global f_num
        global sec_num
        global first_value

        top_voltage_input = Toplevel()
        top_voltage_input.configure(background='gray38')
        top_voltage_input.title('Voltage input')

        labelText = StringVar()
        labelText.set("      Dear user, which variable of the equation would you like to calculate ?\nVoltage (V), current (I), resistance (R) ? ")
        labelDir = Label(top_voltage_input, textvariable=labelText,
                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
        labelDir.grid(row=0, column=0)

        def popup_of_voltage():
            answer = messagebox.showinfo('Popup', 'You exited "Voltage" section')
            if answer:
                top_voltage_input.destroy()

        btnclose = Button(top_voltage_input, text='Close Window', font=('Times New Roman', 12),
                          bg='indian red', fg='black', command=popup_of_voltage)
        btnclose.grid(row=5, column=0, columnspan=3)

        ########Entry for force_mass##############
        entry_voltage_input = Entry(top_voltage_input, fg="#00FF00", bg="black", width=50, borderwidth=30)
        entry_voltage_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        def button_proceed1():
            global first_value
            first_choice = entry_voltage_input.get()
            first_value = str(first_choice)

            if entry_voltage_input.get() == 'R' or entry_voltage_input.get() == 'r':
                top_resistance_voltage = Toplevel()
                top_resistance_voltage.configure(background='gray38')
                top_resistance_voltage.title('Resistance__ voltage')

                labelText = DoubleVar()
                labelText.set("Enter the desired voltage magnitude (volts):                                       ")
                labelDir = Label(top_resistance_voltage, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_resistance_voltage, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_resistance_voltage.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                entry_resistance_voltage = Entry(top_resistance_voltage, fg="#00FF00", bg="black", width=50,
                                                 borderwidth=30)
                entry_resistance_voltage.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed2():
                    first_num = entry_resistance_voltage.get()
                    f_num = first_num

                    top_resistance_current = Toplevel()
                    top_resistance_current.configure(background='gray38')
                    top_resistance_current.title('Resistance__ current')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired current magnitude (ampere):                                            ")
                    labelDir = Label(top_resistance_current, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_resistance_current, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_resistance_current.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_resistance_current = Entry(top_resistance_current, fg="#00FF00", bg="black", width=50,
                                                     borderwidth=30)
                    entry_resistance_current.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def button3():
                        sec_num = entry_resistance_current.get()
                        sec_num = sec_num

                        top_result_resistance = Toplevel()
                        top_result_resistance.configure(background='gray38')
                        top_result_resistance.title('Resistance__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (ohm):                                                                        ")
                        labelDir = Label(top_result_resistance, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_resistance, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_resistance.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_resistance = Entry(top_result_resistance, font=('Times New Roman', 15),
                                                        fg="#00FF00", bg="black", width=50,
                                                        borderwidth=30)
                        entry_result_resistance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_resistance.insert(0, float(f_num) / (float(sec_num)))

                    buttonproceed3 = Button(top_resistance_current, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=button3)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_resistance_voltage, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed2)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_voltage_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_voltage_input.get() == 'I' or entry_voltage_input.get() == 'i':
                top_current_voltage = Toplevel()
                top_current_voltage.configure(background='gray38')
                top_current_voltage.title('Current__ voltage')

                labelText = DoubleVar()
                labelText.set("Enter the desired voltage magnitude (volts):                                       ")
                labelDir = Label(top_current_voltage, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_current_voltage, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_current_voltage.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_current_voltage = Entry(top_current_voltage, fg="#00FF00", bg="black", width=50,
                                              borderwidth=30)
                entry_current_voltage.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed2():
                    first_num = entry_current_voltage.get()
                    f_num = first_num

                    top_current_resistance = Toplevel()
                    top_current_resistance.configure(background='gray38')
                    top_current_resistance.title('Current__ resistance')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired resistance magnitude (ohm):                                            ")
                    labelDir = Label(top_current_resistance, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_current_resistance, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_current_resistance.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_current_resistance = Entry(top_current_resistance, fg="#00FF00", bg="black", width=50,
                                                     borderwidth=30)
                    entry_current_resistance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceed3():
                        sec_num = entry_current_resistance.get()
                        sec_num = sec_num

                        top_result_current = Toplevel()
                        top_result_current.configure(background='gray38')
                        top_result_current.title('Current__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (ampere):                                                                        ")
                        labelDir = Label(top_result_current, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_current, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_current.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_current = Entry(top_result_current, font=('Times New Roman', 15),
                                                     fg="#00FF00", bg="black", width=50,
                                                     borderwidth=30)
                        entry_result_current.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_current.insert(0, float(f_num) / float(sec_num))

                    buttonproceed3 = Button(top_current_resistance, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=buttonproceed3)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_current_voltage, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed2)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_voltage_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_voltage_input.get() == 'V' or entry_voltage_input.get() == 'v':
                top_voltage_current = Toplevel()
                top_voltage_current.configure(background='gray38')
                top_voltage_current.title('Voltage__ current')

                labelText = DoubleVar()
                labelText.set(" Enter the desired current magnitude (ampere):                                     ")
                labelDir = Label(top_voltage_current, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_voltage_current, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_voltage_current.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_voltage_current = Entry(top_voltage_current, fg="#00FF00", bg="black", width=50,
                                              borderwidth=30)
                entry_voltage_current.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed2():
                    first_num_current = entry_voltage_current.get()
                    f_num = first_num_current

                    top_voltage_resistance = Toplevel()
                    top_voltage_resistance.configure(background='gray38')
                    top_voltage_resistance.title('Voltage__ resistance')

                    ###########Label close for force_mass##########
                    labelText = DoubleVar()
                    labelText.set(" Enter the desired resistance magnitude (ohm):                          ")
                    labelDir = Label(top_voltage_resistance, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_voltage_resistance, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_voltage_resistance.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_voltage_resistance = Entry(top_voltage_resistance, fg="#00FF00", bg="black", width=50,
                                                     borderwidth=30)
                    entry_voltage_resistance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceed_result_voltage():
                        sec_number = entry_voltage_resistance.get()
                        sec_num = sec_number

                        top_result_voltage = Toplevel()
                        top_result_voltage.configure(background='gray38')
                        top_result_voltage.title('Voltage__ result')

                        ###########Label close for force_mass##########
                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (volts):                                                                        ")
                        labelDir = Label(top_result_voltage, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_voltage, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_voltage.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_voltage_result = Entry(top_result_voltage, font=('Times New Roman', 15),
                                                     fg="#00FF00", bg="black", width=50,
                                                     borderwidth=30)
                        entry_voltage_result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_voltage_result.insert(0, float(f_num) * float(sec_num))

                    buttonproceed3 = Button(top_voltage_resistance, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=buttonproceed_result_voltage)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_voltage_current, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed2)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

        buttonproceed_input = Button(top_voltage_input, text='Continue', padx=90, pady=20,
                                     font=('Times New Roman', 10),
                                     command=button_proceed1)
        buttonproceed_input.grid(row=3, column=0, columnspan=3)

    def button_charge():
        global f_num
        global sec_num
        global first_value

        top_charge_input = Toplevel()
        top_charge_input.configure(background='gray38')
        top_charge_input.title('Charge input')

        labelText = StringVar()
        labelText.set("      Dear user, which variable of the equation would you like to calculate ?\nCharge (Q), current (I), or time (t)")
        labelDir = Label(top_charge_input, textvariable=labelText,
                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
        labelDir.grid(row=0, column=0)

        def popup_of_charge():
            answer = messagebox.showinfo('Popup', 'You exited "Charge" section')
            if answer:
                top_charge_input.destroy()

        btnclose = Button(top_charge_input, text='Close Window', font=('Times New Roman', 12),
                          bg='indian red', fg='black', command=popup_of_charge)
        btnclose.grid(row=5, column=0, columnspan=3)

        ########Entry for force_mass##############
        entry_voltage_input = Entry(top_charge_input, fg="#00FF00", bg="black", width=50, borderwidth=30)
        entry_voltage_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        def button_proceed1():
            global first_value
            first_choice = entry_voltage_input.get()
            first_value = str(first_choice)

            if entry_voltage_input.get() == 'I' or entry_voltage_input.get() == 'i':
                top_current_charge = Toplevel()
                top_current_charge.configure(background='gray38')
                top_current_charge.title('Current__ charge')

                labelText = DoubleVar()
                labelText.set("Enter the desired charge magnitude (coulombs):                                       ")
                labelDir = Label(top_current_charge, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_current_charge, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_current_charge.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                entry_current_charge = Entry(top_current_charge, fg="#00FF00", bg="black", width=50,
                                             borderwidth=30)
                entry_current_charge.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed2():
                    first_num = entry_current_charge.get()
                    f_num = first_num

                    top_current_time = Toplevel()
                    top_current_time.configure(background='gray38')
                    top_current_time.title('Current__ time')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired time magnitude (seconds):                                            ")
                    labelDir = Label(top_current_time, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_current_time, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_current_time.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_current_time = Entry(top_current_time, fg="#00FF00", bg="black", width=50,
                                               borderwidth=30)
                    entry_current_time.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def button3():
                        sec_num = entry_current_time.get()
                        sec_num = sec_num

                        top_result_current = Toplevel()
                        top_result_current.configure(background='gray38')
                        top_result_current.title('Current__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (ampere):                                                                        ")
                        labelDir = Label(top_result_current, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_current, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_current.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_current = Entry(top_result_current, font=('Times New Roman', 15),
                                                     fg="#00FF00", bg="black", width=50,
                                                     borderwidth=30)
                        entry_result_current.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_current.insert(0, float(f_num) / float(sec_num))

                    buttonproceed3 = Button(top_current_time, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=button3)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_current_charge, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed2)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_charge_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_voltage_input.get() == 't' or entry_voltage_input.get() == 'T':
                top_time_charge = Toplevel()
                top_time_charge.configure(background='gray38')
                top_time_charge.title('Time__ charge')

                labelText = DoubleVar()
                labelText.set("Enter the desired charge magnitude (coulombs):                                       ")
                labelDir = Label(top_time_charge, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_time_charge, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_time_charge.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_time_charge = Entry(top_time_charge, fg="#00FF00", bg="black", width=50,
                                          borderwidth=30)
                entry_time_charge.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed2():
                    first_num = entry_time_charge.get()
                    f_num = first_num

                    top_time_current = Toplevel()
                    top_time_current.configure(background='gray38')
                    top_time_current.title('Time__ current')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired current magnitude (ampere):                                            ")
                    labelDir = Label(top_time_current, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_time_current, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_time_current.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_time_current = Entry(top_time_current, fg="#00FF00", bg="black", width=50,
                                               borderwidth=30)
                    entry_time_current.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceed3():
                        sec_num = entry_time_current.get()
                        sec_num = sec_num

                        top_result_time = Toplevel()
                        top_result_time.configure(background='gray38')
                        top_result_time.title('Time__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (seconds):                                                                        ")
                        labelDir = Label(top_result_time, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_time, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_time.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_time = Entry(top_result_time, font=('Times New Roman', 15),
                                                  fg="#00FF00", bg="black", width=50,
                                                  borderwidth=30)
                        entry_result_time.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_time.insert(0, float(f_num) / float(sec_num))

                    buttonproceed3 = Button(top_time_current, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=buttonproceed3)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_time_charge, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed2)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_charge_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_voltage_input.get() == 'q' or entry_voltage_input.get() == 'Q':
                top_charge_current = Toplevel()
                top_charge_current.configure(background='gray38')
                top_charge_current.title('Charge__ current')

                labelText = DoubleVar()
                labelText.set(" Enter the desired current magnitude (ampere):                                     ")
                labelDir = Label(top_charge_current, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_charge_current, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_charge_current.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_charge_current = Entry(top_charge_current, fg="#00FF00", bg="black", width=50,
                                             borderwidth=30)
                entry_charge_current.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed2():
                    first_num_current = entry_charge_current.get()
                    f_num = first_num_current

                    top_charge_time = Toplevel()
                    top_charge_time.configure(background='gray38')
                    top_charge_time.title('Charge__ time')

                    ###########Label close for force_mass##########
                    labelText = DoubleVar()
                    labelText.set(" Enter the desired time magnitude (seconds):                          ")
                    labelDir = Label(top_charge_time, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_charge_time, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_charge_time.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_charge_time = Entry(top_charge_time, fg="#00FF00", bg="black", width=50, borderwidth=30)
                    entry_charge_time.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def result_charge():
                        sec_number = entry_charge_time.get()
                        sec_num = sec_number

                        top_result_charge = Toplevel()
                        top_result_charge.configure(background='gray38')
                        top_result_charge.title('Charge__ result')

                        ###########Label close for force_mass##########
                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (coloumbs):                                                                        ")
                        labelDir = Label(top_result_charge, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_charge, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_charge.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_charge = Entry(top_result_charge, font=('Times New Roman', 15),
                                                    fg="#00FF00", bg="black", width=50,
                                                    borderwidth=30)
                        entry_result_charge.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_charge.insert(0, float(f_num) * float(sec_num))

                    buttonproceed3 = Button(top_charge_time, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=result_charge)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_charge_current, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed2)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

        buttonproceed_input = Button(top_charge_input, text='Continue', padx=90, pady=20,
                                     font=('Times New Roman', 10),
                                     command=button_proceed1)
        buttonproceed_input.grid(row=3, column=0, columnspan=3)

    def button_tension():
        global f_num
        global sec_num
        global first_value

        top_tension_input = Toplevel()
        top_tension_input.configure(background='gray38')
        top_tension_input.title('Tension input')

        labelText = StringVar()
        labelText.set("      Dear user, which variable of the equation would you like to calculate ?\nTension (T), stiffness (k), or elongation (x) ?")
        labelDir = Label(top_tension_input, textvariable=labelText,
                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
        labelDir.grid(row=0, column=0)

        def popup_of_tension():
            answer = messagebox.showinfo('Popup', 'You exited "Tension" section')
            if answer:
                top_tension_input.destroy()

        btnclose = Button(top_tension_input, text='Close Window', font=('Times New Roman', 12),
                          bg='indian red', fg='black', command=popup_of_tension)
        btnclose.grid(row=5, column=0, columnspan=3)

        ########Entry for force_mass##############
        entry_tension_input = Entry(top_tension_input, fg="#00FF00", bg="black", width=50, borderwidth=30)
        entry_tension_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        def button_proceed1():
            global first_value
            first_choice = entry_tension_input.get()
            first_value = str(first_choice)

            if entry_tension_input.get() == 'x' or entry_tension_input.get() == 'X':
                top_elong_tension = Toplevel()
                top_elong_tension.configure(background='gray38')
                top_elong_tension.title('Elongation__ tension')

                labelText = DoubleVar()
                labelText.set("Enter the desired tension magnitude (Newtons):                                       ")
                labelDir = Label(top_elong_tension, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_elong_tension, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_elong_tension.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                entry_elong_tension = Entry(top_elong_tension, fg="#00FF00", bg="black", width=50,
                                            borderwidth=30)
                entry_elong_tension.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed2():
                    first_num = entry_elong_tension.get()
                    f_num = first_num

                    top_elong_stiffness = Toplevel()
                    top_elong_stiffness.configure(background='gray38')
                    top_elong_stiffness.title('Elongation__ stiffness')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired stiffness magnitude (N/m):                                            ")
                    labelDir = Label(top_elong_stiffness, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_elong_stiffness, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_elong_stiffness.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_elong_stiffness = Entry(top_elong_stiffness, fg="#00FF00", bg="black", width=50,
                                                  borderwidth=30)
                    entry_elong_stiffness.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def button3():
                        sec_num = entry_elong_stiffness.get()
                        sec_num = sec_num

                        top_result_elong = Toplevel()
                        top_result_elong.configure(background='gray38')
                        top_result_elong.title('Elongation__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (meters):                                                                        ")
                        labelDir = Label(top_result_elong, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_elong, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_elong.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_elongation = Entry(top_result_elong, font=('Times New Roman', 15),
                                                        fg="#00FF00", bg="black", width=50,
                                                        borderwidth=30)
                        entry_result_elongation.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_elongation.insert(0, float(f_num) / float(sec_num))

                    buttonproceed3 = Button(top_elong_stiffness, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=button3)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_elong_tension, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed2)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_tension_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_tension_input.get() == 'k' or entry_tension_input.get() == 'K':
                top_stiffness_tension = Toplevel()
                top_stiffness_tension.configure(background='gray38')
                top_stiffness_tension.title('Stiffness__ tension')

                labelText = DoubleVar()
                labelText.set("Enter the desired tension magnitude (Newtons):                                       ")
                labelDir = Label(top_stiffness_tension, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_stiffness_tension, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_stiffness_tension.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_stiffness_tension = Entry(top_stiffness_tension, fg="#00FF00", bg="black", width=50,
                                                borderwidth=30)
                entry_stiffness_tension.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed2():
                    first_num = entry_stiffness_tension.get()
                    f_num = first_num

                    top_stiffness_elong = Toplevel()
                    top_stiffness_elong.configure(background='gray38')
                    top_stiffness_elong.title('Stiffness__ elongation')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired elongation magnitude (meters):                                            ")
                    labelDir = Label(top_stiffness_elong, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_stiffness_elong, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_stiffness_elong.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_stiffness_elongation = Entry(top_stiffness_elong, fg="#00FF00", bg="black", width=50,
                                                       borderwidth=30)
                    entry_stiffness_elongation.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def buttonproceed3():
                        sec_num = entry_stiffness_elongation.get()
                        sec_num = sec_num

                        top_result_stiffness = Toplevel()
                        top_result_stiffness.configure(background='gray38')
                        top_result_stiffness.title('Stiffness__ result')

                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (N/m):                                                                        ")
                        labelDir = Label(top_result_stiffness, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_stiffness, text='Close Window',
                                          font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_stiffness.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_stiffness = Entry(top_result_stiffness, font=('Times New Roman', 15),
                                                       fg="#00FF00", bg="black", width=50,
                                                       borderwidth=30)
                        entry_result_stiffness.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_stiffness.insert(0, float(f_num) / float(sec_num))

                    buttonproceed3 = Button(top_stiffness_elong, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=buttonproceed3)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_stiffness_tension, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed2)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_tension_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button_proceed1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

            #############################################################################################################################
            #############################################################################################################################
            #############################################################################################################################

            if entry_tension_input.get() == 'T' or entry_tension_input.get() == 't':
                top_tension_stiffness = Toplevel()
                top_tension_stiffness.configure(background='gray38')
                top_tension_stiffness.title('Tension__ stiffness')

                labelText = DoubleVar()
                labelText.set(
                    " Enter the desired stiffness magnitude (N/m) *spring constant:                                     ")
                labelDir = Label(top_tension_stiffness, textvariable=labelText,
                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                labelDir.grid(row=0, column=0)

                btnclose = Button(top_tension_stiffness, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                  bg='gray38', fg='white', command=top_tension_stiffness.destroy)
                btnclose.grid(row=5, column=0, columnspan=3)

                ########Entry for force_mass##############
                entry_tension_stiffness = Entry(top_tension_stiffness, fg="#00FF00", bg="black", width=50,
                                                borderwidth=30)
                entry_tension_stiffness.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                def buttonproceed2():
                    first_num_current = entry_tension_stiffness.get()
                    f_num = first_num_current

                    top_tension_elong = Toplevel()
                    top_tension_elong.configure(background='gray38')
                    top_tension_elong.title('Tension__ elongation')

                    ###########Label close for force_mass##########
                    labelText = DoubleVar()
                    labelText.set(" Enter the desired elongation magnitude (meters):                          ")
                    labelDir = Label(top_tension_elong, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_tension_elong, text='Close Window', font=('Times New Roman', 15),
                                      bg='gray38', fg='white', command=top_tension_elong.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_tension_elong = Entry(top_tension_elong, fg="#00FF00", bg="black", width=50, borderwidth=30)
                    entry_tension_elong.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def result_charge():
                        sec_number = entry_tension_elong.get()
                        sec_num = sec_number

                        top_result_tension = Toplevel()
                        top_result_tension.configure(background='gray38')
                        top_result_tension.title('Tension__ result')

                        ###########Label close for force_mass##########
                        labelText = DoubleVar()
                        labelText.set(
                            "Your result is (Newtons):                                                                        ")
                        labelDir = Label(top_result_tension, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        ###########Button close for force_mass##########
                        btnclose = Button(top_result_tension, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                          bg='gray38', fg='white', command=top_result_tension.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        ########Entry for force_mass##############
                        entry_result_tension = Entry(top_result_tension, font=('Times New Roman', 15),
                                                     fg="#00FF00", bg="black", width=50,
                                                     borderwidth=30)
                        entry_result_tension.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
                        entry_result_tension.insert(0, float(f_num) * float(sec_num))

                    buttonproceed3 = Button(top_tension_elong, text='Show result', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=result_charge)
                    buttonproceed3.grid(row=3, column=0, columnspan=3)

                buttonproceed2 = Button(top_tension_stiffness, text='Continue', padx=90, pady=20,
                                        font=('Times New Roman', 10),
                                        command=buttonproceed2)
                buttonproceed2.grid(row=3, column=0, columnspan=3)

        buttonproceed_input = Button(top_tension_input, text='Continue', padx=90, pady=20,
                                     font=('Times New Roman', 10),
                                     command=button_proceed1)
        buttonproceed_input.grid(row=3, column=0, columnspan=3)



#########################################      Start of advanced formulas
#########################################      Start of advanced formulas
#########################################      Start of advanced formulas
    def button_advanced_formulas():
        top_advanced_formulas = Toplevel()
        top_advanced_formulas.title('Advanced Formulas')
        top_advanced_formulas.configure(background='black')

        entrytext = StringVar()
        entry2 = Entry(top_advanced_formulas, fg="#00FF00", bg="black", textvariable=entrytext, width=30,
                       borderwidth=30)
        entry2.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        new_text = '     Pick any formula. Thank you!'
        entrytext.set(new_text)

        def button_electrostatic_force():
            global f_num
            global sec_num
            global third_num
            global fourth_num
            global first_value

            top_electricforce_input = Toplevel()
            top_electricforce_input.configure(background='gray38')
            top_electricforce_input.title('Electric Force input')

            labelText = StringVar()
            labelText.set(
                "      Dear user, which variable of the equation would you like to calculate ?\nForce (F)\nCharge 1(q1)\nCharge 2 (q2)\nDistance (r)")
            labelDir = Label(top_electricforce_input, textvariable=labelText,
                             font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=6)
            labelDir.grid(row=0, column=0)

            def popup_of_electricforce():
                answer = messagebox.showinfo('Popup', 'You exited "Electric Force" section')
                if answer:
                    top_electricforce_input.destroy()

            btnclose = Button(top_electricforce_input, text='Close Window', font=('Times New Roman', 12),
                              bg='indian red', fg='black', command=popup_of_electricforce)
            btnclose.grid(row=5, column=0, columnspan=3)

            entry_electricforce_input = Entry(top_electricforce_input, fg="#00FF00", bg="black", width=50,
                                              borderwidth=30)
            entry_electricforce_input.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

            def button1():
                global first_value
                first_choice = entry_electricforce_input.get()
                first_value = str(first_choice)
#########################################################################################################
#########################################################################################################
#########################################################################################################
                if entry_electricforce_input.get() == 'r' or entry_electricforce_input.get() == 'distance':
                    top_distance_charge1 = Toplevel()
                    top_distance_charge1.configure(background='gray38')
                    top_distance_charge1.title('Distance__ Charge 1')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired charge 1 magnitude (Coulombs):                                       ")
                    labelDir = Label(top_distance_charge1, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_distance_charge1, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                      bg='gray38', fg='white', command=top_distance_charge1.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_distance_charge1 = Entry(top_distance_charge1, fg="#00FF00", bg="black", width=50,
                                                borderwidth=30)
                    entry_distance_charge1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def button2_distance():
                        top_distance_charge2 = Toplevel()
                        top_distance_charge2.configure(background='gray38')
                        top_distance_charge2.title('Distance__ Charge 2')

                        labelText = DoubleVar()
                        labelText.set(
                            "Enter the desired charge 2 magnitude (Coulombs):                                            ")
                        labelDir = Label(top_distance_charge2, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        btnclose = Button(top_distance_charge2, text='Close Window', font=('Times New Roman', 15),
                                          bg='gray38', fg='white', command=top_distance_charge2.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        entry_distance_charge2 = Entry(top_distance_charge2, fg="#00FF00", bg="black", width=50,
                                                    borderwidth=30)
                        entry_distance_charge2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                        def button3_distance():
                            top_distance_force = Toplevel()
                            top_distance_force.configure(background='gray38')
                            top_distance_force.title('Distance__ Force')

                            labelText = DoubleVar()
                            labelText.set(
                                "Enter the desired Force (Newtons):                                            ")
                            labelDir = Label(top_distance_force, textvariable=labelText,
                                             font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                            labelDir.grid(row=0, column=0)

                            btnclose = Button(top_distance_force, text='Close Window', font=('Times New Roman', 15),
                                              bg='gray38', fg='white', command=top_distance_force.destroy)
                            btnclose.grid(row=5, column=0, columnspan=3)

                            entry_distance_force = Entry(top_distance_force, fg="#00FF00", bg="black", width=50,
                                                         borderwidth=30)
                            entry_distance_force.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                            def button4_distance():
                                top_result_distance = Toplevel()
                                top_result_distance.configure(background='gray38')
                                top_result_distance.title('Distance__ result')
                                labelText = DoubleVar()
                                labelText.set(
                                    "Your result is (meters):                                                                        ")
                                labelDir = Label(top_result_distance, textvariable=labelText,
                                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white',
                                                 height=4)
                                labelDir.grid(row=0, column=0)
                                btnclose = Button(top_result_distance, text='Close Window',
                                                  font=('Times New Roman', 15, 'bold'),
                                                  bg='gray38', fg='white', command=top_result_distance.destroy)
                                btnclose.grid(row=5, column=0, columnspan=3)
                                entry_result_distance = Entry(top_result_distance,
                                                           font=('Times New Roman', 15),
                                                           fg="#00FF00", bg="black", width=50,
                                                           borderwidth=30)
                                entry_result_distance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                                number1 = entry_distance_charge1.get()
                                number2 = entry_distance_charge2.get()
                                number3 = entry_distance_force.get()
                                entry_result_distance.insert(0, ( (9000000000*float(number1)*float
                                (number2))/ float(number3) )**0.5)

                            buttonproceed4 = Button(top_distance_force, text='Show result', padx=90,
                                                    pady=20, font=("Times New ROman", 10),
                                                    command=button4_distance)
                            buttonproceed4.grid(row=3, column=0, columnspan=3)

                        buttonproceed3 = Button(top_distance_charge2, text='Continue', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=button3_distance)
                        buttonproceed3.grid(row=3, column=0, columnspan=3)

                    buttonproceed2 = Button(top_distance_charge1, text='Continue', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=button2_distance)
                    buttonproceed2.grid(row=3, column=0, columnspan=3)

                buttonproceed_input = Button(top_electricforce_input, text='Continue', padx=90, pady=20,
                                             font=('Times New Roman', 10),
                                             command=button1)
                buttonproceed_input.grid(row=3, column=0, columnspan=3)


########################################################################################################
#########################################################################################################
#########################################################################################################

                if entry_electricforce_input.get() == 'F' or entry_electricforce_input.get() == 'f':
                    top_force_charge1 = Toplevel()
                    top_force_charge1.configure(background='gray38')
                    top_force_charge1.title('Force__ Charge 1')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired charge 1 magnitude (Coulombs):                                       ")
                    labelDir = Label(top_force_charge1, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_force_charge1, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                      bg='gray38', fg='white', command=top_force_charge1.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_force_charge1 = Entry(top_force_charge1, fg="#00FF00", bg="black", width=50,
                                                borderwidth=30)
                    entry_force_charge1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def button2_force():
                        top_force_charge2 = Toplevel()
                        top_force_charge2.configure(background='gray38')
                        top_force_charge2.title('Force__ Charge 2')

                        labelText = DoubleVar()
                        labelText.set(
                            "Enter the desired charge 1 magnitude (Coulombs):                                            ")
                        labelDir = Label(top_force_charge2, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        btnclose = Button(top_force_charge2, text='Close Window', font=('Times New Roman', 15),
                                          bg='gray38', fg='white', command=top_force_charge2.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        entry_force_charge2 = Entry(top_force_charge2, fg="#00FF00", bg="black", width=50,
                                                      borderwidth=30)
                        entry_force_charge2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                        def button3_force():
                            top_force_distance = Toplevel()
                            top_force_distance.configure(background='gray38')
                            top_force_distance.title('Force__ distance')

                            labelText = DoubleVar()
                            labelText.set(
                                "Enter the desired distance (meters):                                            ")
                            labelDir = Label(top_force_distance, textvariable=labelText,
                                             font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                            labelDir.grid(row=0, column=0)

                            btnclose = Button(top_force_distance, text='Close Window', font=('Times New Roman', 15),
                                              bg='gray38', fg='white', command=top_force_distance.destroy)
                            btnclose.grid(row=5, column=0, columnspan=3)

                            entry_force_distance = Entry(top_force_distance, fg="#00FF00", bg="black", width=50,
                                                           borderwidth=30)
                            entry_force_distance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                            def button4_force():
                                top_result_eforce = Toplevel()
                                top_result_eforce.configure(background='gray38')
                                top_result_eforce.title('Force__ result')
                                labelText = DoubleVar()
                                labelText.set(
                                    "Your result is (Newtons):                                                                        ")
                                labelDir = Label(top_result_eforce, textvariable=labelText,
                                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white',
                                                 height=4)
                                labelDir.grid(row=0, column=0)
                                btnclose = Button(top_result_eforce, text='Close Window',
                                                  font=('Times New Roman', 15, 'bold'),
                                                  bg='gray38', fg='white', command=top_result_eforce.destroy)
                                btnclose.grid(row=5, column=0, columnspan=3)
                                entry_result_force = Entry(top_result_eforce,
                                                             font=('Times New Roman', 15),
                                                             fg="#00FF00", bg="black", width=50,
                                                             borderwidth=30)
                                entry_result_force.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                                number1 = entry_force_charge2.get()
                                number2 = entry_force_distance.get()
                                number3 = entry_force_charge1.get()
                                entry_result_force.insert(0, (9000000000*float(number1)*float(number3)
                                                              )/ (float(number2)**2))

                            buttonproceed4 = Button(top_force_distance, text='Show result', padx=90,
                                                    pady=20, font=("Times New ROman", 10),
                                                    command=button4_force)
                            buttonproceed4.grid(row=3, column=0, columnspan=3)

                        buttonproceed3 = Button(top_force_charge2, text='Continue', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=button3_force)
                        buttonproceed3.grid(row=3, column=0, columnspan=3)

                    buttonproceed2 = Button(top_force_charge1, text='Continue', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=button2_force)
                    buttonproceed2.grid(row=3, column=0, columnspan=3)

                buttonproceed_input = Button(top_electricforce_input, text='Continue', padx=90, pady=20,
                                             font=('Times New Roman', 10),
                                             command=button1)
                buttonproceed_input.grid(row=3, column=0, columnspan=3)

########################################################################################################
########################################################################################################
########################################################################################################

                if entry_electricforce_input.get() == 'q2' or entry_electricforce_input.get() == 'Q2':
                    top_charge2_force = Toplevel()
                    top_charge2_force.configure(background='gray38')
                    top_charge2_force.title('Charge 2__ Force')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired Force magnitude (Newtons):                                       ")
                    labelDir = Label(top_charge2_force, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_charge2_force, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                      bg='gray38', fg='white', command=top_charge2_force.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_charge2_force = Entry(top_charge2_force, fg="#00FF00", bg="black", width=50,
                                                borderwidth=30)
                    entry_charge2_force.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def button2_charge2():
                        top_charge2_charge1 = Toplevel()
                        top_charge2_charge1.configure(background='gray38')
                        top_charge2_charge1.title('Charge 2__ Charge 1')

                        labelText = DoubleVar()
                        labelText.set(
                            "Enter the desired charge 1 magnitude (Coulombs):                                            ")
                        labelDir = Label(top_charge2_charge1, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        btnclose = Button(top_charge2_charge1, text='Close Window', font=('Times New Roman', 15),
                                          bg='gray38', fg='white', command=top_charge2_charge1.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        entry_charge2_charge1 = Entry(top_charge2_charge1, fg="#00FF00", bg="black", width=50,
                                                      borderwidth=30)
                        entry_charge2_charge1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                        def button3_charge2():
                            top_charge2_distance = Toplevel()
                            top_charge2_distance.configure(background='gray38')
                            top_charge2_distance.title('Charge 2__ distance')

                            labelText = DoubleVar()
                            labelText.set(
                                "Enter the desired distance (meters):                                            ")
                            labelDir = Label(top_charge2_distance, textvariable=labelText,
                                             font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                            labelDir.grid(row=0, column=0)

                            btnclose = Button(top_charge2_distance, text='Close Window', font=('Times New Roman', 15),
                                              bg='gray38', fg='white', command=top_charge2_distance.destroy)
                            btnclose.grid(row=5, column=0, columnspan=3)

                            entry_charge2_distance = Entry(top_charge2_distance, fg="#00FF00", bg="black", width=50,
                                                           borderwidth=30)
                            entry_charge2_distance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                            def button4_charge2():
                                top_result_charge2 = Toplevel()
                                top_result_charge2.configure(background='gray38')
                                top_result_charge2.title('Charge 2__ result')
                                labelText = DoubleVar()
                                labelText.set(
                                    "Your result is (Coulombs):                                                                        ")
                                labelDir = Label(top_result_charge2, textvariable=labelText,
                                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white',
                                                 height=4)
                                labelDir.grid(row=0, column=0)
                                btnclose = Button(top_result_charge2, text='Close Window',
                                                  font=('Times New Roman', 15, 'bold'),
                                                  bg='gray38', fg='white', command=top_result_charge2.destroy)
                                btnclose.grid(row=5, column=0, columnspan=3)
                                entry_result_charge2 = Entry(top_result_charge2,
                                                                   font=('Times New Roman', 15),
                                                                   fg="#00FF00", bg="black", width=50,
                                                                   borderwidth=30)
                                entry_result_charge2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                                number1 = entry_charge1_force.get()
                                number2 = entry_charge2_charge1.get()
                                number3 = entry_charge2_distance.get()
                                entry_result_charge2.insert(0, (float(number3) ** 2) * float(number1) /
                                                                  float(number2) * 9000000000)

                            buttonproceed4 = Button(top_charge2_distance, text='Show result', padx=90,
                                                    pady=20, font=("Times New ROman", 10),
                                                    command=button4_charge2)
                            buttonproceed4.grid(row=3, column=0, columnspan=3)

                        buttonproceed3 = Button(top_charge2_charge1, text='Continue', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=button3_charge2)
                        buttonproceed3.grid(row=3, column=0, columnspan=3)

                    buttonproceed2 = Button(top_charge2_force, text='Continue', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=button2_charge2)
                    buttonproceed2.grid(row=3, column=0, columnspan=3)

                buttonproceed_input = Button(top_electricforce_input, text='Continue', padx=90, pady=20,
                                             font=('Times New Roman', 10),
                                             command=button1)
                buttonproceed_input.grid(row=3, column=0, columnspan=3)
#################################################################################
#################################################################################
#################################################################################


                if entry_electricforce_input.get() == 'q1' or entry_electricforce_input.get() == 'Q1':
                    top_charge1_force = Toplevel()
                    top_charge1_force.configure(background='gray38')
                    top_charge1_force.title('Charge 1__ Force')

                    labelText = DoubleVar()
                    labelText.set(
                        "Enter the desired Force magnitude (Newtons):                                       ")
                    labelDir = Label(top_charge1_force, textvariable=labelText,
                                     font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                    labelDir.grid(row=0, column=0)

                    btnclose = Button(top_charge1_force, text='Close Window', font=('Times New Roman', 15, 'bold'),
                                      bg='gray38', fg='white', command=top_charge1_force.destroy)
                    btnclose.grid(row=5, column=0, columnspan=3)

                    entry_charge1_force = Entry(top_charge1_force, fg="#00FF00", bg="black", width=50,
                                                borderwidth=30)
                    entry_charge1_force.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                    def button2_charge1():
                        top_charge1_charge2 = Toplevel()
                        top_charge1_charge2.configure(background='gray38')
                        top_charge1_charge2.title('Charge 1__ Charge 2')

                        labelText = DoubleVar()
                        labelText.set(
                            "Enter the desired charge 2 magnitude (Coulombs):                                            ")
                        labelDir = Label(top_charge1_charge2, textvariable=labelText,
                                         font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                        labelDir.grid(row=0, column=0)

                        btnclose = Button(top_charge1_charge2, text='Close Window', font=('Times New Roman', 15),
                                          bg='gray38', fg='white', command=top_charge1_charge2.destroy)
                        btnclose.grid(row=5, column=0, columnspan=3)

                        entry_charge1_charge2 = Entry(top_charge1_charge2, fg="#00FF00", bg="black", width=50,
                                                      borderwidth=30)
                        entry_charge1_charge2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                        def button3_charge1():
                            top_charge1_distance = Toplevel()
                            top_charge1_distance.configure(background='gray38')
                            top_charge1_distance.title('Charge 1__ distance')

                            labelText = DoubleVar()
                            labelText.set(
                                "Enter the desired distance (meters):                                            ")
                            labelDir = Label(top_charge1_distance, textvariable=labelText,
                                             font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white', height=4)
                            labelDir.grid(row=0, column=0)

                            btnclose = Button(top_charge1_distance, text='Close Window', font=('Times New Roman', 15),
                                              bg='gray38', fg='white', command=top_charge1_distance.destroy)
                            btnclose.grid(row=5, column=0, columnspan=3)

                            entry_charge1_distance = Entry(top_charge1_distance, fg="#00FF00", bg="black", width=50,
                                                           borderwidth=30)
                            entry_charge1_distance.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                            def button4_charge1():
                                top_result_charge1 = Toplevel()
                                top_result_charge1.configure(background='gray38')
                                top_result_charge1.title('Charge 1__ result')
                                labelText = DoubleVar()
                                labelText.set(
                                    "Your result is (Coulombs):                                                                        ")
                                labelDir = Label(top_result_charge1, textvariable=labelText,
                                                 font=('Times New Roman', 15, 'bold'), bg='gray38', fg='white',
                                                 height=4)
                                labelDir.grid(row=0, column=0)
                                btnclose = Button(top_result_charge1, text='Close Window',
                                                  font=('Times New Roman', 15, 'bold'),
                                                  bg='gray38', fg='white', command=top_result_charge1.destroy)
                                btnclose.grid(row=5, column=0, columnspan=3)
                                entry_result_charge1 = Entry(top_result_charge1,
                                                                   font=('Times New Roman', 15),
                                                                   fg="#00FF00", bg="black", width=50,
                                                                   borderwidth=30)
                                entry_result_charge1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

                                number1 = entry_charge1_force.get()
                                number2 = entry_charge1_charge2.get()
                                number3 = entry_charge1_distance.get()
                                entry_result_charge1.insert(0, (float(number3) ** 2) * float(number1) /
                                                                  float(number2) * 9000000000)

                            buttonproceed4 = Button(top_charge1_distance, text='Show result', padx=90,
                                                    pady=20, font=("Times New ROman", 10),
                                                    command=button4_charge1)
                            buttonproceed4.grid(row=3, column=0, columnspan=3)

                        buttonproceed3 = Button(top_charge1_charge2, text='Continue', padx=90, pady=20,
                                                font=('Times New Roman', 10),
                                                command=button3_charge1)
                        buttonproceed3.grid(row=3, column=0, columnspan=3)

                    buttonproceed2 = Button(top_charge1_force, text='Continue', padx=90, pady=20,
                                            font=('Times New Roman', 10),
                                            command=button2_charge1)
                    buttonproceed2.grid(row=3, column=0, columnspan=3)

            buttonproceed_input = Button(top_electricforce_input, text='Continue', padx=90, pady=20,
                                         font=('Times New Roman', 10),
                                         command=button1)
            buttonproceed_input.grid(row=3, column=0, columnspan=3)

#######################################################


        def button_quadratic():
            top_quadratic_eqn = Toplevel()
            top_quadratic_eqn.configure(background='gray15')
            top_quadratic_eqn.title('Quadratic equation')
            txta = StringVar()
            z = 0

            def adding():
                x1 = 0
                a = float(E1.get())
                b = float(E2.get())
                c = float(E3.get())
                z = (b ** 2 - 4 * a * c)
                if z > 0:
                    x1_init = (-b + (z ** 0.5)) / (2 * a)
                    x1 = (round(x1_init, 3))
                    x2_init = (-b - (z ** 0.5)) / (2 * a)
                    x2 = (round(x2_init, 3))
                    txta.set('x =' + str(x1) + " or x = " + str(x2))
                elif z < 0:
                    txta.set('No real solution, Δ<0')
                elif z == 0:
                    x1_init = (-b / (2 * a))
                    x1 = (round(x1_init, 3))
                    txta.set('x =' + str(x1))

            L1 = Label(top_quadratic_eqn,font=('Times New Roman', 15,'bold'),bg = 'gray15',fg = 'white',width = 31,height = 4
            ,text='Enter the value of a,b, and c of\nax²+ bx+ c = 0')
            L1.grid(row=0, column=0, columnspan=2)
            LA = Label(top_quadratic_eqn, bg = 'gray15',width = 26, font=('Times New Roman', 12,'bold'),fg = 'white'
                       ,text="a = ")
            LA.grid(row=1, column=0)

            LB = Label(top_quadratic_eqn,bg = 'gray15',width = 26, font=('Times New Roman', 12,'bold'),fg = 'white'
            , text="b = ")
            LB.grid(row=2, column=0)

            LC = Label(top_quadratic_eqn,bg = 'gray15',width = 26, font=('Times New Roman', 12,'bold'),fg = 'white'
            , text="c = ").grid(row=3, column=0)

            E1 = Entry(top_quadratic_eqn,bg = 'azure',width = 18)
            E1.grid(row=1, column=1)
            E2 = Entry(top_quadratic_eqn,bg = 'azure',width = 18)
            E2.grid(row=2, column=1)
            E3 = Entry(top_quadratic_eqn,bg = 'azure',width = 18)
            E3.grid(row=3, column=1)

            L4 = Label(top_quadratic_eqn,bg = 'gray15',width = 26, font=('Times New Roman', 12,'bold'),fg = 'white'
            , text="Answer:")
            L4.grid(row=5, column=0)

            E4 = Entry(top_quadratic_eqn, textvariable=txta)
            E4.grid(row=5, column=1)

            Button1 = Button(top_quadratic_eqn, font = ("Times New Roman",10,'bold'), bg = 'white',fg = 'indian red',text="Solve Equation",command=lambda: adding()).grid(row=4, column=1)


            image1 = Image.open("C:\\Users\\Ahmad Shreif\\PycharmProjects\\First calculator with scientific formulas\\horizontal.PNG")
            test = ImageTk.PhotoImage(image1)

            label1 = Label(top_quadratic_eqn,image=test)
            label1.image = test

            label1.grid(row = 6,column = 0,columnspan = 3)

            L5 = Label(top_quadratic_eqn,bg = 'gray15',width = 26, font=('Times New Roman', 12,'italic'),fg = 'white'
            , text="Radical: ")
            L5.grid(row=7, column=0, columnspan=1)


            E5 = Entry(top_quadratic_eqn,bg = 'azure',fg ='black')
            E5.grid(row = 7,column = 1)


            txtb = StringVar()
            def rad_to_dec():
                a = float(E5.get())
                value_init = a**0.5
                value = (round(value_init, 3))
                txtb.set(str(value))




            Button2 = Button(top_quadratic_eqn, bg = 'white',fg = 'indian red',font = ("Times New Roman",10,'bold'),text="Convert to decimal",command= lambda: rad_to_dec()).grid(row=8, column=1)
            L6 = Label(top_quadratic_eqn, bg='gray15', width=26, font=('Times New Roman', 12, 'italic'), fg='white'
                       , text="Decimal: ")
            L6.grid(row=9, column=0, columnspan=1)

            E6 = Entry(top_quadratic_eqn,textvariable =txtb)
            E6.grid(row=9, column=1)

            btnclose1 = Button(top_quadratic_eqn, text='Terminate Window', width=42, bg='indian red', padx=40, pady=20,
                              font=('Times New Roman', 10), command=popup)
            btnclose1.grid(row = 10,column = 0,columnspan = 3)

###########################################################################################
###########################################################################################
###########################################################################################

        #######################     Button for the electric force formula   #################################

        button_electric_force = Button(top_advanced_formulas, text='F = K q1q2 / r²', bg='gold3', padx=27.6,
                                               pady=15, width = 28,
                                               font=('Times New Roman', 10), command=button_electrostatic_force)
        button_electric_force.grid(row=1, column=0,columnspan = 3)
        #######################        Button for the quadratic equation    #################################

        button_QE = Button(top_advanced_formulas, text='ax²+ bx+ c = 0', bg='gold3', padx=27.6,
                                       pady=15, width=28,
                                       font=('Times New Roman', 10), command=button_quadratic)
        button_QE.grid(row=2, column=0, columnspan=3)

        def popup_of_formulas():
            answer = messagebox.askyesno('Popup', 'Are you sure want to exit ?')
            if answer:
                top_advanced_formulas.destroy()

        btnclose = Button(top_advanced_formulas, bg='indian red', text='Close Window', width=25, command=popup_of_formulas)
        btnclose.grid(row=3, column=1, columnspan=1)

        def button_info():
            top_information = Toplevel()
            top_information.title('Variable information')

            def popup1():
                top_information.destroy()

            login_btn = PhotoImage(file="C:\\Users\\Ahmad Shreif\\PycharmProjects\\First calculator with scientific formulas\\formulas2.PNG")

            img_label = Label(image=login_btn)

            myButton = Button(top_information, image=login_btn, command=popup1, border=10)
            myButton.grid(row=0, column=0)

            myLabel = Label(top_information, text='')
            myLabel.pack(pady=20)

        button_info = Button(top_advanced_formulas, text='i', bg='steel blue', width=1, height=1,
                             font=('Times New Roman', 10, 'italic', 'bold'), command=button_info)
        button_info.grid(row=3, column=0)




#############################################Force = mass x acceleration##############################################

    button_force_newton = Button(top, text = 'F = ma', bg = 'gold3',padx=30, pady=15,
                                font = ('Times New Roman',10), command= button_force)
    button_force_newton.grid(row = 2,column = 0)

#############################################Weight = mass x gravity##############################################
    button_weight = Button(top, text='w = mg', bg = 'gold3', padx=36, pady=15,width = 5,
                           font=('Times New Roman', 10), command=button_weight)
    button_weight.grid(row=2, column=1)


#############################################Velocity = distance / time##############################################

    button_velocity = Button(top, text='v = Δd / Δt', bg='gold3', padx=29, pady=15,
                             font=('Times New Roman', 10), command=button_velocity)
    button_velocity.grid(row=2, column=2)

#############################################Energy = mass x speed of light##############################################

    button_energy_einstein = Button(top, text = 'E = mc²',bg = 'gold3', padx=27.6, pady=15,
                           font = ('Times New Roman',10), command= button_energy)
    button_energy_einstein.grid(row = 3,column =0)


#############################################Power = work / Δtime##############################################

    button_power = Button(top, text = 'P = W / Δt',bg = 'gold3', padx=25, pady=15,
                           font = ('Times New Roman',10), command= buttonpower)
    button_power.grid(row = 3,column =1)

#############################################Wave speed = frequency x wavelength##############################################

    button_velocity_waves = Button(top, text = 'v = f / λ',bg = 'gold3', padx=37, pady=15,
                           font = ('Times New Roman',10), command= buttonvelocityfromwave)
    button_velocity_waves.grid(row = 3,column =2)
#############################################Voltage=A x resistance######################################################

    button_voltage = Button(top, text='V = IR', bg='gold3', padx=34, pady=15,width = 4,
                                   font=('Times New Roman', 10), command=button_voltage)
    button_voltage.grid(row=4, column=0)
#############################################Charge (coloumbs)= I(current) x time######################################################

    button_charge = Button(top, text='Q = It', bg='gold3', padx=35.5, pady=15, width=5,
                            font=('Times New Roman', 10), command=button_charge)
    button_charge.grid(row=4, column=1)

#############################################Force (Tension)= kx######################################################

    button_tension = Button(top, text='F = kx', bg='gold3', padx=39.3, pady=15, width=5,
                           font=('Times New Roman', 10), command=button_tension)
    button_tension.grid(row=4, column=2)

#############################################"Advanced Formulas"######################################################

    button_advanced_formulas = Button(top, text='Advanced Formulas', bg='gold3', padx=45, pady=15, width=35,
                                 font=('Times New Roman', 10), command=button_advanced_formulas)
    button_advanced_formulas.grid(row=6, column=0, columnspan=3)



#############################################   "More info" BUTTON   ##############################################
    def button_info():
        top_information = Toplevel()
        top_information.title('Variable information')

        def popup1():
                top_information.destroy()


        login_btn2 = PhotoImage(file="C:\\Users\\Ahmad Shreif\\PycharmProjects\\First calculator with scientific formulas\\formulas.PNG")

        img_label2 = Label(image=login_btn2)

        myButton = Button(top_information, image=login_btn2, command=popup1, border=10)
        myButton.grid(row = 0,column = 0)


        myLabel = Label(top_information, text='')
        myLabel.pack(pady=20)



    button_info = Button(top, text='i', bg='steel blue',width = 1,height = 1,
                                   font=('Times New Roman', 10,'italic','bold'), command=button_info)
    button_info.grid(row=7, column=0)


#################################### Tag of the first "Formulas" section  #################################
button_formulas = Button(root,text ='Formulas', fg = 'snow',
                         bg = 'gray38',padx = 34,pady = 20,font=('Times New Roman',10),width=4,command = button_formulas)
button_formulas.grid(row = 7, column = 1)











########################   Define the operations of the normal calculator   ##########################

def button_clear():
    entry.delete(0,END)

def button_click(number):
    #entry.delete(0,END)
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))

def button_add():
    firstnumber = entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(firstnumber)
    entry.delete(0,END)

def button_subtract():
    firstnumber = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(firstnumber)
    entry.delete(0, END)
def button_multiply():
    firstnumber = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(firstnumber)
    entry.delete(0, END)

def button_divide():
    firstnumber = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(firstnumber)
    entry.delete(0, END)

def button_radical():
    firstnumber = entry.get()
    global f_num
    global math
    math = 'radical'
    f_num = int(firstnumber)
    entry.delete(0, END)

def button_squared():
    firstnumber = entry.get()
    global f_num
    global math
    math = 'squared'
    f_num = int(firstnumber)
    entry.delete(0, END)

def button_sin():
    firstnumber = entry.get()
    global f_num
    global math
    math = 'sin'
    f_num = int(firstnumber)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0,END)
    if math == 'addition':
        entry.insert(0,f_num + int(second_number))
    elif math == 'subtraction':
        entry.insert(0,f_num - int(second_number))
    elif math == 'division':
        entry.insert(0,f_num / int(second_number))
    elif math == 'multiplication':
        entry.insert(0,f_num * int(second_number))
    elif math == 'squared':
        entry.insert(0, f_num * f_num)
    elif math == 'radical':
        entry.insert(0, f_num ** 0.5)
    elif math == 'times10':
        entry.insert(0,f_num *10)



#########################    Identify the buttons of the calculaor  ##########################
button_1 = Button(root,text = '1', bg = 'gray38',fg = 'snow',
                  font=('Times New Roman',10,'bold'),padx = 40,pady = 20, command = lambda: button_click(1))
button_2 = Button(root,text = '2', bg = 'gray38',fg = 'snow',
                  font=('Times New Roman',10,'bold'),padx = 42.3,pady = 20,command = lambda: button_click(2))
button_3 = Button(root,text = '3', bg = 'gray38',fg = 'snow',
                  font=('Times New Roman',10,'bold'),padx = 40,pady = 20, command = lambda: button_click(3))

button_4 = Button(root,text = '4', bg = 'gray38',fg = 'snow',
                  font=('Times New Roman',10,'bold'),padx = 40,pady = 20, command = lambda: button_click(4))
button_5 = Button(root,text = '5', bg = 'gray38',fg = 'snow',
                  font=('Times New Roman',10,'bold'),padx = 42.3,pady = 20, command = lambda: button_click(5))
button_6 = Button(root,text = '6', bg = 'gray38',fg = 'snow',
                  font=('Times New Roman',10,'bold'),padx = 40,pady = 20, command = lambda: button_click(6))

button_7 = Button(root,text = '7', bg = 'gray38', fg = 'snow',
                  font=('Times New Roman',10,'bold'),padx = 40,pady = 20, command = lambda: button_click(7))
button_8 = Button(root,text = '8', bg = 'gray38',fg = 'snow',
                  font=('Times New Roman',10,'bold'),padx = 42.3,pady = 20, command = lambda: button_click(8))
button_9 = Button(root,text = '9', bg = 'gray38',fg = 'snow',
                  font=('Times New Roman',10,'bold'),padx = 40,pady = 20, command = lambda: button_click(9))
button_0 = Button(root,text = '0', bg = 'gray38',fg = 'snow',
                  font=('Times New Roman',10,'bold'),padx = 40,pady = 20, command = lambda: button_click(0))


button_add = Button(root,text = '+', bg = 'gray38', fg = 'snow',
                    font=('Times New Roman',10,'bold'),padx = 40, pady = 20,command = button_add)
button_equal = Button(root,text = '=', bg = 'gray38', fg = 'snow',
                      font=('Times New Roman',10,'bold'),padx = 92, pady = 20,command = button_equal)
button_clear = Button(root, text = 'Clear',width = 5, fg = 'snow',bg = 'gray38',
                      font=('Times New Roman',10,'bold'),padx = 78, pady = 20, command = button_clear)

button_subtract = Button(root,text = '-', padx = 41, fg = 'snow',pady = 20,bg = 'gray38',
                         font=('Times New Roman',10,'bold'),command = button_subtract)
button_multiply = Button(root,text = 'x', bg = 'gray38',fg = 'snow',
                         font=('Times New Roman',10,'bold'),padx = 45, pady = 20, command = button_multiply)
button_divide = Button(root,text = '÷', bg = 'gray38',fg = 'snow',
                       font=('Times New Roman',10,'bold'),padx = 41, pady = 20, command = button_divide)

button_radical = Button(root, text = '√x', bg = 'gray38', fg = 'snow',font=('Times New Roman',10,'bold'),padx = 37,pady = 20,command = button_radical)

button_squared = Button(root, text = 'x²', bg = 'gray38', fg = 'snow',font=('Times New Roman',10,'bold'),padx = 39,pady = 20,command = button_squared)

button_sin = Button(root, text = 'sin', bg = 'gray38', fg = 'snow',font=('Times New Roman',10,'bold'),padx = 35,pady = 20,command = button_sin)
button_cos = Button(root, text = 'cos', bg = 'gray38', fg = 'snow',font=('Times New Roman',10,'bold'),padx = 38,pady = 20,command = button_squared)
button_tan = Button(root, text = 'tan', bg = 'gray38', fg = 'snow',font=('Times New Roman',10,'bold'),padx = 35,pady = 20,command = button_squared)

def popup():
    #showerror, showwarning, showinfo, askquestion, askokcancel, askyesno
    answer = messagebox.askyesno('Popup','Are you sure want to exit ?')
    if answer:
        root.destroy()


btnclose = Button(root, text='Terminate Window',width = 30, bg = 'indian red',padx = 40, pady = 20, font=('Times New Roman',10),command=popup)



###########################  Grid the buttons on screen of normal calculator  #########################

button_1.grid(row = 3 ,column =0 )
button_2.grid(row = 3,column = 1)
button_3.grid(row = 3,column = 2)

button_4.grid(row = 2,column =0 )
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)

button_7.grid(row =1,column =0 )
button_8.grid(row =1,column =1 )
button_9.grid(row =1,column =2 )

button_0.grid(row = 4,column = 0)
button_clear.grid(row = 4,column = 1,columnspan = 2)
button_equal.grid(row = 5, column = 1, columnspan = 2)
button_add.grid(row = 5, column = 0)

button_subtract.grid(row = 6, column = 0)
button_multiply.grid(row = 6, column = 1)
button_divide.grid(row = 6, column = 2)

button_radical.grid(row = 7, column = 0)
button_squared.grid(row = 7, column = 2)

btnclose.grid(row = 9, column = 0, columnspan = 3)

button_sin.grid(row = 8,column = 0)
button_cos.grid(row = 8,column = 1)
button_tan.grid(row = 8,column = 2)


root.mainloop()