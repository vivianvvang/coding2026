class Solution:
    def minimize_table_height(self, text1, text2, total_width):
        words1, words2 = text1.split(), text2.split()

        def get_height(words: list[str], col_width: int) -> int:
            if not words:
                return 0
            lines = 1
            current_line_len = 0

            for word in words:
                word_len = len(word)
                if current_line_len == 0:
                    current_line_len = word_len
                elif current_line_len + 1 + word_len <= col_width:
                    current_line_len += word_len
                else:
                    lines += 1
                    current_line_len = word_len
            return lines

        min_w1 = max([len(w) for w in words1], default = 0)
        min_w2 = max([len(w) for w in words2], default = 0)

        l = min_w1
        r = total_width - min_w2

        ans = float('inf')
        while l < r:
            mid = l + (r - l) //2 
            h1, h2 = get_height(words1, mid), get_height(words2, total_width - mid)
            tmp_height = max(h1, h2)
            ans = min(tmp_height, ans)

            if h1 == h2:
                break
            elif h1 > h2:
                l  = mid + 1
            else:
                r = mid  - 1
        return int(ans)

s = Solution()
text1 = "Google is a good company"
text2 = "We are hiring software engineers"
totalWidth = 20
print(s.minimize_table_height(text1, text2, total_width=totalWidth))