from tkinter import *
from tkcalendar import *
from datetime import *
import datetime, time
import os
import re
import requests
import json
import sqlite3
import random
import smtplib, ssl
import json
from PIL import ImageTk,Image

access_key = 'cc2317434d156e394c992cec80841e99' #for phone API in the function phone_info
access_key_email = '2539242dc1a05bf6cb3d5972cfb12e03' # API key for email verify function
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #reference: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/

with open("config.json", "r") as f:
	config = json.load(f)
	print("Config loaded")

#Connect to the database
conn = sqlite3.connect('database.db') # connection to the SQL database
#Create a cursor
cur = conn.cursor() # creation of a cursor
#Create table

cur.execute("""CREATE TABLE IF NOT EXISTS mydatabase1 (
              fname text,
              lname text,
              user_name text,
              pass_word text,
              myemail text,
              myphone text
              )""")

#Commit changes
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS hotels (
              hotelName text,
              starRating text,
              address text,
              city text,
              postCode text
              )""")

conn.commit()

("""CREATE TABLE IF NOT EXISTS Bookings (
            Username text ,
            Hotel text , 
            Class text , 
            NoPeople int , 
            StartDate text, 
            NoNights int, 
            Price int, 
            Reference text
            )""")

conn.commit()


def BookNow1():
	screen21.destroy()
	screen18.destroy()
	booking_page()

def BookNow2():
	screen22.destroy()
	screen18.destroy()
	booking_page()


def BookNow3():
	screen23.destroy()
	screen18.destroy()
	booking_page()

def BookNow4():
	screen24.destroy()
	screen18.destroy()
	booking_page()

def BookNow5():
	screen25.destroy()
	screen18.destroy()
	booking_page()

def quit1():
    screen12.destroy()

def quitview():
	screen9.destroy()

def delete():
    screen13.destroy()

def delete2():
    screen3.destroy()
    screen2.destroy()
    session()
    
def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def delete5():
    screen7.destroy()

def delete6():
    screen1.destroy()

def delete7():
    screen.destroy()

def delete8(): # Log out of session
    screen6.destroy()
    main_screen()

def delete9():
    screen11.destroy()

def delete10():
    screen10.destroy()

def deletehelp():
    screen8.destroy()

def delete11():
	screen14.destroy()

def delete12():
	screen9.destroy()

def delete13():
	bookingscreen.destroy()

def delete14():
	latestB_screen.destroy()

def delete15():
	screen15.destroy()

def delete16():
	screen16.destroy()

def delete17():
	screen17.destroy()

def delete18():
	screen19.destroy()

def delete19():
	screen18.destroy()

def delete20():
	#screen20.destroy()
	pass

def delete21():
	screen21.destroy()

def delete22():
	screen22.destroy()

def delete23():
	screen23.destroy()

def delete24():
	screen24.destroy()

def delete25():
	screen25.destroy()

def delete26():
	BkScreen.destroy()

def delete27():
	noBookings.destroy()

def fname_check(fname_info):
	special_characters = "!@#£$%^&*()-+?_=,<>/1234567890"""  #checks if there is a special character
	if any(c in special_characters for c in fname_info):
		return False
	else:
		return True

def lname_check(lname_info):
	special_characters = "!@#£$%^&*()-+?_=,<>/1234567890""" #checks if there is a special character
	if any(c in special_characters for c in lname_info): 
		return False
	else:
		return True

def check_pass(password_info):
    special_characters = "!@#£$%^&*()-+?_=,<>/"""
    if any(c in special_characters for c in password_info): #checks if there is a special character
        return True
    else:
        return False

def name_error():
	global screen14
	screen14 = Toplevel(screen)
	screen14.geometry("200x90")
	screen14.title("Warning!")
	screen14.iconbitmap('error.ico')
	Label(screen14, text = "First/Last Name entered incorrectly", fg = "red").pack()
	Button(screen14, text = "Ok", command = delete11).pack()

def email_verify_api(email_info):
    url = 'http://apilayer.net/api/check?access_key=' + access_key_email + '&email=' + email_info  #request url to the API
    response = requests.get(url)
    answer = response.json()
    print(answer) # for troubleshooting
    if answer["smtp_check"] == True:
        return True
    else:
        return False

def user_error():
    global screen11
    screen11 = Toplevel(screen)
    screen11.title("Username Error")
    screen11.geometry("200x100")
    screen11.iconbitmap('error.ico')
    Label(screen11, text = "Username inputted contains error").pack()
    Button(screen11, text = "Ok", command = delete9).pack()

def user_taken():
	global screen15
	screen15 = Toplevel(screen)
	screen15.title("Username Taken Error")
	screen15.geometry("200x100")
	screen15.iconbitmap('error.ico')
	Label(screen15, text = "Username is taken").pack()
	Button(screen15, text = "Ok", command = delete15)

def user_exists_check():
    conn =  sqlite3.connect('database.db')
    cur =  conn.cursor()
    cur.execute("SELECT user_name from mydatabase1 WHERE user_name = (:username_placeholder3)",
              {
                    'username_placeholder3': username.get()
              })
    user_input_check = cur.fetchall()
    conn.commit()
    conn.close()
    print(user_input_check) # Troubleshooting
    print(len(user_input_check)) # troubleshooting
    if len(user_input_check) > 0:
        return True
    else:
        return False

def username_check(username_info):
    if(re.search(regex,username_info)): #checking if any of the characters in regex are in the username_info variable / if the username inputted already exists
        return True
    else:
        return False
    

def phone_check(phone_info):
    url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + phone_info + '&country_code=GB' #request url to the API
    response = requests.get(url)
    answer = response.json()
    print(answer) # for troubleshooting
    if answer["valid"] == True:
        return True
    else:
        return False

def delAccount():
	global screen16
	screen16 = Toplevel(screen10)
	screen16.title("Delete Account")
	screen16.geometry("250x100")
	screen16.iconbitmap('bin.ico')
	Label(screen16, text = "NOTE: Account will be permanently deleted").pack()
	Label(screen16, text = "This action cannot be reversed").pack()
	Button(screen16, text = "Continue", fg = 'red', command = delAccConfirmed).pack()
	Button(screen16, text = "No, go back", command = delete16).pack()

def delAccConfirmed():
	screen16.destroy()
	screen10.destroy()
	screen6.destroy()
	conn = sqlite3.connect('database.db') # connection to the SQL database
	#Create a cursor
	cur = conn.cursor() # creation of a cursor
	cur.execute("DELETE FROM mydatabase1 WHERE oid = (:oid_placeholder1)",
    	{
    				'oid_placeholder1':temp_oid1.get()
    	})
	cur.execute("DELETE FROM Bookings WHERE Username = (:user)",
		{
					'user':username_verify.get()
		})
	conn.commit()
	conn.close()
	main_screen()


def view_hotels():
    global screen9
    global my_label
    global cityEntry
    global cityVar
    screen6.attributes('-topmost',False)
    screen9 = Tk()
    screen9.title('View Hotels')
    screen9.iconbitmap('hotel.ico')
    screen9.geometry("800x700")
    #screen9.attributes("-topmost",True)
    Button(screen9, text = "Press to go back", fg = "red", command = delete12).pack()
    Label(screen9, text = "View Hotels", fg = "black", bg = "grey", width = "500", height = "3").pack()
    Label(screen9, text = "").pack()
    Label(screen9, text = "Search for a city below or view all hotels.", font = ("Times", "24", "bold")).pack()
    Label(screen9, text = "").pack()
    Label(screen9, text = "").pack()
    Label(screen9, text = "Enter City Name").pack()
    Label(screen9, text = "Format is where the first letter must be capital and rest lowercase - (Manchester).", fg = 'red').pack()
    cityVar = StringVar()
    cityEntry = Entry(screen9, textvariable = cityVar)
    cityEntry.pack()
    Button(screen9, text = "Submit", command = citySearch).pack()
    Label(screen9, text = "").pack()
    Label(screen9, text = "OR").pack()
    Label(screen9, text = "").pack()
    Button(screen9, text = "View All Hotels", command = viewAll, fg = 'white', bg = 'blue').pack()
    my_img = ImageTk.PhotoImage(Image.open('IHotel.jpeg'))
    canvas = Canvas(screen9, width = 300, height = 300)
    canvas.pack()
    canvas.create_image(20, 20, anchor=NW, image=my_img)
    screen9.mainloop()

