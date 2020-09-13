from model.group import Group
from timeit import timeit


# def test_group_list(app, db):
#     ui_list = app.group.get_group_list()
#     def clean(group):
#         return Group(id=group.id, name=group.name.strip())
#     db_list = db.get_group_list()
#     assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_group_list_time(app, db):
    print("ui", timeit(lambda: app.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print("db", timeit(lambda: map(clean, db.get_group_list()), number=1))
    assert False
