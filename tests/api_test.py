from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

url = 'http://52.43.66.226:8080/api/orders' # Set destination URL here
PASSED = "    \033[92mPASSED\033[0m"
FAILED = "    \033[91mFAILED\033[0m"

def test_create(customer, order, total, address, phone, isFulfilled = 'false'):
    print("> testing create")
    post_fields = {'customer': customer, 'order': order, 'total': total, 'address': address, 'phone':phone , 'isFulfilled':isFulfilled}     # Set POST fields here
    request = Request(url, urlencode(post_fields).encode())
    order = json.loads(urlopen(request).read().decode())
    if order['message'] == 'Order placed!':
        print(PASSED)
        return order['_id']
    else:
        print(FAILED)
        return ''

def test_get_all():
    print("> testing getting all")
    o = urlopen(url)
    if o.getcode() == 200:
        print(PASSED)
    else:
        print(FAILED)

def test_get_one(order_id):
    print("> testing getting one")
    o = urlopen(url+"/"+str(order_id))
    if o.getcode() == 200:
        print(PASSED)
    else:
        print(FAILED)

def test_update(order_id, customer, order, total, address, phone, isFulfilled = 'false'):
    print("> testing updating ")
    post_fields = {'customer': customer, 'order': order, 'total': total, 'address': address, 'phone':phone , 'isFulfilled':isFulfilled}     # Set POST fields here
    request = Request(url+"/"+str(order_id), urlencode(post_fields).encode(),method='PUT')
    order = json.loads(urlopen(request).read().decode())
    if order['message'] == 'Order updated!':
        print(PASSED)
    else:
        print(FAILED)

def test_delete(order_id):
    print("> testing deleting ")
    request = Request(url+"/"+str(order_id), method='DELETE')
    order = json.loads(urlopen(request).read().decode())
    if order['message'] == 'Successfully deleted':
        print(PASSED)
    else:
        print(FAILED)

def test_all():
    test_get_all()
    _id = test_create('Bruce Wayne', 'tonkatsu', '$7.59', 'Wayne Manor, Gotham City', '+1 (215) 890-7600')
    test_get_one(_id)
    # test_update()
    test_update(_id,'Bruce Wayne', 'tonkatsu', '$7.59', 'Wayne Manor, Gotham City', '+1 (215) 890-7600', 'true' )
    test_delete(_id)





# test_all()
test_delete('57c97fd07401380e00000002')
