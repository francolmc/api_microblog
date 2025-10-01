from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

# Create your models here.
class Post(Document):
    content = StringField(max_length=150, required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.content[:50]
    
    meta = {
        'collection': 'posts',
        'ordering': ['-created_at']
    }