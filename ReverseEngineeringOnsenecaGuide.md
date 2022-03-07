# Welcome to my senecalearning.com reverseing guide!

So far I have three ways of messing about with this website:
1. Manipulating the html elements with a js bookmarklet
2. Sending fake GET request to the website api for the json with the answer in
3. Sending fake POST request to website pretending to have done the 



> HTML METHOD
1. Make js script to locate hidden words on the page
2. Make the script change the class of the word from blurred to none
3. Find the hidden answer and copy using clipboard api
4. ez
> GET METHOD
1. Iterate through window.perfomance.logs()
2. Find one equal to 144 characters long this should be the right url
3. Get tonnes of auth stuff from it like signature, policy, correlationid
4. Make a reuqest to this adress and it should respond with another url
5. Make a request to this url
6. That was the easy bit
7. Now spend weeks making a script to parse it
8. Done

> POST METHOD
1. Soon...

