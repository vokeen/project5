import os
from os import system
system("clear")
import random

first=['Vokee' , 'Jamal' ,'Steven' , 'Ryan' , 'Bryan' , 'Tim' , 'Gio' ,'Timmy' , 'Tommy' , 'Tristan' , 'Brandon' ,'Braiden' , 'Cody' , 'Christan' , 'Austin' , 'Anthony' , 'Pedro' , 'Daniel' , 'Hamadi' , 'Joel']
last=['Brown' , 'Johnson' , 'Gonzoles' , 'John' , 'Troy' , 'Bolt' , 'Stevens' , 'Kerr' , 'Jefferson' ,'Lincoln' ,'Obama' ,'Trump','Richard' , 'White' , 'James' , 'Brooks' ,'Lamar' , 'Capin' , 'Porter' ,'Money']
housenum=['001' , '002' , '003' , '004' , '005' ,'006' ,'007' ,'008' ,'009' , '010' , '011' ,'012' ,'013' , '014' ,'015' , '016' ,'017' ,'018' ,'019' ,'020']
street=['Bronco' , 'Horseshoe' , 'Saddle' ,'Water Can' ,'Poncho' , 'Concho' , 'Lake Side' , 'Humming Bird' , 'Cardinal' ,'Blue Jay' , 'Dove' ,'Lily' ,'Lotus' , 'Rose' , 'Tulip' ,'Daisy' ,'Dandy Lion' , 'Daffadill' ,'Sun Flower']
city=['Austin' , 'Dallas' , 'Houston' , 'Des Moine' , 'Kansas City' ,'Miami','Seattle' , 'Toronto' , 'Pensilvania' , 'Los Angeles' , 'San Jose' , 'Fresno' , 'Pismo' , 'Santa Monica' , 'Detroit' , 'San Antonio' , 'San Diego' ,'Phoenix' , 'Frisco']
state=['Texas' , 'Iowa' , 'New Jersey' ,'New York' , 'California' ,'Tennese' , 'Florida', 'Lousiana' ,'Montana' ,'Ohio' , 'North Carolina' ,'South Carolina' , 'Washington' , 'Vermont' , 'New Hampshire' ,'Missisipi' , 'Arizona' , 'New Mexico' , 'Utah' , 'Kansas']
phone=['111-111-1111' , '222-222-2222' , '333-333-3333' , '444-444-4444' , '555-555-5555' ,'666-666-6666' , '777-777-7777' ,'888-888-8888' ,'999-999-9999' , '123-456-7890' ,'940-568-5432' , '543-554-2344' ,'567-631-2456' , '988-327-8635' ,'243-353-8416' , '123-532-6436' , '644-864-2462' ,'234-322-8626' ,'853-345-8190', '432-245-7531']
zipcode=['65432' , '53532', '79483' , '58384' , '58395' , '38489' , '28384' ,'45858' ,'47858' , '39059' ,'20508' , '29407' , '17485' , '18385' ,'20194' , '01938' ,'28349' , '28348', '10394' , '03756' , '70483' , '80492']
email=['pear@gmail.com' ,' ape@gmail.com','apple@gmail.com' , 'pinapple@gmail.com' , 'grape@gmail.com' , 'grapefruit@gmail.com' , 'orange@gmail.com' , 'watermelon@gmail.com' , 'cantalop@gmail.com' , 'starfruit@gmail.com' ,'bannana@gmail.com' , 'strawberry@gmail.com' ,'blueberry@gmail.com' , 'carrot@gmail.com' , 'tomato@gmail.com' , 'potato@gmail.com' , 'squash@gmail.com'  ,'pumpkin@gmail.com' , 'kiwi@gmail.com' , 'dragonfruit@gmail.com']

start = input(" Hi and welcome to identity fraud, would you like to continue ? (y) yes (n) no ")

r1 = random.choice(first)
r2 = random.choice(last)
r3 = random.choice(housenum)
r4 = random.choice(street)
r5 = random.choice(city)
r6 = random.choice(state)
r7 = random.choice(phone)
r8 = random.choice(zipcode)
r9 = random.choice(email)

if start == 'y':
    print(f'Hello, {r1} {r2} {r3} {r4} {r5} {r6} {r7} {r8} {r9}')
else:
    print("Ok Have a Nice Day...")
