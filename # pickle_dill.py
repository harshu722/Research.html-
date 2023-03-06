# pickle_dill.py  
import dill  
  
squaring = lambda x: x * x  
user_pickle = dill.dumps( squaring )  
print( user_pickle )  
