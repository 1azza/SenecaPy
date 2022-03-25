import seneca


user = seneca.User('017437@brgsmail.org.uk', 'Larry1102')


s = user.Session(user.idToken, 'f60acc5d-57d8-4833-96b1-bae36baaf12e')
s.SubmitData()




