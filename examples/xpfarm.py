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
            logging.error('Please enter valid credentials')
            main()

    def sesh():
        args = int(input('How many times would you like to complete the section? '))
        threads = int(input("How many threads?"))
        if threads >= 10:
            logging.warning("High thread amounts may affect stability")

        args = round(args/threads)
        def go(iterations):
            for i in range(iterations):
                s.SubmitData()
        s = user.Session('g60fcc5d-57d8-4833-96b1-bae36baaf12e', user)
        oks = user.info.getKnowledgeScore()
        oks = round(oks/1000000000000, 1)
        s.Start()
        for i in range(threads):
            x1 = threading.Thread(target=go, args=(args,))
            x1.start()
        for i in range(threads):    
            x1.join()
        time.sleep(1)
        s.End()
        nks = user.info.getKnowledgeScore()
        nks = round(nks/1000000000000, 1)
        print('\n\nknowledge score increase:')
        print(f'{oks}T ---> {nks}T\n\n')
        sesh()
    sesh()
main()
