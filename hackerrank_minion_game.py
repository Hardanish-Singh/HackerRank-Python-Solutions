"""
            HACKERRANK THE MINION GAME
    URL: https://www.hackerrank.com/challenges/the-minion-game/problem

    TASK: Kevin and Stuart want to play the 'The Minion Game'.

    RULES:
            1) Both players are given the same string, S
            2) Both players have to make substrings using the letters of the string S.
            3) Stuart has to make words starting with consonants.
            4) Kevin has to make words starting with vowels.
            5) The game ends when both players have made all possible substrings.
    
    SCORING:
            A player gets +1 point for each occurrence of the substring in the string S
    
    FOR EXAMPLE:
                    String S = BANANA
                    
                    Kevin's vowel beginning word = ANA
                    Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

                    For better understanding, see below:


                    STUART                              KEVIN

                    WORDS       SCORE                   WORDS       SCORE
                    B           1                       A           3
                    N           2                       AN          2
                    BA          1                       ANA         2
                    NA          2                       ANAN        1
                    BAN         1                       ANANA       1
                    NAN         1
                    BANA        1
                    NANA        1
                    BANAN       1
                    BANANA      1
    
                    TOTAL       12                      TOTAL       9

    STUART WON
"""
# def find_unique_characters_in_a_string(string):
#     unique_character_list = []
#     for i in range(len(string)):
#         flag = False
#         for j in range(0, i):
#             if(string[i] == string[j]):
#                 flag = True
#                 break
#         if(flag == True):
#             continue
#         unique_character_list.append(string[i])
#     return unique_character_list


def minion_game(string):
    unique_characters_list = list(set(string))
    # unique_characters_list = find_unique_characters_in_a_string(string)
    stuart_count, kevin_count = 0, 0
    for item in unique_characters_list:
        if(item.upper() in ['A', 'E', 'I', 'O', 'U']):
            for rec in range(len(string)):
                if(item == string[rec]):
                    kevin_count = kevin_count + (len(string) - rec)
        else:
            for rec in range(len(string)):
                if(item == string[rec]):
                    stuart_count = stuart_count + (len(string) - rec)

    if(stuart_count > kevin_count):
        print('Stuart ', stuart_count)
    elif(kevin_count > stuart_count):
        print('Kevin ', kevin_count)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
