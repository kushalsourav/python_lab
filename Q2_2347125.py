# 1. LIST
# Write a PYTHON script with List comprehension for the following
# • Is the given list divisible by 3 or NOT?
# • Square of even numbers in a list
# • Sum of digits of all EVEN numbers in a list
# • Remove duplicate numbers in a list

## A dummy list made on video size in gb
dummy_list = [1,2,2,3,6,4,1,7,9,4,5,8]

# • Is the given list divisible by 3 or NOT?

divisable_by_three = []
for i in dummy_list:
    if(i % 3 == 0) :
     divisable_by_three.append(i)
    
print("Number divisable by three : ",divisable_by_three)

# • Square of even numbers in a list

square_of_even = []

for i in dummy_list:
   if(i % 2 == 0):
       square_of_even.append(i ** 2)

print("Square of even numbers:",square_of_even)

# • Sum of digits of all EVEN numbers in a list

sum_even_digits = 0

for i in dummy_list:
   if(i % 2 == 0):
      sum_even_digits += i

print("Sum of even didgits: ",sum_even_digits)


# • Remove duplicate numbers in a list

for i in dummy_list:
   if(dummy_list.count(i) == 2) :
      dummy_list.remove(i)
   
print("Remove duplicate numbers from list",dummy_list)




##2.  Dictionary
##Create a dictionary to store the details of your company employees (name as key and
##birthdate as value).
##{ ‘Virat Kohli’: ‘5 November 1988’, ‘Umesh Yadav’: ‘25 October 1987’, ‘Manish Pandey’:
##‘10 September 1989’, ‘Rohit Sharma’: ‘30 April 1987’, ‘Ravindra Jadeja’: ‘6 December
##1988’, ‘Hardik Pandya’: ‘11 October 1993’ }
##Write a function birthDate() that takes the full name of your employees(as a string) and
##displays the given employee’s birthdate.



#date video updated      
video_updated = {
   "programming": "1 september 2018",
   "desgining": "3 june 2017",
   "coding": "5 january 2020",
   "gaming" : "23 march 2015"
}

def birthDate(name) :
   x =  video_updated.get(name)
   print("video updated on:",x)

video_name = input("Enter the name of video: ")
birthDate(video_name)
