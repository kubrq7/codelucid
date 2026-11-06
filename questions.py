QUIZ_DATA = {
"A_02_basic_info": [
  {
    "q": "What happens when indentation is inconsistent?",
    "a": "IndentationError",
    "options": [
      "IndentationError",
      "SyntaxError",
      "NameError",
      "TypeError"
    ],
    "reason": "Python requires consistent indentation within the same code block." 
  },
  {
    "q": "Is Python case-sensitive?",
    "a": "Yes",
    "options": [
      "Yes",
      "No",
      "Only for variables",
      "Only for function names"
    ],
    "reason": "Variable names such as 'score' and 'Score' are treated as different identifiers."
  },
  {
    "q": "What is the result of type(25)?",
    "a": "<class 'int'>",
    "options": [
      "<class 'int'>",
      "<class 'float'>",
      "<class 'str'>",
      "<class 'bool'>"
    ],
    "reason": "The value 25 is an integer."
  },
  {
    "q": "What happens when a variable is assigned a new value?",
    "a": "The previous value is overwritten",
    "options": [
      "The previous value is overwritten",
      "The values are combined",
      "A new variable is created automatically",
      "Python raises an error"
    ],
    "reason": "A variable always refers to its most recently assigned value."
  },
  {
    "q": "What does str(3) return?",
    "a": "\"3\"",
    "options": [
      "\"3\"",
      "3",
      "3.0",
      "<class 'str'>"
    ],
    "reason": "The str() function converts an integer into a string."
  },
  {
    "q": "Which statement raises a TypeError?",
    "a": "\"Age: \" + 20",
    "options": [
      "\"Age: \" + 20",
      "\"Age: \" + str(20)",
      "\"Age:\", 20",
      "f\"Age: {20}\""
    ],
    "reason": "The '+' operator cannot concatenate a string and an integer directly."
  },
  {
    "q": "Why doesn't changing a local variable affect a global variable with the same name?",
    "a": "They are in different scopes",
    "options": [
      "They are in different scopes",
      "Global variables are read-only",
      "Functions cannot use variables",
      "Python automatically copies all variables"
    ],
    "reason": "Local variables exist only within the function's scope unless the global keyword is used."
  }
],
"A_04_types_numbers": [
  {
    "q": "What is the result of int(3.9)?",
    "a": "3",
    "options": [
      "3",
      "4",
      "3.9",
      "TypeError"
    ],
    "reason": "int() removes the decimal part instead of rounding.",
    "explanation": "Many beginners expect int() to round numbers. It doesn't. It simply truncates the fractional part.",
    "difficulty": "Easy"
  },
  {
    "q": "What happens when you run int(3 + 4j)?",
    "a": "TypeError",
    "options": [
      "TypeError",
      "ValueError",
      "7",
      "3"
    ],
    "reason": "Complex numbers cannot be converted directly to integers.",
    "explanation": "Python does not know how to discard the imaginary part automatically. You must extract the real part yourself.",
    "difficulty": "Medium"
  },
  {
    "q": "What is the result of type(4e2)?",
    "a": "<class 'float'>",
    "options": [
      "<class 'float'>",
      "<class 'int'>",
      "<class 'complex'>",
      "<class 'str'>"
    ],
    "reason": "Scientific notation always creates a floating-point number.",
    "explanation": "Even though 4e2 represents 400, Python stores it as a float.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the main difference between a list and a tuple?",
    "a": "Lists are mutable, tuples are immutable",
    "options": [
      "Lists are mutable, tuples are immutable",
      "Lists are ordered, tuples are unordered",
      "Lists store numbers, tuples store text",
      "Tuples are faster because they use less memory in every situation"
    ],
    "reason": "The defining difference is mutability.",
    "explanation": "Both lists and tuples are ordered collections. The key distinction is that lists can be modified after creation, while tuples cannot.",
    "difficulty": "Easy"
  },
  {
    "q": "Which built-in data type does range() return?",
    "a": "<class 'range'>",
    "options": [
      "<class 'range'>",
      "<class 'list'>",
      "<class 'tuple'>",
      "<class 'generator'>"
    ],
    "reason": "range() creates a range object rather than a list.",
    "explanation": "A range object generates values efficiently without storing them all in memory.",
    "difficulty": "Medium"
  },
  {
    "q": "Which values can randrange(1, 4) return?",
    "a": "1, 2, or 3",
    "options": [
      "1, 2, or 3",
      "1, 2, 3, or 4",
      "2, 3, or 4",
      "Only 1 and 4"
    ],
    "reason": "The stop value is exclusive.",
    "explanation": "randrange(start, stop) includes the start value but excludes the stop value.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of type('100')?",
    "a": "<class 'str'>",
    "options": [
      "<class 'str'>",
      "<class 'int'>",
      "<class 'float'>",
      "<class 'bytes'>"
    ],
    "reason": "Quotation marks create a string.",
    "explanation": "Even if the content looks like a number, quotes make it text.",
    "difficulty": "Easy"
  },
  {
    "q": "Which category does the dictionary data type belong to?",
    "a": "Mapping Type",
    "options": [
      "Mapping Type",
      "Sequence Type",
      "Numeric Type",
      "Set Type"
    ],
    "reason": "A dictionary maps unique keys to values.",
    "explanation": "Unlike sequences, dictionaries access values by keys rather than numeric indexes.",
    "difficulty": "Medium"
  }
],
"A_06_strings": [
  {
    "q": "What is the output of 'Python'[1:4]?",
    "a": "yth",
    "options": [
      "yth",
      "Pyt",
      "thon",
      "yt"
    ],
    "reason": "Slicing includes the start index but excludes the end index.",
    "explanation": "The slice starts at index 1 ('y') and stops before index 4, producing 'yth'.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the output of 'Hello'[-4:-1]?",
    "a": "ell",
    "options": [
      "ell",
      "ello",
      "el",
      "llo"
    ],
    "reason": "Negative indices count from the end, and the stop index is excluded.",
    "explanation": "Index -4 is 'e' and index -1 ('o') is not included, resulting in 'ell'.",
    "difficulty": "Medium"
  },
  {
    "q": "What is printed by the following code?\n\nname = 'john'\nname.upper()\nprint(name)",
    "a": "john",
    "options": [
      "john",
      "JOHN",
      "AttributeError",
      "None"
    ],
    "reason": "String methods return a new string without modifying the original.",
    "explanation": "Strings are immutable. Since the result of upper() isn't assigned back to 'name', the original string remains unchanged.",
    "difficulty": "Medium"
  },
  {
    "q": "What happens when executing msg[len(msg)]?",
    "a": "IndexError",
    "options": [
      "IndexError",
      "KeyError",
      "TypeError",
      "It returns the last character"
    ],
    "reason": "The last valid index is len(msg) - 1.",
    "explanation": "Python strings are zero-indexed. Accessing index len(msg) goes one position beyond the end of the string.",
    "difficulty": "Medium"
  },
  {
    "q": "What is the value of f'{95:.2f}'?",
    "a": "95.00",
    "options": [
      "95.00",
      "95.0",
      "95",
      "95.000"
    ],
    "reason": "The '.2f' format specifier displays exactly two decimal places.",
    "explanation": "Even though 95 is an integer, formatting with '.2f' converts it to a floating-point representation.",
    "difficulty": "Medium"
  },
  {
    "q": "What is the result of 'data' in 'Data Science'?",
    "a": "False",
    "options": [
      "False",
      "True",
      "TypeError",
      "None"
    ],
    "reason": "String membership is case-sensitive.",
    "explanation": "'data' and 'Data' differ because uppercase and lowercase letters are treated as different characters.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of 'apple-banana'.split('-')?",
    "a": "['apple', 'banana']",
    "options": [
      "['apple', 'banana']",
      "['apple-banana']",
      "('apple', 'banana')",
      "'apple', 'banana'"
    ],
    "reason": "split() returns a list of substrings.",
    "explanation": "The delimiter '-' is removed, and the string is divided into two separate list elements.",
    "difficulty": "Easy"
  }
],
"A_07_booleans": [
  {
    "q": "What is the result of bool(' ')?",
    "a": "True",
    "options": [
      "True",
      "False",
      "TypeError",
      "ValueError"
    ],
    "reason": "A string containing a space is not empty.",
    "explanation": "Only an empty string ('') is considered False. A string with one or more characters—even a single space—is True.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the output of the following code?\n\nprint(bool(0.0), bool(-5))",
    "a": "False True",
    "options": [
      "False True",
      "True False",
      "False False",
      "True True"
    ],
    "reason": "Zero is falsy, while every non-zero number is truthy.",
    "explanation": "Python treats numeric zero (0, 0.0, 0j) as False. Any other numeric value evaluates to True.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of bool([0])?",
    "a": "True",
    "options": [
      "True",
      "False",
      "TypeError",
      "Depends on the value inside the list"
    ],
    "reason": "The list contains one element, so it is not empty.",
    "explanation": "Python checks whether the container is empty, not what values it contains. Even [0] is considered True because it has one element.",
    "difficulty": "Medium"
  },
  {
    "q": "What is the result of isinstance(45.2, int)?",
    "a": "False",
    "options": [
      "False",
      "True",
      "TypeError",
      "<class 'float'>"
    ],
    "reason": "45.2 is a float, not an integer.",
    "explanation": "The isinstance() function returns True only if the object belongs to the specified type (or a subclass of it).",
    "difficulty": "Easy"
  },
  {
    "q": "If a class defines __len__() and it returns 0, how is an instance of that class evaluated in a Boolean context?",
    "a": "False",
    "options": [
      "False",
      "True",
      "TypeError",
      "It depends on the object's attributes"
    ],
    "reason": "Objects with a length of zero are considered falsy.",
    "explanation": "When __bool__() is not defined, Python uses __len__(). If __len__() returns 0, the object evaluates to False.",
    "difficulty": "Hard"
  }
],
"A_08_operators": [
  {
    "q": "What are the results of 17 // 5 and 17 % 5?",
    "a": "3, 2",
    "options": [
      "3, 2",
      "3.4, 2",
      "3, 3.4",
      "2, 3"
    ],
    "reason": "'//' performs floor division, while '%' returns the remainder.",
    "explanation": "17 divided by 5 equals 3 with a remainder of 2. The '//' operator returns 3, and '%' returns 2.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of the following code?\n\na = [1, 2]\nb = [1, 2]\nprint(a is b)",
    "a": "False",
    "options": [
      "False",
      "True",
      "[1, 2]",
      "TypeError"
    ],
    "reason": "'is' compares object identity, not values.",
    "explanation": "Although both lists contain the same values, they are stored as two different objects in memory. Use '==' to compare values.",
    "difficulty": "Medium"
  },
  {
    "q": "What is the result of 10 + 2 * 5 ** 2?",
    "a": "60",
    "options": [
      "60",
      "300",
      "144",
      "250"
    ],
    "reason": "Operator precedence is: ** → * → +.",
    "explanation": "Python first evaluates 5 ** 2 (25), then 2 * 25 (50), and finally 10 + 50 (60).",
    "difficulty": "Medium"
  },
  {
    "q": "What is the result of the expression 5 < 8 < 7?",
    "a": "False",
    "options": [
      "False",
      "True",
      "TypeError",
      "None"
    ],
    "reason": "Python evaluates chained comparisons from left to right.",
    "explanation": "The expression is equivalent to (5 < 8) and (8 < 7). Since the second comparison is False, the entire expression is False.",
    "difficulty": "Medium"
  },
  {
    "q": "What is the result of 100 // 5 % 3?",
    "a": "2",
    "options": [
      "2",
      "20",
      "0",
      "1"
    ],
    "reason": "'//' and '%' have the same precedence and are evaluated from left to right.",
    "explanation": "100 // 5 equals 20, and 20 % 3 equals 2.",
    "difficulty": "Medium"
  },
  {
    "q": "Which operator checks whether two variables refer to the same object in memory?",
    "a": "is",
    "options": [
      "is",
      "==",
      "=",
      "in"
    ],
    "reason": "The 'is' operator compares object identity.",
    "explanation": "Use '==' to compare values and 'is' to compare whether two variables reference the exact same object.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of not (True and False)?",
    "a": "True",
    "options": [
      "True",
      "False",
      "None",
      "TypeError"
    ],
    "reason": "The expression inside the parentheses is evaluated first.",
    "explanation": "True and False evaluates to False, and 'not False' becomes True.",
    "difficulty": "Easy"
  }
],
"A_09_lists": [
  {
    "q": "What is printed by the following code?\n\nnumbers = [10, 20, 30]\nprint(numbers[1])",
    "a": "20",
    "options": [
      "20",
      "10",
      "30",
      "IndexError"
    ],
    "reason": "List indexing starts at 0.",
    "explanation": "Index 0 is 10, index 1 is 20, and index 2 is 30.",
    "difficulty": "Easy"
  },
  {
    "q": "What happens after executing the following code?\n\nframework = ['HTML', 'CSS', 'Python']\nframework[1:2] = ['A', 'B']",
    "a": "The list grows by one element",
    "options": [
      "The list grows by one element",
      "The list keeps the same length",
      "TypeError",
      "The list becomes a tuple"
    ],
    "reason": "Slice assignment can replace one element with multiple elements.",
    "explanation": "The slice contains one item ('CSS'), but it is replaced with two items ('A' and 'B'), increasing the list length.",
    "difficulty": "Hard"
  },
  {
    "q": "What is printed by the following code?\n\nlist_a = ['Git']\nlist_b = list_a\nlist_b.append('Python')\nprint(list_a)",
    "a": "['Git', 'Python']",
    "options": [
      "['Git', 'Python']",
      "['Git']",
      "['Python']",
      "TypeError"
    ],
    "reason": "Both variables reference the same list object.",
    "explanation": "Assigning one list to another variable does not create a copy. Both names point to the same object in memory.",
    "difficulty": "Medium"
  },
  {
    "q": "What does list.remove(value) do if the value appears multiple times?",
    "a": "Removes only the first matching element",
    "options": [
      "Removes only the first matching element",
      "Removes every matching element",
      "Raises a ValueError",
      "Removes the last matching element"
    ],
    "reason": "remove() stops after deleting the first occurrence.",
    "explanation": "If you want to remove every occurrence, you must loop through the list or use another approach.",
    "difficulty": "Medium"
  },
  {
    "q": "What is the result of list('Py')?",
    "a": "['P', 'y']",
    "options": [
      "['P', 'y']",
      "['Py']",
      "('P', 'y')",
      "'Py'"
    ],
    "reason": "list() converts an iterable into a list of its elements.",
    "explanation": "A string is iterable, so each character becomes a separate list element.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of the following code?\n\nitems = ['html', 'CSS']\nitems.sort()\nprint(items)",
    "a": "['CSS', 'html']",
    "options": [
      "['CSS', 'html']",
      "['html', 'CSS']",
      "['css', 'html']",
      "TypeError"
    ],
    "reason": "Uppercase letters come before lowercase letters in Unicode ordering.",
    "explanation": "Python sorts strings lexicographically. Since uppercase letters have lower Unicode values than lowercase letters, 'CSS' appears before 'html'.",
    "difficulty": "Hard"
  },
  {
    "q": "What is printed by the following code?\n\nnumbers = [1, 2, 3]\nprint(numbers[-1])",
    "a": "3",
    "options": [
      "3",
      "1",
      "-1",
      "IndexError"
    ],
    "reason": "Negative indices count from the end of the list.",
    "explanation": "Index -1 refers to the last element, -2 to the second last, and so on.",
    "difficulty": "Easy"
  },
  {
    "q": "Which method adds a single element to the end of a list?",
    "a": "append()",
    "options": [
      "append()",
      "extend()",
      "insert()",
      "add()"
    ],
    "reason": "append() adds one object to the end of the list.",
    "explanation": "extend() adds multiple elements from an iterable, insert() places an element at a specific index, and add() is used with sets, not lists.",
    "difficulty": "Easy"
  }
],
"A_10_tuples": [
  {
    "q": "What is the result of type(('production'))?",
    "a": "<class 'str'>",
    "options": [
      "<class 'str'>",
      "<class 'tuple'>",
      "<class 'list'>",
      "<class 'set'>"
    ],
    "reason": "Parentheses alone do not create a tuple; the trailing comma does.",
    "explanation": "('production') is just a string inside parentheses. To create a one-element tuple, write ('production',).",
    "difficulty": "Easy"
  },
  {
    "q": "What happens when executing the following code?\n\nports = (80, 443)\nports[0] = 8080",
    "a": "TypeError",
    "options": [
      "TypeError",
      "IndexError",
      "ValueError",
      "The tuple is updated successfully"
    ],
    "reason": "Tuples are immutable.",
    "explanation": "Once a tuple is created, its elements cannot be modified. Any attempt to assign a new value raises a TypeError.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the value of workers after executing the following code?\n\nnodes = ('Server1', 'Server2', 'Server3', 'Server4')\nleader, *workers, backup = nodes",
    "a": "['Server2', 'Server3']",
    "options": [
      "['Server2', 'Server3']",
      "('Server2', 'Server3')",
      "'Server2'",
      "['Server2', 'Server3', 'Server4']"
    ],
    "reason": "The starred variable collects all remaining elements into a list.",
    "explanation": "Even though the original object is a tuple, the '*' operator always collects the remaining values into a list.",
    "difficulty": "Medium"
  },
  {
    "q": "What happens after executing del data if data is a tuple variable?",
    "a": "The variable is deleted",
    "options": [
      "The variable is deleted",
      "The tuple becomes empty",
      "The first element is removed",
      "The tuple is converted to None"
    ],
    "reason": "del removes the variable reference, not the tuple contents.",
    "explanation": "After using del, the variable no longer exists. Trying to access it raises a NameError.",
    "difficulty": "Medium"
  },
  {
    "q": "What is the result of the following code?\n\nscores = (95, 100, 100, 85)\nprint(scores.index(100))",
    "a": "1",
    "options": [
      "1",
      "2",
      "(1, 2)",
      "ValueError"
    ],
    "reason": "index() returns the first matching position.",
    "explanation": "Although 100 appears twice, index() always returns the index of its first occurrence.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\nnumbers = (1, 2, 3)\nprint(numbers * 2)",
    "a": "(1, 2, 3, 1, 2, 3)",
    "options": [
      "(1, 2, 3, 1, 2, 3)",
      "(2, 4, 6)",
      "(1, 2, 3)",
      "TypeError"
    ],
    "reason": "Multiplying a tuple repeats its contents.",
    "explanation": "The '*' operator repeats the tuple rather than multiplying its numeric values.",
    "difficulty": "Medium"
  },
  {
    "q": "Which statement correctly creates an empty tuple?",
    "a": "()",
    "options": [
      "()",
      "[]",
      "{}",
      "tuple[]"
    ],
    "reason": "An empty tuple is created using empty parentheses.",
    "explanation": "[] creates a list, {} creates a dictionary (or set when populated), and tuple[] is invalid syntax.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\ncolors = ('red', 'green', 'blue')\nprint('green' in colors)",
    "a": "True",
    "options": [
      "True",
      "False",
      "TypeError",
      "None"
    ],
    "reason": "The 'in' operator checks membership.",
    "explanation": "Since 'green' exists in the tuple, the membership test returns True.",
    "difficulty": "Easy"
  }
],
"A_11_sets": [
  {
    "q": "What is the length of the following set?\n\n{0, False, 'auth', 1, True}",
    "a": "3",
    "options": [
      "3",
      "5",
      "4",
      "2"
    ],
    "reason": "0 and False are considered equal, as are 1 and True.",
    "explanation": "Sets store only unique values. Since False == 0 and True == 1, duplicate values are removed, leaving {0, 'auth', 1}.",
    "difficulty": "Hard"
  },
  {
    "q": "What does set.pop() do?",
    "a": "Removes and returns an arbitrary element",
    "options": [
      "Removes and returns an arbitrary element",
      "Removes the first element",
      "Removes the last element",
      "Removes a random index"
    ],
    "reason": "Sets are unordered collections.",
    "explanation": "Because sets have no defined order, pop() removes an arbitrary element rather than the first or last one.",
    "difficulty": "Medium"
  },
  {
    "q": "What is the result of the '^' operator between two sets?",
    "a": "Symmetric difference",
    "options": [
      "Symmetric difference",
      "Intersection",
      "Union",
      "Difference"
    ],
    "reason": "The '^' operator returns elements that exist in exactly one of the two sets.",
    "explanation": "For example, {1,2,3} ^ {3,4,5} produces {1,2,4,5}.",
    "difficulty": "Medium"
  },
  {
    "q": "What happens when executing the following code?\n\nnumbers = {1, 2, 3}\nprint(numbers[0])",
    "a": "TypeError",
    "options": [
      "TypeError",
      "IndexError",
      "KeyError",
      "1"
    ],
    "reason": "Sets do not support indexing.",
    "explanation": "Unlike lists and tuples, sets are unordered collections and cannot be accessed using numeric indexes.",
    "difficulty": "Easy"
  },
  {
    "q": "What happens when executing {1, 2, 3} - [2, 3]?",
    "a": "TypeError",
    "options": [
      "TypeError",
      "{1}",
      "{1, 2, 3}",
      "[1]"
    ],
    "reason": "Set operators require both operands to be sets.",
    "explanation": "Convert the list first using set([2, 3]) before performing set subtraction.",
    "difficulty": "Medium"
  },
  {
    "q": "What happens if discard() is called with an element that does not exist?",
    "a": "Nothing happens",
    "options": [
      "Nothing happens",
      "KeyError",
      "ValueError",
      "The element is added"
    ],
    "reason": "discard() safely ignores missing elements.",
    "explanation": "Unlike remove(), discard() never raises an exception when the element is absent.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\nA = {1, 2, 3}\nB = {3, 4, 5}\nprint(A & B)",
    "a": "{3}",
    "options": [
      "{3}",
      "{1, 2, 4, 5}",
      "{1, 2, 3, 4, 5}",
      "{}"
    ],
    "reason": "The '&' operator returns the intersection of two sets.",
    "explanation": "Only elements present in both sets are included in the result.",
    "difficulty": "Easy"
  },
  {
    "q": "Which statement correctly creates an empty set?",
    "a": "set()",
    "options": [
      "set()",
      "{}",
      "[]",
      "()"
    ],
    "reason": "{} creates an empty dictionary, not a set.",
    "explanation": "To create an empty set, use the set() constructor. Curly braces without elements create a dictionary.",
    "difficulty": "Easy"
  }
],
"A_12_dictionaries": [
  {
    "q": "What happens if a dictionary is created with duplicate keys?\n\ndata = {'a': 1, 'b': 2, 'a': 5}\nprint(data)",
    "a": "{'a': 5, 'b': 2}",
    "options": [
      "{'a': 5, 'b': 2}",
      "{'a': 1, 'b': 2}",
      "KeyError",
      "SyntaxError"
    ],
    "reason": "Dictionary keys must be unique.",
    "explanation": "When duplicate keys are provided, the last value assigned to that key replaces the previous one.",
    "difficulty": "Easy"
  },
  {
    "q": "Which statement raises a KeyError if the key does not exist?",
    "a": "data['age']",
    "options": [
      "data['age']",
      "data.get('age')",
      "data.get('age', 0)",
      "'age' in data"
    ],
    "reason": "Square bracket notation requires the key to exist.",
    "explanation": "get() safely returns None or a default value, while [] raises KeyError when the key is missing.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\ndata = {'x': 10}\nkeys = data.keys()\ndata['y'] = 20\nprint(list(keys))",
    "a": "['x', 'y']",
    "options": [
      "['x', 'y']",
      "['x']",
      "KeyError",
      "TypeError"
    ],
    "reason": "Dictionary view objects are dynamic.",
    "explanation": "The object returned by keys() reflects changes made to the dictionary after it is created.",
    "difficulty": "Hard"
  },
  {
    "q": "What does popitem() return?",
    "a": "A (key, value) tuple",
    "options": [
      "A (key, value) tuple",
      "Only the key",
      "Only the value",
      "A list"
    ],
    "reason": "popitem() removes and returns the last inserted key-value pair.",
    "explanation": "The returned object is always a tuple containing both the key and its corresponding value.",
    "difficulty": "Medium"
  },
  {
    "q": "What is printed by the following code?\n\ndata_a = {'name': 'Alice'}\ndata_b = data_a\ndata_b['age'] = 20\nprint(data_a)",
    "a": "{'name': 'Alice', 'age': 20}",
    "options": [
      "{'name': 'Alice', 'age': 20}",
      "{'name': 'Alice'}",
      "{'age': 20}",
      "TypeError"
    ],
    "reason": "Assignment copies the reference, not the dictionary.",
    "explanation": "Both variables refer to the same dictionary object. Changing one also changes the other.",
    "difficulty": "Medium"
  },
  {
    "q": "Which object can be used as a dictionary key?",
    "a": "(1, 2)",
    "options": [
      "(1, 2)",
      "[1, 2]",
      "{1, 2}",
      "{'a': 1}"
    ],
    "reason": "Dictionary keys must be hashable.",
    "explanation": "Tuples are immutable and hashable, while lists, sets, and dictionaries are mutable and cannot be used as keys.",
    "difficulty": "Medium"
  },
  {
    "q": "What is printed by the following code?\n\ndata = {'a': 1}\nprint('a' in data)",
    "a": "True",
    "options": [
      "True",
      "False",
      "1",
      "KeyError"
    ],
    "reason": "The 'in' operator checks dictionary keys.",
    "explanation": "Membership testing on a dictionary searches only the keys, not the values.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of len({'x': 1, 'y': 2, 'z': 3})?",
    "a": "3",
    "options": [
      "3",
      "6",
      "2",
      "1"
    ],
    "reason": "len() returns the number of key-value pairs.",
    "explanation": "Each key-value pair counts as one dictionary item.",
    "difficulty": "Easy"
  }
],
"A_13_conditions": [
  {
    "q": "What is the Boolean value of an empty list ([]) in an if statement?",
    "a": "False",
    "options": [
      "False",
      "True",
      "None",
      "TypeError"
    ],
    "reason": "Empty containers are considered falsy in Python.",
    "explanation": "Python treats empty lists, tuples, dictionaries, sets, and strings as False in Boolean contexts.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\nx = 0\nif x and 10 / x:\n    print('Yes')\nelse:\n    print('No')",
    "a": "No",
    "options": [
      "No",
      "Yes",
      "ZeroDivisionError",
      "TypeError"
    ],
    "reason": "The 'and' operator short-circuits when the left operand is False.",
    "explanation": "Since x is 0 (falsy), Python never evaluates '10 / x', preventing a ZeroDivisionError.",
    "difficulty": "Hard"
  },
  {
    "q": "Which operator precedence is correct in Python?",
    "a": "not > and > or",
    "options": [
      "not > and > or",
      "or > and > not",
      "and > or > not",
      "not > or > and"
    ],
    "reason": "Logical operators have a fixed precedence order.",
    "explanation": "Python evaluates 'not' first, then 'and', and finally 'or'. Parentheses can always be used to override this order.",
    "difficulty": "Medium"
  },
  {
    "q": "How do you create an empty if block without causing a SyntaxError?",
    "a": "Use pass",
    "options": [
      "Use pass",
      "Leave the block empty",
      "Use continue",
      "Use break"
    ],
    "reason": "Python requires every code block to contain at least one statement.",
    "explanation": "The 'pass' statement acts as a placeholder when no code needs to be executed.",
    "difficulty": "Easy"
  },
  {
    "q": "What happens in an if-elif-else chain when multiple conditions are True?",
    "a": "Only the first True block executes",
    "options": [
      "Only the first True block executes",
      "Every True block executes",
      "The else block always executes",
      "Python raises a SyntaxError"
    ],
    "reason": "An if-elif-else chain stops after the first matching condition.",
    "explanation": "Once Python finds the first True condition, it skips all remaining elif and else blocks.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of bool('False')?",
    "a": "True",
    "options": [
      "True",
      "False",
      "None",
      "TypeError"
    ],
    "reason": "Non-empty strings are always truthy.",
    "explanation": "Python does not interpret the text 'False' as the Boolean value False. Since the string contains characters, it evaluates to True.",
    "difficulty": "Medium"
  },
  {
    "q": "What is printed by the following code?\n\nx = 5\nif x > 10:\n    print('A')\nelif x > 3:\n    print('B')\nelse:\n    print('C')",
    "a": "B",
    "options": [
      "B",
      "A",
      "C",
      "Nothing"
    ],
    "reason": "The first True condition in the chain is executed.",
    "explanation": "The first condition is False, but the second condition (5 > 3) is True, so 'B' is printed.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of not False and False?",
    "a": "False",
    "options": [
      "False",
      "True",
      "None",
      "TypeError"
    ],
    "reason": "'not' is evaluated before 'and'.",
    "explanation": "Python evaluates 'not False' first, producing True. The expression then becomes True and False, which evaluates to False.",
    "difficulty": "Medium"
  }
],
"A_14_loops": [
  {
    "q": "What is the output of list(range(1, 4))?",
    "a": "[1, 2, 3]",
    "options": [
      "[1, 2, 3]",
      "[1, 2, 3, 4]",
      "[0, 1, 2, 3]",
      "[2, 3, 4]"
    ],
    "reason": "The stop value in range() is exclusive.",
    "explanation": "range(start, stop) includes the start value but excludes the stop value.",
    "difficulty": "Easy"
  },
  {
    "q": "What does the continue statement do inside a loop?",
    "a": "Skips the rest of the current iteration",
    "options": [
      "Skips the rest of the current iteration",
      "Stops the loop completely",
      "Restarts the loop from the beginning",
      "Exits the program"
    ],
    "reason": "continue skips only the remaining statements in the current iteration.",
    "explanation": "After continue is executed, Python immediately starts the next iteration of the loop.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\nfor i in range(3):\n    if i == 1:\n        continue\n    print(i, end=' ')",
    "a": "0 2",
    "options": [
      "0 2",
      "0 1 2",
      "1 2",
      "0"
    ],
    "reason": "The iteration where i equals 1 is skipped.",
    "explanation": "The continue statement prevents print() from running when i is 1.",
    "difficulty": "Medium"
  },
  {
    "q": "When does the else block of a while loop execute?",
    "a": "When the loop finishes without a break",
    "options": [
      "When the loop finishes without a break",
      "Every time the loop runs",
      "Only if break is executed",
      "Only if continue is executed"
    ],
    "reason": "The else block runs only after normal loop termination.",
    "explanation": "If the loop exits because of a break statement, the else block is skipped.",
    "difficulty": "Medium"
  },
  {
    "q": "What is printed by the following code?\n\nfor i in range(5):\n    if i == 3:\n        break\nprint(i)",
    "a": "3",
    "options": [
      "3",
      "4",
      "2",
      "0"
    ],
    "reason": "The loop stops immediately when i becomes 3.",
    "explanation": "The break statement terminates the loop before the next iteration begins.",
    "difficulty": "Medium"
  },
  {
    "q": "Which pattern in a match statement should normally appear last?",
    "a": "_",
    "options": [
      "_",
      "0",
      "None",
      "\"default\""
    ],
    "reason": "The wildcard pattern matches anything.",
    "explanation": "If '_' appears earlier, it matches every remaining value and makes later cases unreachable.",
    "difficulty": "Hard"
  },
  {
    "q": "What is a pattern guard in a match statement?",
    "a": "An if condition attached to a case",
    "options": [
      "An if condition attached to a case",
      "A loop inside a case",
      "A try-except block",
      "A default case"
    ],
    "reason": "Pattern guards provide additional conditions for a successful match.",
    "explanation": "A case is selected only if both the pattern matches and the guard condition evaluates to True.",
    "difficulty": "Hard"
  },
  {
    "q": "What is printed by the following code?\n\ncount = 0\nwhile count < 3:\n    count += 1\nelse:\n    print('Done')",
    "a": "Done",
    "options": [
      "Done",
      "Nothing",
      "TypeError",
      "Infinite loop"
    ],
    "reason": "The loop finishes normally without encountering a break statement.",
    "explanation": "Since the while loop ends because its condition becomes False, the else block executes.",
    "difficulty": "Medium"
  }
],
"A_15_functions": [
  {
    "q": "What does the '/' symbol mean in a function definition?\n\ndef greet(name, /):\n    ...",
    "a": "Parameters before '/' are positional-only.",
    "options": [
      "Parameters before '/' are positional-only.",
      "Parameters after '/' are keyword-only.",
      "It starts a comment.",
      "It performs division."
    ],
    "reason": "The '/' marker makes all preceding parameters positional-only.",
    "explanation": "Arguments before '/' cannot be passed using their parameter names.",
    "difficulty": "Medium"
  },
  {
    "q": "What is printed by the following code?\n\ndef add(item, items=[]):\n    items.append(item)\n    return items\n\nprint(add(1))\nprint(add(2))",
    "a": "[1]\\n[1, 2]",
    "options": [
      "[1]\\n[1, 2]",
      "[1]\\n[2]",
      "[1, 2]\\n[1, 2]",
      "TypeError"
    ],
    "reason": "Mutable default arguments are created only once.",
    "explanation": "The same list object is reused every time the function is called unless a new one is provided.",
    "difficulty": "Hard"
  },
  {
    "q": "Which keyword allows a nested function to modify a variable from its enclosing function?",
    "a": "nonlocal",
    "options": [
      "nonlocal",
      "global",
      "local",
      "static"
    ],
    "reason": "nonlocal gives access to variables in the nearest enclosing scope.",
    "explanation": "Use 'global' for module-level variables and 'nonlocal' for variables in an outer function.",
    "difficulty": "Medium"
  },
  {
    "q": "What happens if a decorator does not use functools.wraps()?",
    "a": "The wrapped function's metadata is replaced.",
    "options": [
      "The wrapped function's metadata is replaced.",
      "The decorator does not work.",
      "A TypeError is raised.",
      "The function becomes recursive."
    ],
    "reason": "Without wraps(), attributes such as __name__ and __doc__ belong to the wrapper.",
    "explanation": "functools.wraps() preserves the original function's metadata.",
    "difficulty": "Hard"
  },
  {
    "q": "Is it valid to use both '/' and '*' in the same function definition?",
    "a": "Yes",
    "options": [
      "Yes",
      "No",
      "Only in Python 2",
      "Only inside lambda functions"
    ],
    "reason": "Python supports positional-only and keyword-only parameters in the same function.",
    "explanation": "Parameters before '/' are positional-only, while parameters after '*' are keyword-only.",
    "difficulty": "Medium"
  },
  {
    "q": "What exception is eventually raised by infinite recursion?",
    "a": "RecursionError",
    "options": [
      "RecursionError",
      "StackOverflowError",
      "RuntimeError",
      "MemoryError"
    ],
    "reason": "Python stops recursive calls when the recursion limit is exceeded.",
    "explanation": "Unlike some languages, Python raises RecursionError instead of crashing immediately.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\ndef multiply(a, b=2):\n    return a * b\n\nprint(multiply(5))",
    "a": "10",
    "options": [
      "10",
      "5",
      "7",
      "TypeError"
    ],
    "reason": "The default value of b is used.",
    "explanation": "Since no second argument is provided, Python uses the default value b=2.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\nx = 10\n\ndef test():\n    x = 20\n\nprint(x)",
    "a": "10",
    "options": [
      "10",
      "20",
      "30",
      "NameError"
    ],
    "reason": "The local variable does not affect the global variable.",
    "explanation": "Variables defined inside a function exist only within that function unless declared as global.",
    "difficulty": "Easy"
  }
],
"A_16_sequences": [
  {
    "q": "What is the output of list(range(5, 1, -1))?",
    "a": "[5, 4, 3, 2]",
    "options": [
      "[5, 4, 3, 2]",
      "[5, 4, 3, 2, 1]",
      "[1, 2, 3, 4, 5]",
      "[5, 4, 3]"
    ],
    "reason": "The stop value in range() is excluded.",
    "explanation": "The sequence starts at 5, decreases by 1, and stops before reaching 1.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\nnumbers = [5, 2, 9]\nresult = numbers.sort()\nprint(result)",
    "a": "None",
    "options": [
      "None",
      "[2, 5, 9]",
      "[5, 2, 9]",
      "TypeError"
    ],
    "reason": "list.sort() modifies the list in place and returns None.",
    "explanation": "Many beginners expect sort() to return a sorted list. Instead, it changes the original list and returns None.",
    "difficulty": "Medium"
  },
  {
    "q": "What is the result of type(range(5))?",
    "a": "<class 'range'>",
    "options": [
      "<class 'range'>",
      "<class 'list'>",
      "<class 'tuple'>",
      "<class 'generator'>"
    ],
    "reason": "range() creates a range object.",
    "explanation": "Python uses a lightweight range object instead of creating a list immediately.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of 6 in range(0, 10, 3)?",
    "a": "True",
    "options": [
      "True",
      "False",
      "TypeError",
      "ValueError"
    ],
    "reason": "The range contains 0, 3, 6, and 9.",
    "explanation": "Membership testing works directly on range objects without converting them to lists.",
    "difficulty": "Medium"
  },
  {
    "q": "What is printed by the following code?\n\nitems = ['A', 'B', 'C']\nprint(items.pop(1))",
    "a": "B",
    "options": [
      "B",
      "A",
      "C",
      "['A', 'C']"
    ],
    "reason": "pop(index) removes and returns the element at the given index.",
    "explanation": "After calling pop(1), the list becomes ['A', 'C'], but the returned value is 'B'.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the result of range(10)[2:8:2]?",
    "a": "range(2, 8, 2)",
    "options": [
      "range(2, 8, 2)",
      "[2, 4, 6]",
      "(2, 4, 6)",
      "TypeError"
    ],
    "reason": "Slicing a range returns another range object.",
    "explanation": "Unlike lists, slicing a range does not create a list. It produces a new range object.",
    "difficulty": "Hard"
  },
  {
    "q": "Which method returns a new sorted list without modifying the original list?",
    "a": "sorted()",
    "options": [
      "sorted()",
      "sort()",
      "reverse()",
      "copy()"
    ],
    "reason": "sorted() creates and returns a new list.",
    "explanation": "Unlike list.sort(), the sorted() function leaves the original iterable unchanged.",
    "difficulty": "Medium"
  },
  {
    "q": "What is printed by the following code?\n\nnumbers = [1, 2, 3]\ncopy = numbers[:]\ncopy.append(4)\nprint(numbers)",
    "a": "[1, 2, 3]",
    "options": [
      "[1, 2, 3]",
      "[1, 2, 3, 4]",
      "[4]",
      "TypeError"
    ],
    "reason": "Slicing creates a shallow copy of the list.",
    "explanation": "Appending to the copied list does not affect the original list because they are different list objects.",
    "difficulty": "Medium"
  }
],
"A_17_iterators_modules": [
  {
    "q": "What is printed by the following code?\n\nnumbers = iter([10, 20, 30])\nprint(next(numbers))",
    "a": "10",
    "options": [
      "10",
      "20",
      "[10, 20, 30]",
      "StopIteration"
    ],
    "reason": "next() returns the next item from an iterator.",
    "explanation": "The iterator starts before the first element, so the first call to next() returns 10.",
    "difficulty": "Easy"
  },
  {
    "q": "What happens when next() is called after an iterator has no remaining elements?",
    "a": "StopIteration",
    "options": [
      "StopIteration",
      "IndexError",
      "EOFError",
      "TypeError"
    ],
    "reason": "Iterators signal completion by raising StopIteration.",
    "explanation": "Unlike lists, iterators do not support indexing. When exhausted, next() raises StopIteration.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\nit = iter('Hi')\nprint(next(it))\nprint(next(it))",
    "a": "H\\ni",
    "options": [
      "H\\ni",
      "Hi",
      "H H",
      "StopIteration"
    ],
    "reason": "Strings are iterable character by character.",
    "explanation": "Each call to next() returns the next character until the iterator is exhausted.",
    "difficulty": "Easy"
  },
  {
    "q": "Which built-in function creates an iterator from an iterable object?",
    "a": "iter()",
    "options": [
      "iter()",
      "next()",
      "iterator()",
      "enumerate()"
    ],
    "reason": "iter() converts an iterable into an iterator.",
    "explanation": "Lists, tuples, strings, dictionaries, and sets are iterable. Calling iter() returns an iterator object.",
    "difficulty": "Easy"
  },
  {
    "q": "What is the output of the following code?\n\nit = iter([1])\nnext(it)\nnext(it)",
    "a": "StopIteration",
    "options": [
      "StopIteration",
      "IndexError",
      "None",
      "1"
    ],
    "reason": "The iterator contains only one element.",
    "explanation": "The first next() consumes the only element. The second call raises StopIteration.",
    "difficulty": "Medium"
  },
  {
    "q": "Which statement correctly imports only the sqrt function from the math module?",
    "a": "from math import sqrt",
    "options": [
      "from math import sqrt",
      "import math.sqrt",
      "include math.sqrt",
      "using math import sqrt"
    ],
    "reason": "Python uses the 'from ... import ...' syntax.",
    "explanation": "This imports only the sqrt function instead of the entire module.",
    "difficulty": "Easy"
  },
  {
    "q": "What is printed by the following code?\n\nimport math\nprint(math.pi > 3)",
    "a": "True",
    "options": [
      "True",
      "False",
      "3.14",
      "TypeError"
    ],
    "reason": "math.pi is approximately 3.14159.",
    "explanation": "Since π is greater than 3, the comparison evaluates to True.",
    "difficulty": "Easy"
  },
  {
    "q": "Which statement is considered the best practice?",
    "a": "import math",
    "options": [
      "import math",
      "from math import *",
      "import *",
      "using math"
    ],
    "reason": "Explicit imports improve readability and avoid namespace pollution.",
    "explanation": "Wildcard imports make it difficult to determine where names come from and are generally discouraged.",
    "difficulty": "Medium"
  },
  {
    "q": "What does enumerate(['a', 'b']) return when converted to a list?",
    "a": "[(0, 'a'), (1, 'b')]",
    "options": [
      "[(0, 'a'), (1, 'b')]",
      "['a', 'b']",
      "[(1, 'a'), (2, 'b')]",
      "[0, 1]"
    ],
    "reason": "enumerate() pairs each item with its index, starting from 0 by default.",
    "explanation": "The returned object is an iterator that yields (index, value) tuples.",
    "difficulty": "Medium"
  },
  {
    "q": "Which object is NOT an iterator?",
    "a": "[1, 2, 3]",
    "options": [
      "[1, 2, 3]",
      "iter([1, 2, 3])",
      "enumerate([1, 2])",
      "map(str, [1, 2])"
    ],
    "reason": "A list is iterable but not an iterator.",
    "explanation": "Lists can be iterated over, but they do not implement the iterator protocol until passed to iter().",
    "difficulty": "Hard"
  }
],
  "A_18_datetime_math_json": [
    {
      "q": "What is printed by datetime(2026, 12, 25).strftime('%m-%d-%y')?",
      "a": "12-25-26",
      "options": ["25-12-2026", "12-25-26", "12-25-2026", "2026-12-25"],
      "reason": "%y gives 2-digit year.",
      "explanation": "strftime formats date as month-day-year(two digit).",
      "difficulty": "Easy"
    },
    {
      "q": "math.floor(-3.4) and math.ceil(-3.4) result?",
      "a": "-4, -3",
      "options": ["-3, -2", "-4, -3", "-3, -3", "-4, -2"],
      "reason": "floor goes down, ceil goes up.",
      "explanation": "Floor moves toward -infinity, ceil toward +infinity.",
      "difficulty": "Medium"
    },
    {
      "q": "json.loads('{\"a\": 1}') with single quotes version raises?",
      "a": "JSONDecodeError",
      "options": ["dict", "None", "JSONDecodeError", "ValueError"],
      "reason": "JSON requires double quotes.",
      "explanation": "Single quotes are invalid JSON syntax.",
      "difficulty": "Medium"
    },
    {
      "q": "max([10,5,20]) + min([30,40])?",
      "a": "50",
      "options": ["40", "50", "60", "30"],
      "reason": "20 + 30 = 50",
      "explanation": "max returns 20, min returns 30.",
      "difficulty": "Easy"
    },
    {
      "q": "datetime(2026) call results in?",
      "a": "TypeError",
      "options": ["datetime object", "None", "TypeError", "ValueError"],
      "reason": "Missing required args.",
      "explanation": "datetime needs year, month, day.",
      "difficulty": "Easy"
    }
  ],
  "A_19_regEx": [
    {
      "q": "re.findall() with no matches returns?",
      "a": "[]",
      "options": ["None", "[]", "False", "Error"],
      "reason": "Always returns list.",
      "explanation": "No matches => empty list.",
      "difficulty": "Easy"
    },
    {
      "q": "match_obj.group() when match_obj is None?",
      "a": "AttributeError",
      "options": ["None", "False", "AttributeError", "ValueError"],
      "reason": "NoneType has no group().",
      "explanation": "Calling method on None raises error.",
      "difficulty": "Easy"
    },
    {
      "q": "hel{2}o matches which string?",
      "a": "hello",
      "options": ["helo", "hello", "hellllo", "heello"],
      "reason": "{2} means exactly 2 l's.",
      "explanation": "Pattern: hel+o with exactly 2 l.",
      "difficulty": "Medium"
    },
    {
      "q": "re.split('-', 'A-B-C-D', maxsplit=2)?",
      "a": "['A','B','C-D']",
      "options": [
        "['A','B','C','D']",
        "['A','B-C-D']",
        "['A','B','C-D']",
        "['A-B','C','D']"
      ],
      "reason": "Only 2 splits allowed.",
      "explanation": "Remaining part stays un-split.",
      "difficulty": "Medium"
    },
    {
      "q": "r'\\bcode' vs '\\bcode' difference?",
      "a": "Match vs invalid escape",
      "options": ["Same", "Match vs invalid escape", "Both match", "Both fail"],
      "reason": "raw string keeps regex boundary.",
      "explanation": "Without r'', \\b becomes backspace.",
      "difficulty": "Hard"
    }
  ],

  "A_20_pip_exceptions": [
    {
      "q": "pip install inside Python script results in?",
      "a": "SyntaxError",
      "options": ["Works", "SyntaxError", "RuntimeError", "None"],
      "reason": "pip is shell command.",
      "explanation": "Must be run in terminal.",
      "difficulty": "Easy"
    },
    {
      "q": "try-except-else: else runs when?",
      "a": "No exception occurs",
      "options": ["Always", "Error occurs", "No exception occurs", "Finally runs"],
      "reason": "else = success block.",
      "explanation": "Only executes if try succeeds.",
      "difficulty": "Easy"
    },
    {
      "q": "finally block behavior?",
      "a": "Always executes",
      "options": ["Only error", "Only success", "Always executes", "Never"],
      "reason": "Guaranteed execution.",
      "explanation": "Runs even after return.",
      "difficulty": "Easy"
    },
    {
      "q": "except (TypeError, ValueError) means?",
      "a": "Handles both errors",
      "options": ["Only TypeError", "Only ValueError", "Both errors", "Syntax error"],
      "reason": "tuple exception handling.",
      "explanation": "Multiple exceptions grouped.",
      "difficulty": "Medium"
    }
  ],

  "A_21_string_formatting": [
    {
      "q": "f-string invalid usage?",
      "a": "f'{x'",
      "options": ["f'{x}'", "f\"{x}\"", "f'{x+1}'", "f'{x}'"],
      "reason": "missing closing brace.",
      "explanation": "Syntax error in format string.",
      "difficulty": "Easy"
    },
    {
      "q": "{:.2f}.format(1.6789) output?",
      "a": "1.68",
      "options": ["1.67", "1.68", "1.70", "1.6789"],
      "reason": "rounding rule.",
      "explanation": "2 decimal precision rounding.",
      "difficulty": "Easy"
    },
    {
      "q": "{:b}.format(6) result?",
      "a": "110",
      "options": ["101", "110", "111", "100"],
      "reason": "binary conversion.",
      "explanation": "6 in binary = 110.",
      "difficulty": "Easy"
    },
    {
      "q": "{0.85:.0%} output?",
      "a": "85%",
      "options": ["0.85%", "85%", "0%", "85.0%"],
      "reason": "percentage format.",
      "explanation": "0.85 * 100 = 85%.",
      "difficulty": "Medium"
    }
  ],

  "A_22_none_input_venv": [
    {
      "q": "input('5') * 2 returns?",
      "a": "55",
      "options": ["10", "55", "5", "Error"],
      "reason": "string repetition.",
      "explanation": "'5' * 2 = '55'.",
      "difficulty": "Easy"
    },
    {
      "q": "None == None and None is None?",
      "a": "True True",
      "options": ["False True", "True False", "True True", "False False"],
      "reason": "singleton object.",
      "explanation": "None identity is always same.",
      "difficulty": "Medium"
    },
    {
      "q": "list.sort() return value?",
      "a": "None",
      "options": ["sorted list", "None", "boolean", "iterator"],
      "reason": "in-place operation.",
      "explanation": "sort modifies original list.",
      "difficulty": "Easy"
    },
    {
      "q": "venv deletion method?",
      "a": "delete folder",
      "options": ["pip uninstall", "delete folder", "deactivate", "reset python"],
      "reason": "venv is just directory.",
      "explanation": "No registry uninstall needed.",
      "difficulty": "Easy"
    }
  ],

  "B_01_oop": [
    {
      "q": "__init__ return value?",
      "a": "None",
      "options": ["object", "None", "int", "str"],
      "reason": "constructor rule.",
      "explanation": "__init__ must not return value.",
      "difficulty": "Easy"
    },
    {
      "q": "__str__ missing return causes?",
      "a": "TypeError",
      "options": ["None", "TypeError", "AttributeError", "Silent fail"],
      "reason": "must return string.",
      "explanation": "Python expects string return.",
      "difficulty": "Medium"
    },
    {
      "q": "private variable access method?",
      "a": "_ClassName__var",
      "options": ["obj.var", "__var", "_ClassName__var", "obj->var"],
      "reason": "name mangling.",
      "explanation": "Python hides private vars via mangling.",
      "difficulty": "Hard"
    },
    {
      "q": "polymorphism example?",
      "a": "same method different behavior",
      "options": [
        "same method different behavior",
        "only inheritance",
        "only constructors",
        "only private vars"
      ],
      "reason": "runtime override.",
      "explanation": "Method overriding defines polymorphism.",
      "difficulty": "Medium"
    }
  ],

  "C_01_file_handling": [
    {
      "q": "open('file.txt','r') missing file?",
      "a": "FileNotFoundError",
      "options": ["None", "FileNotFoundError", "ValueError", "Empty file"],
      "reason": "read mode requires file.",
      "explanation": "r mode doesn't create file.",
      "difficulty": "Easy"
    },
    {
      "q": "'w' mode behavior?",
      "a": "truncate file",
      "options": ["append", "truncate file", "read only", "encrypt"],
      "reason": "clears content.",
      "explanation": "w overwrites file.",
      "difficulty": "Easy"
    },
    {
      "q": "with open(...) behavior after block?",
      "a": "file closed",
      "options": ["open", "deleted", "closed", "locked"],
      "reason": "context manager.",
      "explanation": "auto close file.",
      "difficulty": "Easy"
    },
    {
      "q": "binary read in text mode causes?",
      "a": "UnicodeDecodeError",
      "options": ["TypeError", "UnicodeDecodeError", "ValueError", "IndexError"],
      "reason": "invalid encoding.",
      "explanation": "binary != text encoding.",
      "difficulty": "Medium"
    }
  ]
}





   
  
    

















