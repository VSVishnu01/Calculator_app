import tkinter as tk

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
DIMGRAY = "#C1CDCD"
DARKGOLD="#FFB90F"
GREEN="#3D9140"
DARKGREY="#1E1E1E"
GREY="#333333"

class Calculator:
    def __init__(self):
        
        self.operations=''
        self.results=''
        
        #Tkinter's Quarry
        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.iconbitmap(r"img\calculator_icon.ico")
        self.root.geometry('375x667+0+0')
        self.root.resizable(0,0)
    
        #Creating the Frames
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True,
                   fill='both'
                   )
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(expand=True,
                          fill='both'
                          )
               
        #Adding the Display Labels
        #Current expression labels
        self.cu_e_labels=tk.Label(self.frame,
                           text=self.operations,
                           anchor=tk.E,
                           padx=24,
                           font=('arial',25),
                           background=DARKGREY,
                           foreground=DIMGRAY,
                           borderwidth=0,
                           )
        self.cu_e_labels.pack(expand=True,
                       fill='both'
                       )
                
        #Total expression labels
        self.to_e_labels=tk.Label(self.frame,
                           text=self.results,
                           anchor=tk.E,
                           padx=25,
                           font=('arial',50,'bold'),
                           background=DARKGREY,
                           foreground=WHITE,
                           borderwidth=0
                           )
        self.to_e_labels.pack(expand=True,
                       fill='both'
                       )
    
        self.digits={
                7:(1,1),8:(1,2),9:(1,3),
                4:(2,1),5:(2,2),6:(2,3),
                1:(3,1),2:(3,2),3:(3,3),
                '.':(4,1),0:(4,2)
                }
        
        self.op_symbols={"/":"\u00F7","*":"\u00D7",
                    "-":"-","+":"+"}
        
        self.Digit_Buttons()
        self.Operator_Buttons()
        self.Clear_Button()
        self.Equal_Button()
        self.Expand_Buttons()
        self.Sqrt_Button()
        self.Sq_Button()
        self.bind_keys()
        
    #Adding the Buttons    
    #Digit Buttons
    def Digit_Buttons(self):
        
        for digit,grid_value in self.digits.items():
            
            button=tk.Button(self.button_frame,
                             text=str(digit),
                             background=GREY,
                             activebackground=GREY,
                             foreground=WHITE,
                             activeforeground=WHITE,
                             font=('arial',24,'bold'),
                             borderwidth=0,
                             command=lambda x=digit:self.add_digits(x)
                             )
            button.grid(row=grid_value[0],
                        column=grid_value[1],
                        sticky=tk.NSEW
                        )
        
    #Operator Buttons
    def Operator_Buttons(self): 
        
        i=0
        
        for op,symbol in self.op_symbols.items():
            
            button=tk.Button(self.button_frame,
                             text=str(symbol),
                             background=DARKGOLD,
                             activebackground=DARKGOLD,
                             foreground=WHITE,
                             activeforeground=WHITE,
                             font=('arial',24,),
                             borderwidth=0,
                             command=lambda x=op:self.add_operators(x)
                             )
            button.grid(row=i,
                        column=4,
                        sticky=tk.NSEW
                        )
            i+=1
    
    #Clear Button
    def Clear_Button(self):
        
        button=tk.Button(self.button_frame,
                         text='C',
                         background=GREEN,
                         activebackground=GREEN,
                         foreground=WHITE,
                         activeforeground=WHITE,
                         font=('arial',24,'bold'),
                         borderwidth=0,
                         command=lambda:self.clear_all()
                         )
        button.grid(row=0,
                    column=1,
                    columnspan=1,
                    sticky=tk.NSEW
                    )
        
    #Square root Button
    def Sqrt_Button(self):
        
        button=tk.Button(self.button_frame,
                         text="\u221ax",
                         background=DARKGOLD,
                         activebackground=DARKGOLD,
                         foreground=WHITE,
                         activeforeground=WHITE,
                         font=('arial',24),
                         borderwidth=0,
                         command=lambda:self.sqrt(self.results)
                         )
        button.grid(row=0,
                    column=3,
                    columnspan=1,
                    sticky=tk.NSEW
                    )
     
    #Square Button
    def Sq_Button(self):
        
        button=tk.Button(self.button_frame,
                         text="x\u00b2",
                         background=DARKGOLD,
                         activebackground=DARKGOLD,
                         foreground=WHITE,
                         activeforeground=WHITE,
                         font=('arial',24),
                         borderwidth=0,
                         command=lambda:self.square(self.results)
                         )
        button.grid(row=0,
                    column=2,
                    columnspan=1,
                    sticky=tk.NSEW
                    )
        
    #Equal Button
    def Equal_Button(self):
        
        button=tk.Button(self.button_frame,
                         text='=',
                         background=GREEN,
                         activebackground=GREEN,
                         foreground=WHITE,
                         activeforeground=WHITE,
                         font=('arial',24,),
                         borderwidth=0,
                         command=lambda:self.equal_total('')
                         )
        button.grid(row=4,
                    column=3,
                    columnspan=2,
                    sticky=tk.NSEW
                    )
    
    #Expand Buttons Sizes
    def Expand_Buttons(self):  
        
        self.button_frame.rowconfigure(0,weight=1)  
        
        for i in range(1,5):
            self.button_frame.rowconfigure(i,
                                      weight=1)
            self.button_frame.columnconfigure(i,
                                         weight=1)
    
    
    #Adding Functionality to the Buttons
    #Display Digit
    def add_digits(self,value):    
          
        self.results+=str(value)
        self.append_operator(self.results)
        
    #Display Operator
    def add_operators(self,value):  
        
        try:
            for digit,grid_value in self.digits.items():
                
                #For not adding addition expression once an expression displayed
                if self.results[-1]==str(digit):
                    self.results+=str(value)
                    self.append_operator(self.results)
                    
        except Exception():
            self.exception_output()
  
    #Square Root the Digit  
    def sqrt(self,value):
        
        try:
            self.results=str(eval(f'{value}**0.5'))           
            self.symbol_error()
                
        except Exception:
            self.exception_output()
            
    #Square the Digit
    def square(self,value):
        
        try:
            self.results=str(eval(f'{value}**2'))
            self.symbol_error()

        except Exception:
            self.exception_output()
            
    #Clear Fields
    def clear_all(self):
        
        self.operations=''
        self.results=''
        self.cu_e_labels.config(text=self.operations)
        self.to_e_labels.config(text=self.results)    
        
    #Equal All
    def equal_total(self,value):
           
        self.operations=self.results+str(value)
         
        try: 
            self.results=str(eval(self.operations))
            self.symbol_error()
            
        except Exception:
            self.exception_output()
        
        finally:
            self.operations=''
            
    #Freeze on non complete operation
    def symbol_error(self):
        
        for op in self.op_symbols.items():
            
            if self.results[-1]!=str(op):
                self.append_operator(self.results)   
            else:
                pass
        
    #Display Error on Error code
    def exception_output(self):
        
        self.operations=''
        self.results=''
        
        self.cu_e_labels.config(text=self.operations)
        self.to_e_labels.config(text='Error')
        
    #For Display Expression Symbol on Display
    def append_operator(self,value):
        
        op_expression=self.operations
        expression=self.results
        
        for op,symbol in self.op_symbols.items():
            expression=expression.replace(op,f'{symbol}')
            op_expression=op_expression.replace(op,f'{symbol}')
            
        self.cu_e_labels.config(text=op_expression)
        self.to_e_labels.config(text=expression[:9])
        
    #Binding with Keyboard Keys
    def bind_keys(self):
        self.root.bind('<Return>', lambda event:self.equal_total(''))
        self.root.bind('<Delete>', lambda event:self.clear_all())
        self.root.bind('<Shift_R>', lambda event:self.square(self.results))
        self.root.bind('<Control_R>', lambda event:self.sqrt(self.results))
        
        for key in self.digits:
            self.root.bind(str(key), lambda event,digit=key:self.add_digits(digit))
            
        for op in self.op_symbols:
            self.root.bind(op, lambda event,operator=op:self.add_operators(operator))
            
    def run(self):
        self.root.mainloop()

if __name__=='__main__':
    calc = Calculator()
    calc.run()   
