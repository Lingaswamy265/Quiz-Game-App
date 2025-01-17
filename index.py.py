#PYTHON QUIZ GAME PROJECT ON GENERAL KNOWLEDGE
#QNS,OPTIONS,ANSWER,CORRECT,INCORRECT,GUESS,SCORE
questions = ("1.Which animal is known as the ship of the dessert?: ",
           "2.How many days are there in a week?: ",
           "3.How many hours are there in a day?: ",
           "4.How many letters are there in the English?: ",
           "5.Rainbow consist of how many colours?: ",
           "6.How many days are there in a year?: ",
           "7.How many minutes are there in an hour?: ",
           "8.How many seconds are there in a one minute?: ",
           "9.How many seconds make one hour?: ",
           "10.How many consonants are there in the English alphabet?: ",
           "11.How many vowels are there in the English alphabet and name them?: ",
           "12.Which animal is known as the king of the jungle?: ",
           "13.Name of the National bird of india?: ",
           "14.Name of the National animal of India?: ",
           "15.What is the National Anthem?: ",
           "16.Name of the National flower of india?: ",
           "17.Name of the National Fruit?: ",
           "18.What is the National song of India?: ",
           "19.Who designed by National flag of india?: ",
           "20.Name of the National Game of india?: ",
           "21.Name of the National River of india?: ",
           "22.What is the Capital of India?: ",
           "23.Name of the Biggest continent in the world?: ",
           "24.How many continents are there in the world?: ",
           "25.Name the primary colours?: ",
           "26.Which is the smallest Month of the year?: ",
           "27.Which colour symbolises peace?: ",
           "28.sun rises in the.....?: ",
           "29.How many sides are there in a Traingle?: ",
           "30.Who was the first Prime Minister of India?: ",
           "31.Who is the first woman Prime Minister of India?: ",
           "32.Who is the first citizen of india?: ",
           "33.How many states are there in india?: ",
           "34.How many years are there in one Millenium?: ",
           "35.Name is called cricket of Master...?: ",
           "36.Name the densest jungle in the world?: ",
           "37.What type of gas is absorbed by plants?: ",
           "38.How many days a February month have in the leap year?: ",
           "39.Name of the smallest continent in the world?: ",
           "40.Which is the principal source of energy for the Earth?: ",
           "41.Clockwise is it from left or right?: ",
           "42.Anti-Clockwise is it from left or right?: ",
           "43.Which festival is known as the festival of light?: ",
           "44.which is the tallest mounatain in the world?: ",
           "45.Which continent is known as the 'Dark' Continent?: ",
           "46.Name the Planet known as the Red planet?: ",
           "47.Who invented Watch?: ",
           "48.Name of the Largest 'Democracy' of the world?: ",
           "49.Name the hardest substance available on Earth?: ",
           "50.Who is the Father of Indian Nation?: ")

options = (("A.Camel","B.cat","C.Dog","D.Monkey"),
("A.6 days","B.7 days","C.8 days","D.9 days"),
("A.21 hours","B.22 hours","C.23 hours ","D.24 hours"),
("A.25 letters","B.26 letters","C.27 letters","D.28 letters"),
("A.5 colours","B.6 colours","C. 7 clours","D.8 colours"),
("A.364 days","B.365 days","C.366 days ","D.367 days"),
("A.50 min","B.60 min","C.70 min","D.80 min"),
("A.40 sec","B.50 sec","C.60 sec ","D.30 sec"),
("A.3500 seconds","B.3600 seconds ","C.3700 seconds","D. 3800 seconds"),
("A.20","B.21","C.22","D.23"),
("A.5","B.6","C.7 ","D.8 "),
("A.Cat","B.Tiger","C.Lion","D.chithah"),
("A.Peacacko","B.Parrot","C.crows","D.chiken"),
("A.Cat","B.Tiger","C.Lion","D.chithah"),
("A.Jana gana mana","B.Vande matharam"," sarah jahatsa achha","Desam hey"),
("A.Rose","B.sun flower","C. lotus flower","D.jasmine"),
("A.apple","B.banana","C.Mango","D.orange"),
("A.Jana gana mana","B.Vande matharam"," sarah jahatsa achha","Desam hey"),
("A.Potti sreeramulu","B.Pingali venkayya","C.abdul kalaam","D.pv narasima"),
("A.kabaddi","B.football","C.cricket","D.Hockey"),
("A.yamuna","B.ganga","C.thunga","D.sarayu"),
("A.hyderbad","B.chennai","C.New delhi","D.vizag"),
("A.Austrilia","B.france","C.Asia","D.italy"),
("A.5","B.6","C.7","D.8"),
("A.red,yellow,blue","B.blue,black,white","C.red,green,pink","D.red,green,blue"),
("A.January","B.February","C.March","D.July"),
("A.white","B.Blue","C.Green","D.Red"),
("A.East","B.West","C.South","D.North"),
("A.1","B.2","C.3","D.4"),
("A.Jaharlal Nehru","B.Narendra Modi","C.Manmohan sing ","D.Rajeev gandi"),
("A.Sonia gandhi","B.indiraa gandhi","C.Mother therasaa","D.Priyanka"),
("A.chief minister","B.Home minister","C.President of india","D.Prime minister"),
("A.26 ","B.27 ","C.28","D.29"),
("A.10","B.100","C.1000","D.10000"),
("A.Ganguly","B.Rickey ponting","C.chris gayle","D.Sachin Tendulkar"),
("A.Nalla Malla forest","B.Amozon Rain forest","C.green forest","D.Tirupathi forest"),
("A.co2","B.H2o","C.hcl","D.o2"),
("A.28 days","B.29 days","C.30 days","D.31 days"),
("A.Austelia","B.India","C.England","D.china"),
("A.kinetic energy","B.Potential energy ","C.wind energy ","D.sun energy"),
("A.Right","B.Left ","C.Upward","D.Downward"),
("A.Left","B.Right","C.Top","D.Bottum"),
("A.Sankranthi","B.Vinayaka chavithi","C.Dewaali","D.Ramjzan"),
("A.Mount","B.Everest","C. Mount Everest","D.Himalayas"),
("A.India","B.Africa","C.china","D.Usa"),
("A.Mars","B.earth","C.moon","D.sun"),
("A.Peterson","B.mitchel","C.quartz","D.Peter Henlein"),
("A.sri lanka","B.Nepal","C.china","D.India"),
("A.gold","B.silver","C.Dimond","D.bronze"),
("A.Nelson Mandel","B.Mahathma Gandhi","C.Bhagath sing","D.subhas chand bhose"))

answers = ("A","B","D","B","C",
           "B","B","C","B","B",
           "A","C","A","B","A",
           "C","C","B","B","D",
           "B","C","C","C","A",
           "B","A","A","C","A",
           "B","C","C","C","D",
           "B","A","B","A","D",
           "A","A","C","C","B",
           "A","D","D","C","B") 
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}")