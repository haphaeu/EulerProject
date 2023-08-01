from math import sqrt
import tqdm

def brute():
    def is_perfect_square(n):
        sn = sqrt(n)
        if sn == int(sn):
            return True
        return False


    sum_half_perimeters = 0

    limit = int(200_000)

    # assuming a is always an odd integer ...
    # which makes b always an even integer
    #for a in tqdm.tqdm(range(3, limit, 2)):
    for a in range(3, limit, 2):
        for b in (a + 1, a - 1):
            s = a + b // 2  # b is even
            area_squared = s * (s - a) * (s - a) * (s - b)
            if is_perfect_square(area_squared):
                print(f'{a}\t{a}\t{b}')
                sum_half_perimeters += s


def cheat():
    """By running brute() and analysing the first numbers coming out of it,
    there are patterns in the sequence of a, a, b:
    
      - b alternates between a+1 and a-1
      
      - when b is a+1, a[n] = 14 * a[n-1] - a[n-2] - 4
      
      - when b is a-1, a[n] = 14 * a[n-1] - a[n-2] + 4

    Running up to a < 200_000:
      5       5       6
      17      17      16
      65      65      66
      241     241     240
      901     901     902
      3361    3361    3360
      12545   12545   12546
      46817   46817   46816
      174725  174725  174726
    """
    def per(_a, _b):
        return 2 * _a + _b

    ap_0 = 5
    ap_1 = 65
    am_0 = 17
    am_1 = 241

    sum_perimeters = per(ap_0, ap_0 + 1)
    sum_perimeters += per(ap_1, ap_1 + 1)
    sum_perimeters += per(am_0, am_0 - 1)
    sum_perimeters += per(am_1, am_1 - 1)

    while True:
        ap = 14 * ap_1 - ap_0 - 4
        perimeter = per(ap, ap + 1)
        if perimeter > 1e9:
            break
        sum_perimeters += perimeter

        am = 14 * am_1 - am_0 + 4
        perimeter = per(am, am - 1)
        if perimeter > 1e9:
            break
        sum_perimeters += perimeter

        ap_0 = ap_1
        ap_1 = ap
        am_0 = am_1
        am_1 = am
    print(sum_perimeters)

if __name__ == '__main__':
    brute()
    cheat()