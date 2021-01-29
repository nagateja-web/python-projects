nominee_1 = input("Enter the nominee 1 name : ") #input for the nominee_1
nominee_2 = input("Enter the nominee 2 name : ") #input for the nominee_2

nom_1_votes = 0 #to count the votes of nominee_1
nom_2_votes = 0 #to count the votes of nominee_2

voters_id = [1,2,3,4,5,6,7,8,9,10]  # list to store the voters id

num_of_voter = len(voters_id) # length of votes to count the voters

                
while True:
    if voters_id == []:  # if the voters id is empty or completed , this condition executes
        print("Voting session over")

        if nom_1_votes > nom_2_votes:  # comparision between nominne_1 and nominee_2 votes
            percent = (nom_1_votes/num+_of_voter)*100
            print(nominee_1, "has won", "with",percent,"% votes")


        elif nom_2_votes > nom_1_votes:
            percent = (nom_2_votes/num_of_voter)*100
            print(nominee_2, "has won", "with",percent,"% votes")
    else:
        voter = int(input("Enter your voter id no :"))  # input to get the voter id

        
        if voter in voters_id:  # condition to check wheather the voter id is present in voters list or not
            print("you are a voter")
            
            voters_id.remove(voter)   # to remove the voters id after the voting
            
            vote = int(input("enter your vote 1 or 2 : "))  # input to get the voter fo nominee_1 or nominee_2
            if vote == 1:
                nom_1_votes += 1
                print("Thank you for casting your vote")

            
            elif vote == 2:
                nom_2_votes += 1
                print("Thank you for casting your vote")

            else:
                print("Your are not a voter or you have already voted")

        
