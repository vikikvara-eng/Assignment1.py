cart_total = (150)

user_status = "vip"

has_promo_code = True

loyalty_points =  (750)

delivery_city = "batumi"

is_account_active = True

if is_account_active == False:
    print  ("account is blocked,order cannot be processed")

if cart_total <= 0:
    print ("error")

    cart_total = 100

if user_status == "vip":
    cart_total =(cart_total * 0.8) 

    if loyalty_points >= 500:
        cart_total=(cart_total * 0.95)

        if has_promo_code == True:
             cart_total =(cart_total * 0.9)


             print (cart_total)

if user_status == "admin":
    cart_total = (cart_total * 0.5)

if delivery_city in ["batumi", "tbilisi","kutaisi"]:
    if cart_total >= 100:
        delivery_Free = 0
    else:
        delivery_Free = 5
else:
    delivery_Free = 15

    Final_amount = cart_total + delivery_Free
    print (cart_total)
    print(delivery_Free)
    print(Final_amount)