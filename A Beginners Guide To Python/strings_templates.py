import string
# Initialise the template with ¢variables that
# will be substitute with actual values
template = string.Template('$artist sang $song in $year')
print(template.substitute(artist='Freddie Mercury', song='The Great Pretender', year=1987))

import string
# Initialise the template with $variables that
# will be substitute with actual values
template = string.Template('$artist sang $song in $year')
# Replace / substitute template variables with actual values # Can use a key = value pairs where the key is the name of # the template Variable and the value is the value to use
# in the string
print(template.substitute(artist='Freddie Mercury', song='The Great Pretender', year=1987))
print(template.substitute(artist='Ed Sheeran', song='Galway Girl', year=2017)) 
print(template.substitute(artist='Camila Cabello', song='Havana', year=2018))
d = dict(artist = 'Billy Idol', song='Eyes Without a Face', year = 1984)
print(template.substitute(d))