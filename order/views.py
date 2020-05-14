from django.shortcuts import render
from order.models import Order





def order(request):
    return render(request, 'order/order.html')


def orderview(request):
        print("YOUR ORDER IS PLACED")
        Email = request.POST["Email"]
        Phonenumber = request.POST["Phonenumber"]
        caketype = request.POST["caketype"]
        Quantity=request.POST["Quantity"]
        Comments = request.POST["Comments"]
        Address = request.POST["Address"]
        City = request.POST["City"]
        State = request.POST["State"]
        order_obj = Order(Email=Email, Phonenumber=Phonenumber, caketype=caketype, Quantity=Quantity,
                          Comments=Comments, Address=Address,
                          City=City, State=State, )
        order_obj.save()
        return render(request, 'order/done.html')



