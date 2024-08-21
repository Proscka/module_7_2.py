def custom_write(file_name,strings):
    strings_positions ={}
    with open(file_name, "w", encoding="utf-8") as file:


        for i, strings in enumerate(strings):

            strings_positions[(i)+1, file.tell()]=strings
            file.write(strings + "\n")
    file.close()
    return strings_positions


info={(1,0):"Text for tell.",(2,16):" Используйте кодировку utf-8."}

strings_positions=[(1,2),(0,16)]

str="Text for tell."," Используйте кодировку utf-8."

info = [
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!"
    ]
result = custom_write("test.txt",info)
for elem in result.items():
 print(elem)







