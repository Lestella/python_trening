from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, hometelephone=None, mobiletelephone=None, worktelephone=None,
                 fax=None, email_1=None, email_2=None, email_3=None, homepage=None, birthday=None, birthmonth=None,
                 birthyear=None, annday=None, annmonth=None, annyear=None, address_2=None, home_2=None, notes_2=None,
                 id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.hometelephone = hometelephone
        self.mobiletelephone = mobiletelephone
        self.worktelephone = worktelephone
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birthday = birthday
        self.birthmonth = birthmonth
        self.birthyear = birthyear
        self.annday = annday
        self.annmonth = annmonth
        self.annyear = annyear
        self.address_2 = address_2
        self.home_2 = home_2
        self.notes_2 = notes_2
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
