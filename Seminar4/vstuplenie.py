st = "1  2 \t3 \n4"  # -> [1, 2, 3, 4]
sp = st.split()
print(sp)

st = "1234"
sp = list(st)
print(sp)

20:24
st = "1  2 \t3 \n4"  # -> [1, 2, 3, 4]
sp = st.split()
print(sp)

st1 = "-".join(sp)
print(st1)


a = "aassddd"
sl = {}
for i in a:
    sl[i] = sl.get(i, 0) + 1
    # if i not in sl:
    #     sl[i] = 1
    # else:
    #     sl[i] += 1
print(sl)

sl["g"] = 100
print(sl)
for key, value in sl.items():
    print(key, value)


sl = {"ABC": 1, ("A", "B", "C"): 4}

b = "a"
for k, v in sl.items():
    if b in k:
        print(v)
