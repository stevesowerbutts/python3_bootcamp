# Define the Comment class below:

class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

c = Comment("davey124", "lol you're so silly", 3)
print(c.username, c.text, c.likes)
