class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Initialize a stack to keep track of characters and their counts

        for char in s:
            if stack and stack[-1][0] == char:
                # Increment the count of the top character
                stack[-1][1] += 1
                # If the count reaches k, pop it from the stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Otherwise, push the current character with a count of 1
                stack.append([char, 1])

        # Reconstruct the final string from the stack
        result = []
        for char, count in stack:
            result.append(char * count)  # Append the character count times

        return ''.join(result)  # Join the list into a final string
