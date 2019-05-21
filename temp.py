# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import gmpy2 
import time 


def get_gpq(): 
    randnum = gmpy2.random_state(int(1000 * time.time())) 
    
    Len_p=1024 
    Len_q=256 
    Len_t=768 
    
    p=4 
    
    q=gmpy2.mpz_urandomb(randnum, Len_q) 
    q=gmpy2.next_prime(q) 
    while not gmpy2.is_prime(p): 
        t=gmpy2.mpz_urandomb(randnum, Len_t) 
        p=t*q+1 
        
        g = 1 
        while not g > 1: 
            r = gmpy2.mpz_urandomb(randnum, Len_p) 
            g = gmpy2.powmod(r, t, p) 
    
    f = open('gpq.txt', 'w') 
    print('g = ', g) 
    print('p = ', p) 
    print('q = ', q) 
    f.write('g = '+ str(g)+'\n') 
    f.write('p = '+ str(p)+'\n') 
    f.write('q = '+ str(q)) 
    f.close() 

get_gpq()