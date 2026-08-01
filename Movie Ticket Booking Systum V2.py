from argparse import Action

 
print("🎥===== MOVIE TICKET SYSTEM =====")
#--------AGE CHECK--------
age=int(input("Enter Your Age: "))
if age>=18:
    print("✅You Can Book Ticket")
    #-------MOVIE SELECTION--------
    print("\nSelect Movie:")
    print("1. Action")
    print("2. Comedy")
    print("3. Horror")
    movie_type=input("Enter Movie Type:")
   #------Display the lists based on selection------
    if movie_type=="1": 
         print("1.kill")
         print("2.RRR")
         print("3.pushpa")
    elif movie_type=="2":
         print("1.3 idiots")
         print("2.Hera Peri")
         print("3.golmaal")
    elif movie_type=="3":
         print("1. The Conjuring")
         print("2.Stree")
         print("3.Razz")   
      #----Ask for the movie nmme -----
    movie_name=input("\nEnter Avaiable movie name:") 
    #-------TICKET BOOKING--------
    print("\nselect seat type:")
    print("1. silver")
    print("2. gold")
    print("3. platinum")
    print("IF YOU WILL BOOK THE PLATINUM SEAT , YOU WILL GET THE FREE POPCORN")
    seat=input("Enter Seat Types: ").lower()
    if seat=="silver":
         amount=200
    elif seat=="gold":
         amount=300
    elif seat=="platinum":
         amount=500
    else:
         amount=0
         print("❌Invalid Seat") 
    print("Ticket price: ",amount)
     #--------Free Popcorn--------
    if amount>=500:
       print("🍿You are eligible for free popcorn")
    else:
         print("❌You are not eligible for free popcorn🍿")
     #--------PAYMENT--------
    Payment=input("\npayment done? (yes/no): ").lower().strip()
    if Payment=="yes":
             print("✅Ticket Booked Successfully!")
    else:
         payment="no"
         print("❌Booking failed!,Payment required.")
         
     #--------CUSTOMER TYPE-------
    Visits = int(input("\nEnter Number of Visits: "))
    if Visits>5:
         print("🥰 You Are VIP Customer")
    else:
        print("You Are Regular Customer")
     
     #--------Thank You Message--------
    print("🥰Thank you for booking with us!")
    print("😘Enjoy your movie!")
else:
     print("❌you are not eligible to book ticket")