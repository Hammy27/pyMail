

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from PyMail.main import PyMail
    with open('core/input.html') as fp:
        html = fp.read()

    mail = PyMail(html).transform('body')
    print(mail)


