from pyscript import display, document

def get_name(e):
    document.getElementById('div1').innerHTML = ''

    first_name= ["pocholo", "arkin", "lara", "liam" "comanda", "san agustin", "estrada", "lao"]
    last_name= ["comanda", "san agustin", "estrada", "lao"]

    name_first = document.getElementById('fname').value.lower().strip()
    first_name_checker = name_first in first_name

    name_last = document.getElementById('lname').value.lower().strip()
    last_name_checker = name_last in last_name

    mixed_name = ()

    display_message = ('Sorry you are not registered to this club', f' Welcome {name_first}  {name_last} to the ICT club')

    display(display_message[first_name_checker], target='div1')
    



