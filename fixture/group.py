class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group_object, word):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group_object)
        print(word)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def test_delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # delete
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    #def edit_first_group(self, group):
        #wd = self.app.wd
        #self.open_group_page()
        # open edit page
        #wd.find_element_by_name("selected[]").click()
        #wd.find_element_by_name("edit").click()
        #self.fill_group_form(group)
        # submit group creation
        #wd.find_element_by_name("update").click()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open edit form
        wd.find_element_by_name("edit").click()
        # fill group firm
        self.fill_group_form(new_group_data)
        # submit group edit
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
