def myfirst_yoursecond(p,q):
    
    p_end=p.find(" ")
    q_start=q.find(" ")
    if p[:p_end] == q[q_start+1:]:
        return True
    else:
        return False

print (myfirst_yoursecond("bell hooks", "curer bell"))
