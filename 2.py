testlist = [
    "11 - 22",
    "95 - 115",
    "998 - 1012",
    "1188511880 - 1188511890",
    "222220 - 222224",
    "1698522 - 1698528",
    "446443 - 446449",
    "38593856 - 38593862",
    "565653 - 565659",
    "824824821 - 824824827",
    "2121212118 - 2121212124",
]

mylist = [
    "9226466333 - 9226692707",
    "55432 - 96230",
    "4151 - 6365",
    "686836 - 836582",
    "519296 - 634281",
    "355894 - 471980",
    "971626 - 1037744",
    "25107 - 44804",
    "15139904 - 15163735",
    "155452 - 255998",
    "2093 - 4136",
    "829776608 - 829880425",
    "4444385616 - 4444502989",
    "2208288 - 2231858",
    "261 - 399",
    "66 - 119",
    "91876508 - 91956018",
    "2828255673 - 2828317078",
    "312330 - 341840",
    "6464 - 10967",
    "5489467 - 5621638",
    "1 - 18",
    "426 - 834",
    "3434321102 - 3434378477",
    "4865070 - 4972019",
    "54475091 - 54592515",
    "147 - 257",
    "48664376 - 48836792",
    "45 - 61",
    "1183 - 1877",
    "24 - 43",
]

ids_tosum1 = []

for valuerange in mylist:
    start, end = map(int, valuerange.split(" - "))
    for number in range(start, end + 1):
        str_num = str(number)
        mid = len(str_num) // 2
        first = str_num[:mid]
        second = str_num[mid:]
        if first == second:
            ids_tosum1.append(number)

print(sum(ids_tosum1))


ids_tosum2 = []
for valuerange in mylist:
    start, end = map(int, valuerange.split(" - "))
    for number in range(start, end + 1):
        str_num = str(number)
        length = len(str_num)
        for i in range(1, length // 2 + 1):
            pattern = str_num[:i]
            if pattern * (length // i) == str_num:
                ids_tosum2.append(number)
                break

print(sum(ids_tosum2))
