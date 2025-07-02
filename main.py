import sys

# import pyjokes as pyjokes
import speech_recognition as sr
import pyttsx3

import pandas as pd
import numpy as np
from fpdf import FPDF
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('Arial', '', 14)


print(pd.__version__)
data = np.random.randint(0, 200, size=5)
# df = pd.DataFrame(data, columns=['column name'])
df = pd.read_csv('BANK.csv')

print(df.head())
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Welcome to Wisdom Banking Bot.')
# engine.say('tell your account number')

engine.runAndWait()
def talk(text):

    engine.say(text)
    engine.runAndWait()
    newVoiceRate = 90
    # engine.setProperty('rate', newVoiceRate)



def take_command():
    try:
        with sr.Microphone() as source:
            talk("listening bro")
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'wisdom' in command:
                command = command.replace('wisdom', '')
                print(command)
        print(command)
        return command
    except:
        print("didn't Get the Command")
        talk('did not Get the Command. want to restart?')
        talk('Say YES or No')
        response = take_command()
        print('this is the response',response)
        if('yes' in response or 's' in response):
            talk('restarting the system you have to give the operations from starting with account number.')
            run_alexa()
        elif('no' in response):
            talk('closing the bot. thank you visit again.')
            sys.exit()
        else:
            talk('no response recorded closing the bot')
            sys.exit()
        # take_command()



