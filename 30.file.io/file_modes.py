# w - writes and erases existing contents
with open("haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# a - appends to end, preserving original contents
NO CONTROL OVER CURSOR
with open("haiku.txt", "a") as file:
	file.seek(0)
	file.write(":)\n")

# r+ read and write
with open("haiku.txt", "r+") as file:
	file.write(":)")
	file.seek(10)
	file.write(":(")

# r+ will not create a file if it doesn't exist
with open("hello.txt", "a") as file:
	file.write("HELLO!!!")
