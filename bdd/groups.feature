Scenario: Add new group
    Given a group list
    Given a group with <name>, <header> and <footer>
    When I add a the group the list
    Then the new group list is equal the old list with the added group

    Example:
    |name|header|footer|
    |name1|header1|footer1|
    |name2|header2|footer2|