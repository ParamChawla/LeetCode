class Solution:
    def solve(self, index, flag, numbers, result):
        if index >= len(numbers):
            result.append("".join(numbers))
            return

        # Always place 0
        numbers[index] = "1"
        self.solve(index + 1, True, numbers, result)

        # Place 1 only if previous digit was not 1
        if flag:
            numbers[index] = "0"
            self.solve(index + 1, False, numbers, result)


    def validStrings(self, n: int) -> List[str]:
        numbers = ["0"] * n
        result = []
        self.solve(0, True, numbers, result)
        return result