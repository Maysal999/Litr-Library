

from product.models import Product


def search_product(request):
    key = request.POST.get('key')
    cards = Product.objects.filter(title=key)
    return cards