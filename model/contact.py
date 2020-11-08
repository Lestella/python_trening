from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 nickname=None, title=None, company=None, address=None,
                 fax=None, email_1=None, email_2=None, email_3=None,
                 homepage=None, birthday=None, birthmonth=None,
                 birthyear=None, annday=None, annmonth=None,
                 annyear=None, address_2=None, notes_2=None,
                 id=None, all_phones_from_home_page=None, all_phones_from_view_page=None,
                 all_emails_from_home_page=None, all_main_info_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
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
        self.notes_2 = notes_2
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_phones_from_view_page = all_phones_from_view_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_main_info_from_home_page = all_main_info_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,
                                      self.address, self.homephone, self.mobilephone,
                                      self.workphone, self.secondaryphone, self.email_1, self.email_2, self.email_3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname and self.address == other.address and self.all_phones_from_home_page == other.all_phones_from_home_page and self.all_emails_from_home_page == other.all_emails_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
