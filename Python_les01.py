# coding: utf-8

# Python. Быстрый старт.
# Занятие 5.

# Домашнее задание: 
#         создать функцию из действия удаления дубликатов, которая возвращала бы количество удаленных дубликатов


import os
import sys
import shutil
import psutil 


def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")  
            return False

            
def sys_info():
    print("Вот что я знаю о системе:")
    print("Количество процессоров: ", psutil.cpu_count())
    print("Платформа: ", sys.platform)
    print("Кодировка файловой системы: ", sys.getfilesystemencoding())
    print("Текущая директория: ", os.getcwd())
    print("Текущий пользователь: ", os.getlogin())  


print("Great Python Program!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = ''    
  
while answer != 'q':
    answer = input("Давайте поработаем? (Y/N/q)")    
    if answer == 'Y':
        print("Отлично, хозяин!")
        print("Я умею:")
        print(" [1] - выведу список файлов")
        print(" [2] - выведу информацию о системе")
        print(" [3] - выведу список процессов")
        print(" [4] - продублирую файлы в текущей директории")
        print(" [5] - продублирую указанный файл")
        print(" [6] - удалю дубликаты файлов")
        do = int(input("Укажите номер действия: "))
        
        if do == 1:
            print(os.listdir())
        elif do == 2:
            sys_info()
            
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("=Дублирование файлов в текущей директории=")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i += 1
                
        elif do == 5:
            print("=Дублирование указанного файла=")
            filename = input("Укажите имя файла:")
            duplicate_file(filename)
            
        elif do == 6:
            print("=Удаление дубликатов в директории=")
            dirname = input("Укажите имя директории:")
            file_list = os.listdir(dirname)
            
            # i = 0
            # while i < len(file_list):
            
            # Для работы со списками удобней и лучше использовать цикл for
            for f in file_list:
                # функция join сформирует полный путь к файлу независимо от ОС
                fullname = os.path.join(dirname, f)       
                if fullname.endswith('.dupl'):
                    os.remove(fullname)
                # i += 1    
                    
        else:
            pass
        
    elif answer == 'N':    
        print("До свидания!")
    else:
        print("Неизвестный ответ")    