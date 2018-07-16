import json as jsn
dic = jsn.load(open('data.json'))## this is were the jason data-set was passed in

print("*********** WELCOME TO Elozzy'S DICTIONARY ********")
print("-----------------------------------------------------------------------------------------------------------------------------")
def Dict():
    print('Search a word')
    str = input()
    print()
    for key, value in dic.items():
        #to get the key from the dictionary
        if str == key: 
            print('Word: ' + key)
            for i in value:
                print(i)
                ###### if value in not in dictionary
        elif str not in dic.keys(): 
            print('{} not found in dictionary'.format(str))

Dict() #Function call to make the code work

