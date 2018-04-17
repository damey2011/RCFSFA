from django.contrib import admin

# Register your models here.
from social.models import FeedPost, Conversation, ConversationReplies, CommentLike, PostLike, Comment

admin.site.register(FeedPost)
admin.site.register(Comment)
admin.site.register(PostLike)
admin.site.register(CommentLike)
admin.site.register(Conversation)
admin.site.register(ConversationReplies)
