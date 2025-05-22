# Notes .read()= all the data into one string
# Notes .readline()= one line of data at a time

# How to read a File
File= "File_name.txt"
with open(File)as f:
    read_data= f.read()
print(read_data)

#Exercise 1
def writefile(file_name, a_string, mode):
  with open(file_name, mode) as f:
    f.write(a_string)

writefile('new_file.txt', 'This is so cool', 'w')


#Exercise 2
def open_file(filename, option):
  with open(filename, 'r') as f:
    if option == 'read':
      return f.read()
    elif option =='readlines':
      return f.readlines()
    else:
      return None

print(open_file('File_name.txt','readlines'))


#Exercise 3
def printFile(file):
    with open(file)as f:
        read_data= f.read()
    return read_data

print(printFile('File_name.txt'))

#Exercise 4
def sumcolumn(filename):
  list_of_num=[]
  with open(filename)as f:
    data= f.read
    for data in f:
      int_data=int(data)
      list_of_num.append(int_data)
    final=sum(list_of_num)

  return final

print(sumcolumn('Sum_column.txt'))

#Exercise 5
def  sum_all(filename):
    list_of_num=[]
    with open(filename) as f:
        data= f.read()
        for num in data:
          nums=data.split()
        for items in nums:
          int_nums=int(items)
          list_of_num.append(int_nums)
        final= sum(list_of_num)
    return final
print(sum_all('sum_all.txt'))

#Exercise 6
def readColumn(filename, ColumnNo):
    list_of_num_in_columnNo=[]
    with open(filename) as f:
      data= f.readlines()
      for line in data:
        line_split=line.split()
        value=line_split[ColumnNo-1]
        list_of_num_in_columnNo.append(value)
    return list_of_num_in_columnNo
print(readColumn('Read_column.txt', 3))

#Excercise 7
def countWord(Filename, word):
    word_counter=0
    wordandcounter={}
    with open(Filename) as f:
        data= f.readlines()
        for values in data:
            individual=values.split()
            for words in individual:
                if words == word:
                    word_counter+=1
            wordandcounter[word]=word_counter
        for key,value in wordandcounter.items():
            line=f"word:\t Number of Times It Appears:\n{key}: \t\t{value}\n"
            writefile2('Words_in_text.txt',line,'a')

def writefile2(file_name, a_string, mode):
  with open(file_name, mode) as f:
    f.write(a_string)
    
countWord('zenOfPython.txt', 'If')
# Notes .read()= all the data into one string
# Notes .readline()= one line of data at a time

# How to read a File
File= "File_name.txt"
with open(File)as f:
    read_data= f.read()
print(read_data)

#Exercise 1
def writefile(file_name, a_string, mode):
  with open(file_name, mode) as f:
    f.write(a_string)

writefile('new_file.txt', 'This is so cool', 'w')


#Exercise 2
def open_file(filename, option):
  with open(filename, 'r') as f:
    if option == 'read':
      return f.read()
    elif option =='readlines':
      return f.readlines()
    else:
      return None

print(open_file('File_name.txt','readlines'))


#Exercise 3
def printFile(file):
    with open(file)as f:
        read_data= f.read()
    return read_data

print(printFile('File_name.txt'))

#Exercise 4
def sumcolumn(filename):
  list_of_num=[]
  with open(filename)as f:
    data= f.read
    for data in f:
      int_data=int(data)
      list_of_num.append(int_data)
    final=sum(list_of_num)

  return final

print(sumcolumn('Sum_column.txt'))

#Exercise 5
def  sum_all(filename):
    list_of_num=[]
    with open(filename) as f:
        data= f.read()
        for num in data:
          nums=data.split()
        for items in nums:
          int_nums=int(items)
          list_of_num.append(int_nums)
        final= sum(list_of_num)
    return final
print(sum_all('sum_all.txt'))

#Exercise 6
def readColumn(filename, ColumnNo):
    list_of_num_in_columnNo=[]
    with open(filename) as f:
      data= f.readlines()
      for line in data:
        line_split=line.split()
        value=line_split[ColumnNo-1]
        list_of_num_in_columnNo.append(value)
    return list_of_num_in_columnNo
print(readColumn('Read_column.txt', 3))

#Excercise 7
def countWord(Filename, word):
    word_counter=0
    wordandcounter={}
    with open(Filename) as f:
        data= f.readlines()
        for values in data:
            individual=values.split()
            for words in individual:
                if words == word:
                    word_counter+=1
            wordandcounter[word]=word_counter
        for key,value in wordandcounter.items():
            line=f"word:\t Number of Times It Appears:\n{key}: \t\t{value}\n"
            writefile2('Words_in_text.txt',line,'a')

def writefile2(file_name, a_string, mode):
  with open(file_name, mode) as f:
    f.write(a_string)
    
countWord('zenOfPython.txt', 'If')
