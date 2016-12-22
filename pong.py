#!/usr/local/bin/python3

import tkinter 
import tkinter.messagebox
from tkinter import StringVar
import math
import PIL.Image
import PIL.ImageTk
import time
import random
import os 
os.chdir("C:\\Users\\vasilis\\Desktop\\work\\programming\\assignments")

rootwindow = tkinter.Tk()
rootwindow.title("The Image Drawer")
rootwindow.lift()
rootwindow.config(height = 600, width = 600, bg = "yellow")
width = 10
points = 7
score_1 = 0
score_2 = 0

def set_width(p_width):
	global width
	width = p_width
	
def length(g_points):
	global points
	points = g_points

menu = tkinter.Menu(rootwindow)
rootwindow.config(menu=menu)

submenu = tkinter.Menu(menu)
menu.add_cascade(label="Paddle size", menu = submenu)
submenu.add_command(label= "Small", command =lambda: set_width(10))
submenu.add_command(label= "Medium", command =lambda: set_width(25))
submenu.add_command(label= "Big", command =lambda: set_width(40))

editMenu = tkinter.Menu(menu)	
menu.add_cascade(label="length", menu=editMenu)
editMenu.add_command(label = "7 points", command=lambda:length(7))
editMenu.add_command(label = "15 points", command=lambda:length(15))
editMenu.add_command(label = "21 points", command=lambda:length(21))

drawarea = tkinter.Canvas(rootwindow, height = 400, width = 600, bg = "pink")
drawarea.grid(row = 2, column = 0, columnspan = 4, sticky = "wens")

i = 0
deltax = random.randint(1,3)
deltay = random.randint(-3,3)
paddley = random.randint(-3,3)
paddle_2y = 200


J=drawarea.create_text(60,30, text=( score_1), font=("Comic Sans", 10))
K=drawarea.create_text(30,30, text=( score_2), font=("Comic Sans", 10))	
#entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
def reset():
	score_1 = 0
	score_2 = 0
	rootwindow.delete(0, END)

reset_button = tkinter.Button(rootwindow, text="Reset", command=lambda: reset)
	# w = tkinter.Message(rootwindow, text="Game is over")
	# w.pack()



def hitimage2_1 () :
	global tkcanvasimage,i,deltax,deltay,score_1,score_2,width,points,paddlex,paddley,paddle_2y

	timedelay = 10
	canvasimage.seek(i)
	i = (i + 1) % 25
	tkcanvasimage = PIL.ImageTk.PhotoImage(canvasimage)
	drawarea.itemconfig(ballid, image = tkcanvasimage)

	location = drawarea.coords(ballid)
	location2_1 = drawarea.coords(paddleid_1)
	location2_2 = drawarea.coords(paddleid_2)
	location2_3 = drawarea.coords(paddleid_3)

	if location[0] + 37 >= 602 :
		drawarea.coords(ballid,(300,200))
		deltax = random.randint(1,3)
		deltay = random.randint(-3,3)
		paddley = random.randint(-3,3)
		timedelay = 1000
		score_2 += 1

	if location[0] - 37 <= -2 :
		drawarea.coords(ballid,(300,200))
		deltax = random.randint(1,3)
		deltay = random.randint(-3,3)
		paddley = random.randint(-3,3)
		timedelay = 1000
		score_1 += 1



	if location[1] + 37 >= 402 :
		deltay = -deltay

	if location[1] - 37 <= 0 :
		deltay = -deltay

	if location2_3[1] + width >= 402 :
		paddley = -paddley

	if location2_3[1] - width <= 0 :
		paddley = -paddley

	if location[0] + 37 >= location2_1[0] - 5 and location[1] <= location2_1[1] + width and location[1] >= location2_1[1] - width :
		deltax = -deltax

	if location[0] - 37  <= location2_2[0] + 5 and location[1] <= location2_2[1] + width and location[1] >= location2_2[1] - width :
		deltax = -deltax

	if (location[0] - 37  <= location2_3[0] and location[0] - 37 >300 ) or (location[0] + 37  >= location2_3[0] and location[0] - 37 <300 ) and location[1] <= location2_3[1] + width and location[1] >= location2_3[1] - width :
		deltax = -deltax


