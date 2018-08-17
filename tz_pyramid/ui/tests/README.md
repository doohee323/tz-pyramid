Usage of Pytest
==========================================================================

# Setup
```
    pip3 install pytest
    pip3 install mock
    pip3 install requests
    
    or 
    
    vi requirements.txt
    mock == 2.0.0
    pytest == 3.7.1
    requests == 2.19.1
    
    pip3 install --upgrade -r requirements.txt
```

# How to run
```
    cd ~/tests
    
    pytest -vs

    pytest -vs tests

    pytest -vs tests/test_setup1.py
    
    pytest -vs tests -k "test3 or test4"
    
    pytest -vs tests -m "test41"
    
    pytest -vs tests --ignore tests/folder1

    pytest -vs tests --maxfail 1

```

# Plugins
```
    - pytest-repeat
        https://pypi.org/project/pytest-repeat/
    
    - pytest-random-order
        https://pypi.org/project/pytest-random-order/
    
    - pytest-cov
        https://pypi.org/project/pytest-cov/
        
        pip3 install pytest-cov
    
        pytest tests --cov-report html --cov=tests --cov-branch
        # pytest -vs --fixtures tests/unittest01
        
        open -n -a "Google Chrome" --args "--new-window" `pwd`/htmlcov/index.html 
    
    - get 10 slow testcases 
        pytest --durations=10
    
```
