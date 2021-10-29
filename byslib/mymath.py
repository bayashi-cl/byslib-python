# ax+by = gcd(a,b)
# def ext_gcd(a, b):
#     if b == 0:
#         return (1, 0)
#     q, r = divmod(a, b)
#     s, t = ext_gcd(b, r)
#     return (t, -q * t + s)


def ext_gcd(a, b):
    if b:
        d, y, x = ext_gcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0


def crt(a, b, mod1, mod2):
    g, k, _ = ext_gcd(mod1, mod2)
    if (b - a) % g != 0:
        return -1
    k *= (b - a) // g
    ans = mod1 * k + a
    lcm = mod1 * mod2 // g
    return ans % lcm


if __name__ == "__main__":
    print(crt(3, 5, 2, 3))
