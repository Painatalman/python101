x = raw_input("what is your name?")
# '123' // will always be string
x = input("what is your name?")
# 123... will try to deduce

# https://en.wikibooks.org/wiki/Python_Programming/Input_and_Output

x = None
while not x:
    try:
        x = int(raw_input())
    except ValueError:
        print 'Invalid Number'

# ficheiros
http://www.tutorialspoint.com/python/python_files_io.htm

# ficheiro sera criado se nao existir
f = open('test.txt', 'r+')  # r para leitura, w para escrita
for line in f:
    print line
f.write('\n mais esta linha')
f.seek(0, 0);
f.readline
# MUITO IMPORTANTE
f.close()
