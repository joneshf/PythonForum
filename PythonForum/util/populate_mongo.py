import datetime
from mongoengine import *
import sys
import shortuuid

if __name__ != "__main__":
    sys.exit(1)

try:
    host = sys.argv[1]
    cont = sys.argv[3]
except IndexError:
    host = raw_input("Give me a host in the URI format: ")
    cont = bool(raw_input("WARNING, this wipes the database, type y to continue: ") == 'y')

if not cont:
    sys.exit(1)

db = connect("forum", host=host)


from ..database import forum, categories, boards, threads, posts, login

# drop all the documents!
for document in [forum.Forum, categories.Category, boards.Board, threads.Thread, posts.Post]:
    document.drop_collection()

# create a forum
python_forum = forum.Forum()
# create the categories
general = categories.Category(name="General", description="General discussions related to Python.")
general.save()
python_coding = categories.Category(name="Python Coding", description="Everything related to coding in Python")
python_coding.save()
activities = categories.Category(name="Forum Activities", description="Everything related to goings on in the Forum")
activities.save()
misc = categories.Category(name="Miscellaneous", description="Talk about anythong non Python here")
misc.save()
# add the categories to the forum
python_forum.categories.extend([general, activities, python_coding, misc])
python_forum.save()
# create some boards
python_general = boards.Board(name="Python General", description="General coding questions", board_id=1)
general.boards.append(python_general)
python_general.save()
general.save()

beginners = boards.Board(name="Beginners..", description="The board for beginners to post in!", board_id=2)
python_coding.boards.append(beginners)
beginners.save()
python_coding.save()

contests = boards.Board(name="Contests", description="Compete for non existant prizes!", board_id=3)
activities.boards.append(contests)
contests.save()
activities.save()

bar = boards.Board(name="Bar", description="Talk about everything not only python.", board_id=4)
misc.boards.append(bar)
bar.save()
misc.save()

demo_user_1 = login.User(email="test@test1.com", username="bobcat", active=True)
demo_user_1.save()
demo_user_2 = login.User(email="test@test2.com", username="davebob", active=True)
demo_user_2.save()

posts = [posts.Post(author=demo_user_1, tile="Reply number 1", content="Demo"),
         posts.Post(author=demo_user_2, tile="Reply number 2", content="Demo"),
         posts.Post(author=demo_user_1, tile="Reply number 3", content="Demo"),]
for post in posts:
    post.save()

test_topic = threads.Thread(posts=posts, author=demo_user_2, title="Test thread", is_announcement=False, topic_uuid=shortuuid.uuid(),
                            date=datetime.date.today())

test_topic.save()

python_general.topics.append(test_topic)
python_general.save()
print "Done."