########################
# import greetings

# greetings.greet("Mario")
# print(greetings.AUTHOR)
########################
# import greetings as g

# g.greet("Mario")
# print(g.AUTHOR)
########################
from greetings import greet

greet("Mario")
########################
import connections

connections.connect()
########################
from my_package import internet, website

internet.connect()
website.load("www.google.com")
