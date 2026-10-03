print(1)
try:
    print("A")
    x = int("abc")
    print("B")
except ValueError:
    print("C")
finally:
    print("D")

# Output A C D

print("\n2")
def f():
    try:
        return "try"
    finally:
        print("cleanup")
 
print(f())

print("\n3")
try:
    nums = [1, 2, 3]
    print(nums[5])
except (IndexError, KeyError) as e:
    print(type(e).__name__)
else:
    print("no error")

print("\n4")
try:
    print(10 / 2)
except ZeroDivisionError:
    print("zero")
else:
    print("ok")
