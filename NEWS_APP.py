import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
import threading


class NewsApp:

    def __init__(self):
        # Initialize the GUI
        self.load_gui()
        # Fetch news data in a separate thread to prevent freezing
        threading.Thread(target=self.fetch_data).start()
        # Start the Tkinter main loop
        self.root.mainloop()

    def fetch_data(self):
        try:
            # Fetch data from the news API
            self.data = requests.get(
                'https://newsapi.org/v2/top-headlines?country=us&apiKey=46078ba07caa4dbf85e1d779bbd52ae1').json()
            # Schedule loading the first news item after data is fetched
            self.root.after(0, lambda: self.load_news_item(0))
        except Exception as e:
            # If there's an error, display it in the console and show a message in the app
            print("Failed to fetch data:", e)
            self.root.after(0, lambda: self.show_error_message("Failed to fetch news. Please try again later."))

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.title('Live News App')
        self.root.configure(background='black')

    def clear(self):
        for widget in self.root.pack_slaves():
            widget.destroy()

    def load_news_item(self, index):
        # Clear the screen for the new news item
        self.clear()

        # Frame for buttons
        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        # Add Prev button only if not on the first item
        if index > 0:
            prev = Button(frame, text='<Prev', width=16, height=3, command=lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        # Read more button
        read = Button(frame, text='Read More +', width=16, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        # Add Next button only if not on the last item
        if index < len(self.data['articles']) - 1:
            next = Button(frame, text='Next>', width=16, height=3, command=lambda: self.load_news_item(index + 1))
            next.pack(side=LEFT)

        # Load the image in a separate thread
        threading.Thread(target=lambda: self.load_image(index)).start()

        # Headline
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=350,
                        justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15,"bold"))

        # Date
        date= Label(self.root, text=self.data['articles'][index]['publishedAt'], bg='black', fg='white', wraplength=350,
                        justify='center')
        date.pack(pady=(10, 20))
        date.config(font=('verdana', 8))

        # Description
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                        wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))


    def load_image(self, index):
        img_url = self.data['articles'][index].get('urlToImage', None)

        # Default image URL
        default_img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
        try:
            if img_url:
                # Try loading the image with a timeout
                raw_data = urlopen(img_url, timeout=5).read()  # Set a timeout of 5 seconds
                im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
                photo = ImageTk.PhotoImage(im)
            else:
                raise Exception("Image URL not found")

        except Exception as e:
            print(f"Failed to load image: {e}")
            # Fall back to default image
            raw_data = urlopen(default_img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        # Update the image on the main thread
        self.root.after(0, lambda: self.update_image(photo))

    def update_image(self, photo):
        label = Label(self.root, image=photo, bg='black')
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack(pady=(10, 0))

    def open_link(self, url):
        webbrowser.open(url)

    def show_error_message(self, message):
        # Display an error message if fetching data fails
        self.clear()
        error_label = Label(self.root, text=message, bg='black', fg='red', wraplength=350, justify='center')
        error_label.pack(pady=(10, 20))
        error_label.config(font=('verdana', 12))


# Run the application
obj = NewsApp()
