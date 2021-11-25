def change_file_encoding(in_file_name:str, in_encoding:str, out_file_name:str,out_encoding:str,):
    with open(in_file_name,'r',encoding=in_encoding,buffering=1) as file_in:
         with open(out_file_name,'w',encoding=out_encoding,errors='replace') as file_out:
            file_out.write(file_in.read( ))
