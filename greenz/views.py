from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import NotFound
from django.db import connection
from django.contrib import messages
from greenz.models import *
from django.views import View



# main page
def main(request):
    if request.COOKIES.get('id'):
        return render(request, 'main.html', context={'text': 'Logout'})
    else:
        return render(request, 'main.html', context={'text': 'Login'})


# product list page(디폴트는 fresh food 리스트를 보여주는 페이지)
def product(request):
    product = FreshFoodList.objects.all()

    if request.COOKIES.get('id'):
        text = 'Logout'
    else:
        text = 'Login'

    return render(request, 'freshfood.html', context={'text': text, 'food_list': product})


def source(request):
    if request.COOKIES.get('id'):
        return render(request, 'source.html', context={'text': 'Logout'})
    else:
        return render(request, 'source.html', context={'text': 'Login'})


def freshfood(request, product_id):
    try:
        product = FreshFoodList.objects.get(id=product_id)
    except Product.DoesNotExist:
        product = None

    if product is None:
        raise NotFound("페이지를 찾을 수 없습니다.")

    if request.COOKIES.get('id'):
        text = 'Logout'
    else:
        text = 'Login'

    return render(request, 'product.html', context={'text': text, 'fresh_food': product})


# recipe list page
def recipe(request):
    if request.COOKIES.get('id'):
        return render(request, 'Recipe_List.html', context={'text': 'Logout'})
    else:
        return render(request, 'Recipe_List.html', context={'text': 'Login'})


# restaurant list page
def restaurant(request):
    info_res = RMAP.objects.all()  # RMAP data 불러오기
    if request.COOKIES.get('id'):
        return render(request, 'Restaurant_map.html', context={'text': 'Logout', 'info_res': info_res})
    else:
        return render(request, 'Restaurant_map.html', context={'text': 'Login', 'info_res': info_res})


def list_restaurant(request, rmap_id):

    store = RMAP.objects.get(id=rmap_id)

    return render(request, 'Restaurant2.html', context={'store': store})


# cart page
def cart(request):
    if request.COOKIES.get('id'):
        return render(request, 'cart.html', context={'text': 'Logout'})
    else:
        messages.add_message(request, messages.ERROR, '권한이 없습니다. 로그인해주세요.')
        return render(request, 'login.html', context={'text': 'Login'})


