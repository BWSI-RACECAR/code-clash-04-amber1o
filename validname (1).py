"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #4 - Validate Name (validname.py)


Author: Wonjun Lee

Difficulty Level: 3/10

Prompt: Bill is trying to come up with a name for his RACECAR, but he wants to name his 
car so that there are no duplicate characters in the name. Please write a function that 
returns whether a given string input is a valid name or not. 

Constraints: Inputs will consist of only alphanumeric characters. Lowercase and uppercase
characters are considered different. The length of string will be in the range [0, 100] inclusive.

Test Cases:
Input: “AaBbCc1234”     Output: True 
Input: “Aa123a”         Output: False
Input: “qwer12341”      Output: False
"""

class Solution:
    def validateName(self,input):
        output= []
        for c in input:
            if input.isalnum:
                if c not in output:
                    return False 
            else: 
                return False
            
        # return: bool
            
        # TODO: Write code below to return a bool with the solution to the prompt
        pass


def my_grocery_list(self,str1,str2):
        final_list = []
        list1 = str1.split(' ')
        list1[len(list1)-1] = list1[len(list1) - 1].strip()
        list2 = str2.split(' ')
        list2[len(list2)-1] = list2[len(list2)- 1].strip()
        for item in list1:
            if item not in final_list and item != '':
                final_list.append(item)
        for item in list2:
            if item not in final_list and item != '':
                final_list.append(item)
        return final_list
def main():
    string1 = input()

    tc1 = Solution()
    ans = tc1.validateName(string1)
    print(ans)

if __name__ == "__main__":
    main()