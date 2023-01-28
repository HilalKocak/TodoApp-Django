## Django ORM Query





```shell 
python manage.py shell

```

```python
# Import Todo module 
from todo.models import Todo

# All objects
Todo.objects.all()

#Count of all objects
Todo.objects.all().count()

#Creating new Todo object
Todo.objects.create(title='I created this via shell')

#Show is_active=True
Todo.objects.filter(is_active=True)

#Count is_active=True
Todo.objects.filter(is_active=True).count()

#UPDATE
# You can change the fileds of objects provided from query
Todo.objects.filter(is_active=False).update(is_active=True)

#Find not contains "Django" in title and add their ending
todos=Todo.objects.exclude(title__icontains="Django")
for item in todos:
    item.title=f"{item.title} -Django"
    item.save()
```