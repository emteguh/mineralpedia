import paypalrestsdk
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Product
from .forms import OrderForm
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    TemplateView,
)

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    context_object_name = 'product'
    
    
class OrderView(FormView):
    template_name = 'product/product_order.html'
    form_class = OrderForm
    success_url = 'thank-you/'  # URL untuk halaman setelah berhasil checkout
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])  # Ganti dengan logika pengambilan produk yang sesuai
        context['price'] = product.price
        return context

    def form_valid(self, form):
        # Simpan instance Order ke database menggunakan ModelForm
        self.order = form.save()
        # return super().form_valid(form)

        # Proses pembayaran menggunakan PayPal
        paypalrestsdk.configure({
            "mode": "sandbox",  # Ganti dengan "live" jika sudah di produksi
            "client_id": "AW324B4Y4NbZXj6vfGSDic0v6MY_9V-xqEsYfy_6Wa-vuv2P-70cXTez2enxJlsf9nVJz7jIDIIVJuHV",
            "client_secret": "EDsBzYdVYXeKbNkeks74gcz6-KoEONyOVQxseIOOzjAAle-x8GOOh41oXqGz8uv0xr1L0IrW7weTnFNU"
        })

        # Buat objek pembayaran PayPal
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": self.request.build_absolute_uri(self.get_success_url()),
                "cancel_url": self.request.build_absolute_uri(self.get_cancel_url())
            },
            "transactions": [
                {
                    "amount": {
                        "total": str(self.order.total_amount),  # Total pembayaran dari order
                        "currency": "USD"  # Ganti dengan mata uang yang sesuai
                    },
                    "description": "Deskripsi pembayaran"  # Deskripsi pembayaran yang ingin ditampilkan
                }
            ]
        })

        # Buat pembayaran PayPal
        if payment.create():
            # Redirect pengguna ke halaman pembayaran PayPal
            for link in payment.links:
                if link.method == "REDIRECT":
                    redirect_url = str(link.href)
                    return HttpResponseRedirect(redirect_url)
        else:
            # Handle jika pembuatan pembayaran gagal
            # Misalnya, tampilkan pesan kesalahan atau redirect kembali ke halaman checkout
            return super().form_invalid(form)
        
    def get_cancel_url(self):
        pk = self.kwargs['pk']  # Mendapatkan nilai pk dari argumen URL
        return reverse_lazy('product:product-order', kwargs={'pk': pk})


    def form_invalid(self, form):
        # Handle jika form checkout tidak valid
        # Misalnya, tampilkan pesan kesalahan atau redirect kembali ke halaman checkout
        return super().form_invalid(form)

class ThankYouView(TemplateView):
    template_name = 'product/thank_you.html'
    
