
# Import required modules
from tkinter import *
from tkcalendar import Calendar, DateEntry
from datetime import date


# Define cache
env = {}


# Define content
content = {
    'home': {
        'title': 'Welcome',
        'para': 'This is the homepage, welcome here.\nFeel free to take a look around. :)'
    },
    'account': {
        'title': 'Account',
        'para': 'Welcome to your account section,\ninformation about you will be stored here.\n\nAge: Unknown\nBirthday date: Unknown'
    },
    'store': {
        'title': 'Store',
        'para': 'This is the store, soon there will be items ready for purschase.\n( Not really though, this is just a template :D )'
    },
    'settings': {
        'title': 'Settings',
        'para': 'In this section you\'d be able to tweak application related settings.'
    }
}


# Define TK and attributes
app = Tk()
app.title('Basic TK GUI')
app.geometry('500x250')
app.configure(bg='#000')


# Hook into labels
hook = {
    'text': {
        'title': StringVar(app),
        'para': StringVar(app)        
    }
}


# Set default page data
hook['text']['title'].set(content['home']['title'])
hook['text']['para'].set(content['home']['para'])


# Env frame
env['frame'] = {
    'menu': Frame(app, 
        bg='#262625', 
        width=125, 
        height=250),
    'root': Frame(app,
        bg='#000',
        width=375,
        height=250)
}


# Env label
env['label'] = {
    'root': {
        'title': Label(env['frame']['root'],
            textvariable=hook['text']['title'],
            font='Arial, 18',
            fg='#fff',
            bg='#000'),
        'para': Label(env['frame']['root'],
            textvariable=hook['text']['para'],
            font='Arial, 8',
            padx=10,
            pady=10,
            fg='#fff',
            bg='#262625')
    }
}


# Page switcher
def goTo(page):
    hook['text']['title'].set(content[page]['title'])
    hook['text']['para'].set(content[page]['para'])

    # Page specific env elements
    if page == 'account':
        env['button']['calendar'].place(
            x=10,
            y=165)
    else: 
        env['button']['calendar'].place_forget()


# Calculate age from birthdate
def getAge(bdayDate):
    today = date.today()
    return today.year - int(bdayDate.strftime('%Y')) - ((today.month, today.day) < (int(bdayDate.strftime('%m')), int(bdayDate.strftime('%d'))))


# Append calendar
def openCal():

    # Summon new popup
    top = Toplevel(app)

    # Append calendar
    cal = Calendar(top, 
        font="Arial 14", 
        selectmode='day', 
        locale='en_US',
        cursor="hand1",
        year=2003, 
        month=5, 
        day=2)

    # Visualize calendar
    cal.pack(
        fill="both", 
        expand=True)

    # Process calendar output
    def print_sel(): 
        content['account']['para'] = 'Welcome to your account section,\ninformation about you will be stored here.\n\nAge: {}\nBirthday date: {}'.format(getAge(cal.selection_get()), cal.selection_get())
        goTo('account')
        top.destroy()

    # Submit calendar input
    Button(top, 
        text="Choose this date", 
        width=60,
        bg="#262625",
        bd=0,
        fg="#fff",
        command=print_sel
    ).pack()


# Env buttons
env['button'] = {
    'home': Button(env['frame']['menu'], 
        text='Home',
        command=lambda: goTo('home'), 
        fg='white', 
        bg='#3a3a39', 
        width=15,
        height=1,
        bd=0),
    'account': Button(env['frame']['menu'], 
        text='Account',
        command=lambda: goTo('account'), 
        fg='white', 
        bg='#3a3a39', 
        width=15,
        height=1,
        bd=0),
    'store': Button(env['frame']['menu'], 
        text='Store',
        command=lambda: goTo('store'), 
        fg='white', 
        bg='#3a3a39', 
        width=15,
        height=1,
        bd=0),
    'settings': Button(env['frame']['menu'], 
        text='Settings',
        command=lambda: goTo('settings'), 
        fg='white', 
        bg='#3a3a39', 
        width=15,
        height=1,
        bd=0),
    'calendar': Button(env['frame']['root'], 
        text="Change birthday date", 
        command=openCal,
        pady=5,
        padx=52,
        bg='#3a3a39',
        fg='#fff',
        bd=0)
}


# Styling
env['frame']['menu'].grid(
    column=0, 
    row=0)
env['frame']['root'].grid(
    column=1, 
    row=0)
env['button']['home'].place(
    x=6, 
    y=12)
env['button']['account'].place(
    x=6, 
    y=39)
env['button']['store'].place(
    x=6, 
    y=66)
env['button']['settings'].place(
    x=6, 
    y=223)
env['label']['root']['title'].place(
    x=10,
    y=10)
env['label']['root']['para'].place(
    x=10,
    y=50)


# Initiate application
app.mainloop()
