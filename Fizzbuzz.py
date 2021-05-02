#Fizzbuzz Program By ShiroKlein 2021


welcome_message = "This program will check if the number is divisable on 5 or 3, Please Enter a number:";
print(welcome_message);


x= input();


my_number= 'Your Number is {}';
print(my_number.format(x));


if (x%5 == 0) and (x%3 ==0):
    ans = '{} is divisable by both 5 and 3';
    print(ans.format(x));
elif (x%5 ==0): 
    ans = '{} is only divisable by 5';
    print(ans.format(x));
elif x%3 ==0:
    ans = '{} is only divisable by 3'
    print(ans.format(x));
else:
    ans = '{} is not either divisable by 3 nor 5'
    print(ans.format(x));

