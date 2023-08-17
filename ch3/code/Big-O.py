# O(N)단계 
things = ['apples', 'baboons','cribs','dulcimers']

for thing in things:
    print("Here's a thing: %s" % thing)

# O(1)단계 
print('Hello world!')

# O(N)단계 
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True 
