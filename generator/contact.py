from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

print(opts)
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    #punctuation and space
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="",
            lastname="",
            nickname="", title="",
            company="", address="",
            homephone="", mobilephone="",
            workphone="", fax="", email_1="",
            email_2="",
            email_3="",
            homepage="",
            annday="", address_2="",
            secondaryphone="",
            notes_2="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), title=random_string("title", 20),
            company=random_string("company", 20), address=random_string("address", 30),
            homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10),
            workphone=random_string("workphone", 10), fax=random_string("fax", 10), email_1=random_string("email", 10),
            email_2=random_string("email2", 10),
            email_3=random_string("email3", 10),
            homepage=random_string("homepage", 10), birthday="2", birthmonth="August", birthyear="1900",
            annday="2",
            annmonth="March", annyear="1900", address_2=random_string("address2", 10),
            secondaryphone=random_string("secondaryphone", 10),
            notes_2=random_string("notes2", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))