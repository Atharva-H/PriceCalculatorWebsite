from calculator.models import User


def test_handler_get():
    user = User.objects.all()
    userlist = []
    for i in user:
        userlist.append(i.username)
    return userlist


def test_handler_post(request_body):

    user = User.objects.all()
    userlist = []
    for i in user:
        userlist.append(i.username)
    return userlist
