import seneca

user = seneca.User('017437@brgsmail.org.uk', 'Larry1102')
print('New knowledge score:')    
ks = user.info.getKnowledgeScore()   
ks = round(ks/1000000000000, 1)
print(ks)
