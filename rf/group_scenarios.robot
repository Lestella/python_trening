*** Settings ***
Library  rf.AddressBook
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new group
    Create Group  name1  header 1  footer1