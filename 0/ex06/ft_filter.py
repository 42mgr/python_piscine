def ft_filter(function, iterable):
    if function is None:
        # list comprehension 1
        return (item for item in iterable if item)

    # list comprehension 2
    return (item for item in iterable if function(item))


ft_filter.__doc__ = """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""

# import typing as t
#
# T = t.TypeVar("T")
#
#
# def ft_filter_type(
#     function: t.Optional[t.Callable[[T], t.Any]], iterable: t.Iterable[T]
# ) -> t.Iterator[T]:
#     if function is None:
#         return (item for item in iterable if item)
#     return (item for item in iterable if function(item))
