import unittest

import app

def test_main():
    assert "HelloWorld:" in app.helloworld() 

def test_hello():
    assert "hello this is me" in app.hello()
    