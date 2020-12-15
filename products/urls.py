from django.urls import path, include
import products.views

urlpatterns = [

    # View routes
    path('shop', products.views.view_shop,
         name="view_shop"),
    path('view/<product_id>', products.views.view_single_product,
         name="view_single_product"),

    # Create routes
    path('create', products.views.create_product,
         name="create_product"),
    path('create-category', products.views.create_category,
         name="create_category"),
    path('create-supplier', products.views.create_supplier,
         name="create_supplier"),
    
    # Update routes
    path('update/<product_id>', products.views.update_product,
         name="update_product"),
    path('update-category/<category_id>', products.views.update_category,
         name="update_category"),
    path('update-supplier/<supplier_id>', products.views.update_supplier,
         name="update_supplier"),

    # Delete routes
    path('delete/<product_id>', products.views.delete_product,
         name="delete_product"),
]
