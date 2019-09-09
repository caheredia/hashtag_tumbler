foo = {"row_id": "stt", "value": 3, "qualifier": True}


def helper(row):
    items = ["row_id", "family", "qualifier", "value"]
    formatted = []
    for item in items:
        try:
            formatted.append(row[item].encode())
        except AttributeError:
            formatted.append(row[item])
        except KeyError:
            formatted.append(None)
    return formatted


row = helper(foo)
print(row)


def unpack_print(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


unpack_print(*row)
