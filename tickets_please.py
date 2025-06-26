5
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2022.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 11295881 # put your student number here as an integer
student_name   = 'James Martell' # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Tickets, Please!
#
#  In this assignment you will combine your knowledge of HTMl/CSS
#  mark-up languages with your skills in Python scripting, pattern
#  matching, databases and Graphical User Interface design to produce
#  a robust, interactive application that allows its user to view
#  and save data from multiple online sources.
#
#  See the client's briefings accompanying this file for full
#  details.
#
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#

# Import standard Python 3 modules needed to complete this assignment.
# You should not need to use any modules other than those provided
# in a standard Python 3 installation for your solution.
#
# In particular, you may NOT use any Python modules that need to be
# downloaded and installed separately, such as "Beautiful Soup" or
# "Pillow", because the markers will not have access to such modules
# and will not be able to run your code.  Only modules that are part
# of a standard Python 3 installation may be used.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from asyncio import events
from glob import glob
from msilib.schema import ComboBox
from optparse import Values
from sys import exit as abort
from turtle import heading, title
from typing import List, final

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox, Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# All the standard SQLite functions.
from sqlite3 import *

# Confirm that the student has declared their authorship.
# You must NOT change any of the code below.
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

#
#--------------------------------------------------------------------#



#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  (You are not required to use this function, but it may
# save you some effort.)
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded
    from urllib.error import URLError

    # Open the web document for reading
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                               'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            print("Warning - Request does not reveal client's true identity.")
            print("          This is both unreliable and unethical!")
            print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except URLError:
        print("Download error - Cannot access URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# To make it easy for the marker to find, use this filename
# for your ticket in Task 2B
ticket_file = 'your_ticket.html'

# Your code goes here

#Create the window
gui = Tk()
gui.title('Tickets Please')
gui.configure(bg = '#ebe9ed')

#Predefine values
vlist = ["Suncorp Stadium", "QPAC", "Rick's Bar and Cafe"] 
n = StringVar()  

#Button to lock in the selected venue
def check_venue(): 
    #Get the number of the selected venue
    selected_venue = str(venue_selection.current())

    #secure a connection to the bookings database
    connection = connect(database = 'bookings.db')
    bookings_db = connection.cursor()

    #get the name of the booked events
    check_sql = "SELECT event FROM tickets_bought"
    bookings_db.execute(check_sql)

    #give the collected name a vlaue to call from
    row_events = bookings_db.fetchall()

    #depending on the selected event run code
    if selected_venue == '0':
        #display to the user what event was chossen
        venue_info_frame['text'] = 'Selected Venue: Suncorp Stadium'
        #check whether the current event name is already in the database. If so then disable the booking button, if not then enable it
        suncorp_html = urlopen('https://suncorpstadium.com.au/what-s-on.aspx')
        suncorp_html_read = suncorp_html.read().decode('UTF-8')
        suncorp_event_name = findall('<h6 class="event-title">(.+)</h6>', suncorp_html_read)
        if str(suncorp_event_name[0]) in str(row_events):
            save_bookings['state'] = DISABLED
        else:
            save_bookings['state'] = NORMAL
        suncorp_html.close()

    elif selected_venue == '1':
        venue_info_frame['text'] = 'Selected Venue: QPAC'
        qpac_html = urlopen('https://qpac.com.au/')
        qpac_html_read = qpac_html.read().decode('UTF-8')
        qpac_event_name = findall('''<h3>\s*(.+)\s*(?:\s)<span class="date">''', qpac_html_read)
        qpac_event_name_refined = qpac_event_name[0].replace('\r', '')
        qpac_list = list(qpac_event_name_refined)
        if str(qpac_list[0]) in str(row_events):
            save_bookings['state'] = DISABLED
        else:
            save_bookings['state'] = NORMAL
        qpac_html.close()

    elif selected_venue == '2':
        venue_info_frame['text'] = "Selected Venue: Rick's bar and cafe"
        rick_html = urlopen('http://ricsbar.com.au/')
        rick_html_read = rick_html.read().decode('UTF-8')
        rick_event_name = findall('<h2>(.+)</h2>', rick_html_read)
        if str(rick_event_name[0]) in str(row_events):
            save_bookings['state'] = DISABLED
        else:
            save_bookings['state'] = NORMAL
        rick_html.close()

    #if the a venue is selected, then enable the buttons
    if selected_venue != '-1':
        show_event['state'] = NORMAL
        display_details['state'] = NORMAL
        print_ticket['state'] = NORMAL

    #save the changes made to the database and close the connection to it
    connection.commit()
    
    bookings_db.close()
    connection.close()

#Display information of the first event of the selected venue
def find_venue_info():
    #Delete info in listbox
    venue_info.delete(0, END)

    #get the selected venue's list number
    selected_venue = str(venue_selection.current())

    #depending on the selected venue
    if selected_venue == '0':
        #get the information from the venue's site and displya it in the listbox
        download('https://suncorpstadium.com.au/what-s-on.aspx', 'Suncorp_Stadium')
        suncorp_html = urlopen('https://suncorpstadium.com.au/what-s-on.aspx')
        suncorp_html_read = suncorp_html.read().decode('UTF-8')
        suncorp_event_name = findall('<h6 class="event-title">(.+)</h6>', suncorp_html_read)
        suncorp_event_time = findall('<h7 class="event-date text-uppercase">(.+)</h7>', suncorp_html_read)
        venue_info.insert(1, (suncorp_event_name[0]))
        venue_info.insert(2, (suncorp_event_time[0]))
        suncorp_html.close()

    elif selected_venue == '1':
        download('https://qpac.com.au/', 'qpac')
        qpac_html = urlopen('https://qpac.com.au/')
        qpac_html_read = qpac_html.read().decode('UTF-8')
        qpac_event_name = findall('''<h3>\s*(.+)\s*(?:\s)<span class="date">''', qpac_html_read)
        qpac_event_time = findall('''<span class="date">\s*(.+)\s*(?:\s)</span>''', qpac_html_read)
        venue_info.insert(1, (qpac_event_name[0]))
        venue_info.insert(2, (qpac_event_time[0]))
        qpac_html.close()

    elif selected_venue == '2':
        download('http://ricsbar.com.au/', 'rick')
        rick_html = urlopen('http://ricsbar.com.au/')
        rick_html_read = rick_html.read().decode('UTF-8')
        rick_event_name = findall('<h2>(.+)</h2>', rick_html_read)
        rick_event_time = findall('''<time class="datetime">(.+)</time>''', rick_html_read)
        venue_info.insert(1, (rick_event_name[0]))
        venue_info.insert(2, (rick_event_time[0]))
        rick_html.close()

#take the user to the website of the selected venue
def find_venue_page():
    selected_venue = str(venue_selection.current())

    if selected_venue == '0':
        urldisplay('https://suncorpstadium.com.au/what-s-on.aspx')

    elif selected_venue == '1':
        urldisplay('https://qpac.com.au')

    elif selected_venue == '2':
        urldisplay('http://ricsbar.com.au/')

#make a ticket for the selected venue based on the first event
def make_ticket():
    #create the html template
    ticket_text = """<!DOCTYPE html>
    <html>
    <head>
        <title>Title</title>
    </head>
    <h1>Admit One</h1>
    <h3>This is your ticket courtesy of<br>
    Hiram's Live Entertainment</h3>

    <body>
    <h2>EventName</h2>
    <img src="EventImage">
    <h2>EventLocation</h2>
    <h3>EventTime</h3>
    <br>
    <a href='EventInformation'>For more information, Click here!</a>

    </body>
    </html>
    """

    selected_venue = str(venue_selection.current())

    #depending on the selected venue, run the code
    if selected_venue == '0':
        #create a connection to the site of the venue and store some values
        suncorp_html = urlopen('https://suncorpstadium.com.au/what-s-on.aspx')
        suncorp_html_read = suncorp_html.read().decode('UTF-8')
        suncorp_event_name = findall('<h6 class="event-title">(.+)</h6>', suncorp_html_read)
        suncorp_event_time = findall('<h7 class="event-date text-uppercase">(.+)</h7>', suncorp_html_read)
        suncorp_event_image = findall('<img src="(.*)" class="cover-img-top position-absolute">', suncorp_html_read)

        #create the name of the ticket's html file
        event_ticket_name = f"{suncorp_event_name[0]}.html"

        #store the values that will be injected into the html template
        Title = 'Suncorp Event Ticket'
        Event_Name = suncorp_event_name[0]
        Event_Image = f"https://suncorpstadium.com.au{suncorp_event_image[0]}"
        Event_Location = 'Suncorp Stadium'
        Event_Time = suncorp_event_time[0]
        Event_Information = "https://suncorpstadium.com.au/what-s-on.aspx"

        suncorp_html.close()

    elif selected_venue == '1':
        qpac_html = urlopen('https://qpac.com.au/')
        qpac_html_read = qpac_html.read().decode('UTF-8')
        qpac_event_name = findall('''<h3>\s*(.+)\s*(?:\s)<span class="date">''', qpac_html_read)
        qpac_event_time = findall('''<span class="date">\s*(.+)\s*(?:\s)</span>''', qpac_html_read)
        qpac_event_image = findall('''<div class="thumb"><img src="(.*)anchor''', qpac_html_read)

        #replace \r with whitespace
        name = qpac_event_name[0]
        name = name.replace('\r','')

        event_ticket_name = f"{name}.html"

        Title = 'QPAC Event Ticket'
        Event_Name = qpac_event_name[0]
        Event_Image = f"https://qpac-umbraco-cdn.azureedge.net{qpac_event_image[0]}"
        Event_Location = 'QPAC Arts Centre'
        Event_Time = qpac_event_time[0]
        Event_Information = 'https://www.qpac.com.au/'

        qpac_html.close()

    elif selected_venue == '2':
        rick_html = urlopen('http://ricsbar.com.au/')
        rick_html_read = rick_html.read().decode('UTF-8')
        rick_event_name = findall('<h2>(.+)</h2>', rick_html_read)
        rick_event_time = findall('''<time class="datetime">(.+)</time>''', rick_html_read)
        rick_event_image = findall('''<img src="(.+)" alt="''', rick_html_read)

        event_ticket_name = f"{rick_event_name[0]}.html"

        Title = "Rics Event Ticket"
        Event_Name = rick_event_name[0]
        Event_Image = rick_event_image[0]
        Event_Location = 'Rics Cafe - Bar'
        Event_Time = rick_event_time[0]
        Event_Information = 'http://ricsbar.com.au'

    #change the information in the html template to that of the selected venue
    ticket_text = ticket_text.replace('Title', Title)
    ticket_text = ticket_text.replace('EventName', Event_Name)
    ticket_text = ticket_text.replace('EventImage', Event_Image)
    ticket_text = ticket_text.replace('EventLocation', Event_Location)
    ticket_text = ticket_text.replace('EventTime', Event_Time)
    ticket_text = ticket_text.replace('EventInformation', Event_Information)

    #create the ticket's html file
    event_ticket = open(event_ticket_name, 'w')

    #inject the edited html template into the html ticket file 
    event_ticket.write(ticket_text)

    #close the ticket html file
    event_ticket.close()

    #open the html ticket file to display to the user
    urldisplay(event_ticket_name)

#make bookings based on the selected venue's first event 
def inject_venue_info_to_database():

    selected_venue = str(venue_selection.current())

    #disable the button when it is pushed
    save_bookings['state'] = DISABLED

    if selected_venue == '0':         
        #open the connection to the selected venues website and store the needed values
        suncorp_html = open('Suncorp_Stadium.html')
        suncorp_html_read = suncorp_html.read()
        suncorp_event_name = findall('<h6 class="event-title">(.+)</h6>', suncorp_html_read)
        suncorp_event_time = findall('<h7 class="event-date text-uppercase">(.+)</h7>', suncorp_html_read)
        suncrop_event_venue = 'Suncrop Stadium'
        suncorp_event_URL = 'https://suncorpstadium.com.au/what-s-on.aspx'

        #create an sql query that holds the selected venues infromation for the first event
        event_sql = "INSERT into tickets_bought(event, date_or_dates, venue, website) VALUES('" + suncorp_event_name[0] + "', '" + suncorp_event_time[0] + "', '" \
          + suncrop_event_venue + "', '" + suncorp_event_URL + "')"

        suncorp_html.close()

    elif selected_venue == '1':

        qpac_html = urlopen('https://qpac.com.au/')
        qpac_html_read = qpac_html.read().decode('UTF-8')
        qpac_event_name = findall('''<h3>\s*(.+)\s*(?:\s)<span class="date">''', qpac_html_read)
        qpac_event_time = findall('''<span class="date">\s*(.+)\s*(?:\s)</span>''', qpac_html_read)
        qpac_event_venue = 'QPAC Centre'
        qpac_event_URL = 'https://qpac.com.au/event/'

        event_sql = "INSERT into tickets_bought(event, date_or_dates, venue, website) VALUES('" + qpac_event_name[0] + "', '" + qpac_event_time[0] + "', '" \
          + qpac_event_venue + "', '" + qpac_event_URL + "')"

        qpac_html.close()

    elif selected_venue == '2':
        rick_html = urlopen('http://ricsbar.com.au/')
        rick_html_read = rick_html.read().decode('UTF-8')
        rick_event_name = findall('<h2>(.+)</h2>', rick_html_read)
        rick_event_time = findall('''<time class="datetime">(.+)</time>''', rick_html_read)
        rick_event_venue = "Rics Cafe and Bar"
        rick_event_URL = 'http://ricsbar.com.au/'

        event_sql = "INSERT into tickets_bought(event, date_or_dates, venue, website) VALUES('" + rick_event_name[0] + "', '" + rick_event_time[0] + "', '" \
          + rick_event_venue + "', '" + rick_event_URL + "')"

        rick_html.close()

    #create the connection to the bookings database
    connection = connect(database = 'bookings.db')
    bookings_db = connection.cursor()

    #store the information in the databse
    bookings_db.execute(event_sql)

    #display the affecterd rows of the database
    row = bookings_db.fetchone()
    row2 = bookings_db.rowcount
    print(row)
    print(row2)

    #save the changes and end the connection
    connection.commit()
    
    bookings_db.close()
    connection.close()
    
#Create Widgets 
venue_selection = Combobox(gui, width = 14, textvariable = n, values = vlist, font = ('HP Simplified Hans', 10, 'bold'))
venue_selection.set('Select a Venue')  

check_venue_button = Button(gui, text = 'Select Venue', font = ('HP Simplified Hans', 10, 'bold'), command = check_venue)

venue_info_frame = LabelFrame(gui, text = 'Selected Venue: ?', font = ('HP Simplified Hans', 25, 'bold'))
venue_info = Listbox(venue_info_frame, font = ('HP Simplified Hans', 10), width = 75, relief = 'solid')

settings_frame = LabelFrame(gui, text = 'Options', font = ('HP Simplified Hans', 15, 'bold'))
show_event = Button(settings_frame, text = 'Show Event', font = ('HP Simplified Hans', 10), state = DISABLED, command = find_venue_info)
display_details = Button(settings_frame, text = 'Display details', font = ('HP Simplified Hans', 10), state = DISABLED,
                        command = find_venue_page)
print_ticket = Button(settings_frame, text = 'Print ticket', font = ('HP Simplified Hans', 10), state = DISABLED,
                        command = make_ticket)
save_bookings = Button(settings_frame, text = 'Save Bookings', font = ('HP Simplified Hans', 10), state = DISABLED,
                        command = inject_venue_info_to_database)

width_icon = 400
height_icon = 400
icon_canvas = Canvas(gui, width = width_icon, height = height_icon)
icon = PhotoImage(file = 'Temp_img.gif')
icon_canvas .create_image(width_icon/2, height_icon/2, anchor=CENTER, image = icon)

#Other stuff
thing = str('Event name will appear here')
thing2 = str('Event date(s) will apear here')
venue_info.insert(1, (thing))
venue_info.insert(2, (thing2))

#Display buttons
venue_selection.grid(column = 1, row = 0, sticky = NW, padx = 3, pady = 3)
check_venue_button.grid(column = 1, row = 0, columnspan = 1, sticky = NE, padx = 3)

venue_info_frame.grid(column = 1, row = 1, columnspan = 3, sticky = NW, padx = 3, pady =3)
venue_info.grid(column = 1, row = 1, padx = 3, pady = 3)

settings_frame.grid(column = 3, row = 0, rowspan = 1, sticky = NE, padx = 3, pady = 3)
show_event.grid(column = 0, row = 0, padx = 3, pady = 3)
display_details.grid(column = 0, row = 1, padx = 3, pady = 3)
print_ticket.grid(column = 0, row = 2, padx = 3, pady = 3)
save_bookings.grid(column = 0, row = 3, padx = 3, pady = 3)

icon_canvas.grid(column = 0, row = 0, rowspan = 2, sticky = SW, padx = 3, pady = 3, )

#proof of submission:
#748fbe8a-f389-49d6-81e1-5a6b2aae88f5

#loop the window so that it actually works
gui.mainloop()