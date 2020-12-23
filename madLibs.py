import json
import re

stories_storage_file_name = 'stories.json'
def createEmptyStoriesFile():
    """If no stories file found then it creats a new stories file with empty json."""

    f = open(stories_storage_file_name, 'w+')
    f.write('{}') #empty json indicating no stories
    f.close()

def addStories() :
    """Adds new stories that user enters to the stories file."""

    print("""Use the following formats for replacement string
    Noun - &&noun&&
    Adjective - &&adjective&&
    Verb - &&verb&&
    """)
    stories = readStories()
    story_name = input("Enter the new story name : ")
    story_content = input("Enter the story content : ")
    stories[story_name] = story_content
    f = open(stories_storage_file_name, 'w')
    f.write(json.dumps(stories))
    f.close()

def readStories() :
    """Reads stories from stories file to a dictionary"""

    try:
        f = open(stories_storage_file_name, 'r')
    except FileNotFoundError as fnf:
        print("Exception:", fnf)
        createEmptyStoriesFile()
        f = open(stories_storage_file_name, 'r')
    f_content = f.read()
    f.close()
    return json.loads(f_content)

stories = readStories()
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
    addStories()
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