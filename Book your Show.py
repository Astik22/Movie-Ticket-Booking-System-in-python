import tkinter as tk
from tkinter import messagebox, simpledialog

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Your Show")

        self.bill = {}
        self.movies = {
            'bollywood': ['1.Bhaiya jii', '2.Crew', '3.Shaitaan', '4.Yodha', '5.Fighter',
                          '6.Maidaan', '7.Bade Miya Chote Miya', '8.Crakk', '9.Artical 370', '10.Dunki'],
            'hollywood': ['1.Kingdom of The Planet Of The Apes', '2.The Ministry Of Ungentlemanly Warfare',
                          '3.Furiosa:A Mad Max Saga', '4.Megalopolis', '5.Mother of The Bride', '6.Challengers',
                          '7.The Fall Guy', '8.IF', '9.Godzilla x Kong:The New Empire', '10.Wicked'],
            'tollywood': ['1.', '2.HanuMan', '3.Pushpa 2', '4.Kalki', '5.Captain Miller', '6.Leo', '7.Aavesham'],
            'animation': ['1.Sing 2 ', '2.Encanto', '3.Minions:The Rise of Guru', '4.Cars', '5.Boss Baby',
                          '6.What If', '7.Arcane'],
            'anime': ['1.My Hero Academia:World Hero Misson', '2.Sword Art Online:Progressive Aria of a Starless Night',
                      '3.Dragon ball Z', '4.Death Note', '5.Naruto', '6.Pokemon']
        }

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="                   PROJECT BY Astik                       ").pack()
        tk.Label(self.root, text="--------------------Book Your Show-------------------------").pack()
        self.name_label = tk.Label(self.root, text="Enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.category_label = tk.Label(self.root, text="SELECT MOVIE TYPE: 1.Bollywood 2.Hollywood 3.Tollywood 4.Animation 5.Anime")
        self.category_label.pack()

        self.category_var = tk.StringVar()
        self.category_entry = tk.Entry(self.root, textvariable=self.category_var)
        self.category_entry.pack()
        
        self.submit_btn = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_btn.pack()

    def submit(self):
        name = self.name_entry.get()
        category = self.category_var.get()

        if not name:
            messagebox.showwarning("Input Error", "Please enter your name")
            return

        self.bill['name'] = name

        if category == '1':
            self.bill['category'] = 'bollywood'
            self.Movies(self.movies['bollywood'])
        elif category == '2':
            self.bill['category'] = 'hollywood'
            self.Movies(self.movies['hollywood'])
        elif category == '3':
           
            self.bill['category'] = 'tollywood'
            self.Movies(self.movies['tollywood'])
        elif category == '4':
            self.bill['category'] = 'animation'
            self.Movies(self.movies['animation'])
        elif category == '5':
            self.bill['category'] = 'anime'
            self.Movies(self.movies['anime'])
        else:
            messagebox.showerror("Invalid Option", "INVALID OPTION CHOSEN!")
    
    def Movies(self, movies):
        self.movie_window = tk.Toplevel(self.root)
        self.movie_window.title("Select Movie")

        tk.Label(self.movie_window, text="<< Top Showing >>").pack()
        self.movie_var = tk.StringVar()
        self.movie_listbox = tk.Listbox(self.movie_window, listvariable=self.movie_var)
        self.movie_listbox.pack()

        for movie in movies:
            self.movie_listbox.insert(tk.END, movie)

        tk.Button(self.movie_window, text="Select", command=self.select_movie).pack()

    def select_movie(self):
        selected_movie = self.movie_listbox.get(tk.ACTIVE)
        if selected_movie:
            self.bill['movie'] = selected_movie.split('.')[1].strip()
            self.show_halls()
        else:
            messagebox.showwarning("Selection Error", "Please select a movie")

    def show_halls(self):
        self.movie_window.destroy()
        self.hall_window = tk.Toplevel(self.root)
        self.hall_window.title("Select Hall")

        tk.Label(self.hall_window, text="<< Halls near You >>").pack()
        halls = ['1.Novelty-Aligang', '2.Novelty-Lalbagh', '3.Sahu-Cinemas', '4.Wave-The-Mall', '5.Inox', '6.PVR-Cinemas',
                 '7.Cinepolis-Cinemas', '8.Pratibha-Theater', '9.Shubham-Cinemas', '10.Fun-Cinemas']
        self.hall_var = tk.StringVar()
        self.hall_listbox = tk.Listbox(self.hall_window, listvariable=self.hall_var)
        self.hall_listbox.pack()

        for hall in halls:
            self.hall_listbox.insert(tk.END, hall)

        tk.Button(self.hall_window, text="Select", command=self.select_hall).pack()

    def select_hall(self):
        selected_hall = self.hall_listbox.get(tk.ACTIVE)
        if selected_hall:
            self.bill['hall'] = selected_hall.split('.')[1].strip()
            self.hall_window.destroy()
            self.buy()
        else:
            messagebox.showwarning("Selection Error", "Please select a hall")

    def buy(self):
        self.buy_window = tk.Toplevel(self.root)
        self.buy_window.title("Buy Tickets")

        tk.Label(self.buy_window, text="1.Balcony=Rs.180 2.Classic=Rs.140 3.Special=Rs.220").pack()
        self.seat_var = tk.StringVar()
        self.seat_entry = tk.Entry(self.buy_window, textvariable=self.seat_var)
        self.seat_entry.pack()

        tk.Button(self.buy_window, text="Select", command=self.buy_ticket).pack()

    def buy_ticket(self):
        seat_type = self.seat_var.get()
        if seat_type == '1':
            self.bill['seat'] = 'Balcony'
            self.bill['price'] = 180
            self.payment(180)
        elif seat_type == '2':
            self.bill['seat'] = 'Classic'
            self.bill['price'] = 140
            self.payment(140)
        elif seat_type == '3':
            self.bill['seat'] = 'Special'
            self.bill['price'] = 220
            self.payment(220)
        else:
            messagebox.showerror("Invalid Option", "INVALID OPTION CHOSEN!")

    def payment(self, ticketcash):
        self.buy_window.destroy()
        num_seats = simpledialog.askinteger("Number of Seats", "Enter number of seats:")
        self.bill['total_price'] = num_seats * ticketcash

        self.payment_window = tk.Toplevel(self.root)
        self.payment_window.title("Payment")

        tk.Label(self.payment_window, text="How would you like to pay").pack()
        payment_methods = ['1.Phone Pe', '2.Google Pay', '3.Amazon Pay', '4.Net Banking', '5.Pay at counter']
        self.payment_var = tk.StringVar()
        self.payment_listbox = tk.Listbox(self.payment_window, listvariable=self.payment_var)
        self.payment_listbox.pack()

        for method in payment_methods:
            self.payment_listbox.insert(tk.END, method)

        tk.Button(self.payment_window, text="Select", command=self.process_payment).pack()

    def process_payment(self):
        selected_payment = self.payment_listbox.get(tk.ACTIVE)
        notation = ("Pay to this number 6206426438. Tickets would be sent to your mobile as a message.\nIf not, money would be sent back in short time")
        if selected_payment:
            if selected_payment.startswith('1') or selected_payment.startswith('2') or selected_payment.startswith('3'):
                messagebox.showinfo("Payment", notation)
            elif selected_payment.startswith('4'):
                account_number = simpledialog.askinteger("Net Banking", "Enter account number:")
                if account_number:
                    messagebox.showinfo("Payment", "Amount Received. " + notation)
            elif selected_payment.startswith('5'):
                messagebox.showinfo("Payment", "Tickets would be given at counter")
            else:
                messagebox.showerror("Invalid Option", "INVALID OPTION SELECTED!")
            self.payment_window.destroy()
            self.makebill()
        else:
            messagebox.showwarning("Selection Error", "Please select a payment method")

    def makebill(self):
        bill_info = f''' 
        -------------- TICKET ---------------
        • BOOK MY SHOW MANAGEMENT •       

        MOVIE NAME : {self.bill['movie']}
        CATEGORY   : {self.bill['category']}
        SEAT       : {self.bill['seat']}
        PRICE      : ₹{self.bill['total_price']}
        HALLNAME   : {self.bill['hall']}
        -------------------------------------
        '''
        messagebox.showinfo("Ticket", bill_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
