import sys
# Set path to script folder.
sys.path.append('/Scripts/')

# Import the whole script.
import module1

# Or import single function to maintain lean code.
from module2 import main

print(module1.main(1,3))
print(main(3,3))