#(location[0] - 37  <= location2_3[0] and location[0] - 37 >300 ) or (location[0] + 37  >= location2_3[0] and location[0] - 37 <300 )
	drawarea.move(ballid,deltax,deltay)
	drawarea.move(paddleid_3,0,paddley)
	rootwindow.after(timedelay, hitimage2_1)
	drawarea.itemconfig(J, text=score_1)
	drawarea.itemconfig(K, text=score_2)


	if score_1 == points:
		#rootwindow.quit()
		# if tkinter.messagebox.askyesno("Game Over", "Do you want to play again?"):
		# 	score_1 = 0 
		# 	score_2 = 0 
		# else: 
		# 	rootwindow.quit()
		score_1 = 0 
		score_2 = 0 


	if score_2 == points:
		#rootwindow.destroy()
		#tkinter.Message(rootwindow, text="Player 1 won!").pack()
		# if tkinter.messagebox.askyesno("Game Over", "Do you want to play again?"):
		# 	score_1 = 0 
		# 	score_2 = 0 
		# else: 
		# 	rootwindow.quit()
		score_1 = 0 
		score_2 = 0 


def AI(ev):
	location = drawarea.coords(ballid)
	location2_2 = drawarea.coords(paddleid_2)
	# # while score_1 < points and score_2 < points:
	# 	if location[1] + 37 < location2_2[1]+ width :
	# 		drawarea.move(paddleid_2, 0, -5)
	# 	elif location[1] + 37 > location2_2[1]+ width :
	# 		drawarea.move(paddleid_2, 0, +5)
	if location[1] + 37 < location2_2[1]+ width :
		drawarea.move(paddleid_2, 0, -5)
	elif location[1] + 37 > location2_2[1]+ width :
		drawarea.move(paddleid_2, 0, +5)



def hitimage_slow_1 () :

	rootwindow.after(100, hitimage2_1)

def hitimage_normal_1 () :

	rootwindow.after(1000, hitimage2_1)

def hitimage_fast_1 () :

	rootwindow.after(10000, hitimage2_1)
 
def hitkeyup(ev) :

	drawarea.move(paddleid_1, 0, -5)

def hitkeydown(ev) :

	drawarea.move(paddleid_1, 0, 5)

def hitkeyW(ev) :

	drawarea.move(paddleid_2, 0, -5)

def hitkeyS(ev) :

	drawarea.move(paddleid_2, 0, 5)


labelimage = PIL.Image.open("dummyimage.jpg")
labelimage.thumbnail((20, 40))
tklabelimage2 = PIL.ImageTk.PhotoImage(labelimage)

radiuslabel = tkinter.Label(rootwindow, image = tklabelimage2)
radiuslabel.grid(row = 0, column = 0, sticky = "wens")

buttonimage_slow = PIL.Image.open("blob_slow.png")
buttonimage_slow.thumbnail((30,30))
tkbuttonimage_slow = PIL.ImageTk.PhotoImage(buttonimage_slow)
imagebutton_slow = tkinter.Button(rootwindow, image = tkbuttonimage_slow, command = hitimage_slow_1)
imagebutton_slow.grid(row = 0, column = 1, sticky = "wens")


buttonimage_normal = PIL.Image.open("blob.png")
buttonimage_normal.thumbnail((30,30))
tkbuttonimage_normal = PIL.ImageTk.PhotoImage(buttonimage_normal)
imagebutton_normal = tkinter.Button(rootwindow, image = tkbuttonimage_normal, command = hitimage_normal_1)
imagebutton_normal.grid(row = 0, column = 2, sticky = "wens")

buttonimage_fast = PIL.Image.open("blob_fast.png")
buttonimage_fast.thumbnail((30,30))
tkbuttonimage_fast = PIL.ImageTk.PhotoImage(buttonimage_fast)
imagebutton_fast = tkinter.Button(rootwindow, image = tkbuttonimage_fast, command = hitimage_fast_1)
imagebutton_fast.grid(row = 0, column = 3, sticky = "wens")

reset_button = tkinter.Button(rootwindow, text="Reset", command=lambda: reset)


canvasimage = PIL.Image.open("animated-ball-image-0046.gif")
tkcanvasimage = PIL.ImageTk.PhotoImage(canvasimage)
ballid = drawarea.create_image(300, 200, image = tkcanvasimage)

paddleid_1 = drawarea.create_image(595, 200, image = tklabelimage2)

paddleid_2 = drawarea.create_image(	5, 200, image = tklabelimage2)

paddleid_3 = drawarea.create_image(300, 100, image = tklabelimage2)


drawarea.bind("<Up>", hitkeyup)
drawarea.bind("<Down>", hitkeydown)
drawarea.bind("<w>",hitkeyW)
drawarea.bind("<s>",hitkeyS)
drawarea.bind("<a>",AI)
drawarea.focus_set()
 #
rootwindow.rowconfigure(0, weight = 1)
rootwindow.rowconfigure(2, weight = 1)
rootwindow.columnconfigure(0, weight = 1)
rootwindow.columnconfigure(4, weight = 1)
rootwindow.mainloop()

