

# ============================================================================================================ #
#                                                                                                              #
# input: dog, god                                                                                              #              
#                                                                                                              #                              
# -----------------------------------------------------------------------------------------------------        #                      
# t_dict  |{d:1} | {d:1, o:1} | {d:1, o:1, g:1} | {d:1, o:1, g:0} | {d:1, o:0, g:0} | {d:0, o:0, g:0} |        #                  
# letter1 |   d  |      o     |        g        |                 |                 |                 |        #                                  
# letter2 |      |            |                 |        g        |        o        |        d        |        #       
# count   |      |            |                 |                 |                 |                 |    |   #                   
#                                                                                                          |   #  
#                                                                                                       <--+   #
#                                                                                                              #                          
# cont' ---------------------------------------------------------                                              #
# t_dict  | {d:0, o:0, g:0} | {d:0, o:0, g:0} | {d:0, o:0, g:0} |                                              #                  
# letter1 |                 |                 |                 |                                              #                                  
# letter2 |                 |                 |                 |     return True                              #                            
# count   |        0        |        0        |        0        |                                              #      
# ============================================================================================================ #                                                            

def is_anagram(string_one, string_two):

    truth_dict = {}

    for letter in string_one:
        if letter in truth_dict:
            truth_dict[letter] += 1
        else:
            truth_dict[letter] = 1
    
    for letter in string_two:
        if letter in truth_dict:
            truth_dict[letter] -= 1
        else:
            return False

    for count in truth_dict.values():
        if count is not 0:
            return False

    return True