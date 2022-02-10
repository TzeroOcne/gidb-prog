from cProfile import label
from re import A
import tkinter as tk
from tkinter import ttk
import json
import os
import sys

data = {}
if 'min-data.json' in os.listdir():
    with open('min-data.json', 'r') as file:
        data = json.loads(file.read())

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.vars_element = { name: tk.StringVar(self, value='') for name in [
            'Pyro',
            'Hydro',
            'Anemo',
            'Electro',
            'Dendro',
            'Cryo',
            'Geo',
        ]}

        self.vars_weapon = { name: tk.StringVar(self, value='') for name in [
            'sword',
            'bow',
            'claymore',
            'polearm',
            'catalyst',
        ]}

        self.selected_character = tk.StringVar(self, value=[ char['name'] for char in data['characters'] ])

        self.geometry('1280x720')

        tab_root = ttk.Notebook(self)
        tab_root.pack(fill='both')

        frame_view = ttk.Frame(tab_root)
        frame_modify = ttk.Frame(tab_root)

        frame_view.pack(expand=True)
        frame_modify.pack(expand=True)

        tab_root.add(frame_view, text='View')
        tab_root.add(frame_modify, text='Modify')

        tab_view = ttk.Notebook(frame_view)
        tab_view.pack(fill='both', expand=True)

        frame_view_char = ttk.Frame(tab_view)
        frame_view_char.pack(fill='both')
        tab_view.add(frame_view_char, text='Characters')

        label_elements = ttk.Label(frame_view_char, text='Elements')
        label_elements.grid(column=0, row=0, columnspan=7)
        
        for name, index in zip(self.vars_element.keys(), range(len(self.vars_element))):
            btn = ttk.Checkbutton(frame_view_char,
                text=name,
                variable=self.vars_element[name],
                onvalue=name, offvalue=''
                )
            btn.grid(column=index, row=1)
            self.vars_element[name].trace('w', self.set_filtered_characters)

        label_weapons = ttk.Label(frame_view_char, text='Weapons')
        label_weapons.grid(column=0, row=2, columnspan=7)
        
        for name, index in zip(self.vars_weapon.keys(), range(len(self.vars_element))):
            btn = ttk.Checkbutton(frame_view_char,
                text=name,
                variable=self.vars_weapon[name],
                onvalue=name, offvalue=''
                )
            btn.grid(column=index+1, row=3)
            self.vars_weapon[name].trace('w', self.set_filtered_characters)

        listbox = tk.Listbox(frame_view_char,
            listvariable=self.selected_character
            )
        listbox.grid(row=4, column=0, columnspan=7, sticky='ew')

        for i in range(frame_view_char.grid_size()[0]):
            frame_view_char.columnconfigure(i, weight=1)
    
    def get_selected_elements_list(self):
        result = [ name for name, element in self.vars_element.items() if element.get() != '' ]
        return result if len(result) > 0 else self.vars_element.keys()
    
    def get_selected_weapons_list(self):
        result = [ name for name, weapon in self.vars_weapon.items() if weapon.get() != '' ]
        return result if len(result) > 0 else self.vars_weapon.keys()
    
    def set_filtered_characters(self, *args, **kwargs):
        selected_element = self.get_selected_elements_list()
        selected_weapon = self.get_selected_weapons_list()
        self.selected_character.set([ char['name'] for char in data['characters'] if
            char['element'] in selected_element and char['weapon'] in selected_weapon ])

if __name__ == '__main__':
    app = App()
    app.mainloop()
