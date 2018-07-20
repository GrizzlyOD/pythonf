people={
    'alice':{
        'phone':'2345',
        'addr':'foo drive 23'
        },
    'beth':{
      'phone':'9102',
      'addr':'bar street 45'
      },
    'cecil':{
      "phone":"3158",
      "addr":"baz avenue 90"
      }
    }

labers={
    "phone":"phone number",
    'addr':'address'
    }

name=input("name:")
request=input("phone number (p) or address(a)")

if request=="p":key="phone"
if request=='a':key='address'
if name in people : print("%s's %s is %s ." %(name,labers[key],people[name][key]))
