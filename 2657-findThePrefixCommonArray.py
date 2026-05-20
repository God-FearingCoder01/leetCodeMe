class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n, i_value, C = len(A), 0, []
        for i in range(n):
            B_at_i = B[:(i+1)]
            for j in range(len(B_at_i)):
                if A[j] in B_at_i: i_value += 1
            C.append(i_value)
            i_value = 0
        return C