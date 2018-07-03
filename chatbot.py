#写経 + 少し改造

import sys
import tkinter as tk
import tkinter.messagebox as tkm
import pya3rt


apikey = "xxxxxx"
client =pya3rt.TalkClient(apikey)

root =tk.Tk()

root.title(u'chatbot')
#titlename

root.geometry('400x300')
#windowsize

def addList(text):
    mysay ="you:" +text
    print (mysay)
    ListBox1.insert(tk.END,mysay)
    chatbot ='chatbot:' + talk(text)
    Entry1.delete(0,tk.END)
    addRep(chatbot)

def addRep(chatbot):
    ListBox1.insert(tk.END,chatbot)

def talk(say):
    if say == 'end':
        return('またお話しましょう')

    else:
        ans_json = client.talk(say)
        ans = ans_json['results'][0]['reply']
        print(ans)
        return (ans)

Static1 =tk.Label(text =u'botに話しかけよう！▼')
Static1.pack()


Entry1 =tk.Entry(width =50)
Entry1.insert(tk.END, u'こんにちは')
Entry1.pack()

Button1 = tk.Button(text =u'はなす', width=50, command=lambda: addList(Entry1.get()))
Button1.pack()

ListBox1 = tk.Listbox(width=55,height =14)
ListBox1.pack()

root.mainloop()
