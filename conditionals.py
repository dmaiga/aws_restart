userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == 'yes' :
    print('we can help you ship that package! ')
else:
    print("Please come back when you need to ship a package. Thank you")
    
userReply = input (" Would you like to buy stamps,buy an envelope,or make a copy, (entre Stamps,Envelope,Copy)")
if userReply == 'Stamps':
    print("we have many stamps designs to choose from")
elif userReply == 'Envelope':
    print("We have many envelope size to choose from")
elif userReply == 'Copy':
    copies=input ("how many please ")
    print("here are {} copies".format(copies))
else:
    print("after")
