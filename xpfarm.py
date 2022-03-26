import seneca


user = seneca.User('017437@brgsmail.org.uk', 'Larry1102')


s = user.Session('g60fcc5d-57d8-4833-96b1-bae36baaf12e', user)


s.Start()

for i in range(50):
    s.SubmitData()



