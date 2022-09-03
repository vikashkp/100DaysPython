import resource as Res


def report():
    global res
    print(f"Water: {res.get('Water')}ml")
    print(f"Milk: {res.get('Milk')}ml")
    print(f"Coffee: {res.get('Coffee')}g")
    print(f"Money: ${res.get('Money')}")


def get_req(coffee_type):
    if coffee_type == "espresso":
        return Res.espresso_req
    elif coffee_type == "latte":
        return Res.latte_req
    elif coffee_type == "cappuccino":
        return Res.cappuccino_req
    print("Unknown Coffee Type")
    return None


def check_req(req):
    if res.get('Milk') < req.get('Milk'):
        print("Sorry there is not enough Milk.")
        return False
    if res.get('Water') < req.get('Water'):
        print("Sorry there is not enough Water.")
        return False
    if res.get('Coffee') < req.get('Coffee'):
        print("Sorry there is not enough Coffee.")
        return False
    return True


def handle_money(req):
    print('Please insert coins.')
    quarter = int(input('How many quarters?:'))
    dime = int(input('How many dimes?:'))
    nickle = int(input('How many nickles?:'))
    penny = int(input('How many pennies?:'))
    amount = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (penny * 0.01)
    print(f"Amount entered ${amount}")
    is_enough_money = amount > req.get('Cost')
    if is_enough_money:
        print(f"Here is ${round(amount - req.get('Cost'),2)} in change")
    else:
        print(f"Sorry that's not enough money. Money refunded.")
    return is_enough_money


def make_coffee(req):
    res['Milk'] = res.get('Milk') - req.get('Milk')
    res['Water'] = res.get('Water') - req.get('Water')
    res['Coffee'] = res.get('Coffee') - req.get('Coffee')
    res['Money'] = res.get('Money') + req.get('Cost')


def process(coffee_type):
    if not check_req(get_req(coffee_type)):
        return
    if not handle_money(get_req(coffee_type)):
        return
    make_coffee(get_req(coffee_type))
    print(f"Here is your {coffee_type} ☕ Enjoy")


res = Res.resource
while True:
    inp = input("What would you like? (espresso/latte/cappuccino):")
    if inp == "report":
        report()
    elif inp == "off":
        print("Turning Machine Off!")
        break
    elif inp == "espresso" or inp == "latte" or inp == "cappuccino":
        process(inp)
    else:
        print('Invalid input! Try Again!')
