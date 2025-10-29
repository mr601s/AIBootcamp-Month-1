def average(numbers):
    try:
        if not isinstance(numbers,list):
            raise TypeError('Invalid must be a list.')
        if len(numbers) == 0:
            raise ValueError('Cannot average an empty list.')
        return sum(numbers) / len(numbers)
    except TypeError:
        print('Error: Input must be a list of numbers')
    except ValueError:
        print('Error: Cannot average an empty list.')
    except Exception as e:
        print('An unexpected error occurred:', e)


def is_prime(number):
    if not isinstance[number, int]:
        raise TypeError('Input must be an interger.')
    if number < 2: 
        return False 
    for candidate in range(2, int(number**0.5) + 1):
        if number % candidate == 0:
            return False
    return True

def count_vowels(string):
    vowels = 'aeiou'
    return sum(1 for char in string.lower() if char in vowels)

