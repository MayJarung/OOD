class translator:
    def deciToRoman(self, number):
        roman = []
        while number > 0:
            if number//1000 >= 1:
                roman.append("M")
                number -= 1000
            elif number //900 >= 1:
                roman.append("CM")
                number -= 900
            elif number//500 >= 1:
                roman.append("D")
                number -= 500
            elif number//400 >= 1:
                roman.append("CD")
                number -= 400
            elif number//100 >= 1:    # 256 // 100 = 2      # 156 // 100 = 1
                roman.append("C")   # roman = ['C']       # roman = ['C','C']
                number -= 100         # number = 156        # number = 56
            elif number//90 >= 1:
                roman.append("XC")
                number -= 90
            elif number//50 >= 1:     # 56 // 50 = 1
                roman.append("L")   # roman = ['C','C','L']
                number -= 50          # number = 6
            elif number//40 >= 1:
                roman.append("XL")
                number -= 40
            elif number//10 >= 1:
                roman.append("X")
                number -= 10
            elif number//9 >= 1:
                roman.append("IX")
                number -= 9
            elif number//5 >= 1:      # 6 // 5 = 1
                roman.append("V")   # roman = ['C','C','L','V]
                number -= 5           # number = 1
            elif number//4 >= 1:
                roman.append("IV")
                number -= 4
            elif number//1 >= 1:      # 1 //1 = 1
                roman.append("I")   # roman = ['C','C','L','V,'I']
                number -= 1           # number = 0
        str = ""
        for i in range(len(roman)):
                str += roman[i]
        return str
    def romanToDeci(self, s):

        romanDic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        Ans = 0
        for x in range(len(s)):
            if x > 0 and romanDic[s[x]] > romanDic[s[x-1]]:
                Ans += romanDic[s[x]] - (2*romanDic[s[x-1]])
            else:
                Ans += romanDic[s[x]]

        return Ans


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))
