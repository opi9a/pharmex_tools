# -*- coding: utf-8 -*-
'''Testing docstring in module.'''
# TOOLS FOR PROCESSING THE PHARMEX DATA


def read(in_file):
    '''Testing docstring in read.'''
    with open(in_file, "r") as f:
        lines = f.read().split("\n")
        # need to convert date header strings into time floats
    # this list comprehension ignores the first col (name),
    # puts in zero for any blanks and converts the original YYYYMM string 
    # to a float  (enumerate lets you index as you go)
    dates = [val if i == 0
                 else 0 if val == ""
                 else (float(val)//100) + (float(val)%100/12)
                 for i, val in enumerate(lines[0].split(","))
                 if i >0]
    
    products = []   
    sales = []
    
    for line in lines[1:]: # NB start at row 1, avoiding headings
        if line:           # need this because get a blank row at end     
            products.append(line.split(",")[0])
    # this list comp'n ignores the first col (name), puts in zero for blanks
    # and reads the rest in as floats.
    # NB does this for each line.  (Actually just ignores first col. anyway)
            cells = [float(0) if val == "" 
                     else float(val) 
                     for i, val in enumerate(line.split(",")) 
                     if i > 0]
            
            sales.append(cells)

    return dates, products, sales
#______________________________________________________________________________

def write_out(source, name, *args, **kwargs):
    filename = (name + "_" + "_".join(args) + ".csv")

    print("Writing " + filename 
          + " with rows argument = {}.".format(str('rows' in kwargs)))

    with open(filename, "w") as f:
# test if it's a vector or array
        if type(source[0]) == list:
            for i, row in enumerate(source):
                if kwargs:
                    f.write(kwargs['rows'][i] + ",")
                for cell in row:
                    f.write(str(cell)+",")
                f.write("\n")
        else:
            for cell in source:
                f.write(str(cell)+"\n")

#______________________________________________________________________________

def find_launch(sales):
    '''Taking a list as input, returns the index of the first non-zero element.
    If no non-zeroes found returns "no data"
    
    Works with tuples and pd.Series
    '''
    try:
        for i, val in enumerate(sales):
            if i == 0 and val > 0:
                return 0
            elif i > 0 and val > 0:
                return i + 1
    except:
        return "No data"

#______________________________________________________________________________

# First, a function to do this in a list of monthly sales values
def annualise(pcm):
    ann = []
    for i in range(0,len(pcm),12):
        s = sum(pcm[i:i+12])
        ann.append(s)
    return ann


#______________________________________________________________________________

# rebase sales for each product based on year of launch, to give profile
def remove_lead(sales):
    temp = []
    is_up = False
    for i in sales:
        if i > 0:
            temp.append(i)
            is_up = True
        elif is_up:
            temp.append(i)
    return temp


#_________TESTING STUFF________________________________________________________


'''
test_sales = [0,0,0.1,0]
test_sales.extend(list(range(8)))

print(find_launch(test_sales))
    
test_mat = []
for i in range(10):
    temp = []    
    for j in range(61):
        temp.append(i)
    test_mat.append(temp)

test_pa = []
for row in test_mat:
    test_pa.append(annualise(row))

test_ann = [1]*121
print(sum(test_ann))
print(annualise(test_ann))
print(sum(annualise(test_ann)))

test_arr = []
for i in range(5):
   row = []
   for j in range(5):    
       row.append(j + (i*5))
   test_arr.append(row)
    
'''