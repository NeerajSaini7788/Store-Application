from tkinter import *
import backend


def get_selected_record(event):
    index = outputwindow.curselection()

    global selected_tuple
    selected_tuple = outputwindow.get(index)

    authorEntry.delete(0,END)
    authorEntry.insert(END , selected_tuple[1])

    titleEntry.delete(0,END)
    titleEntry.insert(END, selected_tuple[0])

    yearEntry.delete(0,END)
    yearEntry.insert(END, selected_tuple[2])

    isbnEntry.delete(0,END)
    isbnEntry.insert(END, selected_tuple[3])
    return selected_tuple


def view_command():
    outputwindow.delete(0,END)
    output = backend.view()
    for record in output:
        outputwindow.insert(END , record)




def search_command():
    outputwindow.delete(0,END)
    output = backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    for record in output:
        outputwindow.insert(END , record)


def add_command():
    outputwindow.delete(0,END)
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    outputwindow.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get() ))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())









window = Tk()
window.title("Store")
window.resizable(0,0)







## Buidling GUI on left to right

##labels and Entries

authorLabel = Label(window , text ="Author")
authorLabel.grid(row = 0 , column = 0 , padx = 10)

author_text = StringVar()
authorEntry = Entry(window ,  textvariable = author_text)
authorEntry.grid(row = 0 , column = 1 )


titleLabel = Label(window , text ="Title")
titleLabel.grid(row = 0 , column = 2 , padx = 10)

title_text = StringVar()
titleEntry = Entry(window , textvariable = title_text)
titleEntry.grid(row = 0 , column = 3 )

yearLabel = Label(window , text ="Year")
yearLabel.grid(row = 1 , column = 0 , padx = 10)

year_text = StringVar()
yearEntry = Entry(window , textvariable = year_text)
yearEntry.grid(row = 1 , column = 1 )


isbnLabel = Label(window , text ="ISBN")
isbnLabel.grid(row =  1, column = 2 , padx = 10)

isbn_text = StringVar()
isbnEntry = Entry(window , textvariable = isbn_text)
isbnEntry.grid(row = 1 , column = 3 )


#Output window
outputwindow = Listbox(window,height=10 , width = 35)
outputwindow.grid(row = 2 , column = 0 , rowspan = 6, columnspan =2, pady = 10, padx =10)
outputwindow.bind('<<ListboxSelect>>', get_selected_record)



scrollbar = Scrollbar(window)
scrollbar.grid(row = 2, column = 2 , rowspan = 6)


outputwindow.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = outputwindow.yview)


#adding Buttons

viewButton = Button(window , text = "View All", width = 12 , command = view_command)
viewButton.grid(row = 2 , column = 3)

searchButton = Button(window , text = "Search Entry", width = 12, command =search_command)
searchButton.grid(row = 3 , column = 3)

addButton = Button(window , text = "Add Entry", width = 12 , command = add_command)
addButton.grid(row = 4 , column = 3)

updateButton = Button(window , text = "Update", width = 12, command = update_command)
updateButton.grid(row = 5 , column = 3)

deleteButton = Button(window , text = "Delete", width = 12, command = delete_command)
deleteButton.grid(row = 6 , column = 3)

closeButton = Button(window , text = "Close", width = 12 , command = window.destroy)
closeButton.grid(row = 7 , column = 3)





window.mainloop()
