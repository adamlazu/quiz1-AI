import pandas as pd

dataset = pd.read_csv("./leaf.csv")


def addData(leaf_width=None,leaf_length=None, leaf_thickness=None):
    if leaf_width == None:
        leaf_width = dataset["Leaf Width"].mean()
    elif leaf_length == None:
        leaf_length = dataset["Leaf Length"].mean()


    area = leaf_length*leaf_width
    #determine the biggest value of leaf area that belongs to small-leaf category
    biggest_small_leaf  = max(dataset["Leaf Width"][dataset["Species"]=="small-leaf"]*dataset["Leaf Length"][dataset["Species"]=="small-leaf"])
    #determine the smallest value of leaf area that belongs to big-leaf category
    smallest_big_leaf = min(dataset["Leaf Width"][dataset["Species"]=="big-leaf"]*dataset["Leaf Length"][dataset["Species"]=="big-leaf"])
    #the parameter is defined by the middle value of 2 earlier variables
    parameter = (smallest_big_leaf + biggest_small_leaf)/2

    if leaf_thickness is None:
        if area < parameter:
            data = {"Leaf Width":leaf_width, "Leaf Length":leaf_length, "Leaf Thickness":0.0, "Species":"small-leaf"}
            dataset.loc[len(dataset)] = data
        else:
            data = {"Leaf Width":leaf_width, "Leaf Length":leaf_length, "Leaf Thickness":0.0,"Species":"big-leaf"}
            dataset.loc[len(dataset)] = data

    if leaf_thickness is not None:
        try:
            thick = dataset["Leaf Thickness"]
            if area < parameter:
                if leaf_thickness > 0.5:
                    data = {"Leaf Width":leaf_width, "Leaf Length":leaf_length, "Leaf Thickness":leaf_thickness, "Species":"small-thick-leaf"}
                    dataset.loc[len(dataset)] = data
                    
                else:
                    data = {"Leaf Width":leaf_width, "Leaf Length":leaf_length, "Leaf Thickness":leaf_thickness, "Species":"small-thin-leaf"}
                    dataset.loc[len(dataset)] = data
                    
            else:
                if leaf_thickness > 0.5:
                    data = {"Leaf Width":leaf_width, "Leaf Length":leaf_length, "Leaf Thickness":leaf_thickness, "Species":"big-thick-leaf"}
                    dataset.loc[len(dataset)] = data
                    
                else:
                    data = {"Leaf Width":leaf_width, "Leaf Length":leaf_length, "Leaf Thickness":leaf_thickness, "Species":"big-thin-leaf"}
                    dataset.loc[len(dataset)] = data
                    
        except:
            thickness = [0] * (len(dataset))
            dataset["Leaf Thickness"] = thickness
            if area < parameter:
                if leaf_thickness > 0.5:
                    data = {"Leaf Width":leaf_width, "Leaf Length":leaf_length, "Leaf Thickness":leaf_thickness, "Species":"small-thick-leaf"}
                    dataset.loc[len(dataset)] = data
                    
                else:
                    data = {"Leaf Width":leaf_width, "Leaf Length":leaf_length, "Leaf Thickness":leaf_thickness, "Species":"small-thin-leaf"}
                    dataset.loc[len(dataset)] = data
                    
            else:
                if leaf_thickness > 0.5:
                    data = {"Leaf Width":leaf_width, "Leaf Length":leaf_length, "Leaf Thickness":leaf_thickness, "Species":"big-thick-leaf"}
                    dataset.loc[len(dataset)] = data
                    
                else:
                    data = {"Leaf Width":leaf_width, "Leaf Length":leaf_length, "Leaf Thickness":leaf_thickness, "Species":"big-thin-leaf"}
                    dataset.loc[len(dataset)] = data
                    



    


def main():
    token = int(input("Welcome!\n press 1 to input data\n press 2 to observe current data\n press 3 to save data\n press 0 to end program\n"))
    while token != 0:
        if token == 1:
            length = input("length (click enter if you want to leave it blank): ")
            width = input("width (click enter if you want to leave it blank): ")
            thickness = input("thickness (click enter if you want to leave it blank): ")
            if thickness == "":
                if width == "" and length =="":
                    length = None
                    width = None
                    addData(width,length)
                elif width == "":
                    width = None
                    addData(width,float(length))
                elif length =="":
                    length = None
                    addData(float(width),length) 
                else:
                    addData(float(width),float(length))
            else:
                if width == "" and length =="":
                    length = None
                    width = None
                    addData(width,length,float(thickness))
                elif width == "":
                    width = None
                    addData(width,float(length),float(thickness))
                elif length =="":
                    length = None
                    addData(float(width),length,float(thickness)) 
                else:
                    addData(float(width),float(length),float(thickness))
        if token == 2:
            print(dataset)
        if token == 3:
            dataset.to_csv("./leaf.csv", index=False)
        token = int(input("\n press 1 to input data\n press 2 to observe current data\n press 3 to save data\n press 0 to end program\n"))
        
            

main()
