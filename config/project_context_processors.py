from todo.models import Category

def global_category_contex(request):
    global_categories= Category.objects.filter(is_active=True)
    return dict(
        global_categories=global_categories,
    )
