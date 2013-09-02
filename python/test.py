import string
import os

labls = {
    'phone': 'phone number',
    'addr' : 'address'
}

name = raw_input('Name: ')

request =raw_input('Phone number (p) or address (a)? ')

key =request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print "%s 's %s is %s," % (name, label, result)