def mypage(request):
    if request.COOKIES.get('id'):
        # return render(request, 'mypage.html', context={'text': 'Logout'})
        # if request.method == "GET":
            global datas
            try:
                userid = request.COOKIES.get('id')
                # userid = "user1"
                pk = User.objects.get(id=userid).uid
                cursor = connection.cursor()
                strSql = "SELECT uid,id, name, email, address,phone_number FROM user where uid=%d" % pk
                result = cursor.execute(strSql)
                user = cursor.fetchall()
                connection.commit()
                connection.close()

                # 사용자의 주문 번호에 따른 정보들
                cursor = connection.cursor()
                strSql = " CREATE OR REPLACE VIEW orderbill AS SELECT user_id, id from orders where user_id=%d order by created_date" % pk
                result = cursor.execute(strSql)
                connection.commit()
                connection.close()

                cursor = connection.cursor()
                strSql = "select * from orderbill"
                result = cursor.execute(strSql)
                orderbill = cursor.fetchall()
                connection.commit()
                connection.close()

                cursor = connection.cursor()
                # strSql = "CREATE OR REPLACE VIEW orderitems AS SELECT o.user_id,oi.cart_item_id, oi.order_id,p.name, p.cost, ci.quantity, o.created_date,status s from cart_item ci, product p, order_item oi,orders o, status s where o.user_id=%d and oi.cart_item_id=ci.id and ci.product_id=p.id and o.id=oi.order_id and o.status_id=s.id"%pk
                strSql = "CREATE OR REPLACE VIEW orderitems AS SELECT o.user_id, oi.order_id,p.name, p.cost, ci.quantity, o.created_date,s.status,p.image from cart_item ci, product p, order_item oi,orders o,status s where o.user_id=%d and oi.cart_item_id=ci.id and ci.product_id=p.id and o.id=oi.order_id and o.status_id=s.id" % pk
                result = cursor.execute(strSql)
                connection.commit()
                connection.close()

                cursor = connection.cursor()
                strSql = "CREATE OR REPLACE VIEW toi AS select order_id,created_date, ANY_VALUE(name) AS pname,status from orderitems group by order_id order by created_date"
                result = cursor.execute(strSql)
                strSql = "select * from toi"
                result = cursor.execute(strSql)
                orderitems = cursor.fetchall()
                connection.commit()
                connection.close()

                # 총가격
                orders = []
                cursor = connection.cursor()
                for ob in orderbill:
                    strSql = "select order_id,sum(cost*quantity) as Price from orderitems where order_id=%d" % ob[1]
                    result = cursor.execute(strSql)
                    temp = cursor.fetchall()
                    orders.append(temp[0][1])
                    # temp+=temp
                connection.commit()
                connection.close()

                # 건수
                orderpnum = []
                cursor = connection.cursor()
                for ob in orderbill:
                    strSql = "select count(name)-1 as casenum  from orderitems where order_id=%d" % ob[1]
                    result = cursor.execute(strSql)
                    temp = cursor.fetchall()
                    orderpnum.append(temp[0])
                    # temp+=temp
                connection.commit()
                connection.close()

                # 상세 내역 보기
                orderdetail = []
                cursor = connection.cursor()
                for ob in orderbill:
                    strSql = "select name,cost*quantity as price from orderitems where order_id=%d" % ob[1]
                    result = cursor.execute(strSql)
                    temp = cursor.fetchall()
                    orderdetail.append(temp)
                    # temp+=temp
                connection.commit()
                connection.close()

                # 이미지
                img = []
                cursor = connection.cursor()
                for ob in orderbill:
                    strSql = "select image from orderitems where order_id=%d" % ob[1]
                    result = cursor.execute(strSql)
                    temp = cursor.fetchall()
                    img.append(temp[0])
                    # temp+=temp
                connection.commit()
                connection.close()

                forder = []
                i = 0
                for data in orderitems:
                    row = [
                        data[1],  # 날짜
                        data[2],  # 상품명
                        data[0],  # 주문번호
                        orders[i],  # 결제 금액
                        data[3],  # 배송상태
                        orderpnum[i],  # 건수
                        orderdetail[i],
                        img[i],
                    ]
                    i = i + 1
                    forder.append(row)



            except:
                connection.rollback()
                print("Failed selecting in mypageview")

            context = {'user': user,
                       'forder': forder,
                       'text': 'Logout'
                       }
            # return HttpResponse(orderlist)
            # return render(request, 'mypage.html', context={'user':user})
            # return render(request, 'mypage.html', context={'orderlist':orderlist})
            return render(request, 'mypage.html', context)
    else:
        messages.add_message(request, messages.ERROR, '권한이 없습니다. 로그인해주세요.')
        return render(request, 'login.html', context={'text': 'Login'})




@csrf_exempt
def join_view(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        phone_number = request.POST.get("phone_number")

        # User 모델 가져오기
        user = User()
        user.id = id
        user.name = name
        user.email = email
        user.password = password
        user.address = address
        user.phone_number = phone_number

        # db에 저장
        user.save()

        nowuser = User.objects.get(id=id)
        # cart 생성
        cart = Cart()
        cart.user_id = nowuser.uid
        cart.save()

    return render(request, 'main.html')



# login page
@csrf_exempt
def login(request):
    if request.COOKIES.get('id'):
        messages.add_message(request, messages.INFO, '로그아웃 되었습니다.')
        response = render(request, 'main.html', context={'text': 'Login'})
        response.delete_cookie('id')
        return response
    else:
        return render(request, 'login.html', context={'text': 'Login'})


@csrf_exempt
def login_view(request):
    id = request.POST.get("id")
    password = request.POST.get("password")

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        user = None

    if user is None:
        messages.add_message(request, messages.WARNING, '아이디가 잘못되었습니다. 다시 입력해주세요.')
        return render(request, 'login.html', context={'text': 'Login'})

    if user.password == password:
        response = render(request, 'main.html', context={'text': 'Logout'})
        response.set_cookie('id', id)
        return response
    else:
        messages.add_message(request, messages.WARNING, '비밀번호가 잘못되었습니다.')
        return render(request, 'login.html', context={'text': 'Login'})

#
# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user.id

    # 여기서 카트 uid 담아와서 카트 받아오는거 수정해야함...
    cartall = Cart.objects.all()
    cart = Cart.objects.get(user=user)

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request, total=2000, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(user=request.user.id)
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.cost * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))

