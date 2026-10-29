#ვქმნი ფუნქციას რომელსაც პარამეტრში გადაეცემა n.
def factorial_recursive(n):
#თუ n ნაკლებია ნულზე ანუ თუ უარყოფითი რიცხვია
 if n < 0:
#ვაბრუნებთ შედეგს => „უარყოფითი რიცხვებისთვის ფაქტორიალი განსაზღვრული არ არის.“
   return "Factorial is not defined for negative numbers."
 #ვამატებ საბაზისო შემთხვევას(გაჩერების პირობას) თუ n ტოლია 0 ან n ტოლია 1 ის(შეამოწმებს n ხომ არაა ან 0 ან 1)
if n == 0 or n == 1:
   #დააბრუნებს შედეგს 1
   return 1
#return აბრუნებს n რიცხვის ფაქტორიალს რეკურსიის გამოყენებით,ფუნქცია გამოთვლის პროცესში თავის თავს იძახებს ყოველ ჯერზე ერთით პატარა რიცხვით.
# return n * factorial_recursive(n - 1)
#ვიძახებ factorial_recursive ფუნქციას რომელიც გამოითვლის 5-ის ფაქტორიალს და გამომიტანს შედეგს და შემდეგ print დაბეჭდავს შედეგს ეკრანზე.
print(factorial_recursive(5))  # Output: 120
#ვიძახებ ფუნქციას რომელსაც არგუმენტად გადაეცემა 0,რახან საბაზისო შემთხვევაში n==0 ან n==1 ასეა მითითებული  გამოიტანს 1 და print დაბეჭდავს შედეგს ეკრანზე.
print(factorial_recursive(0))  # Output: 1
#################################################################################


def calculate_cart_total(discount_rate,*prices):
  total=0
  for i in prices:
    disscount_price = i * discount_rate / 100
    final_price= i-disscount_price
    total += final_price
  return float(total)
  
  ###############################################################################


  
def filter_and_sort_products(**products):
    filtered_products = filter(
        lambda item: item[1] >= 100,
        products.items()
    )

    return sorted(filtered_products, key=lambda item: item[1])


########################################################################################

def pair_students(names_list, scores_list):
    paired = zip(names_list, scores_list)
    return list(paired)


def get_passed_students(paired_data, passing_score=60):
    passed = filter(lambda student: student[1] >= passing_score, paired_data)
    return list(passed)


from functools import reduce

def calculate_average_of_passed(passed_students):
    scores = map(lambda student: student[1], passed_students)
    total = reduce(lambda x, y: x + y, scores)
    return total / len(passed_students)