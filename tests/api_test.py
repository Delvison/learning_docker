from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://127.0.0.1:8080/api/orders' # Set destination URL here
PASSED = "    \033[92mPASSED\033[0m"
FAILED = "    \033[91mFAILED\033[0m"

def test_create(customer, order):
    post_fields = {'customer': customer, 'order': order}     # Set POST fields here
    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    return json

def test_get_all():
    json = urlopen(url).read().decode()
    return json

def test_get_one(order_id):
    json = urlopen(url+"/"+str(order_id)).read().decode()
    return json

def test_update(order_id, customer, order):
    post_fields = {'customer': customer, 'order': order}
    request = Request(url+"/"+str(order_id), urlencode(post_fields).encode(),method='PUT')
    json = urlopen(request).read().decode()
    return json

def test_delete(order_id):
    request = Request(url+"/"+str(order_id), method='DELETE')
    json = urlopen(request).read().decode()
    return json

def test_all():
    print("> testing create")
    print(PASSED) if test_create('delvison','cheese pizza') == '{"message":"Order placed!"}' else print(FAILED)
    print("> testing getting all")
    print(test_get_all())
    print("> testing getting one")
    print(test_get_one(345))
    print("> testing updating ")
    print(test_update(345, 'delvison', 'cheeseburger'))
    print("> testing deleting ")
    print(test_delete(345))




test_all()
