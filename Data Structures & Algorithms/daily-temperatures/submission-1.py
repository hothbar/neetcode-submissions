class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        st = []

        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                stTem, stInd = st.pop()
                output[stInd] = i - stInd
            st.append((t, i))
        return output
            
