import json

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
