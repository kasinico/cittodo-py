#File handling

#books.write("i am reading a book\n")
#books.write("read another book")
#books.close()
#print (books.read())


import pickle

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")


   # File Handling in Python 
   # # books = open("books.txt", "w") 
   # # books.write("I am a book two\n") 
   # # books.write("I am another book") 
   # # books.close() # print(books.read()) 
   # # f = open("file.txt") # print(f.read()) 
   # # f.close() import pickle f = open("books.txt", "r") 
   # for line in f.readlines(): print(line.strip()) f.close()
   #  # try: # l = open("lorem.txt") # for line in l.readlines():
   #  # print(line.strip()) 
   # # finally: 
   # # l.close() with open("file.txt") as my_file: print(my_file.read())
   #  _username = input("Enter your username: ") 
   # _password = input("Enter your password: ") 
   # data = f"{_username} \n {_password}" 
   # with open("user", "wb") as f: pickle.dump(data, f) with open("user", "rb") as d: 
   # dt = pickle.load(d) 
   # print(dt) 