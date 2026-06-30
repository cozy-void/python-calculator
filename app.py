import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("320x400")
root.resizable(False,False)

text_result = tk.Entry(root, font= ("Arial",20), justify="right")
text_result.grid(row= 0, column= 0, columnspan=5, ipady=10)

expression = ""

def brackets():
    global expression

    if expression.count("(") > expression.count(")"):
        click(")")
    else:
        click("(")


def click(value):
    global expression
    expression +=str(value)
    text_result.delete(0, tk.END)
    text_result.insert(0, expression)


def clear():
    global expression
    expression = ""
    text_result.delete(0, tk.END)

def equal():
    global expression
    try:
        result = str(eval(expression))
        text_result.delete(0, tk.END)
        text_result.insert(0, result)
    except:
        text_result.delete(0, tk.END)
        text_result.insert(0, "ERROR")
        expression = ""

def percentage():
    global expression
    try:
        value = float(expression)
        value = value/100
        expression = str(value)
        text_result.delete(0, tk.END)
        text_result.insert(0, expression)
    except:
        text_result.delete(0, tk.END)
        text_result.insert(0, "ERROR")
        expression = ""

def P_N():
    global expression

    if expression.startswith("-"):
        expression = expression[1:]
    else:
        expression = "-" + expression

    text_result.delete(0, tk.END)
    text_result.insert(0, expression)

#first row

button_c = tk.Button(root, text="C", font=("Arial", 18), width=4, height=2, command=clear)
button_c.grid(row=1, column=0)

button_b = tk.Button(root, text="( )", font=("Arial", 18), width=4, height=2, command=brackets)
button_b.grid(row=1, column=1)

button_p = tk.Button(root, text="%", font=("Arial", 18), width=4, height=2, command= percentage)
button_p.grid(row=1, column=2)

#---------------------------------------------------Numb_Pad--------------------------------------------------------------

# ----------------------------------------------------Row_2------------------------------------------------------------------
button_7 = tk.Button(root, text="7", font=("Arial", 18), width=4, height=2, command= lambda:click(7))
button_7.grid(row= 2, column= 0)

button_8 = tk.Button(root, text="8",font=("Arial", 18), width=4, height=2, command=lambda:click(8))
button_8.grid(row=2, column=1)

button_9 = tk.Button(root, text="9",font=("Arial", 18), width=4, height=2, command=lambda:click(9))
button_9.grid(row=2, column=2)

#-----------------------------------------------------Row_3-------------------------------------------------------------
button_4 = tk.Button(root, text="4", font=("Arial", 18), width=4, height=2, command= lambda:click(4))
button_4.grid(row= 3, column= 0)

button_5 = tk.Button(root, text="5", font=("Arial", 18), width=4, height=2, command= lambda:click(5))
button_5.grid(row= 3, column= 1)

button_6 = tk.Button(root, text="6", font=("Arial", 18), width=4, height=2, command= lambda:click(6))
button_6.grid(row= 3, column= 2)

#-------------------------------------------------------Row_4---------------------------------------------
button_1 = tk.Button(root, text="1", font=("Arial", 18), width=4, height=2, command= lambda:click(1))
button_1.grid(row= 4, column= 0)

button_2 = tk.Button(root, text="2", font=("Arial", 18), width=4, height=2, command= lambda:click(2))
button_2.grid(row= 4, column= 1)

button_3 = tk.Button(root, text="3", font=("Arial", 18), width=4, height=2, command= lambda:click(3))
button_3.grid(row= 4, column= 2)

#----------------------------------------------------------Row_5---------------------------------------

button_0 = tk.Button(root, text="0", font=("Arial", 18), width=4, height=2, command= lambda:click(0))
button_0.grid(row= 5, column= 1)

#------------------------------------------------------- Operators--------------------------------------

button_div = tk.Button(root, text="÷",font=("Arial", 18), width=4, height=2, command=lambda: click("/"))
button_div.grid(row=1, column=3)

button_mup = tk.Button(root, text="X",font=("Arial", 18), width=4, height=2, command=lambda: click("*"))
button_mup.grid(row=2, column=3)

button_min = tk.Button(root, text="-",font=("Arial", 18), width=4, height=2, command=lambda: click("-"))
button_min.grid(row=3, column=3)

button_add = tk.Button(root, text="+",font=("Arial", 18), width=4, height=2, command=lambda: click("+"))
button_add.grid(row=4, column=3)

button_equ = tk.Button(root, text="=",font=("Arial", 18), width=4, height=2, command=equal)
button_equ.grid(row=5, column=3)

button_P_N = tk.Button(root, text="+/-",font=("Arial", 18), width=4, height=2, command=P_N)
button_P_N.grid(row=5, column=0)

button_dot = tk.Button(root, text=".",font=("Arial", 18), width=4, height=2, command=lambda: click("."))
button_dot.grid(row=5, column=2)


root.mainloop()
