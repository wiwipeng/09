# -*- coding: utf-8 -*-

#1A2B game
import random
import streamlit as st

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#random.shuffle(items)
answer=''
a_count=0 # initial A count
b_count=0 # initial B count
#cofirm_input = st.button('輸入確認')
#if cofirm_input:
for i in range(4):
    answer+=str(items[i])
while(True):
    number=st.text_input('Enter the number: ')
    st.write(answer)
    if not number.isdigit(): 
        pass
    else:
        if number==answer:
            st.write('excellent you guess the correct number')
            random.shuffle(items)
            break
            cofirm_input = st.button('輸入確認')
            if cofirm_input:
                
        for i in range(4):
            for j in range(4):
                if i==j and number[i]==answer[j]:
                    a_count+=1
                elif number[i]==answer[j]:
                    b_count+=1
        st.write('{0}A{1}B'.format(a_count,b_count))
        a_count=0
        b_count=0
