from tkinter import *
import time
import random
x = 0

window = Tk()
window.geometry("400x200")

def game():
    global x
    if x == 0:
        window.destroy()
        x += 1

    def check_result():
        if entry.get() == sentences[sentence]:
            end = time.time()
            print(end - start)
        else:
            print("Wrong Answer")
    sentences = ['He loves to play basketball.','He goes to school.','Does he go to school?','She writes an e-mail to her best friend.','He thinks he is very handsome.','It usually rains every day here.','It smells very delicious in the kitchen.','We generally sing songs all together.','We go to a gallery every Sunday.','Does he write an email?','The sun rises at the east.','She goes to work by car.','It doesn’t rain here in the summer.','We cook every day.','We go to the gym club together.','You have a big house.','Do we know each other?','They sleep in the afternoon.','When do they usually talk to each other?','The children are at home.','The earth goes round the sun.','George brushes his teeth twice a day.','He gets up early every day.','They speak English in USA.','I like reading detective stories.','I like geography and science.','She doesn’t study German on Monday.','Does she live in Paris?','He doesn’t teach math.','Cats hate water.','Every child likes an icecream.','My mother never lies.','The Earth is spherical.','She doesn’t use a computer.','It snows a lot in winter in Russia.','We live in Texas.','You go to holiday every summer.','Do you like spaghetti?','My daughter does the laundry.','My brother takes out the trash.','The course starts next Sunday.','She swims every morning.','I don’t wash the dishes.','We see them every week.','I don’t like tea.','When does the train usually leave?','She always forgets her purse.','You don’t have children.','I and my sister don’t see each other anymore.','They don’t go to school tomorrow.'] 
    sentence = random.randint(0, (len(sentences)-1))
    start = time.time()
    windows = Tk()
    windows.geometry("800x200")

    x2 = Label(windows, text = sentences[sentence], font = "times 30")
    x2.place(x = 10, y = 10)

    x3 = Label(windows, text = "Enter the above Sentence...", font = "times 15")
    x3.place(x = 10, y = 80)

    entry = Entry(windows)
    entry.place(x = 300, y = 80)

    b2 = Button(windows, text = "SUBMIT", command = check_result, width = 12, bg = 'yellow')
    b2.place(x = 10, y = 150)

    b3 = Button(windows, text = "TRY AGAIN", command = game, width = 12, bg = 'red')
    b3.place(x = 120, y = 150)

    windows.mainloop()


x1 = Label(window, text = "Lets start this Game...", font = "times 20")
x1.place(x = 80, y = 50)

b1 = Button(window, text = "START", command = game, width = 12, bg = 'red')
b1.place(x = 150, y = 100)

window.mainloop()