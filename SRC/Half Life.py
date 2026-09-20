

name=input('hello my frind please enter your name :')
print('welcome',name+'!please fill the blanks below about genome content:')
year=input('please enter the year of generation:')
month=input('please enter the month of generation:')
day=input('please enter the day of generation:')
print('enter date of today:')
year1=input('year number:')
month1=input('month number:')
day1=input('day number:')
Content_amount=input( 'Please Enter genome amount in grams:')
half_life=input( 'Please Enter half life of genome content in days:')

A=(int(year1)-int(year))-1
B1=int(A)//4
B2=((int(A)+1)//4)
B3=((int(A)+2)//4)
B4=((int(A)+3)//4)
Distance1=((365*int(A))+int(B1))
Distance2=((365*int(A))+int(B2))
Distance3=((365*int(A))+int(B3))
Distance4=((365*int(A))+int(B4))
if(int(year)%4==0)and(int(month)==1):
 z=0
if(int(year)%4==0)and(int(month)==2):
 z=31
if(int(year)%4==0)and(int(month)==3):
 z=29+31
if(int(year)%4==0)and(int(month)==4):
 z=31+29+31
if(int(year)%4==0)and(int(month)==5):
 z=30+31+29+31
if(int(year)%4==0)and(int(month)==6):
 z=31+30+31+29+31
if(int(year)%4==0)and(int(month)==7):
 z=30+31+30+31+29+31
if(int(year)%4==0)and(int(month)==8):
 z=31+30+31+30+31+29+31
if(int(year)%4==0)and(int(month)==9):
 z=31+31+30+31+30+31+29+31
if(int(year)%4==0)and(int(month)==10):
 z=30+31+31+30+31+30+31+29+31
if(int(year)%4==0)and(int(month)==11):
 z=31+30+31+31+30+31+30+31+29+31
if(int(year)%4==0)and(int(month)==12):
 z=30+31+30+31+31+30+31+30+31+29+31

if(int(year)%4!=0)and(int(month)==1):
 z=0
if(int(year)%4!=0)and(int(month)==2):
 z=31
if(int(year)%4!=0)and(int(month)==3):
 z=28+31
if(int(year)%4!=0)and(int(month)==4):
 z=31+28+31
if(int(year)%4!=0)and(int(month)==5):
 z=30+31+28+31
if(int(year)%4!=0)and(int(month)==6):
 z=31+30+31+28+31
if(int(year)%4!=0)and(int(month)==7):
 z=30+31+30+31+28+31
if(int(year)%4!=0)and(int(month)==8):
 z=31+30+31+30+31+28+31
if(int(year)%4!=0)and(int(month)==9):
 z=31+31+30+31+30+31+28+31
if(int(year)%4!=0)and(int(month)==10):
 z=30+31+31+30+31+30+31+28+31
if(int(year)%4!=0)and(int(month)==11):
 z=31+30+31+31+30+31+30+31+28+31
if(int(year)%4!=0)and(int(month)==12):
 z=30+31+30+31+31+30+31+30+31+28+31



if(int(year1)%4==0)and(int(month1)==1):
 y=0
if(int(year1)%4==0)and(int(month1)==2):
 y=31
if(int(year1)%4==0)and(int(month1)==3):
 y=29+31
if(int(year1)%4==0)and(int(month1)==4):
 y=31+29+31
if(int(year1)%4==0)and(int(month1)==5):
 y=30+31+29+31
if(int(year1)%4==0)and(int(month1)==6):
 y=31+30+31+29+31
if(int(year1)%4==0)and(int(month1)==7):
 y=30+31+30+31+29+31
if(int(year1)%4==0)and(int(month1)==8):
 y=31+30+31+30+31+29+31
if(int(year1)%4==0)and(int(month1)==9):
 y=31+31+30+31+30+31+29+31
if(int(year1)%4==0)and(int(month1)==10):
 y=30+31+31+30+31+30+31+29+31
if(int(year1)%4==0)and(int(month1)==11):
 y=31+30+31+31+30+31+30+31+29+31
if(int(year1)%4==0)and(int(month1)==12):
 y=30+31+30+31+31+30+31+30+31+29+31
 
if(int(year1)%4!=0)and(int(month1)==1):
 y=0
if(int(year1)%4!=0)and(int(month1)==2):
 y=31
if(int(year1)%4!=0)and(int(month1)==3):
 y=28+31
if(int(year1)%4!=0)and(int(month1)==4):
 y=31+28+31
if(int(year1)%4!=0)and(int(month1)==5):
 y=30+31+28+31
if(int(year1)%4!=0)and(int(month1)==6):
 y=31+30+31+28+31
if(int(year1)%4!=0)and(int(month1)==7):
 y=30+31+30+31+28+31
if(int(year1)%4!=0)and(int(month1)==8):
 y=31+30+31+30+31+28+31
if(int(year1)%4!=0)and(int(month1)==9):
 y=31+31+30+31+30+31+28+31
if(int(year1)%4!=0)and(int(month1)==10):
 y=30+31+31+30+31+30+31+28+31
if(int(year1)%4!=0)and(int(month1)==11):
 y=31+30+31+31+30+31+30+31+28+31
if(int(year1)%4!=0)and(int(month1)==12):
 y=30+31+30+31+31+30+31+30+31+28+31


x=int(z)+int(day)
left_of_year_1=365-int(x)
left_of_year_2=366-int(x)

m=int(y)+int(day1)
passed_of_year1=int(y)


if(int(year)%4==0):
    d=((left_of_year_2)+(passed_of_year1)+(Distance1))
    print('The age of genome content is',(int(left_of_year_2)+int(passed_of_year1)+int(Distance1)),'DAYS OLD!',(24*(int(left_of_year_2)+int(passed_of_year1)+int(Distance1))),'HOURS OLD!',(60*24*(int(left_of_year_2)+int(passed_of_year1)+int(Distance1))),'MINUTES OLD!')
if(int(year)%4!=0)and((int(year)%4)==1):
    d=((left_of_year_1)+(passed_of_year1)+(Distance2))
    print('The age of genome content is',(int(left_of_year_1)+int(passed_of_year1)+int(Distance2)),'DAYS OLD!',(24*(int(left_of_year_1)+int(passed_of_year1)+int(Distance2))),'HOURS OLD!',(60*24*(int(left_of_year_1)+int(passed_of_year1)+int(Distance2))),'MINUTES OLD!')
if(int(year)%4!=0)and((int(year)%4)==2):
    d=((left_of_year_1)+(passed_of_year1)+(Distance3))
    print('The age of genome content is',(int(left_of_year_1)+int(passed_of_year1)+int(Distance3)),'DAYS OLD!',(24*(int(left_of_year_1)+int(passed_of_year1)+int(Distance3))),'HOURS OLD!',(60*24*(int(left_of_year_1)+int(passed_of_year1)+int(Distance3))),'MINUTES OLD!')
if(int(year)%4!=0)and((int(year)%4)==3):
    d=((left_of_year_1)+(passed_of_year1)+(Distance4))
    print('The age of genome content is',(int(left_of_year_1)+int(passed_of_year1)+int(Distance4)),'DAYS OLD!',(24*(int(left_of_year_1)+int(passed_of_year1)+int(Distance4))),'HOURS OLD!',(60*24*(int(left_of_year_1)+int(passed_of_year1)+int(Distance4))),'MINUTES OLD!')


remaind= (int (Content_amount)/int (2**(int (d)/int (half_life))))
print('There is', remaind, 'gram remaining.')
