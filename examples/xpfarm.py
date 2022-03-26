import seneca
import threading
import time
EMAIL = input('Please enter your email for senecalearning.com: ')
PASSWORD = input('Please enter your password for senecalearning.com: ')
def main():
    args = round(int(input('How many times would you like to complete the section? '))/4)
    
    def go(iterations):
        for i in range(iterations):
            s.SubmitData()
    print('ok')
    user = seneca.User(USERNAME, PASSWORD)
    s = user.Session('g60fcc5d-57d8-4833-96b1-bae36baaf12e', user)
    s.Start()
    
    x1 = threading.Thread(target=go, args=(args,))
    x3 = threading.Thread(target=go, args=(args,))
    x2 = threading.Thread(target=go, args=(args,))
    x4 = threading.Thread(target=go, args=(args,))
    
    x1.start()
    x2.start()
    x3.start()
    x4.start()
    
    x1.join()
    x2.join()
    x3.join()
    x4.join()
    
    time.sleep(1)
    print('\n\nNew knowledge score:')    
    ks = user.info.getKnowledgeScore()   
    ks = round(ks/1000000000000, 1)
    print(ks, 'T\n\n')
    main()
main()
    
