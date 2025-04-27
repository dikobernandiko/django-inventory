from django.shortcuts import render,  get_object_or_404
from django.db import models  
from .models import Item, Category, Supplier
from django.db.models import Sum, Avg, Count

def stock_summary(request):
    items = Item.objects.all()
    total_stock = sum(item.quantity for item in items)
    total_value = sum(item.price * item.quantity for item in items)
    avg_price = items.aggregate(models.Avg('price'))['price__avg'] or 0

    context = {
        "total_stock": total_stock,
        "total_value": total_value,
        "average_price": avg_price
    }
    return render(request, "stock_summary.html", context)

def low_stock_items(request):
    threshold = int(request.GET.get('threshold', 5))
    items = Item.objects.filter(quantity__lt=threshold)
    context = {
        "items": items,
        "threshold": threshold
    }
    return render(request, "low_stock_items.html", context)

def items_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = Item.objects.filter(category=category)
    context = {
        "category": category,
        "items": items
    }
    return render(request, "items_by_category.html", context)

def category_summary(request):
    from django.contrib.humanize.templatetags.humanize import intcomma
    categories = Category.objects.all()
    summary = []
    for cat in categories:
        items = Item.objects.filter(category=cat)
        jumlah_barang = items.count()
        total_nilai = items.aggregate(total=Sum('price'))['total'] or 0
        rata_rata = items.aggregate(avg=Avg('price'))['avg'] or 0
        summary.append({
            "category": cat,
            "jumlah_barang": jumlah_barang,
            "total_nilai": total_nilai,
            "rata_rata": rata_rata
        })
    context = {"summary": summary}
    return render(request, "category_summary.html", context)

def supplier_summary(request):
    suppliers = Supplier.objects.all()
    summary = []
    for sup in suppliers:
        items = Item.objects.filter(supplier=sup)
        jumlah_barang = items.count()
        total_nilai = items.aggregate(total=Sum('price'))['total'] or 0
        summary.append({
            "supplier": sup,
            "jumlah_barang": jumlah_barang,
            "total_nilai": total_nilai
        })
    context = {"summary": summary}
    return render(request, "supplier_summary.html", context)

def system_summary(request):
    total_barang = Item.objects.count()
    total_nilai = Item.objects.aggregate(total=Sum('price'))['total'] or 0
    total_kategori = Category.objects.count()
    total_supplier = Supplier.objects.count()
    context = {
        "total_barang": total_barang,
        "total_nilai": total_nilai,
        "total_kategori": total_kategori,
        "total_supplier": total_supplier
    }
    return render(request, "system_summary.html", context)