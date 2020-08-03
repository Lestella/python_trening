# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app):
    app.group.create(Group(name="Group 1", header="egwtg", footer="wrtrth"), word="pohui cho")
    app.session.logout()

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""), word="pohui cho")
