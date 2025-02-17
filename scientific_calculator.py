

import tkinter as tk

class ScientificCalculator:
    def __init__(self, root):
        # set window title and size
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("600x700")

        self.create_calculator()  # Ensure buttons are created

    def create_calculator(self):
        # create a display area
        self.entry = tk.Entry(self.root, width=30, borderwidth=5, font=('Arial', 18))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # create how buttons distribute
        buttons = [
                   ('7',1,0), ('8',1,1), ('9',1,2), ('+',1,3),
                   ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
                   ('1',3,0), ('2',3,1), ('3',3,2), ('*',3,3),
                   ('0',4,0), ('.',4,1), ('/',4,2), ('=',4,3),
                   ('sin',5,0), ('cos',5,1), ('tan',5,2), ('clear',5,3),
                   ('arcsin',6,0), ('arccos',6,1), ('arctan',6,2), ('^2',6,3),
                   ('sqrt',7,0),('delete',7,1)
                  ]

        # create buttons
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=2, font=('Arial', 12),
                               command=lambda t=text: self.click_button(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def click_button(self, button_text):
        # calculate the result
        if button_text == "=":
           self.calculate_result()
        # clear the input box
        elif button_text == "clear":
            self.entry.delete(0, tk.END)
        # calculate scientific functions
        elif button_text in ("sin", "cos", "tan", "arcsin", "arccos", "arctan", "sqrt", "^2"):
            self.calculate_function(button_text)
        # delete the last character from the input field   
        elif button_text=="delete":
            # get the text in the input field
            current_text=self.entry.get()
            # ensure input field is not empty
            if current_text: 
            # delete last character
               self.entry.delete(len(current_text)-1, tk.END)  
        # add text in input box
        else:
            self.entry.insert(tk.END, button_text)
    
    # calculate math expressions
    def calculate_result(self):
        try:
            # get the expression in the input box
            expression = self.entry.get()
            # calculate the result directly
            result = eval(expression)
            # clear the input box
            self.entry.delete(0, tk.END)
            # show the result
            self.entry.insert(0, str(result))
        except Exception:
            self.entry.delete(0, tk.END)
            # show the error message
            self.entry.insert(0, "Error")

    # calculate scientific functions
    def calculate_function(self, func_name):
        try:
    # Get the input value
            value = self.entry.get()
    # Do nothing if input is empty            
            if not value:
                return
            self.entry.delete(0, tk.END)
    # Display function call in input box
            self.entry.insert(tk.END, f"{func_name}({value})")  
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()