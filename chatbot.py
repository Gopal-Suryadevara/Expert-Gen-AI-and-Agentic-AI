from nltk.chat.util import Chat, reflections

pairs = [
    [
         r"(.*)my name is (.*)",
         ["Hello %2, How are you today?",]
         
     ],
    [
         r"(.*)help(.*)",
         ["I can help you",]        
     ],
    [
         r"(.*)your name?",
         ["My name is chitti",]
     ],
    [
         r"how are you(.*)?",
         ["I'm doing very well", "I'm great!",]
     ],
    [
         r"(hi|hey|hello)(.*)",
         ["Hello", "Hey there",]
     ],
    [
         r"what (.*) want ?",
         ["Make me an offer I can't refuse",]     
     ],
    [
         r"(.*)created(.*)",
         ["Gopal created me",]     
     ],
    [
         r"(.*)(location|city) ?",
         ["Hyderabad, India",]     
     ],
    [
         r"(.*) raining in (.*)",
         ["No rain in the past 4 days here in %2",]   
     ],
    [
         r"how (.*) health (.*)",
         ["Health is very important, but I'm a chatbot",]     
     ],
    [
         r"(.*)(sports|game|sport)(.*)",
         ["I'm a very big fan of cricket",]     
     ],
    [
         r"who (.*) (cricketer|batsman|bowler)?",
         ["Dhoni",]   
     ], 
    [
         r"quit",
         ["Bye, It was nice talking to you. see you soon :)",]
    ], 
    [
         r"(.*)",
         ["Our customer service will reach you",]   
     ], 
    ]

print ("Hi, I'm the clever programmer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave")

chat = Chat(pairs,reflections)

chat.converse()




