# start = int(input())

# while True:
#     start += 1
#     if str(start) == str(start)[::-1]: break
# print(start)
class Palindrome:
    def __init__(self, left, middle):
        assert middle is None or middle < 10 and middle >= 0

        self.left = [int(x) for x in str(left)] # left = list(int(left))
        self.middle = middle

    def add_one_left(self, carry):
        for i in range(len(self.left)):
            ix = -(i + 1)

            if self.left[ix] == 9:
                self.left[ix] = 0
                carry = True
            else:
                self.left[ix] += 1
                carry = False
                break

        if carry:
            if self.middle is None:
                self.middle = self.left[-1]
                self.left = [1] + self.left[:-1]

            else:
                self.left = [1] + self.left
                self.middle = None

    def next_palindrome(self):
        if self.middle is not None: # if number of digits is odd
            if self.middle == 9:
                self.middle = 0
                self.add_one_left(carry=True)
            else:
                self.middle += 1
        else: # if number of digits is even
            self.add_one_left(carry=False)

    def as_int(self):
        if self.middle is None: # if there is an even number of digits
            l = self.left + list(reversed(self.left))
        else: # if there is an odd number of digits
            l = self.left + [self.middle] + list(reversed(self.left))

        return int("".join(str(x) for x in l)) # joins the list together and returns it

    @staticmethod
    def of_int(i):
        s = str(i)

        if len(s) % 2 == 0: # if there is an even number of digits
            left = [int(x) for x in s[: len(s) // 2]]
            middle = None
        else: # if there are an odd number of digits
            left = [int(x) for x in s[: len(s) // 2]]
            middle = int(s[len(left)])

        return Palindrome("".join(str(x) for x in left), middle)

    def __str__(self):
        return str(self.as_int())


i = input()
input_int = int(i)

p = Palindrome.of_int(i) # p has left and middle stored in it (if odd number of digits) 

pali_int = p.as_int()

if pali_int > input_int:
    print(pali_int)
else:
    p.next_palindrome()
    print(p)
