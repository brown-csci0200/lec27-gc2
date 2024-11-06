# cart.py
# Let's track how many courses were added to a registration cart

count = 0
primary_cart = []

def clear_cart() -> None:
    count = 0
    primary_cart = []

def add_course(course: str) -> None:
    count = count + 1
    primary_cart.append(course)


def rem_course(course: str) -> None:
    primary_cart.remove(course)

def show_cart() -> None:
    print(str(primary_cart))

def enroll():
    clear_cart()
    add_course("CSCI1650")   # Software Security and Exploitation 
    add_course("EEPS0050")   # Mars, Moon, and the Earth
    add_course("ARCH0396")   # Islands in the Western Imaginary
    rem_course("CSCI1650")
    add_course("TAPS1320")   # Choreography

enroll()
print(f"Total course adds:  {count}")
show_cart()
