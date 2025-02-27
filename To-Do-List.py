project = " \n \t \t \t 🧭 TO-DO-LIST 🧭 \t \t \t "
print(project)

to_do_list=[]

def menu():

    while True : 

        print(" \n Choose Anything ")
        print(" 1. Add Tasks ")
        print(" 2. Remove Tasks ")
        print(" 3. View Tasks ")
        print(" 4. Chack Tasks ")
        print(" 5. Exit ")
        choose = input(" Choose = 1/2/3/4/5 : ")
    
        if choose == "1" :
            item = input (" Add Tasks : ")
            to_do_list.append( item )
            print(f" {item} is in your 'To-Do-List', now. ")

        elif choose == "2" :
            item = input (" Enter task for remove: ")
            if item in to_do_list :
                to_do_list.remove(item)
                print(f" {item} isn't in your 'To-Do-List', now. ")
            else :
                print(f" {item} is not your To-Do-List. ")

        elif choose == "3" :
            if to_do_list :
                print(" Your 'To-Do-List' : \n ")
            for i, item in enumerate(to_do_list , start=1):
                print(f"{i}. {item}")
            else:
                print(" Your 'To-Do-List' is empty. ")

        elif choose == "4" :
            item = input("Enter the item to check: ")
            if item in to_do_list:
                 print(f" {item} is already in the 'To-Do-List' .")
            else:
                 print(f" {item} is not in the 'To-Do-List' .")


        else:
            print("\nYour final tasks:")
            print(to_do_list[:])  
            print("I hope you enjoyed using 'To-Do-List'. Have a great day!")
            break  
        
result = menu()
print(result)
    
    
