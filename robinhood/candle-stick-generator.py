from typing import List


class Solution:
    def getCandlesticks(
        self, timedPrices: List[List[int]]
    ) -> List[List[int]]:
        if not timedPrices:
            return []

        prices = sorted(timedPrices, key=lambda x: x[0])

        first_time, first_price = prices[0]
        current_start = (first_time // 10) * 10

        max_price = first_price
        min_price = first_price
        open_price = first_price
        close_price = first_price

        result = []

        for time, price in prices[1:]:
            interval_start = (time // 10) * 10

            if interval_start == current_start:
                max_price = max(max_price, price)
                min_price = min(min_price, price)
                close_price = price
                continue

            # 完成当前真实 candle
            result.append([
                current_start,
                max_price,
                min_price,
                open_price,
                close_price,
            ])

            # 补充缺失 interval
            missing_start = current_start + 10
            while missing_start < interval_start:
                result.append([
                    missing_start,
                    close_price,
                    close_price,
                    close_price,
                    close_price,
                ])
                missing_start += 10

            # 初始化新的真实 candle
            current_start = interval_start
            max_price = price
            min_price = price
            open_price = price
            close_price = price

        # 最后一个 candle
        result.append([
            current_start,
            max_price,
            min_price,
            open_price,
            close_price,
        ])

        return result