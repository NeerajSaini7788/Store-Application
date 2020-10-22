from tkinter import *
from backend import *

window = Tk()
window.title("Store")
window.resizable(0,0)




## Buidling GUI on left to right

##labels and Entries

authorLabel = Label(window , text ="Author")
authorLabel.grid(row = 0 , column = 0 , padx = 10)

authorEntry = Entry(window)
authorEntry.grid(row = 0 , column = 1 )


titleLabel = Label(window , text ="Title")
titleLabel.grid(row = 0 , column = 2 , padx = 10)

titleEntry = Entry(window)
titleEntry.grid(row = 0 , column = 3 )

yearLabel = Label(window , text ="Year")
yearLabel.grid(row = 1 , column = 0 , padx = 10)

yearEntry = Entry(window)
yearEntry.grid(row = 1 , column = 1 )


isbnLabel = Label(window , text ="ISBN")
isbnLabel.grid(row =  1, column = 2 , padx = 10)

isbnEntry = Entry(window)
isbnEntry.grid(row = 1 , column = 3 )


#Output window
outputwindow = Listbox(window,height=10 , width = 35)
outputwindow.grid(row = 2 , column = 0 , rowspan = 6, columnspan =2, pady = 10, padx =10)


scrollbar = Scrollbar(window)
scrollbar.grid(row = 2, column = 2 , rowspan = 6)


outputwindow.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = outputwindow.yview)


#adding Buttons

viewButton = Button(window , text = "View All", width = 12)
viewButton.grid(row = 2 , column = 3)

searchButton = Button(window , text = "Search Entry", width = 12)
searchButton.grid(row = 3 , column = 3)

addButton = Button(window , text = "Add Entry", width = 12)
addButton.grid(row = 4 , column = 3)

updateButton = Button(window , text = "Update", width = 12)
updateButton.grid(row = 5 , column = 3)

deleteButton = Button(window , text = "Delete", width = 12)
deleteButton.grid(row = 6 , column = 3)

closeButton = Button(window , text = "Close", width = 12)
closeButton.grid(row = 7 , column = 3)





window.mainloop()
