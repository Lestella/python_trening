def test_clear_group(app):
    while 0 != app.group.count_groups():
        app.group.delete_first_group()
    else:
        print("Group list is already empty")
