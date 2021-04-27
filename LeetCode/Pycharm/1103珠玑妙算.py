class Solution:
    def masterMind(self, solution: str, guess: str):
        result_list = [0,0]
        a_list = []
        b_list = []
        for i,j in enumerate(guess):
            if solution[i] == j:
                result_list[0]+=1
            else:
                a_list.append(solution[i])
                b_list.append(j)

        for i in b_list:
            if i in a_list:
                result_list[1]+=1
                a_list.remove(i)

        return result_list

A=Solution()
