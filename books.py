# Additional imports
import itertools
import numpy as np
import create_output


path = '/home/liam/Desktop/Hash/c_incunabula.txt'

# Read the file, and extract the most important information

def create_dict(): 
  '''
  Creates dictionary for storing libraries, their books, and information about signup and processing time
  '''

  linelist = [line.rstrip('\n').split() for line in open(path)]

  total_books, total_libraries, total_days = int(linelist[0][0]), int(linelist[0][1]), int(linelist[0][2])

  book_points= [int(l) for l in linelist[1]]

  length=len(linelist)
  library_list = [] #List to store libraries
  libraries = dict()

  for i in range(3,length, 2):

    #libraries.update({library_books + str(library_index) : [int(l) for l in linelist[i]]})
    library=({'total_books': linelist[i-1][0], 'signup': linelist[i-1][1], 'shipping': linelist[i-1][2]})
    library.update({'books': [int(l) for l in linelist[i]] })
    library_list.append(library)

  return library_list, total_books, total_libraries, total_days, book_points

# Initialization of variables

library_list, total_books, total_libraries, total_days, book_points = create_dict()

Days=total_days
Score=0
length_books = total_books

length_lib = len(library_list)
sign_up_time = [library_list[i]['signup'] for i in range(length_lib)]
shipping_time = [library_list[i]['shipping'] for i in range(length_lib)]

LB =  np.full((length_lib, total_books), 0) # Matrix with all libraries, this was ineffective for memory

for i in range(length_lib):
  book_list = library_list[i]['books']
  for j in book_list:
    LB[i, j] =  book_points[j]

def weight(LB, sign_up_time, shipping_time): 
  W = np.full(length_lib, 0)
  for i in range(length_lib):

    divider_1 = np.sum(LB[i,:])
    divider_2 = (int(sign_up_time[i])+ np.ceil(int(library_list[i]['total_books'])/int(shipping_time[i])) )

    W[i] = divider_1 / divider_2

  return W

W= weight(LB, sign_up_time, shipping_time)

def maximum(Weight): 
  index_array = Weight.copy()
  for i in range(len(Weight)): 
    
    index = np.argmax(Weight)
    index_array[i] = index
    Weight[index] = 0
  
  return index_array

index_array = maximum(W.copy())

create_output.create_output(library_list, book_list, order=index_array)














      