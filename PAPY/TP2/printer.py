import math

class Printer:

    Formats = [f"A{i}" for i in range(6)]
    Devices = []
    base_width = 200

    @classmethod
    def show_printers_system(cls):
        print(f"Formats: {cls.Formats}, {cls.base_width=} \n {cls.Devices=}")

    def __init__(self, avail_paper):
        self.formats = []
        invalid_formats = []
        for format in avail_paper:
            if format in Printer.Formats:
                self.formats.append(format)
            else:
                invalid_formats.append(format)
        if len(invalid_formats) > 0:
            print(f"Some formats are incorrect: {invalid_formats}")
        Printer.Devices.append(self)
    
    def _printer(self,text, page_width):
        print("###" + page_width * "#" + "###")
        words = text.split("\n")
        words = " ".join(words)
        words = words.split(" ")
        current_line = page_width
        for i in range(len(words)):
            if len(words[i]) > page_width:
                words = words[:i] + [words[i][:page_width], words[i][page_width]] + words[(i+1):]
        print("#  ", end = "")
        while len(words) > 0:
            if len(words[0]) < current_line:
                print(words[0], end = " ")
                current_line -= (len(words[0]) + 1)
                words = words[1:]
            else:
                print(current_line * " " + "  #")
                print("#  ", end = "")
                current_line = page_width
        print(current_line * " " + "  #")
        print("###" + page_width * "#" + "###")



    
    def send(self, text, format = 'Default'):
        if format == 'Default':
            if 'A4' in self.formats:
                format = 'A4'
            else:
                print("No default format")
                return
        format_number = int(format[1])
        page_width = round(Printer.base_width * ((1/math.sqrt(2)) ** format_number))
        self._printer(text, page_width)
        return 

class ColorPrinter(Printer):
    def __init__(self, avail_paper, color):
        super().__init__(avail_paper)
        self.color_code = self.choose_color(color)   
    
    def choose_color(self, choice):
        code = "\033["
        match choice:
            case "Black": code += "30"
            case "Dark red": code += "31"
            case "Dark green": code += "32"
            case "Dark yellow": code += "33"
            case "Dark blue": code += "34"
            case "Dark magenta": code += "35"
            case "Dark cyan":  code += "36"
            case "Light gray": code += "37"
            case "Dark gray": code += "90"
            case "Red": code += "91"
            case "Green": code += "92"
            case "Orage": code += "93"
            case "Blue": code += "94"
            case "Magenta": code += "95"
            case "Cyan":  code += "96"
            case "White": code += "97"
            case _: code += "39"
        print(code)
        code += "m"
        return code
    
    def send(self, text, format):
        print(self.color_code)
        super().send(text,format)
        print("\033[0m") #reset code
        
    


zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

def main():
    generic_printer=Printer(avail_paper=["B1","A4","A0"])
    Printer.show_printers_system()
    #generic_printer.send(zen)
    generic_printer.send(zen,"A0")
    fancy_printer = ColorPrinter(avail_paper=["A2","A4","A0"], color="Cyan")
    fancy_printer.send(zen, "A2")

main()