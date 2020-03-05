import numpy as np

def create_output(library_list, booklist, order = None):
  f= open("b.txt","wt")
  L = len(library_list) #ändra till antal bibliotek
  s = '2 \n'
  s = str(L) + '\n'
  f.write(s)
  for i in range(L):
    lib = library_list[i]
    f.write(str(i) + ' ' + str(lib['total_books']) + '\n')

    temp_booklist = lib['books'].copy()
    books_score = temp_booklist.copy()
    for k in range(len(books_score)):
      books_score[k] = booklist[books_score[k]] #listan med scores
    for k in range(len(temp_booklist)):
        
      index = np.argmax(books_score) #Funktion med maxindex?
      temp_booklist[k] = booklist[index]
      books_score[index] = 0

    f.write(' '.join(str(e) for e in temp_booklist) + '\n')
    #f.write(str(lib['books']) + '\n')
  f.close()  
  
  
  
  
  
  
  
''' 
  f= open("b.txt","wt")
  L = len(library_list) #ändra till antal bibliotek
  s = '2 \n'
  s = str(L) + '\n'
  f.write(s)
  for i in range(L):
    lib = library_list[i]
    f.write(str(i) + ' ' + str(lib['total_books']) + '\n')
    f.write(' '.join(str(e) for e in lib['books']) + '\n')
    #f.write(str(lib['books']) + '\n')
  f.close()
'''