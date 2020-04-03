import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, font, colorchooser,filedialog
import os

main_application_win = tk.Tk()
main_application_win.geometry('1000x600')
main_application_win.title('Text Editor Written on Python by MUHAMMAD ANAS')


##################################### main menu  #####################################
main_menu = tk.Menu()   # here we create our menu bar of text editor

# Creating Menu's on my Menu bar

# FILE MENU
file_menu = tk.Menu(main_menu,tearoff = False)

# ICONS MAKING
new_icon = tk.PhotoImage(file='icons/new.png')
open_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save.png')
save_as_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')


# EDIT MENU

edit_menu = tk.Menu(main_menu,tearoff = False)

# ICONS MAKING
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file='icons/find.png')


# VIEW MENU

view_menu = tk.Menu(main_menu,tearoff = False)

# ICONS MAKING
tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')



# THEME MENU

theme_menu = tk.Menu(main_menu,tearoff = False)

# ICONS MAKING
light_default_icon = tk.PhotoImage(file='icons/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
dark_icon = tk.PhotoImage(file='icons/dark.png')
red_icon = tk.PhotoImage(file='icons/red.png')
monokai_icon = tk.PhotoImage(file='icons/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light (default)' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#474747','#d3b774'),
    'Night Blue' : ('#ededed','#6b9dc2'),
}



# # # # # # # # # # add sub Menu to every menu


# # # # Use add_cascade function to make all these menus appear on the menu bar
main_menu.add_cascade(label = 'File', menu = file_menu)
main_menu.add_cascade(label = 'Edit', menu = edit_menu)
main_menu.add_cascade(label = 'View', menu = view_menu)
main_menu.add_cascade(label = 'Theme', menu = theme_menu)


# -----------------------------&&&&&&& End main menu &&&&&&&---------------------------


##################################### toolbar  #####################################
tool_bar = tk.Label(main_application_win)
tool_bar.pack(side = tk.TOP, fill = tk.X)

# # FONT BOX
font_tuple = tk.font.families()
font_family = tk.StringVar()

# print(tk.font.families())

font_box = ttk.Combobox(tool_bar, width = 30, textvariable = font_family, state = 'readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('fixed'))
font_box.grid(row=0, column=0, padx=5)

# # TEXT SIZE BOX
font_size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width = 14, textvariable = font_size_var, state = 'readonly' )
font_size['values'] = tuple(range(8,81,2))
font_size.current(6)
font_size.grid(row=0, column=1, padx=5)



# # BOLD BUTTON
bold_icon = tk.PhotoImage(file='icons/bold.png')

bold_button = ttk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=0, column=2)

# # ITALIC BUTTON
italic_icon = tk.PhotoImage(file='icons/italic.png')

italic_button = ttk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0, column=3)

# # UNDERLINE BUTTON
underline_icon = tk.PhotoImage(file='icons/underline.png')

underline_button = ttk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=0, column=4)



# # FONT COLOUR BUTTON
font_color_icon = tk.PhotoImage(file='icons/font_color.png')

font_color_button = ttk.Button(tool_bar, image=font_color_icon)
font_color_button.grid(row=0, column=5, padx=5)



# # ALIGN LEFT
align_left_icon = tk.PhotoImage(file='icons/align_left.png')

align_left_button = ttk.Button(tool_bar, image=align_left_icon)
align_left_button.grid(row=0, column=6)


# # ALIGN CENTER
align_center_icon = tk.PhotoImage(file='icons/align_center.png')

align_center_button = ttk.Button(tool_bar, image=align_center_icon)
align_center_button.grid(row=0, column=7)


# # ALIGN RIGHT
align_right_icon = tk.PhotoImage(file='icons/align_right.png')

align_right_button = ttk.Button(tool_bar, image=align_right_icon)
align_right_button.grid(row=0, column=8)



# -----------------------------&&&&&&& End toolbar &&&&&&&---------------------------


##################################### text editor  #####################################
# # # MAIN TEXT EDITOR CODING
# text_editor = tk.Text(main_application_win)
# text_editor.config(wrap = 'word', relief= tk.FLAT)

# # # # # # # # # ORDER OF SCROLL BAR COMMANDS IS NECESSARY OTHERWISE THERE IS SOME DIFFERENT TYPE OD OUTPUT

# # SCROLL BAR coding

text_editor = tk.Text(main_application_win)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application_win)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


# this function is used to change the font of program

current_font_family = 'fixed'
current_font_size = 14

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_font_size(event=None):
    global current_font_size
    current_font_size = font_size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_font_size)



