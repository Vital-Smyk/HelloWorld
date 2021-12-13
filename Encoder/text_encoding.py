import sys, os.path
BUFFER_SIZE = (1024**2)*5
def file_encoding(in_file_name:str, in_encoding:str, out_file_name:str, out_encoding:str):
    with open(in_file_name,'r',encoding=in_encoding,buffering=BUFFER_SIZE) as file_in:
        with open(out_file_name,'a',encoding=out_encoding,errors='replace') as file_out:
          i = 0
          while True:
            m = file_in.read(4)
            file_out.write(m) 
            if m == '':
              break


def main (arg):
    if  arg[1] in {'-h','-H','-help'} :
      print("Используйте: <input_file.txt> <input_encoding> <output_file.txt> <output_encoding>") 
      print("Пример: input.txt utf-8 output.txt ascii")
      sys.exit(1)
    elif len (arg) < 5:
      print ("Ошибка. Слишком мало параметров.")
      sys.exit (1)
    elif len (arg) > 5:
      print ("Ошибка. Слишком много параметров.")
      sys.exit (1)
    elif not os.path.exists(arg[1]) :
      print (f"Ошибка. Указаный файл '{arg[1]}' не найден.")
    else :
      file_encoding(*arg[1:])

if __name__ == '__main__' :
  m = sys.argv
  main(m)