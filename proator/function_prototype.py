'''
Created on Nov 24, 2016

@author: Mohit.Thakur
'''
import sys
import traceback

__all__ = ['prototype', 'ovrprototype'] 

def __exceptionHandler__(got_exception_type, got_exception, got_traceback):
    listing  = traceback.format_exception(got_exception_type, got_exception, got_traceback)
    # Removing the listing of statement raise. 
    del listing[-2]
    filelist = ["org.python.pydev"]
    listing = [ item for item in listing if len([f for f in filelist if f in item]) == 0 ]
    files = [line for line in listing if line.startswith("  File")]
    if len(files) == 1:
        # only one file, remove the header.
        del listing[0]
    print>>sys.stderr, "".join(listing)
    sys.exit(1)
    
def prototype(*outer_args,**outer_kwargs):  
    """ Verify that a method is called with a valid data type value.
        The datatype of a parameter must be a one of the type 
        defined in types package. 
    """
    def decorator(fn):                                          
        def decorated(*args,**kwargs):                            
            #do_something(*outer_args,**outer_kwargs)
            if len(outer_args)!=len(args):
                sys.excepthook = __exceptionHandler__
                raise Exception("Invalid Number of "
                "arguments in function call")
            for [typ, var] in zip(outer_args, args):
                if ( isinstance(var, typ)):
                    pass
                else:
                    sys.excepthook = __exceptionHandler__
                    raise Exception("Invalid Type")
            return fn(*args,**kwargs)                         
        return decorated                                          
    return decorator

def ovrprototype(*outer_args,**outer_kwargs):  
    """ Verify that a method is called with a valid data type value.
        The datatype of a parameter must be a list of type defined 
        in package types. 
    """
    def decorator(fn):                                          
        def decorated(*args,**kwargs):                            
            #do_something(*outer_args,**outer_kwargs)
            if len(outer_args)!=len(args):
                sys.excepthook = __exceptionHandler__
                raise Exception("Invalid Number of "
                "arguments in function call")
            for [typ, var] in zip(outer_args, args):
                matched = False
                for i_typ in typ:
                    if ( isinstance(var, i_typ)):
                        matched = True
                        break
                if matched == False:
                    sys.excepthook = __exceptionHandler__
                    raise Exception("Invalid Type")
            return fn(*args,**kwargs)                         
        return decorated                                          
    return decorator 

