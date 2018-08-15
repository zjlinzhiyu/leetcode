'''暴力求解Brute-force'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) <= 1:
            return s

        length = len(s)
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                substr = s[j:j + i]
                count = 0
                for k in range(len(substr) // 2):
                    if substr[k] == substr[i - k - 1]:
                        count += 1
                    else:
                        break
                if count == i // 2:
                    return substr


'''中间向两边扩散算法'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        maxL, maxR, max = 0, 0, 0
        for i in range(n):
            # 长度为偶数的回文子串
            start = i
            end = i + 1
            while start >= 0 and end < n:
                if s[start] == s[end]:
                    if end - start + 1 > max:
                        maxL = start
                        maxR = end
                        max = end - start + 1
                    start -= 1
                    end += 1
                else:
                    break

            # 长度为奇数的回文子串
            start = i - 1
            end = i + 1
            while start >= 0 and end < n:
                if s[start] == s[end]:
                    if end - start + 1 > max:
                        maxL = start
                        maxR = end
                        max = end - start + 1
                    start -= 1
                    end += 1
                else:
                    break

        return s[maxL:maxR + 1]


'''动态规划法'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        flag_matrix = [[0 for i in range(n)] for i in range(n)]
        logest_substr = ''
        logest_len = 0

        for j in range(n):
            for i in range(j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        flag_matrix[i][j] = 1
                        if logest_len < j - i + 1:
                            logest_substr = s[i:j + 1]
                            logest_len = j - i + 1
                else:
                    if s[i] == s[j] and flag_matrix[i + 1][j - 1]:
                        flag_matrix[i][j] = 1
                        if logest_len < j - i + 1:
                            logest_substr = s[i:j + 1]
                            logest_len = j - i + 1
        return logest_substr

'''Manacher算法'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        sNew = '#' + '#'.join(s) + '#'
        p = [0] * len(sNew)
        maxRight = 0
        pos = 0
        maxLen = 0
        maxSubstr = ''
        flag = 0

        for i in range(len(sNew)):
            if i <= maxRight:
                j = 2 * pos - i
                p[i] = min(p[j], maxRight - i + 1)
            else:
                p[i] = 1

            while i - p[i] >= 0 and i + p[i] < len(sNew) and sNew[i - p[i]] == sNew[i + p[i]]:
                p[i] += 1

            if i + p[i] - 1 >= maxRight:
                maxRight = i + p[i] - 1
                pos = i
            if maxLen < p[i]:
                maxLen = p[i]
                flag = i

        start = (flag - maxLen + 1) // 2
        return s[start:start + maxLen - 1]
