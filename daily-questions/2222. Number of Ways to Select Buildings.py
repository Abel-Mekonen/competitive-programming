class Solution:
    def numberOfWays(self, buildings: str) -> int:
       
        length = len(buildings)
        ones_count_right = [0] * (length + 1)
        zeros_count_right = [0] * (length + 1)

        for i in range(length - 1, -1 , -1):
            if buildings[i] == "0":
                zeros_count_right[i] = zeros_count_right[i + 1] + 1
                ones_count_right[i] = ones_count_right[i + 1]
            else :
                ones_count_right[i] = ones_count_right[i + 1] + 1
                zeros_count_right[i] = zeros_count_right[i + 1]

        ones_count_left = 0 
        zeros_count_left = 0 
        answer = 0
        for i in range(length):
            if buildings[i] == "0":
                answer += (ones_count_left * ones_count_right[i])
                zeros_count_left += 1

            if buildings[i] == "1":
                answer += (zeros_count_left * zeros_count_right[i])
                ones_count_left += 1

        return answer
