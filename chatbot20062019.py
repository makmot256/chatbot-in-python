# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:03:28 2019

@author: Dr. G. Sambasivam
"""

import pyttsx3
import speech_recognition as sr 
import time

    
engine = pyttsx3.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
engine.say("Hi welcome, to isbat university, how can i help you:")
engine.setProperty('rate',140)
engine.setProperty('volume', 2.0)
engine.runAndWait() 

#while True:
#    r = sr.Recognizer()
#    with sr.Microphone() as source:
#        audio = r.listen(source)
#        question = r.recognize_google(audio)
#        question = question.lower()
#            
#        if question in ['hi','hello', 'hey','good morning','good afternoon','good evening','good noon']:
#                currentTime = int(time.strftime('%H'))   
#                #print(currentTime)
#                if currentTime < 12:
#                    greeting = "Good morning"
#                    print(greeting)
#                    engine.setProperty('voice', en_voice_id)
#                    engine.say("hello"+greeting)
#                    rate=engine.getProperty('rate')
#                    engine.setProperty('rate',rate-10)
#                    engine.setProperty('volume', 2.0)
#                    engine.runAndWait()
#                    break;
#                elif currentTime < 18:
#                     greeting = "Good afternoon"
#                     print(greeting)
#                     voices=engine.getProperty('voices')
#                     engine.setProperty('voice', en_voice_id)
#                     engine.say("hello"+greeting)
#                     rate=engine.getProperty('rate')
#                     engine.setProperty('rate',rate-10)
#                     #engine.setProperty('rate',155)
#                     engine.setProperty('volume', 2.0)
#                     engine.runAndWait()
#                     break;
#                else:
#                    greeting = "Good Evening"
#                    print(greeting)
#                    print("Hello")
#                    voices=engine.getProperty('voices')
#                    engine.setProperty('voice', 1)
#                    engine.say("hello"+greeting)
#                    engine.setProperty('rate',155)
#                    engine.setProperty('volume', 2.0)
#                    engine.runAndWait()
#                    break;


while True:
   #en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
   r = sr.Recognizer()
   with sr.Microphone() as source:
        #print("please feel free to ask")
        engine.setProperty('voice', en_voice_id)
        engine.say("please feel free to ask:")
        engine.setProperty('rate',155)
        engine.setProperty('volume', 2.0)
        engine.runAndWait()
        audio = r.listen(source)
        
        try:
            question_recognize = r.recognize_google(audio)
            question_recognize = question_recognize.lower()
            mylist=question_recognize.split()
            print(mylist)
            #question=""
            tinylist = [
'hello',

'who',
'morning',
'afternoon',
'evening',
'noon','name',
'created',
'doing',
'fees',
'fee',
'mission',
'vision',
'times',
'time',
'center',
'semsester',
'scholarships',
'scholarship',
'studies',
'facilities',
'faculty',
'faculties'
'course ',
'dollars',
'installments',
'installment',
'accommodation', 
'online', 
'test', 
'engineering',
'courses', 
'batch',
'graduating',
'evening batch',
'international', 
'business',
'duration',
'admissions',
'admission',
'departments ',
'campus',
'weekend ',
'holidays',
'holiday',
'co-curricular',
'cocurricular',
'minimum',
'engineering',
'languages',
'language',
'animation',
'photography', 
'job',
'study',
'opportunities',
'foundation',
'security',
'semester',
'cyber',
'graduation',
'internship',
'internships',
'industrial',
'library',
'elibrary',
'e-library',
'esports',
'esport',
'commerce',
'blended',
'upcoming',
'transport',
'diploma',
'computer',
'pay',
'job', 
'opportunities',
'thank',
'thank you',
'certificate',
'placement',
'prometric',
'jb',
'john bosco',
'batch','requirements',
'ai','artificial intellgence','bye']
            
#            for question in mylist:
#	            for item1 in tinylist:
#		            if question == item1:
#                       question = question
#                    
#                                        else:
#                        question =question_recognize
                        
            for questionn in mylist:
	            for item in tinylist:
                      if questionn == item:
                          question=questionn
#                      else: 
#                          questionnot=question_recognize.lower
#                          question=questionnot
#                          break                                 #print(questionn)
                        
                        #question=question
                                                                                 
		            #else:
			           # question=question_recognize
                        
                        #question=question_recognize           
                        
            print("the splittedn one---" + question) 
            #print("the recognized one:-" +question_recognize)
            if question in ['hi','hello', 'hey','morning','afternoon','evening','noon']:
                          
                currentTime = int(time.strftime('%H'))   
                if currentTime < 12:
                   greeting = "Good Morning"
                   engine.setProperty('voice', en_voice_id)
                   engine.say("hello"+greeting)
                   engine.runAndWait()
                elif currentTime < 18:
                   greeting = "Good afternoon"
                     #print(greeting)
                   voices=engine.getProperty('voices')
                   engine.setProperty('voice', en_voice_id)
                   engine.say("hello"+greeting)
                   engine.runAndWait()
                else:
                   greeting = "Good Evening"
                   voices=engine.getProperty('voices')
                   engine.setProperty('voice', 1)
                   engine.say("hello"+greeting)

            elif question in ['what is your name','who are you','who created you','is your name','name','created']:
              
                 engine.say("my name is PhantomBot created by the Code engineers group of isbat Univeristy. The people who created me are Donnie, Zeph, Lailah,Johnson, Fanny and Chavito. i am here to help you and provide information about isbat university",'name')
                 engine.setProperty('rate',120)
                 engine.setProperty('volume', 0.9)
                 engine.runAndWait()
                 
            elif question in ['how are you','you']:
                #print("I am fine how are you")
                engine.say("I am fine how are you")
                engine.setProperty('rate',120)
                engine.setProperty('volume', 0.9)
                engine.runAndWait()
           
            elif question in ['what are the study times','times','time','studies']:
                #print("we have day, evening and weekend classes. you can enroll as a student or distance")
                engine.say("Day batch is from 9am to 4pm and evening is from 5pm to 8pm")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you have prometric centre', 'prometric']:
                engine.say("yes we do have a prometric centre")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['job', 'what job oppurtunities are there for cyber security']:
                engine.say("there are many job oppurtunities like cyber security officer, ethical hacker")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you offer scholarships','scholarships','scholarship','do you have scholarships']:
                #print("the university fulfills its social responsibility by offering bursaries to economically backward and academically excelled students through talent hunt scholarship exams")
                engine.say("the university fulfills its social responsibility by offering bursaries, to economically backward and academically excelled students through, talent hunt scholarship exams")
                engine.setProperty('rate',120)
                engine.setProperty('volume', 0.9)
                engine.runAndWait()
            elif question in ['do you have a business course','business','commerce']:
                engine.say("yes we do have business courses, we offer bachelor in business administration, bachelors in hospitality and tourism management, bachelors in commerce in information technology, bachelor of human resource management, bachelor of science in applied economics")
                engine.setProperty('rate',100)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what are the facilities in campus','facilities','facility']:
                #print(":  we have cafeteria, hostel on request, in campus bank facility with atm, wi-fi and biometric access , transport facility")
                engine.say(":  we have cafeteria, hostel on request, in campus bank facility with atm, wi-fi and biometric access , transport facility")
                engine.setProperty('rate',120)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['how many faculties do you have','faculty','faculties']:
                #print("we have efficient faculties in engineering, management and commerce and information and communication technology and cyber vault")
                engine.say("we have efficient faculties in engineering, management and commerce and information and communication technology and cyber vault")
                engine.setProperty('rate',120)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['courses in isbat university','what course do you have','list the courses','course''courses in isbat university','what courses do you have','course','courses']:
                #print("we offer courses like Bachelor of Science in Applied Information technology duration is 3 years, Bachelor of Science in Multimedia & Animation duration is 3 years,Bachelor of Science in Networking and Cyber Security duration is 3 years,Post Graduate Diploma in Information Technology and duration is one year,Master of Science in Information Technology and duration is 2 years")
                engine.say("we offer business courses, computer courses and engineering courses so which one would you like to do?")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in['computer','what computer courses do you offer']:
                #print("we offer courses like Bachelor of Science in Applied Information technology duration is 3 years, Bachelor of Science in Multimedia & Animation duration is 3 years,Bachelor of Science in Networking and Cyber Security duration is 3 years,Post Graduate Diploma in Information Technology and duration is one year,Master of Science in Information Technology and duration is 2 years")
                engine.say("we offer courses like Bachelor of Science in Applied Information technology, Bachelor of Science in Multimedia & Animation,Bachelor of Science in Networking and Cyber Security duration,Post Graduate Diploma in Information Technology and duration,Master of Science in Information Technology")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['online','where can i do online exams','is there any test center here','which tests are done in the test center']:
                #print("Yes, you can do online exams from here. Our test center is on the second floor, next to ROOM 200. In there, we have a personnel who will assist you in any way possible.")
                engine.say("Yes, you can do online exams from here. Our test center is on the second floor, next to ROOM 200. In there, we have a personnel who will assist you in any way possible.")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['engineering''which engineering courses do you offer','Do you have engineering at isbat','engineering']:
                #print("We offer only two Engineerifdhj,k,ng courses, Bachelors in Electronics And Communication engineering and Bachelors in Computer Science Engineering")
                engine.say("We offer only two Engineering courses, Bachelors in Electronics And Communication engineering and Bachelors in Computer Science Engineering")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['Can you expalin about be ce and be ece','explain']:
                #print("be.ec deals with electronic circuits and how they work and communication is basically telecommunication.be ce basically deals with computer learning, both hardware and software… alongside computer programming")
                engine.say("be.ec deals with electronic circuits and how they work and communication is basically telecommunication.be ce basically deals with computer learning, both hardware and software… alongside computer programming")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['pay','how much do you pay per semester','what is the cost or tuition','how much do foreign students pay','how much does it cost','dollars', 'cost']:
                #print("for be.ec, local students pay usd 1000 and foreign students, usd 1,100 per semester.for bsc. ce local students pay usd 800 and foreign students, usd 1,000 per semester.")
                engine.say("for be.ec, local students pay usd 1000 and foreign students, usd 1,100 per semester.for bsc. ce local students pay usd 800 and foreign students, usd 1,000 per semester")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['installments','do you allow installments','do you allow installment','installment','pay','which currency do you use usd or ugx']:
                #print("Payments are made with the accountant on ground floor, and he will give you a leaflet with installment payments. Both dollar payments and Uganda shillings are accepted")
                engine.say("Payments are made with the accountant on ground floor, and he will give you a leaflet with installment payments. Both dollar payments and Uganda shillings are accepted")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['how long is the semester','semester duration','semester']:
                #print("The semester is 4  and half Months")
                engine.say("The semester is 4  and half Months")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['foundation courses','certificate courses','short courses','foundation', 'certificate']:
                #print("IFP is International Foundation Program. It was formerly IFP but it is now called HEC which is Higher Education Certificate. We no longer offer certificate courses, apart from this one. It is a 1 year course.   Its tuition is USD 400 and USD 200 for functional fees.")
                engine.say("IFP is International Foundation Program. It was formerly IFP but it is now called HEC which is Higher Education Certificate. We no longer offer certificate courses, apart from this one. It is a 1 year course.   Its tuition is USD 400 and USD 200 for functional fees.")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
                            
                       
            elif question in ['full','what is isbat in full','isbat','isbat mean','meaning of isbat','meaning of isbat']:
                #print("ISBAT in full is International Science, Business  and Technology university. It has been in Uganda since 2005 , operating in the heart of Kampala, was founded by a renowned philanthropist Mr. Varghese Mundamattam.Established initially as  a tertiary institution, moved on to the level of degree-awarding institution and finally transformed in Jan 2016 into a fully-fledged university with own state of the art metropolitan campus in Kampala")
                engine.say("ISBAT in full is International Science, Business  and Technology university. It has been in Uganda since 2005 , operating in the heart of Kampala, was founded by a renowned philanthropist Mr. Varghese Mundamattam.Established initially as  a tertiary institution, moved on to the level of degree-awarding institution and finally transformed in Jan 2016 into a fully-fledged university with own state of the art metropolitan campus in Kampala")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
           
            elif question in ['what is the isbat mission','mission','vision']:
                #print("The ISBAT vision is To be the most sought after destination for quality Higher Education and STEM focus within the East African Region")
                engine.say("The ISBAT vision is To be the most sought after destination for quality Higher Education and STEM focus within the East African Region")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['when do the admissions start','admission','admissions']:
                #print("we take in two batches one is during the fall and during spring")
                engine.say("we take in two batches one is during the fall in september and during spring in febuary")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what is the isbat vision','vision']:
                #print("The mission is to To provide an enabling training and research environment for societal transformation")
                engine.say("The mission is to To provide an enabling training and research environment for societal transformation")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you have any international associations','international']:
                #print("Engineering programs-Credit transfer to Manipal University Dubai Campus International Membership (AACSB, IACBE, UCAM, APTECH COMPUTER EDUCATION, The Association of common wealth universities leading to global accreditation")
                engine.say("Engineering programs-Credit transfer to Manipal University Dubai Campus International Membership (AACSB, IACBE, UCAM, APTECH COMPUTER EDUCATION, The Association of common wealth universities leading to global accreditation")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what are the department at isbat campus','deparmtment','departments']:
                #print("There are three departments like in Engineering, Management and Commerce , Information and Communication Technology, Cyber vault")
                engine.say("There are three departments like in Engineering, Management and Commerce , Information and Communication Technology, Cyber vault")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what are the engineering courses do you offer','offer']:
                #print("We offer only two Engineering courses, Bachelors in Electronics And Communication engineering and Bachelors in Computer Science Engineering")
                engine.say("We offer only two Engineering courses, Bachelors in Electronics And Communication engineering and Bachelors in Computer Science Engineering")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what is be and ec','be']:
                #print("BE.EC deals with electronic circuits and how they work and Communication is basically Telecommunication. BE CE basically deals with computer learning, both hardware and software alongside computer programming")
                engine.say("BE.EC deals with electronic circuits and how they work and Communication is basically Telecommunication. BE CE basically deals with computer learning, both hardware and software alongside computer programming")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['is there day and evening batch','evening','batch']:
                #print("yes we do offer day and evening batch. The day batch timings are 9.30 am to 4pm. And the evening batch timings are 5pm to 8.30 pm")
                engine.say("yes we do offer day and evening batch. The day batch timings are 9.30 am to 4pm. And the evening batch timings are 5pm to 8.30 pm")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you also offer weekend programs for the courses','weekend']:
                #print("the weekend programs are for only the students pursuing a masters")
                engine.say("the weekend programs are for only the students pursuing a masters")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['how long is the semester','long',]:
                #print("a semester can be 4-5months long ")
                engine.say("a semester can be 4-5months long ")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['how long the duration of the holidays','duration','holidays','holiday']:
                #print("the holidays are 4 weeks")
                engine.say("the holidays are four weeks")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you have cocurricular activities','co-curricular','cocurricular']:
                #print("yes we do have cocurricular activities like sports day, cultural day, debates, and music and dance competition")
                engine.say("yes we do have cocurricular activities like sports day, cultural day, debates, and music and dance competition")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what is the minimum attendance required to sit for exams','minimum']:
                #print("you are required to attend 80 percentage of the lectures and must inform the staff members if you can’t attend any lectures")
                engine.say("you are required to attend 80 percentage of the lectures and must inform the staff members if you can’t attend any lectures")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['how many papers supposed to sit for in every semester','paper','papers']:
                #print("it depends on how many course units you are given  At most you are supposed to do like 5 exams and 2 practicals")
                engine.say("it depends on how many course units you are given  At most you are supposed to do like 5 exams and 2 practicals")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            
            elif question in ['what are the minimum requirements to join in any course','join']:
                #print("the minimum requirements you need to have is 2 principal pass in your a-level certificate or at least have an equivalent qualification from a recognized education institution. ")
                engine.say("the minimum requirements you need to have is 2 principal pass in your a-level certificate or at least have an equivalent qualification from a recognized education institution. ")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['how is applied it different from computer engineering','applied']:
                #print("computer engineering focuses on hardware development, computer science focuses on software development, and IT focuses on running production systems that somebody else has built. I hope that has helped you")
                engine.say("computer engineering focuses on hardware development, computer science focuses on software development, and IT focuses on running production systems that somebody else has built. I hope that has helped you")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what are the computer programming languages will i learn','learn']:
                #print("you will learn programming languages like  C,C++, Java, HTML, python, JavaScrpit ASP.NET,Python")
                engine.say("you will learn programming languages like  C,C++, Java, HTML, python, JavaScrpit ASP.NET,Python")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what course is good for making animations and photography','photography']:
                #print("a Bachelor of Science in Multimedia and Animation")
                engine.say("a Bachelor of Science in Multimedia and Animation")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what are the job  opportunities with mma','mma']:
                #print("you can later become a 3D animator, 3D modeler, Renderer")
                engine.say("you can later become a 3D animator, 3D modeler, Renderer")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you have library','do you have a library','library']:
                #print("Yes we have sophisticated library in our campus")
                engine.say("Yes we have sophisticated library in our campus")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you have lab facility for every course','lab']:
                print("Yes we have sophisticated and modern equipped  labs for all the courses.")
                engine.say("Yes we have sophisticated and modern equipped  labs for all the courses.")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what are the diploma courses','diploma']:
                print("Diploma in business adminstration, diploma in hardware and networking and diploma in information technology")
                engine.say("Diploma in business adminstration, diploma in hardware and networking and diploma in information technology")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you have a course in cyber security','security']:
                print("yes we do. It is a 3 year course and it has a good future in Uganda right now since most of the businesses are opting to go online and it needs to deal with cyber crimes and prevent such.")
                engine.say("yes we do. It is a 3 year course and it has a good future in Uganda right now since most of the businesses are opting to go online and it needs to deal with cyber crimes and prevent such.")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['explain about cyber vault','cyber']:
                print("The CyberVault Advantage CyberVault provides corporate training in the emerging technologies that are essential for digital transformation. Our blended learning approach drives learner engagement and the industry’s highest completion rates")
                engine.say("The CyberVault Advantage CyberVault provides corporate training in the emerging technologies that are essential for digital transformation. Our blended learning approach drives learner engagement and the industry’s highest completion rates")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what are the job opportunities bsc ncs','ncs']:
                print("you can become a security analyst, security architect, security engineer, security engineer, cryptanalyst, cryptographer, security software developer. And lots more it has many career paths.")
                engine.say("you can become a security analyst, security architect, security engineer, security engineer, cryptanalyst, cryptographer, security software developer. And lots more it has many career paths.")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['when does the graduation usually take place','graduation']:
                print("it usually happens during the month of December")
                engine.say("it usually happens during the month of December")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what are the requirements of graduating','graduating']:
                print("you are supposed to pass all your exams with a minimum of 2.5 GPA and clear all your fees and have no remaining papers and projects")
                engine.say("you are supposed to pass all your exams with a minimum of 2.5 GPA and clear all your fees and have no remaining papers and projects")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you have internship placement in companies and industries','placement']:
                print("yes we do help you to send reccomendations and also if possible help to send you to a company for internship.")
                engine.say("yes we do help you to send reccomendations and also if possible help to send you to a company for internship.")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
                
            elif question in ['internships','internship']:
                print("it starts during your 5th and 6th semester period of your course.")
                engine.say("it starts during your 5th and 6th semester period of your course.")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you have e-library','elibrary','library','e-library']:
                print("e-Library is a convenient and affordable online resource giving you easy access to a wide range of quality books.")
                engine.say("e-Library is a convenient and affordable online resource giving you easy access to a wide range of quality books.")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['what is meant by blended learning platform','blended']:
                print("ISBAT university recently launched blended learning platform and it combines classroom learning with online learning, in which students can, in part, control the time, pace, and place of their learning. Blended learning platform and esports is launched by  honorable information technology minister uganda recently.")
                engine.say("ISBAT university recently launched blended learning platform and it combines classroom learning with online learning, in which students can, in part, control the time, pace, and place of their learning. Blended learning platform and esports is launched by  honorable information technology minister uganda recently.")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['tell me about esports','tell me about esport','esport','esports']:
                print("You will learn within a practical technical environment everything required to host small and large scale events. Developing your skills for single player and multi-player team events you will create business plans to build teams, create online communities and promote your events through digital marketing. You will also get the opportunity to explore the culture of esports, its audience and fan base as well as a variety of the most popular current game genres.")
                engine.say("You will learn within a practical technical environment everything required to host small and large scale events. Developing your skills for single player and multi-player team events you will create business plans to build teams, create online communities and promote your events through digital marketing. You will also get the opportunity to explore the culture of esports, its audience and fan base as well as a variety of the most popular current game genres.")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['any upcoming new courses','upcoming']:
                print("Yes ,isbat university going to launch BSC artificial intelligence 3 year course. This Artificial Intelligence course provides training in the skills required for a career in AI and IOT technologies. You will master TensorFlow, Machine Learning, and other AI concepts, plus the programming languages needed to design intelligent agents, deep learning algorithms & advanced artificial neural networks that use predictive analytics to solve real-time decision-making problems.The application you are using now is an application of Artificial intelligence")
                engine.say("Yes ,isbat university going to launch BSC artificial intelligence 3 year course. This Artificial Intelligence course provides training in the skills required for a career in AI and IOT technologies. You will master TensorFlow, Machine Learning, and other AI concepts, plus the programming languages needed to design intelligent agents, deep learning algorithms & advanced artificial neural networks that use predictive analytics to solve real-time decision-making problems.The application you are using now is an application of Artificial intelligence")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
            elif question in ['do you provide any transport','transport']:
                print("Yes we provide transport facilities to students")
                engine.say("Yes we provide transport facilities to students")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
           
            elif question in ['artificial intellgence','ai']:
                print("you are welcome")
                engine.say("Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions. The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving")
                engine.setProperty('rate',120)
                engine.setProperty('volume', 0.9)
                engine.runAndWait()
           
            elif question in ['thank you for this information','thank','bye`']:
                print("you are welcome")
                engine.say("you are welcome see you soon at isbat university")
                engine.setProperty('rate',120)
                engine.setProperty('volume', 0.9)
                engine.runAndWait()
                break;
            elif question in ['Who is john bosco','john']:
                print("you are welcome")
                engine.say("He is a net work engineer at isbat university")
                engine.setProperty('rate',120)
                engine.setProperty('volume', 0.9)
                engine.runAndWait()
                break;   
                           
               
            else:
                print("I don't understand what you said")
                engine.say("i beg your pardon")
                engine.setProperty('rate',155)
                engine.setProperty('volume', 2.0)
                engine.runAndWait()
                
                              
                
        except sr.UnknownValueError:
                    #print(". Please speak again")
                    engine.say('Please speak again')
                    engine.setProperty('rate',155)
                    engine.setProperty('volume', 2.0)
                    engine.runAndWait()
                  