#edit
def edit(request):
    global usr
    if request.method == "POST":
        addr=request.POST['addr']
        name=request.POST['name']
        phone=request.POST['phone']
        userid = request.COOKIES.get('id')
        usera=User.objects.get(id=userid)
        usera.name=name
        usera.address=addr
        usera.phone_number=phone
        usera.save()
        return redirect('/greenz/mypage')
    elif request.method == "GET":
        global datas
        try:
            userid=request.COOKIES.get('id')
            # userid = "user1"
            pk = User.objects.get(id=userid).uid
            cursor = connection.cursor()
            strSql = "SELECT uid,id, name, email, address,phone_number FROM user where uid=%d" % pk
            result = cursor.execute(strSql)
            user = cursor.fetchall()
            connection.commit()
            connection.close()

            # 사용자의 주문 번호에 따른 정보들
            cursor = connection.cursor()
            strSql = " CREATE OR REPLACE VIEW orderbill AS SELECT user_id, id from orders where user_id=%d order by created_date" % pk
            result = cursor.execute(strSql)
            connection.commit()
            connection.close()

            cursor = connection.cursor()
            strSql = "select * from orderbill"
            result = cursor.execute(strSql)
            orderbill = cursor.fetchall()
            connection.commit()
            connection.close()

            cursor = connection.cursor()
            # strSql = "CREATE OR REPLACE VIEW orderitems AS SELECT o.user_id,oi.cart_item_id, oi.order_id,p.name, p.cost, ci.quantity, o.created_date,status s from cart_item ci, product p, order_item oi,orders o, status s where o.user_id=%d and oi.cart_item_id=ci.id and ci.product_id=p.id and o.id=oi.order_id and o.status_id=s.id"%pk
            strSql = "CREATE OR REPLACE VIEW orderitems AS SELECT o.user_id, oi.order_id,p.name, p.cost, ci.quantity, o.created_date,s.status,p.image from cart_item ci, product p, order_item oi,orders o,status s where o.user_id=%d and oi.cart_item_id=ci.id and ci.product_id=p.id and o.id=oi.order_id and o.status_id=s.id" % pk
            result = cursor.execute(strSql)
            connection.commit()
            connection.close()

            cursor = connection.cursor()
            strSql = "CREATE OR REPLACE VIEW toi AS select order_id,created_date, ANY_VALUE(name) AS pname,status from orderitems group by order_id order by created_date"
            result = cursor.execute(strSql)
            strSql = "select * from toi"
            result = cursor.execute(strSql)
            orderitems = cursor.fetchall()
            connection.commit()
            connection.close()

            # 총가격
            orders = []
            cursor = connection.cursor()
            for ob in orderbill:
                strSql = "select order_id,sum(cost*quantity) as Price from orderitems where order_id=%d" % ob[1]
                result = cursor.execute(strSql)
                temp = cursor.fetchall()
                orders.append(temp[0][1])
                # temp+=temp
            connection.commit()
            connection.close()

            # 건수
            orderpnum = []
            cursor = connection.cursor()
            for ob in orderbill:
                strSql = "select count(name)-1 as casenum  from orderitems where order_id=%d" % ob[1]
                result = cursor.execute(strSql)
                temp = cursor.fetchall()
                orderpnum.append(temp[0])
                # temp+=temp
            connection.commit()
            connection.close()

            # 상세 내역 보기
            orderdetail = []
            cursor = connection.cursor()
            for ob in orderbill:
                strSql = "select name,cost*quantity as price from orderitems where order_id=%d" % ob[1]
                result = cursor.execute(strSql)
                temp = cursor.fetchall()
                orderdetail.append(temp)
                # temp+=temp
            connection.commit()
            connection.close()

            # 이미지
            img = []
            cursor = connection.cursor()
            for ob in orderbill:
                strSql = "select image from orderitems where order_id=%d" % ob[1]
                result = cursor.execute(strSql)
                temp = cursor.fetchall()
                img.append(temp[0])
                # temp+=temp
            connection.commit()
            connection.close()

            forder = []
            i = 0
            for data in orderitems:
                row = [
                    data[1],  # 날짜
                    data[2],  # 상품명
                    data[0],  # 주문번호
                    orders[i],  # 결제 금액
                    data[3],  # 배송상태
                    orderpnum[i],  # 건수
                    orderdetail[i],
                    img[i],
                ]
                i = i + 1
                forder.append(row)



        except:
            connection.rollback()
            print("Failed selecting in mypageview")

        context = {'user': user,
                   'forder': forder,
                   }
        # return HttpResponse(orderlist)
        # return render(request, 'mypage.html', context={'user':user})
        # return render(request, 'mypage.html', context={'orderlist':orderlist})
        return render(request, 'mypageedit.html', context)