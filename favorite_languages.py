favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

#Looping through the keys is the default behavior
#so this is the same as just using favorite_languages
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
    if 'erin' not in favorite_languages.keys(): #works for looping and returns a list
        print('Erin, please take our poll!')

#This is how you can get the dictionary keys returned in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#You can also get only values if that is all you are interested in.
print('The flollowing languages have been mentioned: ')
for language in favorite_languages.values():
    print(language.title())

#Use a set to eliminate repeated values
for language in set(favorite_languages.values()):
    print(language.title())
