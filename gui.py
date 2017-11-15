from Tkinter import *
from indeexx import search_match


class display:

	'''Initialise the frame for the class to use as a GUI by passing the master from the main function,
	   Packing the frame to be scalable and passing it to the widgets function
	 '''

	def __init__(self, master):
		frame = Frame(master)
		frame.pack(expand=True)
		self.widgets(frame)

	''' The widget function creates the object of the imported class 'search_match' from the imported file indeexx
	It creates and packs buttons, text fields and packs them within the frame'''


	def widgets(self,frame):
		links = search_match()
		search_query = StringVar()
		keyword = StringVar()
		search_query.set("Enter the search query")
		keyword.set("Enter the keyword/url to be searched")

		def query_pass(event):

			'''Event function called when the button search is clicked, it passes the search query to the match_string
			 function of the imported file & gets the results as a list in 'return_list' variable

			 '''

			links.match_string(search_query.get(), keyword.get())

			return_list = links.match_string(search_query.get(), keyword.get())

			'''Checking for the returned values from the return_list variable
			As per the returned values, Lable is created and displayed with the appropriate message
			'''

			if (len(return_list) is 0 ):

				self.Tokens = Label(frame, fg="Black", bg="White", width=60)
				self.Tokens.config(text="Match not detected in top 10 searches")
				self.Tokens.pack()

			elif (len(return_list) != 0):

				self.Tokens = Label(frame, fg="Black", bg="White", width=60)
				self.Tokens.config(text="Match found in search results with ranks: " + str(return_list).strip('[]'))
				self.Tokens.pack()

		self.button1 = Button(frame, text="Search", fg="Black")
		self.button1.bind("<Button-1>", query_pass)
		self.button1.pack()

		self.button2 = Button(frame, text="Quit", fg="black")
		self.button2.bind("<Button-1>", quit)
		self.button2.pack()

		'''The entry1 and entry2 widgets pass the user input through variables 'search_query'and 'keyword' to the event function'''

		self.Entry1 = Entry(frame, width=50, textvariable=search_query)
		self.Entry1.pack()

		self.Entry2 = Entry(frame, width=50, textvariable=keyword)
		self.Entry2.pack()


def main():
	master = Tk()
	Buttons = display(master)
	master.mainloop()

main()