def citySearch():
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cur.execute("SELECT hotelName FROM hotels WHERE city = (:cityEntry)",
		{
					'cityEntry':cityEntry.get()
		})
	cityResult = cur.fetchall()
	conn.commit()
	conn.close()
	if len(cityResult) == 0:
		noResult()
		return
	global cityArray
	cityArray = []
	for x in cityResult:
		tCityResult = str(x).replace('(', "").replace(',', "").replace(')',"").replace("'","")
		cityArray.append(str(tCityResult))
	print(cityArray) # Troubleshooting
	searchResult()

def searchResult():
	screen9.destroy()
	global screen18
	screen18 = Toplevel(screen6)
	screen18.title("Search Result")
	screen18.iconbitmap('hotel.ico')
	screen18.geometry("400x680")
	Button(screen18, text = "Go Back to Main Page", command= delete19).pack()
	Label(screen18, text = "Below are the results of your search.", fg = "black", bg = "grey", width = "500", height = "3").pack()
	Label(screen18, text = "").pack()
	if 'Adiance Hotel' in cityArray:
		Label(screen18, text = "------------------------------------------------------------------").pack()
		Label(screen18, text = "Adiance Hotel").pack()
		Label(screen18, text = "Click Below to View").pack()
		Button(screen18, text = 'VIEW', fg = "white", bg = "black", command = hotel1).pack()
		Label(screen18, text = "------------------------------------------------------------------").pack()
	if 'Azure Holidays' in cityArray:
		Label(screen18, text = "------------------------------------------------------------------").pack()
		Label(screen18, text = "Azure Holidays").pack()
		Label(screen18, text = "Click Below to View").pack()
		Button(screen18, text = 'VIEW', fg = "white", bg = "black", command = hotel2).pack()
		Label(screen18, text = "------------------------------------------------------------------").pack()
	if 'Collosall Resort' in cityArray:
		Label(screen18, text = "------------------------------------------------------------------").pack()
		Label(screen18, text = "Collosall Resort").pack()
		Label(screen18, text = "Click Below to View").pack()
		Button(screen18, text = 'VIEW', fg = "white", bg = "black", command = hotel3).pack()
		Label(screen18, text = "------------------------------------------------------------------").pack()
	if 'Floorcoast Hotel' in cityArray:
		Label(screen18, text = "------------------------------------------------------------------").pack()
		Label(screen18, text = "Floorcoast Hotel").pack()
		Label(screen18, text = "Click Below to View").pack()
		Button(screen18, text = 'VIEW', fg = "white", bg = "black", command = hotel4).pack()
		Label(screen18, text = "------------------------------------------------------------------").pack()
	if 'Four Seasons' in cityArray:
		Label(screen18, text = "------------------------------------------------------------------").pack()
		Label(screen18, text = "Four Seasons").pack()
		Label(screen18, text = "Click Below to View").pack()
		Button(screen18, text = 'VIEW', fg = "white", bg = "black", command = hotel5).pack()
		Label(screen18, text = "------------------------------------------------------------------").pack()
	screen18.mainloop()


