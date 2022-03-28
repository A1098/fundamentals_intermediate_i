x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ] 
def updt_1():
    x[1] = [15,8,9]
    print(x[:])
    return x
updt_1() 
#2 Change the last_name of the first student from 'Jordan' to 'Bryant'
def updt_2():
    students[0] = {'first_name':  'Michael', 'last_name' : 'Bryant'}
    print(students[:])
updt_2()
#3 In the sports_directory, change 'Messi' to 'Andres'
def updt_3():
    sports_directory['soccer'] = 'Andres', 'Ronaldo', 'Rooney'
    print(sports_directory)
    return sports_directory
updt_3()
# Iterate through a list of dictionaries 
students = [
    {'first_name':  'Michael,', 'last_name' : 'Jordan'},
    {'first_name' : 'John,', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark,', 'last_name' : 'Guillen'},
    {'first_name' : 'KB,', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students): 
    a = 0
    while a < len(students):
        v = []
        v.extend(students[a].values())
        print("first_name - " + v[0], "last_name - " + v[1])
        a += 1
    else:
        print("Attendance is Done!")
iterateDictionary(students)
# Get Value from a list of Dictionaries
def iterateDictionary2(key_name, some_list):
    a = 0 
    while a < len(students):
        print((some_list[a].get(key_name)))
        a += 1 
iterateDictionary2('last_name', students)

#4 Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    k_list = []
    k_list.extend(some_dict.keys())
    v_list = []
    count = 0
    while count < len(dojo):
        s_list = []
        s_list += some_dict[k_list[count]]
        print(str(len(s_list)) ,""+ k_list[count])
        for elem in s_list:
            print(elem)
        count += 1  
printInfo(dojo)

