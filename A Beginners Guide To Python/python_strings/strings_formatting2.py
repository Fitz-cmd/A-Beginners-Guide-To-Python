# Allows multiple values to populate the string 
name = "Adam"
age = 20
print('{} is {} years old'.format(name, age))
#It also illustrates that variables can be used to provide the values 
# for the format method as well as literal values. 
# A literal value is a fixed value such as 42 or the string 'John'.
#By default the values are bound to the placeholders based on the order that 
# they are provided to the format() method; 
# however this can be overridden by pro- viding an index to the placeholder to tell it
#  which value should be bound, for example:
# Can specify an index for the substitution 
format_string = "Hello {1} {0}, you got {2}%"
print(format_string.format('Smith', 'Carol', 75))
#Of course when ordering the values 
# it is quiet easy to get something wrong either 
# because a developer might think the strings are indexed from 1 or 
# just because they get the order wrong.
#An alternative approach is to use named values for the placeholders. 
# In this approach the curly brackets surround the name of the value to be substituted,
#  for example {artist}. 
# Then in the format() method a key=value pair is provided 
# where the key is the name in the format string; 
# this is shown below#
# Can use named substitutions, order is not significant 
format_string = "{artist} sang {song} in {year}" 
print(format_string.format(artist='Paloma Faith', song='Guilty', year=2017))
