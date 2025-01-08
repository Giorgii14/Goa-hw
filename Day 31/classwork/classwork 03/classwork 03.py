def secret_challenge():
  
    my_list = ['giorgi', 'mariami', 'saba', 'sandro', 'nika']
    
    secret_index = 2  
    
   
    user_choice = int(input("choose 0-4: "))
    
  
    if user_choice == secret_index:
        return "good job!"
    else:
        return "you failed,please try again!"

result = secret_challenge()


print(result)
