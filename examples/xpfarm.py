import seneca
import threading
import concurrent.futures
import time
import logging
logging.basicConfig(level=logging.INFO)
def main():                 
    EMAIL = input('Please enter your email for senecalearning.com: ')
    PASSWORD = input('Please enter your password for senecalearning.com: ')
    try: 
        user = seneca.User(EMAIL, PASSWORD)
    except Exception as e:
        if e.__class__.__name__ == 'InvalidCredentials':
            print('Error! please enter valid credentials\n')
            main()

    def sesh():
        args = round(int(input('How many times would you like to complete the section? '))/4)
        def go(iterations):
            for i in range(iterations):
                s.SubmitData()
        s = user.Session('g60fcc5d-57d8-4833-96b1-bae36baaf12e', user)
        oks = user.info.getKnowledgeScore()   
        oks = round(oks/1000000000000, 1)
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
        s.End()
        nks = user.info.getKnowledgeScore()   
        nks = round(nks/1000000000000, 1)
        print('\n\nknowledge score increase:')    
        print(f'{oks}T ---> {nks}T\n\n')
        sesh()
    sesh()  
main()
