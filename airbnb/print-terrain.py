
def terrain(numbers):
    height = max(numbers)
    n = len(numbers)
    res = [ [" "] * n for _ in range(height)]

    # res_tmp = [ [" "] * height for _ in range(n)]
    # for i in range(n):
    #     for j in range(height):
    #         if j < numbers[i]:
    #             res_tmp[i][j] = '+'
    # for i in range(height):
    #     for j in range(n):
    #         res[i][j] = res_tmp[j][height - i - 1]
    # print(res)
    
    for i in range(height):
        for j in range(n):
            hi = numbers[j]
            if height - i <= hi:
                res[i][j] = '+'
    print(res)

    return res

def terrain_part2(numbers, waterAmount, column):
    original_heights = list(numbers)
    
    n = len(numbers)
    while waterAmount > 0:
        # go left:
        best_col = column

        l = column - 1
        while l >= 0:
            if numbers[l] > numbers[l + 1]:
                break
            else:
                if numbers[l] < numbers[best_col]:
                    best_col = l
                l -= 1
        if best_col != column: 
            numbers[best_col] += 1
        else:
            r = column + 1
            # go right:    
            while r < n:
                if numbers[r] > numbers[r - 1]:
                    break
                else:
                    if numbers[r] < numbers[best_col]:
                        best_col = r
                    r += 1
            numbers[best_col] += 1

        waterAmount -= 1
    print("Poored Water")
    renderTerrain(original_heights, numbers)


def renderTerrain(original_heights, final_heights):
    max_h = max(final_heights) if final_heights else 0
    
    # Print from top to bottom
    for h in range(max_h, 0, -1):
        row_chars = []
        for i in range(len(final_heights)):
            if original_heights[i] >= h:
                row_chars.append("+")
            elif final_heights[i] >= h:
                row_chars.append("W")
            else:
                row_chars.append(" ")
        # Print the row as a string for true ASCII rendering
        print("".join(row_chars))

res = terrain_part2([2, 1, 2, 0, 2], 3, 2)
res2 = terrain_part2([5,4,3,2,1,3,4,0,3,4], 8, 1)