def run_alexa():
    try:

        talk('tell your account number.')
        command = take_command()
        command=list(command)
        voice = ""
        for i in command:
            if i != " ":
                print(i,command)
                voice += i

        print(voice , type(voice))

        if voice.isnumeric():
            accountnumber = int(voice)
            talk("Your account Number is"+str(accountnumber))
            print("HELLO")
            talk("please say your Name")
            name = take_command()
            talk(name)
            name = name.capitalize()
            print(name,accountnumber)
            talk("Your name is"+name+"and your account number is"+str(accountnumber))
            found = df.loc[df['AccountNo'] == accountnumber]
            # print(found)
            details = list(found)
            print(details)
            if (found["AccountHoldersName"] == name).bool():
                print(found["AccountHoldersName"])
                talk("you are verified"+name)
                print("Authentication Success")
                ss = int(found["BALANCE AMOUNT"].values[0])
                print(ss)
                print(type(ss))
                # talk("Your balance is"+found["BALANCE AMOUNT"])
                talk("you can go on with your banking")
                talk("speak ONE OR Banking for banking Services, Two or fill form for form filling")
                operation = take_command()
                print(operation)
                if('one' in operation or '1' in operation or 'bank' in operation):
                    print("Operations executed")
                    talk("speak one for balance checking , two for phone number update, three to go to back menu")
                    innerOper = take_command()
                    print(innerOper)
                    if ('one' in innerOper or '1' in innerOper or 'balance' in innerOper):
                        talk("your balance is "+str(ss))
                        print("your balance is"+str(ss))
                        print("Inner oper executed")
                        talk('you are going to starting of the operations')
                    elif ('two' in innerOper or '2' in innerOper or 'number' in innerOper):
                        talk("tell your Phone Number digit by digit like 1,2,3")
                        phone = take_command()
                        phone = list(phone)
                        number = ""
                        for i in phone:
                            if i != " ":
                                print(i, phone)
                                number += i

                        print(number, type(number))

                        if number.isnumeric():
                            phonenumber = int(number)
                            # # data = df.loc[df['AccountNo'] == 1234560124]
                            # indexx = df.loc[df['AccountNo'] == accountnumber].index
                            # print("index of data = ", int(indexx.values[0]))
                            # hehe = data["BALANCE AMOUNT"]
                            # # print(int(hehe.values[0]))
                            # df.loc[indexx, 'PhoneNumber'] = phonenumber
                            # print(df.loc[df['AccountNo'] == accountnumber])

                            data = df.loc[df['AccountNo'] == accountnumber]
                            indexx = df.loc[df['AccountNo'] == accountnumber].index
                            print("index of data = ", int(indexx.values[0]))
                            ind = int(indexx.values[0])
                            hehe = data["BALANCE AMOUNT"]
                            print(int(hehe.values[0]))
                            print("joo")
                            print(indexx)
                            print("hii")
                            df.loc[ind, 'PhoneNumber'] = phonenumber
                            print(df.loc[df['AccountNo'] == accountnumber])
                            df.to_csv("BANK.csv", index=False)
                            # if(df.to_csv("BANK.csv", index=False)):
                            print("Phone number Updated Successfully")
                            talk("updated successfully.")
                            talk("redirecting to home.")
                    elif('3' in innerOper or 'three' in innerOper):
                        sys.exit()
                elif('2' in operation or 'two' in operation or 'form' in operation):
                    print('operation2 is executing form filling')
                    talk('form filling')
                    talk('speak one or withdraw for withdraw form ,two or deposit for deposit form ,three or exit for back menu')
                    operation2 = take_command()
                    if('one' in operation2 or '1' in operation2 or 'withdraw' in operation2):
                        talk('tell the amount to withdraw from your account'+name)
                        amount = take_command()
                        amount = list(amount)
                        cash = ""
                        for i in amount:
                            if i != " ":
                                print(i, amount)
                                cash += i

                        print(cash, type(cash))

                        if cash.isnumeric():
                            cashAmount = int(cash)
                            print(cashAmount)

                            pdf = FPDF()
                            pdf.add_page()
                            pdf.set_font('Arial', '', 14)
                            talk("you are withdrawing"+str(cashAmount))
                            pdf.cell(200, 10, 'Bank for Blind\n', border=True, ln=5)
                            pdf.cell(200, 10, 'WithDrawl Form\n', border=True, ln=5)
                            pdf.cell(200, 10, 'Account No:\n'+str(accountnumber), border=True, ln=5)
                            pdf.cell(200, 10, 'Account Holders Name:\n'+name, border=True, ln=5)
                            pdf.cell(200, 10, 'Amount:\n' +str(cashAmount), border=True, ln=5)
                            pdf.cell(200, 10, 'Verified\n', border=True, ln=5)

                            pdf.output('w'+str(accountnumber)+'g.pdf', 'F')
                            talk('form filled successful')
                            talk('you are going to starting of the operations')
                    elif('two' in operation2 or '2' in operation2 or 'deposit' in operation2):

                        talk('tell the amount to deposit in your account' + name)
                        amount = take_command()
                        amount = list(amount)
                        cash = ""
                        for i in amount:
                            if i != " ":
                                print(i, amount)
                                cash += i

                        print(cash, type(cash))

                        if cash.isnumeric():
                            cashAmount = int(cash)
                            print(cashAmount)

                            pdf = FPDF()
                            pdf.add_page()
                            pdf.set_font('Arial', '', 14)
                            talk("you are depositing" + str(cashAmount))
                            pdf.cell(200, 10, 'Bank for Blind\n', border=True, ln=5)
                            pdf.cell(200, 10, 'Deposit Form\n', border=True, ln=5)
                            pdf.cell(200, 10, 'Account No:\n' + str(accountnumber), border=True, ln=5)
                            pdf.cell(200, 10, 'Account Holders Name:\n' + name, border=True, ln=5)
                            pdf.cell(200, 10, 'Amount:\n' + str(cashAmount), border=True, ln=5)
                            pdf.cell(200, 10, 'Verified\n', border=True, ln=5)

                            pdf.output('D' + str(accountnumber) + 'g.pdf', 'F')
                            talk('form filled successful.')
                            talk('you are going to starting of the operations')
                    else:
                        print("bye bye")
                        talk("Bye")
                        sys.exit()

            else:
                print("Wrong input")
                talk('account number is not correct.')
                talk('restarting')
                run_alexa()

        # elif 'play' in command:
        #     song = command.replace('play', '')
        #     talk('playing ' + song)
        #     pywhatkit.playonyt(song)
        # elif 'time' in command:
        #     time = datetime.datetime.now().strftime('%I:%M %p')
        #     talk('Current time is ' + time)
        # elif 'who is' in command:
        #     person = command.replace('who is', '')
        #     info = wikipedia.summary(person, 1)
        #     print(info)
        #     talk(info)
        # elif 'work' in command:
        #
        #     print('I can work by taking the user text and converting to the machine understandable form, through Speech Recognition.And the working process is simple one can tell the required options through the speaker and i can fill the forms and give them through the printer ')
        #     talk('i can work by taking the user text and converting to the machine understandable form, through Speech Recognition.And the working process is simple one can tell the required options through the speaker and i can fill the forms and give them through the printer')
        # elif 'purpose' in command:
        #     print('I am wisdom banking bot. i am developed to solve the problems that are facing by the blind people in banking system. I can fill forms , i can tell the bank balance,and can talk multiple languages.')
        #     talk('I am wisdom banking bot. i am developed to solve the problems that are facing by the blind people in banking system.')
        #     talk('I can fill forms , i can tell the bank balance,and can talk multiple languages')
        # elif 'operations' in command:
        #     print('one for form filling , two for banking services')
        #     talk('one for form filling , two for banking services')
        # elif 'joke' in command:
        #     talk(pyjokes.get_joke())
        elif 'close' in command:
            sys.exit()
        else:
            talk('Please say the command again.')
    except:
        talk('sorry system failed')
        talk("do you want to continue from starting?")
        talk("say yes or no.")
        response = take_command()
        if('yes' in response or 's' in response or 'restart' in response):
            run_alexa()
        elif('no' in response or 'close' in response or 'exit' in response):
            talk('closing the bot. thank you. visit again')
            sys.exit()


while True:
    run_alexa()