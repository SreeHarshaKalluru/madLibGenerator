import re
import madLibUtil as m

stories = m.readStories()
print("List of stories : ")
if(not bool(stories)):
    print("No stories available")
for i in stories:
    print(i)
print(""" 
OR

Enter 'a' to add a new story
""")

id = input("Enter your choice : ")

#No switch case is available in python
if id == 'a':
    m.addStories()
elif id in stories.keys():
    story_content = stories[id]
    print(story_content)
    replacebales = re.findall(r'&&(.*?)&&', story_content)
    for i in replacebales:
        rplc_val = input("Enter a " + i + " : ")
        story_content = story_content.replace('&&'+i+'&&', rplc_val, 1)
    print(story_content)
else:
    print("Invalid choice.")