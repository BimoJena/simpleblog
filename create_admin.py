from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username="bimochanBlog").exists():
    User.objects.create_superuser("bimochanBlog", "taskbimo@gmail.com", "24mcafsd0008")
    print("✅ Superuser created!")
else:
    print("ℹ️ Superuser already exists.")
