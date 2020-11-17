# def get(in_str):
# #     splits = in_str.split(" ")
# #     output=""
# #     for split in splits:
# #         new_split=""
# #         for i in range(len(split)):
# #             if i==0:
# #                 letter = split[i].upper()
# #             else:
# #                 letter = split[i]
# #             new_split += letter
# #         output = output + new_split+" "
# #     return output
# #
# #
# # get("hello world")
def generate(number_string, num_len):
    if num_len == 0 or num_len == 1:
        return 1
    count = 0
    if number_string[num_len - 1] > '0':
        count = generate(number_string, num_len - 1)
    if number_string[num_len - 2] == '1' or (
            number_string[num_len - 2] == '2' and number_string[num_len - 1] <= '6'):
        count += generate(number_string, num_len - 2)
    return count

line="12"
num_len = len(line)

if line[0] == "0" or "00" in line:
    print("invalid input")
else:
    count = generate(line, num_len)
    print(count, end="")


