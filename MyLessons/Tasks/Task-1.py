## Tapşırıq 1
# Verilmiş bir siyahıdakı bütün cüt ədədləri tapın və onların cəmini hesablayın.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even = 0

for x in numbers:
    if x%2==0:
        sum_even = sum_even+1

print("Cüt ədədlərin cəmi:", sum_even)

## Tapşırıq 2
# Verilmiş bir ədədin müsbət, mənfi və ya sıfır olduğunu təyin edin.

status= ""
number = int(input("Bir ədəd daxil edin: "))
if number < 0:
    status+="Menfi"
elif number>0:
   status+="Musbet"
elif number == 0:
    status+="Sifir"
print("Ədədin vəziyyəti:",  status)

## Tapşırıq 3
# Verilmiş bir siyahıdakı ədədlərin ortalamasını hesablayın.

count =0
numbers = [10, 20, 30, 40, 50]
average = 0

for i in numbers:
  count = count+1
  average+=i

print("Ədədlərin ortalaması:", average/count)

## Tapşırıq 4
# Verilmiş bir siyahıdakı ən böyük və ən kiçik ədədi tapın.

numbers = [5, 3, 8, 6, 7, 2]
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num> max_num:
         max_num = num
    elif num< min_num:
        min_num = num 
 
print("Ən böyük ədəd:", max_num)
print("Ən kiçik ədəd:", min_num)








