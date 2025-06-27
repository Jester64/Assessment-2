<h1/>Tickets Please - Event Booking Application</h1>

This application provides a graphical user interface (GUI) to view, book, and print tickets for upcoming events at select Brisbane venues. It fetches event data from venue websites, allows users to generate a printable HTML ticket, and records bookings in a local SQLite database.
📦 Features

    🎭 Select from 3 venues:

        Suncorp Stadium

        QPAC

        Rick's Bar and Cafe

    🌐 Scrape live event data from the official venue websites

    📋 View event name and date/time

    🖨️ Generate and view a printable HTML ticket for the selected event

    🗃️ Save your booking into a SQLite database (bookings.db)

    🚫 Prevent duplicate bookings (same event will disable booking)

🚀 Getting Started
<h2/>1. Install Python</h2>

Make sure Python 3 is installed on your system. You can download it here:
👉 https://www.python.org/downloads/
<h2/>2. Required Libraries</h2>

This application uses standard Python libraries and tkinter, which comes pre-installed with most Python distributions.

You also need:

pip install requests

If using a minimal Python setup, ensure the following standard modules are available:

    tkinter

    re

    urllib.request

    sqlite3

<h2/>3. Run the Application</h2>

Run the script in a Python environment that supports GUI (e.g., IDLE or via terminal):

python your_script_name.py

Make sure your script is named appropriately (e.g., main.py) and that the bookings.db file exists or is automatically created.
🛠 How It Works

    Venue Selection
    Choose a venue from the dropdown and click "Select Venue".

    View Event
    Click "Show Event" to view the name and time of the first event.

    View Details
    Click "Display Details" to open the venue's website in a browser.

    Print Ticket
    Click "Print Ticket" to generate a stylized .html ticket file with the event details and image.

    Save Booking
    Save the event details to the local database using the "Save Bookings" button.

<h2/>🧾 Project Structure</h2>

.
├── your_script.py

├── bookings.db

├── Temp_img.gif         # Icon/image used in GUI

├── [Generated_Tickets].html

├── [Downloaded_HTML].html

└── README.md

<h2/>📌 Design Notes</h2>

    GUI is built using tkinter, styled minimally for readability.

    HTML data is scraped using urllib.request.urlopen() and parsed with regex (re.findall).

    Events are stored in a local SQLite database to persist bookings.

    HTML templates are dynamically generated and customized for each event.

    Redundant bookings are prevented by checking existing database entries before enabling booking buttons.

<h2/>✅ Proof of Submission</h2>

748fbe8a-f389-49d6-81e1-5a6b2aae88f5

<h2/>📬 Contact</h2>

For any issues, feel free to contact the author of this submission.
