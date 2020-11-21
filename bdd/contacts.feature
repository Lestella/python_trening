Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <homephone>, <mobilephone>, <workphone>, <secondaryphone>, <address>, <email_1>, <email_2>, <email_3>
  When I add a the contact the list
  Then the new contact list is equal the old list with the added contact

  Examples:
  |firstname|lastname|homephone|mobilephone|workphone|secondaryphone|address|email_1|email_2|email_3|
  |firstname1|lastname1|homephone1|mobilephone1|workphone1|secondaryphone1|address1|email_1_1|email_2_1|email_3_1|
  |firstname2|lastname2|homephone2|mobilephone2|workphone2|secondaryphone2|address2|email_1_2|email_2_2|email_3_2|

 Scenario Outline: Edit contact
  Given a contact list
  Given a random contact
  Given a contact with the new data
  When I edit contact data
  Then the new contact list is equal the old list with the edited contact

  Scenario Outline: Delete contact
   Given a contact list
   Given a random contact
   When I delete contact
   Then the new contact list is equal the old list with the deleted contact
