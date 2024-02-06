class string_up:
    def __init__(self):
        self.input_string = ""
        
    def get_string(self):
        self.s=input()

    def print_string(self):
        print(self.s.upper())
answer=string_up()
answer.get_string()
answer.print_string()