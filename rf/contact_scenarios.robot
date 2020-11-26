*** Settings ***
Library  rf.AddressBook
Library  Collections
Library  BuiltIn

Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***

Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname  secondname  address
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}


Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}


Edit contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    ${new_contact}=  New Contact  firstname1  lastname1  address1
    Edit Contact  ${contact}  ${new_contact}
    ${new_list}=  Get Contact List
    List Should Contain Value  ${new_list}  ${new_contact}
    List Should Not Contain Value  ${new_list}  ${contact}
    Contact Lists Len Should Be Equal  ${new_list}  ${old_list}