#BOLD BUTTON FUNCTIONALITY 
def change_bold():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['weight'] == 'normal' and text_property.actual()['slant'] == 'roman':
        text_editor.configure(font= (current_font_family, current_font_size, 'bold','roman'))
    elif text_property.actual()['weight'] == 'bold' and text_property.actual()['slant'] == 'italic':
        text_editor.configure(font= (current_font_family, current_font_size, 'normal','italic'))   
    elif text_property.actual()['weight'] == 'normal' and text_property.actual()['slant'] == 'italic':
        text_editor.configure(font= (current_font_family, current_font_size, 'bold','italic'))
    elif text_property.actual()['weight'] == 'bold' and text_property.actual()['slant'] == 'roman':
        text_editor.configure(font= (current_font_family, current_font_size, 'normal','roman')) 
    

bold_button.configure(command = change_bold)


# ITALIC BUTTON FUNCTIONALITY 
def change_italic():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['weight'] == 'normal' and text_property.actual()['slant'] == 'roman':
        text_editor.configure(font= (current_font_family, current_font_size, 'normal','italic'))
    elif text_property.actual()['weight'] == 'bold' and text_property.actual()['slant'] == 'italic':
        text_editor.configure(font= (current_font_family, current_font_size, 'bold','roman'))   
    elif text_property.actual()['weight'] == 'normal' and text_property.actual()['slant'] == 'italic':
        text_editor.configure(font= (current_font_family, current_font_size, 'normal','roman'))
    elif text_property.actual()['weight'] == 'bold' and text_property.actual()['slant'] == 'roman':
        text_editor.configure(font= (current_font_family, current_font_size, 'bold','italic'))
        

italic_button.configure(command = change_italic)


# UNDERLINE BUTTON FUNCTIONALITY 
def change_underline():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font= (current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font= (current_font_family, current_font_size, 'normal'))
    
    # if text_property.actual()['weight'] == 'normal' and text_property.actual()['slant'] == 'roman':
    #     text_editor.configure(font= (current_font_family, current_font_size, 'normal','roman',1))
    
    # if text_property.actual()['weight'] == 'bold' and text_property.actual()['slant'] == 'roman':
    #     text_editor.configure(font= (current_font_family, current_font_size, 'bold','roman',1))
   
    # if text_property.actual()['weight'] == 'bold' and text_property.actual()['slant'] == 'italic':
    #     text_editor.configure(font= (current_font_family, current_font_size, 'bold','italic',1))

    # if text_property.actual()['weight'] == 'normal' and text_property.actual()['slant'] == 'italic':
    #     text_editor.configure(font= (current_font_family, current_font_size, 'normal','italic',1))    

underline_button.configure(command = change_underline)


# CHANGING FONT COLOUR
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    # print(color_var)  # run this command to see why I use 1 index in text editor
    text_editor.configure(foreground= color_var[1])

font_color_button.configure(command=change_font_color)

# FUNCTION TO ALIGN LEFT
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left') 

align_left_button.configure(command= align_left)


# FUNCTION TO ALIGN CENTER
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_button.configure(command= align_center)


# FUNCTION TO ALIGN RIGHT
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_button.configure(command= align_right)




text_editor.configure(font= ('fixed',14))



# -----------------------------&&&&&&& End text editor &&&&&&&---------------------------


##################################### Status Bar  ##############################################################

status_bar = ttk.Label(main_application_win, text = f'Status Bar')
status_bar.pack(side = tk.BOTTOM)

text_changed = False
def status_change(event= None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f"characters: {characters}   words: {words}")
    text_editor.edit_modified(False)

status_bar.bind_all("<<Modified>>", status_change)

# -----------------------------&&&&&&& End Status Bar &&&&&&&-----------------------------------------------

##################################### main menu functionality  #####################################
# variable
url = ''

# NEW FUNCTIONALITY
def new_file(event=None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)

# OPEN FUNCTIONALITY
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select Files', filetypes=(('Text File', '*.txt',),("All Files", "*.*")))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application_win.title(os.path.basename(url))

# Save Functionality
def save_file(event= None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='UTF-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt',filetypes=(('Text File', '*.txt',),("All Files", "*.*")))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

