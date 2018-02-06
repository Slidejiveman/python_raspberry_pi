#aliens.py
#This program demonstrates nesting by creating dictionaries of aliens then adding those dictionaries to a list
#What follows builds on this idea and makes the program more robust and usable.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('\n')
#Automatically generating more aliens
aliens = []
#Range here returns a set of numbers to control number of repeats
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Pretend the first three aliens have existed long enough to power up
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow': #doesn't do anything since all 'green'
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

print('Total number of aliens: ' + str(len(aliens)))
