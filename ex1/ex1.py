import unittest

def mkdict(k, v):
    rd = dict()
    k_len = len(k)
    v_len = len(v)
    for s in range(0, k_len):
        if s > v_len-1:
            rd[k[s]] = None
        else:
            rd[k[s]] = v[s] 
    return rd 

class test_mkdict(unittest.TestCase):
    def test_KLenLtVLen(self):
        lk = [ 1, 2, 3 ]
        lv = [ 'a', 'b','c', 'd' ]
        res = { 1: 'a',
            2: 'b',
            3: 'c'
        } 
        self.assertEqual(mkdict(lk,lv),res)

    def test_KLenEqVLen(self):
        lk = [ 1, 2, 3, 4 ]
        lv = [ 'a', 'b','c', 'd' ]
        res = { 1: 'a',
            2: 'b',
            3: 'c',
            4: 'd'
        } 
        self.assertEqual(mkdict(lk,lv),res)

    def test_KLenGtVLen(self):
        lk = [ 1, 2, 3, 4 ]
        lv = [ 'a', 'b','c' ]
        res = { 1: 'a',
            2: 'b',
            3: 'c',
            4: None
        } 
        self.assertEqual(mkdict(lk,lv),res)


if __name__ == "__main__":
   unittest.main()

'''
        lk = [ 1, 2, 3, 5, 6, 7, 8, 9 ]
        lv = [ 'a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o' ]
'''
