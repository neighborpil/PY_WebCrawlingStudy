"""
# The double split pattern
 - Sometimes we split a line one way, and then grab one of the pieces
   of the line and split that piece again
"""

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split() # ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
email = words[1] # 'stephen.marquard@uct.ac.za'
pieces = email.split('@') # ['stephen.marquard', 'uct.ac.za']
print(pieces[1]) # uct.ac.za
