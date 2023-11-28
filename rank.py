import re
from collections import Counter

# this is for scoring


def find_and_sort_integers(text):
    # Find all numbers in the string using regex
    integers = re.findall(r'\b\d+\b', text)

    # Convert strings to integers
    integers = [int(num) for num in integers]

    # Count the frequency of each integer
    counter = Counter(integers)

    # Sort the integers by their frequency
    sorted_integers = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    return sorted_integers


# Test the function
text = """2	8	10	16	
10	1	3	19	7
2	9	15	1	11
11	7	4		
8	9	3	18	
11	8	16	18	23
14	5		4	18
14	8	16	9	
				
3	5	18	23	12
5	10	7	8	18
3	13	7		
8	7	5	3	11"""
print(find_and_sort_integers(text))
