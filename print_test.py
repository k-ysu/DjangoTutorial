#!/usr/bin/env python

#age=12
#name="Matt"
#todayIsCold=True

def hello(name="Sean", age=0):
    return "Hello {}. You are {} years old old".format(name,age)

sentence = hello("Matt", 20)
print(sentence)
