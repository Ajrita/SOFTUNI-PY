"""Annie goes to her hometown after a very long period out of the country. After coming home, she sees her
grandmother's old library and remembers her favorite book. Help Annie by writing a program in which she enters
the book (string) she is looking for. Until Annie finds her favorite book or checks out all the books in the library,
the program must read the name of each following book (string). The books in the library are finished once you get
the text "No More Books".
If she does not find the book, print in two lines:
⦁	"The book you search is not here!"
⦁	"You checked {count} books."
If she finds the book, print on a single line:
⦁	"You checked {count} books and found it."  """

text = input()
unos_knjiga = ""
num_input= 0
while unos_knjiga != "No More Books" or text != unos_knjiga:
    unos_knjiga = input()

    if unos_knjiga == "No More Books":
        print(f"The book you search is not here!\nYou checked {num_input} books.")
        break
    if unos_knjiga == text:
        print(f"You checked {num_input} books and found it.")
        break
    num_input += 1
