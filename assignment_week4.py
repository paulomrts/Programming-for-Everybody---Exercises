
"""
Write a program that uses raw_input to prompt a user for their name and then welcomes them. 
Note that raw_input will pop up a dialog box. 
Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.
"""

inp = raw_input ("Enter hours: ")
hours = float (inp)
inp = raw_input ("Enter rate: ")
rate = float (inp)

pay = rate * hours
print pay
