def id_chaker(number):
    try:
        int(number)
    except ValueError:
        return 'You can send only number'
    x , data = 0, []
    if len(number) != 9:
        return 'is id sort or long type Id number Check'

    else:
        for i in number:
            x += 1
            if int(i) * x > 9:
                result = [int(i) * x, 0]
                for row in str(result[0]):
                    result[1] += int(row)
                data.append(str(result[1]))
            else:
                data.append(str(int(i) * x))
            if x == 2:
                x = 0
        if eval('+'.join(data)) % 10 == 0:
            return True
        else:
            return False