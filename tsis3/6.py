s = input().split()
st = {'g'}
for x in s:
    st.add(x)
st.remove('g')
print(len(st))