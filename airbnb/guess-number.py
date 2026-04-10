# https://www.hack2hire.com/companies/airbnb/coding-questions/68cdc7e53735a578b6f27eeb/practice?questionId=68cdc7ec3735a578b6f27eec

class GuessServer:
    def __init__(self, secret):
        self.secret = secret
        self.callCount = 0

    def guessNumber(self, guess):
        self.callCount += 1
        matches = 0
        for i in range(4):
            if guess[i] == self.secret[i]:
                matches += 1
        return matches

    def getCallCount(self):
        return self.callCount


class Solution:
    def __init__(self, server):
        self.server = server

    def guessSecret(self):
        
        ans = "0000"
        corrects = self.server.guessNumber(ans)
        for i in range(0, 4):
            for num in range(1, 10):
                tmp_ans = ans[0:i] + str(num) + ans[i+1:]
                tmp_res = self.server.guessNumber(tmp_ans)
                if tmp_res == 4:
                    return tmp_ans 
                if tmp_res > corrects:
                    ans = tmp_ans
                    corrects = tmp_res
                    break
        return ans


def test1():
    print("===== Test 1 =====")
    guessServer = GuessServer("1234")
    solution = Solution(guessServer)
    result = solution.guessSecret()
    print("Guessed number: " + result)  # Expected: 1234
    print("Total calls: " + str(guessServer.getCallCount()))
    print()


def test2():
    print("===== Test 2 =====")
    guessServer = GuessServer("0809")
    solution = Solution(guessServer)
    result = solution.guessSecret()
    print("Guessed number: " + result)  # Expected: 0809
    print("Total calls: " + str(guessServer.getCallCount()))
    print()


def test3():
    print("===== Test 3 =====")
    guessServer = GuessServer("5578")
    solution = Solution(guessServer)
    result = solution.guessSecret()
    print("Guessed number: " + result)  # Expected: 5578
    print("Total calls: " + str(guessServer.getCallCount()))
    print()


def test4():
    print("===== Test 4 =====")
    guessServer = GuessServer("0000")
    solution = Solution(guessServer)
    result = solution.guessSecret()
    print("Guessed number: " + result)  # Expected: 0000
    print("Total calls: " + str(guessServer.getCallCount()))
    print()


def test5():
    print("===== Test 5 =====")
    guessServer = GuessServer("9999")
    solution = Solution(guessServer)
    result = solution.guessSecret()
    print("Guessed number: " + result)  # Expected: 9999
    print("Total calls: " + str(guessServer.getCallCount()))
    print()


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()