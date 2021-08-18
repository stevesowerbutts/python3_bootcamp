def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is Colt.")

def rage():
	print("I HATE YOU!")

# we are decorating our function 
# with politeness!
greet = be_polite(greet)

polite_rage = be_polite(rage)
polite_rage()
