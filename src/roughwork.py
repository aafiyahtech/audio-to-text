from blog.models import Post
from django.contrib.auth.models import User

# sample queries to run to fetch info from the db
allUsers = User.objects.all()
firstUser = User.object.first()
filteredUser_username = User.objects.filter(username='admin')
filteredUser_username_first = User.objects.filter(username='admin').first()
filteredUSer_id = User.objects.filter(id=1)

#User related queries
user = User.object.first()

userId = user.id
userPrimaryKey = user.pk

userById = User.objects.get(id=1)

#Create Posts

postList = Post.objects.all()

post_1 = Post(title='blog 1', content='First post content', author=user)

#save post

post_1.save()

#create post using user id

post_2 = Post(title='Blog 2', content='Second post content', author_id=user.id)


# Creat a variablbe to access post parameters

newPost = Post.objects.first()

#then we can query like below

newPost.title
newPost.content
newPost.author
newPost.date_posted

#we can access attributes of the author also

newPost.author.email

#access all the posts created by user use '.modelname_set'

user.blog_set

#so to create a new post now.. (see how no need to add an author, as we are already accessing this using'user variable, and user variable value is 'admin)

user.blog_set.create(title='Blog 3', content='Post 3 content')

#-----------------------------------------------------

#Pagnataion practice

from django.core.paginator import Paginator

posts = ['1', '2', '3', '4', '5']

p = Paginator(posts, 2)

p.num_pages #this will give number of pages, in above example there will be 3

for page in p.page_range:
    print(page) #this will loop over number of pages and print each page/ or page numbers

p1 = p.page(1) #access specific page out put <page 1 of 3>
p1.number #this is gives number of the above page
p1.object_list #this is will display posts on this page
p1.has_previous #returns True or False depending on page number
p1.has_next #returns True or False depending on page number
p1.next_page_number #gives us the number of next page