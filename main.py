import tkinter
import pythonping 
import matplotlib

def dataSlice(value):
    noSpaceValue = value.strip()
    value = ""
    for i in noSpaceValue:
        if i == "m" or i == "s":
            break
        else:
            value += i
    return float(value)


def pinging():
    
    testLabel["text"] = ""
    
    dataFull = pythonping.ping("google.com", verbose=True)
    dataValues = []
    for i in dataFull:
        dataValues.append(dataSlice(str(i)[-7:-2]))

    testLabel["text"] = dataValues
    
    root.after(1000, pinging)


root = tkinter.Tk()
root.title("Pyng")
testLabel = tkinter.Label(root)
testLabel.grid()
pinging()




root.mainloop()