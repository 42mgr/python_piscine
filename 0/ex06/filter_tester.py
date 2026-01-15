from ft_filter import ft_filter

example_list = [
    "ananas",
    0,
    "apfel",
    float("nan"),
    False,
    "banane",
    "brombeere",
    "caki",
]

# example list comprehension
print(
    list(
        filter(
            lambda x: isinstance(x, str) and x.startswith("a"),
            example_list,
        )
    )
)
print(
    list(
        ft_filter(
            lambda x: isinstance(x, str) and x.startswith("a"), example_list
        )
    )
)
# length check (only on str with first check)
print(list(filter(lambda x: isinstance(x, str) and len(x) >= 6, example_list)))
print(
    list(ft_filter(lambda x: isinstance(x, str) and len(x) >= 6, example_list))
)
# Delete falsy from the list
print(list(filter(None, example_list)))
print(list(ft_filter(None, example_list)))
# Do nothing filter
print(list(filter(lambda x: True, example_list)))
print(list(ft_filter(lambda x: True, example_list)))
# print info
print(filter.__doc__)
print(ft_filter.__doc__)
