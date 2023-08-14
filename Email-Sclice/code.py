while True:
    email_id = input("Enter email to slice= ")
    if email_id.count('@') == 1 and len(email_id[:email_id.index('@')])>0 and len(email_id[email_id.index('@'):]):
        print("Your user name is:- ",email_id[:email_id.index('@')])
        print("Domain name:- ",email_id[email_id.index('@')+1:])
    elif email_id == 'exit' :
        break
    else:
        print("Enter a valid Email id..!!")