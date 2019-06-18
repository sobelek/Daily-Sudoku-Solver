# Daily-Sudoku-Solver
Program that takes a screenshot of a running game of messenger daily sudoku and solves it

# To use
You need to have a 3000x2000 display and open chrome tab with messenger sudoku game run. Alt tab to consol and run
```python3 screen.py```

# Dependencies 
Opencv 3+
Tensorflow
pyscreenshot
pyautogui
PyQt5
numpy
pickle

# Solving algorithm
It uses brute force recusrive algotithm to solve sudoku

# OCR
It uses pretty basic machine learing model to recgognize characters on the board and then parses it to string that is feed into solver. Its pretty easy task so it is almost 100% correct, if you find it failing to recognise characters let me know 

# TODO
-Right now it only works for my display that is 3000x2000 and have hardcoded variables to find a sudoku board. It would be nice to find a board using cv2 and then do computations
-Clean up a solver a little bit and maybe do a better API for solving

# Feedback

I know this project isnt the best or the cleanest but it was just my oneday side project to win a leaderboard with friend but I am open to critique and feedback and would love to hear from you