# Save As functionality
def save_as_file(event= None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt',filetypes=(('Text File', '*.txt',),("All Files", "*.*")))
        url.write(content)
        url.close()
    except:
        return

# Exit functionality
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application_win.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application_win.destroy()
            elif mbox is False:
                main_application_win.destroy()
        else:
            main_application_win.destroy()
    except:
        return 



# adding sub menus to file
file_menu.add_command(label = 'New', image = new_icon, compound = tk.LEFT, accelerator = 'Ctrl+N', command = new_file) #compond is used to set the position of label on the left side of picture 
file_menu.add_command(label = 'Open', image = open_icon, compound = tk.LEFT, accelerator = 'Ctrl+O', command= open_file) # accelerator is used to add more text after text
file_menu.add_separator()   #add_seperator function is used to add simple line after these two lines
file_menu.add_command(label = 'Save', image = save_icon, compound = tk.LEFT, accelerator = 'Ctrl+S', command = save_file)
file_menu.add_command(label = 'Save as', image = save_as_icon, compound = tk.LEFT, accelerator = 'Ctrl+Shift+S', command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label = 'Exit', image = exit_icon, compound = tk.LEFT, accelerator = 'Ctrl+Q', command= exit_func)

# Find Func
def find_func(event= None):
    find_dialogue_box = tk.Toplevel()
    find_dialogue_box.geometry('350x150+400+250')
    find_dialogue_box.title('Find and Replace')
    find_dialogue_box.resizable(0,0)

    # # frame
    dialogue_box_frame = ttk.LabelFrame(find_dialogue_box, text='Find/Replace')
    dialogue_box_frame.pack(pady=20)

    # labels
    text_find_label = ttk.Label(dialogue_box_frame, text= 'Find: ')
    text_replace_label = ttk.Label(dialogue_box_frame, text= 'Replace: ')

    # #Entry Boxes
    find_input = ttk.Entry(dialogue_box_frame, width=30)
    replace_input = ttk.Entry(dialogue_box_frame, width=30)

    # lable grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)
    # entry box grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex= tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}c'.lower()
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    # Buttons
    find_button = ttk.Button(dialogue_box_frame, text = 'Find', command= find)
    replace_button = ttk.Button(dialogue_box_frame, text = 'Replace', command= replace)

    # buttons grid
    find_button.grid(row=2, column=1, padx=8, pady=4)
    replace_button.grid(row=3, column=1, padx=8, pady=4)

    find_dialogue_box.mainloop()

def clear_all(event= None):
    text_editor.delete(1.0, tk.END)

# adding sub menus to edit menu
edit_menu.add_command(label = 'Copy', image = copy_icon, compound = tk.LEFT, accelerator = 'Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit_menu.add_command(label = 'Paste', image = paste_icon, compound = tk.LEFT, accelerator = 'Ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit_menu.add_command(label = 'Cut', image = cut_icon, compound = tk.LEFT, accelerator = 'Ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit_menu.add_separator()
edit_menu.add_command(label = 'Clear all', image = clear_all_icon, compound = tk.LEFT, accelerator = 'Ctrl+Shift+X', command= clear_all)
edit_menu.add_separator()
edit_menu.add_command(label = 'Find', image = find_icon, compound = tk.LEFT, accelerator = 'Ctrl+F', command= find_func)


#  VIEW  MENU
show_tool_bar = tk.BooleanVar()
show_tool_bar.set(True)
show_status_bar = tk.BooleanVar()
show_status_bar.set(True)

def hide_tool_bar():
    global show_tool_bar
    if show_tool_bar:
        tool_bar.pack_forget()
        show_tool_bar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side= tk.TOP, fill=tk.X)
        text_editor.pack(fill = tk.BOTH, expand = True)
        status_bar.pack(side = tk.BOTTOM)
        show_tool_bar = True

def hide_status_bar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar = False
    else:
        # text_editor.pack_forget()
        # tool_bar.pack_forget()
        # tool_bar.pack(side= tk.TOP, fill=tk.X)
        # text_editor.pack(fill = tk.BOTH, expand = True)
        # status_bar.pack(side = tk.BOTTOM)
        # show_status_bar = True
        status_bar.pack(side = tk.BOTTOM)
        show_status_bar = True

# adding sub-menus (combobox) to view menu
view_menu.add_checkbutton(label = 'Tool bar',onvalue=True, offvalue=0, image = tool_bar_icon, variable = show_tool_bar, compound= tk.LEFT, command= hide_tool_bar)
view_menu.add_separator()
view_menu.add_checkbutton(label = 'Status bar',onvalue=1, offvalue=False, image = status_bar_icon, variable = show_status_bar, compound= tk.LEFT, command=hide_status_bar)




# theme changing function
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background = bg_color, foreground =fg_color)

# Radio Buttons to theme menu
count = 0
for i in color_dict:
    theme_menu.add_radiobutton(label= i, image = color_icons[count],variable=theme_choice, compound = tk.LEFT, command = change_theme)
    count +=1
# -----------------------------&&&&&&& End main menu functionality &&&&&&&---------------------------



main_application_win.config(menu = main_menu) # this show menu bar on the screen

# Shortcut Key binding
main_application_win.bind("<Control-n>", new_file)
main_application_win.bind("<Control-o>", open_file)
main_application_win.bind('<Control-s>', save_file)
main_application_win.bind('<Control-Shift-S>',save_as_file)
main_application_win.bind('<Control-q>', exit_func)
main_application_win.bind('<Control-f>',find_func )
main_application_win.bind('<Control-Shift-X>', clear_all)


main_application_win.mainloop()



