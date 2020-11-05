print('Hello' + ' world')
name = 'Wayne'
place = 'Town'
time = '11AM'
food = 'Sausage rolls'
print('Hello ' + name + ', you are invited to ' + place + ' at ' + time
      + '. There will be ' + food + '.')
print ('Hello %s, you are invited to %s at %s. There will be %s.' #The %s acts as a place holder within the string, the variables can be inserted 
       %(name, place, time, food))                                #after in order to help keep code clean when compared to the line above.
