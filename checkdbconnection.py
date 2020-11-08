from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="192.168.64.2", name="addressbook", user="admin", password="admin")

try:
    l = db.get_contacts_not_in_group(Group(id="411"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
    #db.destroy()
