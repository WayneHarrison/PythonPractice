print('Hello' + ' world')
name = 'Wayne'
place = 'Town'
time = '11AM'
food = 'Sausage rolls'
print('Hello ' + name + ', you are invited to ' + place + ' at ' + time
      + '. There will be ' + food + '.')
print ('Hello %s, you are invited to %s at %s. There will be %s.'
       %(name, place, time, food))
#the %s notes where we want to insert another string into the string.
#We can insert what we want with %(). The specified strings will be inserted in order.