def hotel1():
	global screen21
	screen21 = Tk()
	screen21.title("Adiance Hotel")
	screen21.iconbitmap('hotel.ico')
	screen21.geometry("750x650")
	screen21.config(bg="#222831")
	Button(screen21, text = "Go back to search results",  command = delete21, fg = '#ff2e63', bg = '#393e46').place(x=10,y=600)
	Label(screen21, text = "Adiance Hotel", fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3", font =  ("Calibri", 15)).pack()
	img1 = ImageTk.PhotoImage(Image.open('AdianceV1.jfif'))
	label1= Label(image = img1)
	label1.place(x=10,y=100)
	img2 = ImageTk.PhotoImage(Image.open('AdianceV2.jfif'))
	label2= Label(image = img2)
	label2.place(x=255,y=100)
	img3 = ImageTk.PhotoImage(Image.open('AdianceV3.jfif'))
	label3 = Label(image=img3)
	label3.place(x=500,y=100)
	conn = sqlite3.connect('database.db')
	cur = conn.cursor() # creation of a cursor
	cur.execute("SELECT starRating FROM hotels WHERE hotelName = 'Adiance Hotel'")
	starsT = cur.fetchall()
	stars = []
	for x in starsT:
		temp_stars = str(x).replace('(', "").replace(',', "").replace(')', "").replace("'","")
		stars.append(float(temp_stars))
	print(starsT) #Troubleshooting
	cur.execute("SELECT city FROM hotels WHERE hotelName = 'Adiance Hotel'")
	cityT = cur.fetchall()
	city = []
	for x in cityT:
		temp_city = str(x).replace('(',"").replace(',',"").replace(')',"")
		city.append(temp_city)
	print(city) #troubleshooting
	cur.execute("SELECT address FROM hotels WHERE hotelName = 'Adiance Hotel'")
	addressT = cur.fetchall()
	address = []
	for x in addressT:
		temp_add = str(x).replace('(',"").replace(',',"").replace(')',"").replace("'","")
		address.append(temp_add)
	print(address) #troubleshooting
	cur.execute("SELECT postCode FROM hotels WHERE hotelName = 'Adiance Hotel'")
	postCodeT = cur.fetchall()
	postCode = []
	for x in postCodeT:
		temp_pc = str(x).replace('(',"").replace(',',"").replace(')',"").replace("'","")
		postCode.append(temp_pc)
	print(postCode) #troubleshooting
	cityShown = city[0]
	cityShown = str(cityShown)
	starRatingShown = stars[0]
	starRatingShown = str(starRatingShown)
	addressShown = address[0]
	addressShown = str(addressShown)
	postShown = postCode[0]
	postShown = str(postShown)
	Label(screen21, text = "Welcome to Adiance Hotel in " + cityShown.replace("'","") + " rated at " + starRatingShown.replace("'","") + " stars!",bg="#222831", fg = 'white', font =  ("Calibri", 15)).place(x=130,y=275)
	Label(screen21, text = "Description: Adiance London Hotel is in close proximity to Wembley Stadium and Wembley Arena.",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=310)
	Label(screen21, text = "Each of the 210 modern guest rooms have wireless internet and satellite TV. Deluxe includes Sky Sports TV.",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=335)
	Label(screen21, text = "The hotel has excellent local transport connections into central London. Deluxe includes hotel valet parking.",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=360)
	Label(screen21, text = "Reviews:",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=390)
	Label(screen21, text = "“Very fine hotel with an excellent breakfast buffet.”",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=415)
	Label(screen21, text = "“The neighborhood felt safe and the transit was fairly accessible. Great breakfast!”",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=440)
	Label(screen21, text = "Full Address:",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=470)
	Label(screen21, text = "" + addressShown.replace("'","") + " " + cityShown.replace("'",""),bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=495)
	Label(screen21, text = "" + postShown.replace("'","") + " England",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=520)
	Label(screen21, text = "Pricing: Deluxe is £100 per night and Standard is £85 per night! Book Now using the button below",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=550)
	Button(screen21, text = "Book Now", fg = '#ff2e63', bg = '#393e46', command=BookNow1).place(x = 650, y=600)
	conn.close()
	screen21.mainloop()

def hotel2():
	global screen22
	screen22 = Tk()
	screen22.title("Azure Holidays")
	screen22.iconbitmap('hotel.ico')
	screen22.geometry("750x650")
	screen22.config(bg="#222831")
	Button(screen22, text = "Go back to search results",command = delete22, fg = '#ff2e63', bg = '#393e46').place(x=10,y=600)
	Label(screen22, text = "Azure Holidays", fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3", font =  ("Calibri", 15)).pack()
	img1 = ImageTk.PhotoImage(Image.open('Azure1Resized.jfif'))
	label1= Label(image = img1)
	label1.place(x=10,y=100)
	img2 = ImageTk.PhotoImage(Image.open('Azure2Resized.jfif'))
	label2= Label(image = img2)
	label2.place(x=255,y=100)
	img3 = ImageTk.PhotoImage(Image.open('Azure3Resized.jfif'))
	label3 = Label(image=img3)
	label3.place(x=500,y=100)
	conn = sqlite3.connect('database.db')
	cur = conn.cursor() # creation of a cursor
	cur.execute("SELECT starRating FROM hotels WHERE hotelName = 'Azure Holidays'")
	starsT = cur.fetchall()
	stars = []
	for x in starsT:
		temp_stars = str(x).replace('(', "").replace(',', "").replace(')', "").replace("'","")
		stars.append(float(temp_stars))
	#print(starsT) #Troubleshooting
	cur.execute("SELECT city FROM hotels WHERE hotelName = 'Azure Holidays'")
	cityT = cur.fetchall()
	city = []
	for x in cityT:
		temp_city = str(x).replace('(',"").replace(',',"").replace(')',"")
		city.append(temp_city)
	#print(city) #troubleshooting
	cur.execute("SELECT address FROM hotels WHERE hotelName = 'Azure Holidays'")
	addressT = cur.fetchall()
	address = []
	for x in addressT:
		temp_add = str(x).replace('(',"").replace(',',"").replace(')',"").replace("'","")
		address.append(temp_add)
	#print(address) #troubleshooting
	cur.execute("SELECT postCode FROM hotels WHERE hotelName = 'Azure Holidays'")
	postCodeT = cur.fetchall()
	postCode = []
	for x in postCodeT:
		temp_pc = str(x).replace('(',"").replace(',',"").replace(')',"").replace("'","")
		postCode.append(temp_pc)
	##print(postCode) #troubleshooting
	cityShown = city[0]
	cityShown = str(cityShown)
	starRatingShown = stars[0]
	starRatingShown = str(starRatingShown)
	addressShown = address[0]
	addressShown = str(addressShown)
	postShown = postCode[0]
	postShown = str(postShown)
	Label(screen22, text = "Welcome to Azure Holidays in " + cityShown.replace("'","") + " rated at " + starRatingShown.replace("'","") + " stars!",bg="#222831", fg = 'white', font =  ("Calibri", 15)).place(x=130,y=275)
	Label(screen22, text = "Description: Azure Holidays Hotel is in close proximity to the Trafford Centre.",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=310)
	Label(screen22, text = "Each of the 55 hotel rooms have 5mbps internet and a small TV. Virgin Media TiVo included with Deluxe",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=335)
	Label(screen22, text = "The hotel has some local transport connections into the city centre.",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=360)
	Label(screen22, text = "Reviews:",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=390)
	Label(screen22, text = "“Very good price and for what you get its great”",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=415)
	Label(screen22, text = "“The area was OK, but had some walking distance”",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=440)
	Label(screen22, text = "Full Address:",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=470)
	Label(screen22, text = "" + addressShown.replace("'","") + " " + cityShown.replace("'",""),bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=495)
	Label(screen22, text = "" + postShown.replace("'","") + " England",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=520)
	Label(screen22, text = "Pricing: Deluxe is £29 per night and Standard is £20 per night! Book Now using the button below",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=550)
	Button(screen22, text = "Book Now", fg = '#ff2e63', bg = '#393e46', command=BookNow2).place(x = 650, y=600)
	conn.close()
	screen22.mainloop()


def hotel3():
	global screen23
	screen23 = Tk()
	screen23.title("Collosall Resort")
	screen23.iconbitmap('hotel.ico')
	screen23.geometry("750x650")
	screen23.config(bg="#222831")
	Button(screen23, text = "Go back to search results",command = delete23, fg = '#ff2e63', bg = '#393e46').place(x=10,y=600)
	Label(screen23, text = "Collosall Resort", fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3", font =  ("Calibri", 15)).pack()
	img1 = ImageTk.PhotoImage(Image.open('C1Resized.jfif'))
	label1= Label(image = img1)
	label1.place(x=10,y=100)
	img2 = ImageTk.PhotoImage(Image.open('C2Resized.jfif'))
	label2= Label(image = img2)
	label2.place(x=255,y=100)
	img3 = ImageTk.PhotoImage(Image.open('C3Resized.jfif'))
	label3 = Label(image=img3)
	label3.place(x=500,y=100)
	conn = sqlite3.connect('database.db')
	cur = conn.cursor() # creation of a cursor
	cur.execute("SELECT starRating FROM hotels WHERE hotelName = 'Collosall Resort'")
	starsT = cur.fetchall()
	stars = []
	for x in starsT:
		temp_stars = str(x).replace('(', "").replace(',', "").replace(')', "").replace("'","")
		stars.append(float(temp_stars))
	#print(starsT) #Troubleshooting
	cur.execute("SELECT city FROM hotels WHERE hotelName = 'Collosall Resort'")
	cityT = cur.fetchall()
	city = []
	for x in cityT:
		temp_city = str(x).replace('(',"").replace(',',"").replace(')',"")
		city.append(temp_city)
	#print(city) #troubleshooting
	cur.execute("SELECT address FROM hotels WHERE hotelName = 'Collosall Resort'")
	addressT = cur.fetchall()
	address = []
	for x in addressT:
		temp_add = str(x).replace('(',"").replace(',',"").replace(')',"").replace("'","")
		address.append(temp_add)
	#print(address) #troubleshooting
	cur.execute("SELECT postCode FROM hotels WHERE hotelName = 'Collosall Resort'")
	postCodeT = cur.fetchall()
	postCode = []
	for x in postCodeT:
		temp_pc = str(x).replace('(',"").replace(',',"").replace(')',"").replace("'","")
		postCode.append(temp_pc)
	#print(postCode) #troubleshooting
	cityShown = city[0]
	cityShown = str(cityShown)
	starRatingShown = stars[0]
	starRatingShown = str(starRatingShown)
	addressShown = address[0]
	addressShown = str(addressShown)
	postShown = postCode[0]
	postShown = str(postShown)
	Label(screen23, text = "Welcome to Collosall Resort in " + cityShown.replace("'","") + " rated at " + starRatingShown.replace("'","") + " stars!",bg="#222831", fg = 'white', font =  ("Calibri", 15)).place(x=130,y=275)
	Label(screen23, text = "Description: Collosall Resort is just a 15-minute drive from Luton's center. Deluxe Rooms are larger for families.",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=310)
	Label(screen23, text = "Each of the 67 hotel rooms have 2.5mbps internet and a small TV. Deluxe Rooms include Breakfast",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=335)
	Label(screen23, text = "Internet can be increased to 5mbps at an extra fee or by purchasing a Deluxe Room.",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=360)
	Label(screen23, text = "Reviews:",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=390)
	Label(screen23, text = "“Decent area, not close to centre by walking”",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=415)
	Label(screen23, text = "“No breakfast included with standard but comfy rooms”",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=440)
	Label(screen23, text = "Full Address:",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=470)
	Label(screen23, text = "" + addressShown.replace("'","") + " " + cityShown.replace("'",""),bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=495)
	Label(screen23, text = "" + postShown.replace("'","") + " England",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=520)
	Label(screen23, text = "Pricing: Deluxe is £25 per night and Standard is £15 per night! Book Now using the button below",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=550)
	Button(screen23, text = "Book Now", fg = '#ff2e63', bg = '#393e46', command=BookNow3).place(x = 650, y=600)
	conn.close()
	screen23.mainloop()

def hotel4():
	global screen24
	screen24 = Tk()
	screen24.title("Floorcoast Hotel")
	screen24.iconbitmap('hotel.ico')
	screen24.geometry("750x650")
	screen24.config(bg="#222831")
	Button(screen24, text = "Go back to search results",command = delete24, fg = '#ff2e63', bg = '#393e46').place(x=10,y=600)
	Label(screen24, text = "Floorcoast Hotel", fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3", font =  ("Calibri", 15)).pack()
	img1 = ImageTk.PhotoImage(Image.open('F1Resized.jfif'))
	label1= Label(image = img1)
	label1.place(x=10,y=100)
	img2 = ImageTk.PhotoImage(Image.open('F2Resized.jfif'))
	label2= Label(image = img2)
	label2.place(x=255,y=100)
	img3 = ImageTk.PhotoImage(Image.open('F3Resized.jfif'))
	label3 = Label(image=img3)
	label3.place(x=500,y=100)
	conn = sqlite3.connect('database.db')
	cur = conn.cursor() # creation of a cursor
	cur.execute("SELECT starRating FROM hotels WHERE hotelName = 'Floorcoast Hotel'")
	starsT = cur.fetchall()
	stars = []
	for x in starsT:
		temp_stars = str(x).replace('(', "").replace(',', "").replace(')', "").replace("'","")
		stars.append(float(temp_stars))
	#print(starsT) #Troubleshooting
	cur.execute("SELECT city FROM hotels WHERE hotelName = 'Floorcoast Hotel'")
	cityT = cur.fetchall()
	city = []
	for x in cityT:
		temp_city = str(x).replace('(',"").replace(',',"").replace(')',"")
		city.append(temp_city)
	#print(city) #troubleshooting
	cur.execute("SELECT address FROM hotels WHERE hotelName = 'Floorcoast Hotel'")
	addressT = cur.fetchall()
	address = []
	for x in addressT:
		temp_add = str(x).replace('(',"").replace(',',"").replace(')',"").replace("'","")
		address.append(temp_add)
	#print(address) #troubleshooting
	cur.execute("SELECT postCode FROM hotels WHERE hotelName = 'Floorcoast Hotel'")
	postCodeT = cur.fetchall()
	postCode = []
	for x in postCodeT:
		temp_pc = str(x).replace('(',"").replace(',',"").replace(')',"").replace("'","")
		postCode.append(temp_pc)
	#print(postCode) #troubleshooting
	cityShown = city[0]
	cityShown = str(cityShown)
	starRatingShown = stars[0]
	starRatingShown = str(starRatingShown)
	addressShown = address[0]
	addressShown = str(addressShown)
	postShown = postCode[0]
	postShown = str(postShown)
	Label(screen24, text = "Welcome to Floorcoast Hotel in " + cityShown.replace("'","") + " rated at " + starRatingShown.replace("'","") + " stars!",bg="#222831", fg = 'white', font =  ("Calibri", 15)).place(x=130,y=275)
	Label(screen24, text = "Description: Floorcoast Hotel is a great hotel with value for money. Deluxe Rooms are much larger",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=310)
	Label(screen24, text = "Each of the 109 hotel rooms have free internet and satellite TV. Deluxe includes Sky TV.).",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=335)
	Label(screen24, text = "Great location and walking distance to many great areas in the city! Deluxe Rooms have a nice view.",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=360)
	Label(screen24, text = "Reviews:",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=390)
	Label(screen24, text = "“Comfy rooms, great for price”",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=415)
	Label(screen24, text = "“Breakfast was amazing!”",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=440)
	Label(screen24, text = "Full Address:",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=470)
	Label(screen24, text = "" + addressShown.replace("'","") + " " + cityShown.replace("'",""),bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=495)
	Label(screen24, text = "" + postShown.replace("'","") + " England",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=520)
	Label(screen24, text = "Pricing: Deluxe is £60 per night and Standard is £40 per night! Book Now using the button below",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=550)
	Button(screen24, text = "Book Now", fg = '#ff2e63', bg = '#393e46', command=BookNow4).place(x = 650, y=600)
	conn.close()
	screen24.mainloop()

def hotel5():
	global screen25
	screen25 = Tk()
	screen25.title("Four Seasons")
	screen25.iconbitmap('hotel.ico')
	screen25.geometry("750x650")
	screen25.config(bg="#222831")
	Button(screen25, text = "Go back to search results",command = delete25, fg = '#ff2e63', bg = '#393e46').place(x=10,y=600)
	Label(screen25, text = "Four Seasons", fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3", font =  ("Calibri", 15)).pack()
	img1 = ImageTk.PhotoImage(Image.open('S1Resized.jfif'))
	label1= Label(image = img1)
	label1.place(x=10,y=100)
	img2 = ImageTk.PhotoImage(Image.open('S2Resized.jfif'))
	label2= Label(image = img2)
	label2.place(x=255,y=100)
	img3 = ImageTk.PhotoImage(Image.open('S3Resized.jfif'))
	label3 = Label(image=img3)
	label3.place(x=500,y=100)
	conn = sqlite3.connect('database.db')
	cur = conn.cursor() # creation of a cursor
	cur.execute("SELECT starRating FROM hotels WHERE hotelName = 'Four Seasons'")
	starsT = cur.fetchall()
	stars = []
	for x in starsT:
		temp_stars = str(x).replace('(', "").replace(',', "").replace(')', "").replace("'","")
		stars.append(float(temp_stars))
	#print(starsT) #Troubleshooting
	cur.execute("SELECT city FROM hotels WHERE hotelName = 'Four Seasons'")
	cityT = cur.fetchall()
	city = []
	for x in cityT:
		temp_city = str(x).replace('(',"").replace(',',"").replace(')',"")
		city.append(temp_city)
	#print(city) #troubleshooting
	cur.execute("SELECT address FROM hotels WHERE hotelName = 'Four Seasons'")
	addressT = cur.fetchall()
	address = []
	for x in addressT:
		temp_add = str(x).replace('(',"").replace(',',"").replace(')',"").replace("'","")
		address.append(temp_add)
	#print(address) #troubleshooting
	cur.execute("SELECT postCode FROM hotels WHERE hotelName = 'Four Seasons'")
	postCodeT = cur.fetchall()
	postCode = []
	for x in postCodeT:
		temp_pc = str(x).replace('(',"").replace(',',"").replace(')',"").replace("'","")
		postCode.append(temp_pc)
	#print(postCode) #troubleshooting
	cityShown = city[0]
	cityShown = str(cityShown)
	starRatingShown = stars[0]
	starRatingShown = str(starRatingShown)
	addressShown = address[0]
	addressShown = str(addressShown)
	postShown = postCode[0]
	postShown = str(postShown)
	Label(screen25, text = "Welcome to Four Seasons in " + cityShown.replace("'","") + " rated at " + starRatingShown.replace("'","") + " stars!",bg="#222831", fg = 'white', font =  ("Calibri", 15)).place(x=130,y=275)
	Label(screen25, text = "Description: Four Seasons is a incredible place to stay",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=310)
	Label(screen25, text = "Each of the 86 hotel rooms have fast WiFi and great Virgin Media TV.",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=335)
	Label(screen25, text = "Great location and walking distance to many great areas in the city!",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=360)
	Label(screen25, text = "Deluxe rooms are larger, better for family or luxary. They include faster WiFi and a nice balcony",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=385)
	Label(screen25, text = "Reviews:",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=405)
	Label(screen25, text = "“WiFi was really great, unexpected”",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=430)
	Label(screen25, text = "“Exceptional service, great experience”",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=455)
	Label(screen25, text = "Full Address:",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=480)
	Label(screen25, text = "" + addressShown.replace("'","") + " " + cityShown.replace("'",""),bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=505)
	Label(screen25, text = "" + postShown.replace("'","") + " England",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=525)
	Label(screen25, text = "Pricing: Deluxe is £74 per night and Standard is £45 per night! Book Now using the button below",bg="#222831", fg = 'white', font =  ("Calibri", 12)).place(x=20,y=555)
	Button(screen25, text = "Book Now", fg = '#ff2e63', bg = '#393e46', command=BookNow5).place(x = 650, y=600)
	conn.close()
	screen25.mainloop()

def viewAll():
	global cityArray
	cityArray = ["Adiance Hotel","Azure Holidays","Collosall Resort","Floorcoast Hotel","Four Seasons"]
	searchResult()

def calendarValidate():
	global raw_date
	chosenDate = str(cal.get_date())
	currentDate = str(raw_date)
	cuYear = raw_date.year
	cuMonth = raw_date.month
	chYear = ""
	chMonth = "" +chosenDate[0] + chosenDate[1] 
	cuDay = raw_date.day
	chDay = "" + chosenDate[3] + chosenDate[4]
	if '/' in chDay and chMonth:
		print()
	else:
		chYear = "20"+chosenDate[6]+chosenDate[7]
	if '/' in chDay:
		chDay = chosenDate[2]+chosenDate[3]
	if '/' in chDay and '/' not in chMonth:
		chDay = chosenDate[3]
		chYear = "20"+chosenDate[5]+chosenDate[6]
	if '/' in chMonth:
		chMonth = chosenDate[0]
		if '/' in chDay:
			chDay = chosenDate[2]
			chYear = "20"+chosenDate[4]+chosenDate[5]
		else:
			chYear = "20"+chosenDate[5]+chosenDate[6]
	ciYear = int(chYear)
	ciMonth = int(chMonth)
	ciDay = int(chDay)
	if ciYear > 2023:
		return False
	elif ciYear < cuYear:
		return False
	elif ciYear > cuYear:
		return True
	elif ciYear == cuYear:
		if ciMonth > cuMonth:
			return True
		elif ciMonth < cuMonth:
			return False
		else:
			if ciDay > cuDay:
				return True
			elif ciDay < cuDay:
				return False
			else:
				return False



def refGenerator():
	global refBk
	global refBk1
	global randomNumber
	randomNumber = random.randint(99,999)
	randomNumber1 = str(randomNumber)
	refBk = "REF-INT-"+randomNumber1+"-HTLS"
	refBk1 = StringVar()
	refBk1.set(refBk)
	priceCalculation()

def priceCalculation():
	global hotelName1
	global totalPrice1
	global totalPrice
	hotelName1 = hotelEntry.get()
	nights = nightsNo.get()
	int(nights)
	if hotelName1 == "Azure Holidays":
		if roomClass == "D":
			totalPrice = 29*nights
		else:
			totalPrice = 20*nights
	elif hotelName1 == "Four Seasons":
		if roomClass == "D":
			totalPrice = 74*nights
		else:
			totalPrice = 45*nights
	elif hotelName1 == "Colossal Resort":
		if roomClass == "D": 
			totalPrice = 25*nights
		else:
			totalPrice = 15*nights
	elif hotelName1 == "Adiance Hotel":
		if roomClass == "D":
			totalPrice = 100*nights
		else:
			totalPrice = 85*nights
	elif hotelName1 == "Floorcoast":
		if roomClass == "D":
			totalPrice = 60*nights
		else:
			totalPrice = 40*nights
	int(totalPrice)
	totalPrice1 = IntVar()
	totalPrice1.set(totalPrice)
	successBooking()


def successBooking():
	global BkScreen
	BkScreen = Tk()
	bookingscreen.destroy()
	BkScreen.title('Success Booking')
	BkScreen.geometry('400x200')
	BkScreen.iconbitmap('hotel.ico')
	BkScreen.config(bg="#222831")
	Label(BkScreen, text = "Successful Booking", fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3").pack()
	Label(BkScreen, text = "",bg="#222831", fg = 'white').pack()
	Label(BkScreen, text = ""+refBk,bg="#222831", fg = 'white').pack()
	Label(BkScreen, text = "A confirmation email has been sent to your registered email",bg="#222831", fg = 'white').pack()
	Label(BkScreen, text = "Total Price: £"+str(totalPrice),bg="#222831", fg = 'white').pack()
	Label(BkScreen, text = "",bg="#222831", fg = 'white').pack()
	Button(BkScreen, text = "Go back to main page", fg = "red", command = delete26).pack()
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO Bookings VALUES (:user, :hotel, :class, :people, :sdate, :nights, :price, :ref)",
              {
                    'user': username_verify.get(),
                    'hotel': hotelEntry.get(),     
                    'class': roomClass.get(),
                    'people': peopleNo.get(),
                    'sdate': cal.get_date(),
                    'nights': nightsNo.get(),
                    'price': totalPrice1.get(),
                    'ref': refBk1.get()
              })
	conn.commit()
	cur.execute("SELECT myemail FROM mydatabase1 WHERE user_name = (:username_placeholder1)",
              {
                    'username_placeholder1': username_verify.get()
              })
	emails =  cur.fetchall()
	result1 = []
	for row1 in emails:
		temp_email = str(row1).replace('(', "").replace(',', "").replace(')', "")
		result1.append(str(temp_email))
	emailReceiver = result1[0]
	emailReceiver = emailReceiver.replace("'", "")
	conn.commit()
	conn.close()
	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = config['email']
	receiver_email = str(emailReceiver)
	password = config['password']
	message = """\
	Subject: Hi There

	Thanks for choosing Infinity Hotels, your booking has successfully gone through. You can view details about your bookings through the application

	Kind Regards,
	Infinity Hotels."""
	context = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, port) as server:
		server.ehlo()  # Can be omitted
		server.starttls(context=context)
		server.ehlo()  # Can be omitted
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)

def formError():
	return

def formError():
	return

def validateBooking():
	if calendarValidate() == True and hotelEntry != "" and roomClass != "":
		refGenerator()
	else:
		formError()

def booking_page():
	global bookingscreen
	global raw_date
	global hotelEntry
	global cal
	global nightsNo
	global roomClass
	global peopleNo
	raw_date = date.today()
	screen6.attributes('-topmost',False)
	bookingscreen = Tk()
	bookingscreen.title('Booking Page')
	bookingscreen.iconbitmap('hotel.ico')
	bookingscreen.geometry('1250x350')
	bookingscreen.config(bg="#222831")
	Button(bookingscreen, text = "Press to go back", fg = "red", command = delete13).pack()
	Label(bookingscreen, text = 'Please fill in fields below', fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3").pack()
	Label(bookingscreen, text = 'Enter your check-in date below (cannot be above 2023):',bg="#222831", fg = 'white').place(x=15,y=78)
	cal = Calendar(bookingscreen, selectmode ="day", year = raw_date.year, month = raw_date.month, day = raw_date.day)
	cal.place(x=15,y=100)
	hotelEntry = StringVar()
	Label(bookingscreen, text = "Enter the Hotel you will be booking:",bg="#222831", fg = 'white').place(x=300,y=100)
	Radiobutton(bookingscreen, text = "Adiance Hotel", variable = hotelEntry, value = "Adiance Hotel", bg="#222831", fg = 'white',selectcolor='black').place(x=300,y=120)
	Radiobutton(bookingscreen, text = "Azure Holidays", variable = hotelEntry, value = "Azure Holidays",  bg="#222831", fg = 'white',selectcolor='black').place(x=300,y=140)
	Radiobutton(bookingscreen, text = "Colosall Resort", variable = hotelEntry, value = "Colossal Resort", bg="#222831", fg = 'white',selectcolor='black').place(x=300,y=160)
	Radiobutton(bookingscreen, text = "Four Seasons", variable = hotelEntry, value = "Four Seasons", bg="#222831", fg = 'white',selectcolor='black').place(x=300,y=180)
	Radiobutton(bookingscreen, text = "Floorcoast Hotel", variable = hotelEntry, value = "Floorcoast",bg="#222831", fg = 'white',selectcolor='black').place(x=300,y=200)
	nightsNo = IntVar()
	Label(bookingscreen, text = "Enter the amount of nights you will be staying for:",bg="#222831", fg = 'white').place(x=525,y=100)
	Scale(bookingscreen, variable = nightsNo, from_=1, to = 50,orient=HORIZONTAL).place(x=530, y=130)
	Label(bookingscreen, text = "Enter the room class:",bg="#222831", fg = 'white').place(x=800,y=100)
	roomClass = StringVar()
	Radiobutton(bookingscreen, text = "Standard Room", variable = roomClass, value = 'S', bg="#222831", fg = 'white',selectcolor='black').place(x=800,y=120)
	Radiobutton(bookingscreen, text = "Deluxe Room", variable = roomClass, value = 'D', bg="#222831", fg = 'white',selectcolor='black').place(x=800,y=140)
	peopleNo = IntVar()
	Label(bookingscreen, text = "Enter the amount of people will be staying:",bg="#222831", fg = 'white').place(x=950,y=100)
	Scale(bookingscreen, variable = peopleNo, from_=1, to = 10,orient=HORIZONTAL).place(x=950, y=130)
	Button(bookingscreen, text = "Submit Booking", command = validateBooking).place(x=1150,y=320)
	bookingscreen.mainloop()


def noResult():
	global screen19
	screen19 = Toplevel(screen9)
	screen19.title("No Results")
	screen19.iconbitmap('error.ico')
	screen19.geometry("200x90")
	Label(screen19, text = "No Hotel Results Found").pack()
	Button(screen19, text = "OK", command = delete18).pack()

def latest_bookings():
	global latestB_screen
	global bookings
	screen6.attributes('-topmost',False)
	latestB_screen = Toplevel(screen6)
	latestB_screen.title('Latest Bookings')
	latestB_screen.iconbitmap('hotel.ico')
	latestB_screen.geometry("915x350")
	latestB_screen.config(bg="#222831")
	Button(latestB_screen, text = "Press to go back", fg = "red", command = delete14).pack()
	Label(latestB_screen, text = "Below are your latest bookings, if any exist.", fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3").pack()
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM Bookings WHERE Username = (:username_placeholder5) ORDER BY rowid DESC LIMIT 0,3",
			{
					'username_placeholder5': username_verify.get()
			})
	bookings = cur.fetchall()
	if checkBookings() == False:
		latestB_screen.destroy()
		noBookings()
	else:
		print("")
	cur.execute("SELECT lname FROM mydatabase1 WHERE user_name = (:username_placeholder4)",
    	{
    				'username_placeholder4':username_verify.get()
    	})
	lastname = cur.fetchall()
	result4 = []
	for x in lastname:
		temp_lname = str(x).replace('(',"").replace(',',"").replace(')',"")
		result4.append(str(temp_lname))
		lname_shown = result4[0]
	fullname = str(fname_shown + " " + lname_shown)
	conn.close()
	Label(latestB_screen, text = "Full Name:   " + fullname.replace("''","").replace("'",""),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=15,y=85)
	Label(latestB_screen, text= "Hotel Name:   " + bookings[0][1],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=15,y=110)
	Label(latestB_screen, text ="Room Class:   " + bookings[0][2],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=15,y=135)
	Label(latestB_screen, text= "Number Of People:   " + str(bookings[0][3]),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=15,y=160)
	Label(latestB_screen, text ="Start Date:   " + bookings[0][4],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=15,y=185)
	Label(latestB_screen, text= "Number Of Nights:   " + str(bookings[0][5]),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=15,y=210)
	Label(latestB_screen, text ="Price:   £" + str(bookings[0][6]),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=15,y=235)
	Label(latestB_screen, text= "Reference Code:   " + bookings[0][7],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=15,y=260)
	if len(bookings) >= 2:
		Label(latestB_screen, text = "Full Name:   " + fullname.replace("''","").replace("'",""),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=320,y=85)
		Label(latestB_screen, text= "Hotel Name:   " + bookings[1][1],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=320,y=110)
		Label(latestB_screen, text ="Room Class:   " + bookings[1][2],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=320,y=135)
		Label(latestB_screen, text= "Number Of People:   " + str(bookings[1][3]),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=320,y=160)
		Label(latestB_screen, text ="Start Date:   " + bookings[1][4],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=320,y=185)
		Label(latestB_screen, text= "Number Of Nights:   " + str(bookings[1][5]),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=320,y=210)
		Label(latestB_screen, text ="Price:   £" + str(bookings[1][6]),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=320,y=235)
		Label(latestB_screen, text= "Reference Code:   " + bookings[1][7],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=320,y=260)
	if len(bookings) >= 3:
		Label(latestB_screen, text = "Full Name:   " + fullname.replace("''","").replace("'",""),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=625,y=85)
		Label(latestB_screen, text= "Hotel Name:   " + bookings[2][1],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=625,y=110)
		Label(latestB_screen, text ="Room Class:   " + bookings[2][2],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=625,y=135)
		Label(latestB_screen, text= "Number Of People:   " + str(bookings[2][3]),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=625,y=160)
		Label(latestB_screen, text ="Start Date:   " + bookings[2][4],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=625,y=185)
		Label(latestB_screen, text= "Number Of Nights:   " + str(bookings[2][5]),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=625,y=210)
		Label(latestB_screen, text ="Price:   £" + str(bookings[2][6]),bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=625,y=235)
		Label(latestB_screen, text= "Reference Code:   " + bookings[2][7],bg="#222831", fg = 'white', font = ('Calibri', 14)).place(x=625,y=260)		

	
def checkBookings():
	if len(bookings) > 0:
		return True
	else:
		return False

def noBookings():
	global noBookings
	noBookings = Toplevel(screen6)
	noBookings.title("No Results")
	noBookings.iconbitmap('error.ico')
	noBookings.geometry("200x90")
	Label(noBookings, text = "No Bookings Found").pack()
	Button(noBookings, text = "OK", command = delete27).pack()


def account_details():
	global screen10
	global currentUser
	cur.execute("SELECT lname FROM mydatabase1 WHERE user_name = (:username_placeholder4)",
		{
					'username_placeholder4':username_verify.get()
		})
	lastname = cur.fetchall()
	result4 = []
	for x in lastname:
		temp_lname = str(x).replace('(',"").replace(',',"").replace(')',"")
		result4.append(str(temp_lname))
	global lname_shown
	lname_shown = result4[0]
	fullname = str(fname_shown + " " + lname_shown)
	screen6.attributes('-topmost',False)
	screen10 = Toplevel(screen6)
	screen10.title('Account Details')
	screen10.geometry("400x400")
	screen10.iconbitmap('hotel.ico')
	currentUser=username1
	Label(screen10, text = "Account Details", fg = "black", bg = "grey", width = "500", height = "3").pack()
	Label(screen10, text = "").pack()
	Label(screen10, text = "Full Name:   " + fullname.replace("''","").replace("'",""), font = ('Calibri', 14)).pack()
	Label(screen10, text = "").pack()
	Label(screen10, text = "Your username:   " + username1, font = ('Calibri', 14)).pack()
	Label(screen10, text = "").pack()
	Label(screen10, text = "Your password:   " + password1, font = ('Calibri', 14)).pack()
	Label(screen10, text = "").pack()
	cur.execute("SELECT myemail FROM mydatabase1 WHERE user_name = (:username_placeholder1)",
				{
					'username_placeholder1': username_verify.get()
				})
	emails =  cur.fetchall()
	result1 = []
	for row1 in emails:
		temp_email = str(row1).replace('(', "").replace(',', "").replace(')', "")
		result1.append(str(temp_email))
	cur.execute("SELECT myphone FROM mydatabase1 WHERE user_name = (:username_placeholder2)",
				{
					'username_placeholder2': username_verify.get()
				})
	phones =  cur.fetchall()
	result2 = []
	for row2 in phones:
		temp_phone = str(row2).replace('(', "").replace(',', "").replace(')', "")
		result2.append(str(temp_phone))
	conn.commit()
	conn.close()
	global email_shown
	email_shown = result1[0]
	phone_shown = result2[0]
	Label(screen10, text = "Your email:   " + email_shown.replace("'", ""), font = ('Calibri', 14)).pack()
	Label(screen10, text = "").pack()
	Label(screen10, text = "Your phone:   " + phone_shown.replace("'", ""), font = ('Calibri', 14)).pack()
	Label(screen10, text = "").pack()
	Button(screen10, text = "Delete Account", fg = 'white', bg = 'black', command = delAccount).pack()
	Label(screen10, text = "").pack()
	Button(screen10, text = "Return to main screen", command=delete10).pack()

    
def error():
    global screen7
    screen7 = Toplevel(screen)
    screen7.geometry("200x90")
    screen7.title("Warning!")
    screen7.iconbitmap('error.ico')
    Label(screen7, text = "All fields must be filled correctly", fg = "red").pack()
    Button(screen7, text = "Ok", command = delete5).pack()

def error_email():
    global screen13
    screen13 = Toplevel(screen1)
    screen13.geometry("200x90")
    screen13.iconbitmap('error.ico')
    Label(screen13, text = "Email entered isn't valid", fg = "red").pack()
    Button(screen13, text = "Ok", command = delete).pack()

def helpscreen():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Help")
    screen8.geometry("900x335")
    screen8.iconbitmap('hotel.ico')
    Label(screen8, text = "Help on Registering with us!", fg = "black", bg = "grey", width = "500", height = "3").pack()
    Label(screen8, text = "- Password must be above 6 characters and contain special character", font = ("Calibri", 15), fg = "red").pack()
    Label(screen8, text = "").pack()
    Label(screen8, text = "- Username cannot contain a special character and must be above 4 characters and can't be taken",  font = ("Calibri", 15), fg = "red").pack()
    Label(screen8,text = "").pack()
    Label(screen8, text = "- Email must be valid (must have @)",  font = ("Calibri", 15), fg = "red").pack()
    Label(screen8,text = "").pack()
    Label(screen8, text = "- Phone number must be a valid UK number (API is used)",  font = ("Calibri", 15), fg = "red").pack()
    Label(screen8,text = "").pack()
    Label(screen8, text = " Your first and last name must not include any special characters or numbers",  font = ("Calibri", 15), fg = "red" ).pack()
    Label(screen8,text = "").pack()
    Button(screen8, text = "Press to go back", fg = "red", command = deletehelp).pack()
    
def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    screen3.iconbitmap('hotel.ico')
    Label(screen3, text = "Login Success").pack()
    Button(screen3, text = "Ok", command = delete2).pack()

def session():
	global screen6
	screen6 = Tk()
	screen6.attributes('-topmost',True)
	screen6.title("Dashboard")
	screen6.geometry("400x400")
	screen6.iconbitmap('hotel.ico')
	conn = sqlite3.connect('database.db')
	cur =  conn.cursor()
	cur.execute("SELECT fname FROM mydatabase1 WHERE user_name = (:username_placeholder3)",
		{
					'username_placeholder3':username_verify.get()
		})
	firstname = cur.fetchall()
	result3 = []
	for x in firstname:
		temp_fname = str(x).replace('(',"").replace(',',"").replace(')',"")
		result3.append(str(temp_fname))
	global fname_shown
	fname_shown = result3[0]
	fname_shown = fname_shown.replace("'","")
	conn.close()
	Label(screen6, text = "Welcome to the dashboard, " + fname_shown , fg = "black", bg = "grey", width = "500", height = "3").pack()
	Button(screen6, text = "Go to Booking Page", command = booking_page).pack() 
	Label(screen6, text = "").pack()
	Button(screen6, text = "View Hotels", command = view_hotels).pack() 
	Label(screen6, text = "").pack()
	Button(screen6, text = "View Latest Booking", command = latest_bookings).pack() 
	Label(screen6, text = "").pack()
	Button(screen6, text = "View Account Details", command = account_details).pack()   
	Label(screen6, text = "").pack()
	Label(screen6, text = "To start a booking:").pack()
	Label(screen6, text = "- Click on Go to Booking Page").pack()
	Label(screen6, text = "- To view all our hotels press View Hotels").pack()
	Label(screen6, text = "- Check if your booking is confirmed by looking at your latest one").pack()
	Label(screen6, text = "- And to alter / check your account, click on account details").pack()
	Label(screen6, text = "").pack()
	Button(screen6, text = "Log Out", command = delete8).pack()
	delete7()
	screen6.mainloop()

def blank_error():
	global screen17
	screen17 = Toplevel(screen)
	screen17.title("Error")
	screen17.geometry("150x100")
	screen17.iconbitmap('error.ico')
	Label(screen17, text = "Fill in all required fields", fg = 'red').pack()
	Button(screen17, text = "Ok", command = delete17).pack()

def password_error():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Error")
    screen4.geometry("150x100")
    screen4.iconbitmap('error.ico')
    Label(screen4, text = "Password not recognized").pack()
    Button(screen4, text = "Ok", command = delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error")
    screen5.geometry("150x100")
    screen5.iconbitmap('error.ico')
    Label(screen5, text = "User not found").pack()
    Button(screen5, text = "Ok", command = delete4).pack()

def register_verify():
	global username_info
	global password_info
	global email_info       
	global phone_info
	global lname_info
	global fname_info
	username_info = username.get()
	password_info = password.get()
	email_info = email.get()
	phone_info = phone.get()
	fname_info = fname.get()
	lname_info = lname.get()
	if username_info == "" or password_info == "" or fname_info == "" or lname_info == "" or email_info == "" or phone_info == "":
		blank_error()
	elif username_info  == "" or username_check(username_info) == True or len(username_info) <= 4:
		user_error()
	elif user_exists_check() == True:
		user_taken()
	elif password_info == "" or check_pass(password_info) == False or len(password_info) <= 6:
		error()
	elif fname_info == "" or fname_check(fname_info) == False or len(fname_info) == 1:
		name_error()
	elif lname_info == "" or lname_check(lname_info) == False or len(lname_info) == 1:
		name_error()
	elif email_verify_api(email_info) == False:
		error_email()
	elif phone_check(phone_info) == False:
		error()
	else:
		submit_register()
		Label(screen1, text = "Registration Successful",bg="#222831",fg='green', font = ("Calibri", 11)).pack()
        
    
def hotelOptions():
    global screen12
    global hotelList
    screen12 = Toplevel(screen)
    screen12.title("Hotel Options")
    screen12.geometry("630x315")
    screen12.iconbitmap('hotel.ico')
    screen12.config(bg="#222831")
    conn = sqlite3.connect('database.db') # connection to the SQL database
    #Create a cursor
    cur = conn.cursor() # creation of a cursor
    cur.execute("SELECT hotelName FROM hotels")
    hotelList = cur.fetchall()
    Label(screen12, text = "These are the names & cities of the hotels we offer, for more details, please register by going back to the main menu", fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3").pack()
    extractArray() # a function that creates an array/list from the fetchall function of the SQL query so that it can be used for merge sort.
    Label(screen12, text = "",bg="#222831",fg='white').pack()
    Label(screen12, text = options[0] + " - London",bg="#222831",fg='white').pack()
    Label(screen12, text = "",bg="#222831",fg='white').pack()
    Label(screen12, text = options[1] + " - Manchester",bg="#222831",fg='white').pack()
    Label(screen12, text = "",bg="#222831",fg='white').pack()
    Label(screen12, text = options[2] + " - Luton",bg="#222831",fg='white').pack()
    Label(screen12, text = "",bg="#222831",fg='white').pack()
    Label(screen12, text = options[3] + " - Leeds",bg="#222831",fg='white').pack()
    Label(screen12, text = "",bg="#222831",fg='white').pack()
    Label(screen12, text = options[4] + " - Manchester",bg="#222831",fg='white').pack()
    Label(screen12, text = "",bg="#222831",fg='white').pack()
    Button(screen12, text = "Go Back",bg="#222831",fg='white', command = quit1).pack()
    conn.close()


def extractArray():
    result1 = [] 
    for row1 in hotelList:
        temp_hotel = str(row1).replace('(', "").replace(',', "").replace(')', "").replace("'","")
        result1.append(str(temp_hotel)) # appends it all to result1 to create an array to then be used in the mergesort function
    hotelNameArray = result1   #result1 is now the array, renaming for easier maintainability
    mergeSort(hotelNameArray)


def mergeSort(arr): # mergesorts the array of hotels in the database to sort the order they are viewed in
    
    if len(arr) > 1:
        leftA = arr[:len(arr)//2]
        rightA = arr[len(arr)//2:]
        #recursion
        mergeSort(leftA)
        mergeSort(rightA)
        #merge 
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index
        while i < len(leftA) and j < len(rightA):
            if leftA[i] < rightA[j]:
                arr[k] = leftA[i]
                i += 1
                k += 1
            else:
                arr[k] = rightA[j]
                j += 1
                k += 1 
        while i < len(leftA):
            arr[k] = leftA[i]
            i += 1
            k += 1

        while j < len(rightA):
            arr[k] = rightA[j]
            j += 1
            k += 1
        global options
        options = arr    




def submit_register():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO mydatabase1 VALUES (:firstn, :lastn, :u_name, :p_word, :my_email, :my_phone)",
              {
                    'firstn': fname.get(),
                    'lastn': lname.get(),     
                    'u_name': username.get(),
                    'p_word': password.get(),
                    'my_email': email.get(),
                    'my_phone': phone.get()
              })
    conn.commit()
    conn.close()
    fname_entry.delete(0, END)
    lname_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)    

def login_verify():
	global usernames
	global passwords
	global password1
	global database1
	global username1
	global username_query
	global username_oid
	username1 = username_verify.get()
	password1 = password_verify.get()
	if username1 == "":
		user_not_found()
		return
	elif password1 == "":
		password_error()
		return
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()

	cur.execute("SELECT user_name from mydatabase1 WHERE user_name = (:username_placeholder)",
				{
					'username_placeholder': username_verify.get()
				})
	username_query = cur.fetchall()
	cur.execute("SELECT oid from mydatabase1 WHERE user_name = (:username_placeholder4)",
				{
					'username_placeholder4': username_verify.get()
				})
	username_oid = cur.fetchall()
	global temp_oid1
	sql_user_v()
	if sql_user_v() == True:
		result = []
		for row in username_oid:
			temp_oid = str(row).replace('(', "").replace(',', "").replace(')', "")
			result.append(float(temp_oid))
			temp_oid1 = StringVar()
			temp_oid1.set(temp_oid)
			conn.commit()
			conn.close()
			password_sql_check()
	else:
		user_not_found()


def sql_user_v():
    if len(username_query) > 0:
        return True
    else:
        return False


def password_sql_check():
    print("To password validation success") # Troubleshooting
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT pass_word FROM mydatabase1 WHERE pass_word = (:password_placeholder) AND oid = (:oid_placeholder)",
        {
                    'password_placeholder': password_verify.get(),
                    'oid_placeholder': temp_oid1.get()
        })
    password_query = cur.fetchall()
    conn.commit()
    conn.close()
    if len(password_query) > 0:
        login_success()
    else:
        password_error()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    screen2.iconbitmap('hotel.ico')
    screen2.config(bg="#222831")
    Label(screen2, text = "Please enter credentials to login", fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3").pack()
    Label(screen2, text = "",bg="#222831").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1


    Label(screen2, text = "Username*",bg="#222831",fg = 'white').pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "",bg="#222831").pack()
    Label(screen2, text = "Password*", fg = 'white',bg="#222831").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, show = "*")
    password_entry1.pack()
    Label(screen2, text = "",bg="#222831").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify, fg = '#8F8A89', bg = "#32e0c4").pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register") 
    screen1.geometry("300x400")
    screen1.iconbitmap('hotel.ico')
    screen1.config(bg="#222831")
    Button(screen1, text = "Press to go back", fg = "red", command = delete6).pack()
    global fname
    global lname
    global fname_entry
    global lname_entry
    global username
    global password
    global username_entry
    global password_entry
    global email_entry
    global phone_entry
    global email
    global phone
    fname = StringVar()
    lname = StringVar()
    email = StringVar()
    phone = StringVar()
    username = StringVar()
    password = StringVar()
    Label(screen1, text = "Please enter credentials", fg = '#8F8A89', bg = "#32e0c4", width = "500", height = "3").pack()
    Label(screen1, text = "",bg="#222831").pack()
    Label(screen1, text = "First Name*",bg="#222831", fg = 'white').pack()
    fname_entry = Entry(screen1, textvariable = fname)
    fname_entry.pack()
    Label(screen1, text = "Last Name*",bg="#222831", fg = 'white').pack()
    lname_entry = Entry(screen1, textvariable = lname)
    lname_entry.pack()
    Label(screen1, text = "Username*",bg="#222831", fg = 'white').pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password*",bg="#222831", fg = 'white').pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "Email*",bg="#222831", fg = 'white').pack()
    email_entry = Entry(screen1, textvariable = email)
    email_entry.pack()
    Label(screen1, text = "Phone*",bg="#222831", fg = 'white').pack()
    phone_entry = Entry(screen1, textvariable = phone)
    phone_entry.pack()
    Label(screen1, text = "",bg="#222831", fg = 'white').pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_verify, fg = '#8F8A89', bg = "#32e0c4").pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("450x310")
    screen.title("Infinity Hotel Bookings System")
    screen.iconbitmap('hotel.ico')
    screen.config(bg="#222831")
    Label(text = "Infinity Hotels Bookings", fg = '#8F8A89', bg = "#32e0c4", width ="300", height = "2", font = ("Roboto Condensed", 13)).pack()
    Label(text = "",bg="#222831").pack()
    Button(text = "Login", width = "30", height = "2", command = login, fg = '#ff2e63', bg = '#393e46').pack()
    Label(text = "",bg="#222831").pack()
    Button(text = "Don't Have An Account? Register Here!",width = "30", height = "2", command = register, fg = '#ff2e63', bg = '#393e46').pack()
    Label(text = "",bg="#222831").pack()
    Button(text = "Available Hotel Options",width = "30", height = "2", command = hotelOptions, fg = '#ff2e63', bg = '#393e46').pack()
    Label(text = "",bg="#222831").pack()
    Button(text = "Help", fg = '#8F8A89', bg = "#32e0c4", command = helpscreen).pack()
    Label(screen, text="Copyright © 2021 from Infinity Hotels. All Rights Reserved. Powered by Infinity INC.", bg="grey", fg="black").pack(side = "bottom", fill ="both")

    

    screen.mainloop()

main_screen()
