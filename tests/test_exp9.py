import sys
import os
import django
from django.conf import settings

# Configure minimal Django settings just to load models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../exp09/myproject')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

def test_blog_model_exists():
    django.setup()
    from blog.models import Post

    # Check fields
    fields = [f.name for f in Post._meta.get_fields()]
    assert 'title' in fields, "Post model missing 'title'"
    assert 'content' in fields, "Post model missing 'content'"