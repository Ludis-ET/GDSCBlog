import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDSCBlog.settings')
import django
django.setup()

from BlogApp.models import Post
from CommentApp.models import Comment


one = Post.objects.create(title="Ludis", content="creating contoent for ludis", category="Tech", tags=["tag1", "tag2"])
two = Post.objects.create(title="leul", content="Content for the second post", category="Science", tags=["tag3", "tag4"])
three = Post.objects.create(title="leulseged", content="Content for the third post", category="Travel", tags=["tag5", "tag6"])


tech_posts = Post.objects.filter(category="Tech")
print("Posts in Tech category:", tech_posts)

one.content = "this is the updated content for ludis"
one.save()

three.delete()

comment1 = Comment.objects.create(content="Comment for the first post", author="User1", post=one)
comment2 = Comment.objects.create(content="Comment for the second post", author="User2", post=two)
comment3 = Comment.objects.create(content="Comment for the third post", author="User3", post=three)

one_comments = Comment.objects.filter(post=one)
print("Comments for the first post:", one_comments)

comment1.content = "Updated comment for the first post"
comment1.save()

comment3.delete()
