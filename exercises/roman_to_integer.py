class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0

        exceptions = {
        "CM" : 900,
        "CD" : 400,
        "XC" : 90,
        "XL" : 40,
        "IX" : 9,
        "IV" : 4
        }

        for i in exceptions:
            if i in s:
                output += exceptions[i]
                s = s.replace(i, "", 1)


        values = {
        "M" : 1000,
        "D" : 500,
        "C" : 100,
        "L" : 50,
        "X" : 10,
        "V" : 5,
        "I" : 1
        }

        for i in s:
            output += values[i]

        print(output)



if __name__ == "__main__":
    s = "LVIII"
    run_Solution = Solution()
    run_Solution.romanToInt(s)
