# uncomment for testing with run_file.py
#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str
    
import pylab
import sys

REGION_LIST = ['far_west','great_lakes','mideast','new_england','plains','rocky_mountain','southeast','southwest','all']
VALUES_LIST = ['Pop', 'GDP', 'PI', 'Sub', 'CE', 'TPI', 'GDPp', 'PIp']

def file_opener():
    '''Attempts to open the file repeatedly till the user inputs a existing
    file. No parameters are given and no value is returned. A while loop is 
    put so that its repeatedly asked till its False.'''
    file = input("Enter the name of the file: ")
    while True: # loops through the function till a existing file is entered.
        try:
            file_open = open(file,'r') #tries to open a file with the name of
                                         # the input.
            return file_open # returns the contents of the file.
        except:
            file = input("Enter the name of the file: ") # asks the user
            # for a name of a existing file in the folder.
def file_reader(fp):
    #fp = file_opener()
    fp.readline()
    big_list = [] #initializes a big list 
    while True: # loops through till a valid file name is given
        region_input = input("Enter a region name: ")
        region_input = region_input.lower()
        if region_input in REGION_LIST:
            break
        else:
            print("Error.")
    print(" for the",region_input,"region:")
    big_list = []
    for line in fp:
        line_1st = line.strip().split(",") # removes whitespace 
        region = line_1st[1] # gives the region place 
        region = region.lower()
        GDP_capita = round(float(line_1st[3])/float(line_1st[2]) * 1000,2)
        Income_capita = round(float(line_1st[4])/float(line_1st[2]) * 1000,2)
        if region == region_input: # runs if the input = a valid name
            line_1st.append(GDP_capita) # appends the calculated GDP/capita 
            line_1st.append(Income_capita) # appends the calculated income/cap
            big_list.append(line_1st) # adds the line to the big list 
        if region_input == "all": # runs if the user inputs "all"
            line_1st.append(GDP_capita)
            line_1st.append(Income_capita)
            big_list.append(line_1st)
            
    return (big_list)

def MAX_GDP(big_list):
    max_GDP = 0.0 # initializes a really small value. 
    for state in big_list: # for every list in the big list 
        if state[8] > max_GDP: # targets the term with the GDP
            max_GDP = state[8] # refreshes the value
    return max_GDP

    
def MIN_GDP(big_list):
    min_GDP = 10000000000000000 # initializes a really long code 
    for state in big_list:
        if state[8] < min_GDP:
            min_GDP = state[8]
    return min_GDP

def max_income(big_list):
    max_income = 0.0
    for state in big_list:
        if state[9] > max_income:
            max_income = state[9]
    return max_income
    
def min_income(big_list):
    min_income = 100000000000000
    for state in big_list:
        if state[9] < min_income:
            min_income = state[9]
    return min_income

def maxGDP_printer(big_list):
    finished = MAX_GDP(big_list) # calls the MAX_GDP function.
    for x in big_list:
        if x[8] == finished:
            state = x[0]
    print(state,"has the highest GDP per capita at ${:,.2f}".format(finished))
    # uses .format to refresh the finished variable.
    
def minGDP_printer(big_list):
    finished = MIN_GDP(big_list)
    for x in big_list:
        if x[8] == finished:
            state = x[0] # refreshes the value
    print(state,"has the lowest GDP per capita at ${:,.2f}".format(finished))

def max_income_printer(big_list):
    finished = max_income(big_list)
    for x in big_list:
        if x[9] == finished:
            state = x[0] # refreshes the vaue 
    print(state,"has the max Income per capita at ${:,.2f}".format(finished))
def min_income_printer(big_list):
    finished = min_income(big_list)
    for x in big_list:
        if x[9] == finished:
            state = x[0] # refreshes the value
    print(state,"has the min Income per capita at ${:,.2f}".format(finished))
    
    
def table_maker(big_list):
    VALUES_NAMES = ['State','Population(m)','GDP(b)','Income(b)','Subsidies(m)','Compensation(b)','Taxes(b)','GDP per capita','Income per capita']
    print("{:14s} {:13s} {:>9s} {:>12s} {:>12s} {:>22s} {:>11s} {:>24s} {:>29s}".format(VALUES_NAMES[0],VALUES_NAMES[1],VALUES_NAMES[2],VALUES_NAMES[3],VALUES_NAMES[4],VALUES_NAMES[5],VALUES_NAMES[6],VALUES_NAMES[7],VALUES_NAMES[8]))
    # uses the format to space out the titles evenly.
    # each index 
    for x in big_list: # for every mini list in the big list 
        x[2] = float(x[2])
        x[3] = float(x[3])
        x[4] = float(x[4])
        x[5] = float(x[5])
        x[6] = float(x[6])
        x[7] = float(x[7])
        x[8] = float(x[8])
        print("{:14s}{:14.2f}{:>10.2f}{:>13.2f}{:>13.2f}{:>23.2f}{:>12.2f}{:>25,.2f}{:>30,.2f}".format(x[0],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]))
    
def plot_regression(x,y):
    '''Draws a regression line for values in lists x and y.
       x and y must be the same length.'''
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    m,b = pylab.polyfit(xarr,yarr, deg = 1) #creates line, only takes numpy arrays
    #as parameters
    pylab.plot(xarr,m*xarr + b, '-') #plotting the regression line
    


def plot(big_list):   # you need to replace pass with parameters
    '''Plot the values in the parameters.'''
    # placeholder
    VALUES_NAMES = ['State','Population(m)','GDP(b)','Income(b)','Subsidies(m)','Compensation(b)','Taxes(b)','GDP per capita','Income per capita']
    plot_input = input("Enter an x and y value:")
    #prompt for which values to plot; these will be the x and y
    reply = plot_input.split() 
    index_x = VALUES_LIST.index(reply[0]) + 2 
    index_y = VALUES_LIST.index(reply[1]) + 2 
    x_list = [] # initializes the list 
    y_list = []
    state_list = [] # initializes the list 
    for i in big_list: # for every region list in the big list 
        state_list.append(i[0]) # appends the 0th index 
        x_list.append(i[index_x])
        y_list.append(i[index_y])
    # build x, the list of x values
    # build y, the list of y values
    # hint: list comprehension is a slick way to build x and y

    # In the following you need to replace 'pass' with your own arguments
    # pylab.title(pass)   # plot title

    pylab.xlabel(VALUES_NAMES[index_x-2])   #label x axis
    pylab.ylabel(VALUES_NAMES[index_y-2])   #label y axis
    
    pylab.scatter(x_list,y_list)
    for i, txt in enumerate(state_list): 
        pylab.annotate(txt, (x_list[i],y_list[i]))
    
    plot_regression(x_list,y_list)
    
    # USE ONLY ONE OF THESE TWO
    pylab.show()                # displays the plot      
    #pylab.savefig("plot.png")   # saves the plot to file plot.png

def main():
    fp = file_opener() # opens the file 
    structure = file_reader(fp) # calls the function
    maxGDP_printer(structure) # prints the max GDP
    minGDP_printer(structure) # prints the min GDP
    print()
    max_income_printer(structure) # prints the max income 
    min_income_printer(structure) # prints the min income 
    print()
    table_maker(structure) # creates the table 
    t = 5
    while t:
        plot_question = input("Would you like to plot?") # prompts the question.
        plot_question = plot_question.lower() # lowercases the input 
        if plot_question == "no": # exits the system
            break
        if plot_question == "yes":
            plot(structure) # plots the graph if they answer yes 
            t = 0 
    fp.close()
        
main()
