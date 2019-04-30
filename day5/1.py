with open('input.txt') as input:
    chars = [char for char in input.read()]

    should_continue = True

    while should_continue:
        for i in range(len(chars)-1):
            c_curr = chars[i]
            c_next = chars[i+1]
            if c_curr.lower() == c_next.lower() and c_curr != c_next:
                del chars[i]
                del chars[i]
                break
        else:
            should_continue = False

    result = len(chars)
    print(result)