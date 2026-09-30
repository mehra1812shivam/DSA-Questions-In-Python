def reverse_parenthesis(s):
    st=[]
    for ch in s:
        if ch==')':
            l=[]
            while st and st[-1]!='(':                    
                l.append(st.pop())
            st.pop()
            st=st+l
        else:
            st.append(ch)
    return "".join(st)
print(reverse_parenthesis("(ed(et(oc))el)"))