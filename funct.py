def roman(s):
    intToroman = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
                  50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
    lookup = [
            ["iv", 4],
            ["ix", 9],
            ["xl", 40],
            ["xc", 90],
            ["xd", 400],
            ["cm", 900],
            ["i", 1],
            ["v", 5],
            ["x", 10],
            ["l", 50],
            ["c", 100],
            ["m", 1000]]

    t = 0
    while s:
        found = False
        for l in lookup:
            if s.startswith(l[0]):
                t=t+l[1]
                s=s[len(l[0]):]
                found = True
                break
        if not found:
            return False
    return t

if __name__ == "__main__":
    print (roman('i'))
    print (roman('cmxcix'))
    print (roman('roman'))
