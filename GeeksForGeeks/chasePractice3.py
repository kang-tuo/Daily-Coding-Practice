def generate(dig_str, dig_len):
    if dig_len == 0 or dig_len == 1:
        return 1
    count = 0
    if int(dig_str[dig_len - 1]) > 0:
        count = generate(dig_str, dig_len - 1)
    if int(dig_str[dig_len - 2]) == 1 or (int(dig_str[dig_len - 2]) == 2) and int(dig_str[dig_len - 1]) < 7:
        count += generate(dig_str, dig_len - 2)

    return count

dig_len = 3
dig_str = "12"
if dig_str[0] == "0" or "00" in dig_str:
    print("invalid")
else:
    print(generate(dig_str, dig_len))

#
# def countDecodingDP(digits, n):
#     count = [0] * (n + 1);  # A table to store
#     # results of subproblems
#     count[0] = 1;
#     count[1] = 1;
#
#     for i in range(2, n + 1):
#
#         count[i] = 0;
#
#         # If the last digit is not 0, then last
#         # digit must add to the number of words
#         if (digits[i - 1] > '0'):
#             count[i] = count[i - 1];
#
#             # If second last digit is smaller than 2
#         # and last digit is smaller than 7, then
#         # last two digits form a valid character
#         if (digits[i - 2] == '1' or
#                 (digits[i - 2] == '2' and
#                  digits[i - 1] < '7')):
#             count[i] += count[i - 2];
#
#     return count[n];
#
#
# # Driver Code
# digits = "1234";
# n = len(digits);
# print("Count is",
#       countDecodingDP(digits, n));
#
# # This code is contributed by mits