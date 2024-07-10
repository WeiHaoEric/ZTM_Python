# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
  def wrapper(*args, **kwargs):
    #  print(args, kwargs)
    if(len(args)>0):
        user = args[0]

        if(user['valid']==True):
            print(f"user{user['name']} is {user['valid']}")
            fn(*args, **kwargs)
        else:
            # print('valid' in list(kwargs.keys()), kwargs['valid']==True)
            print("Soooooooooorry")
    else:
       print("user not found!!")

  return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)