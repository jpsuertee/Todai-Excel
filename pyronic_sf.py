from app import *

#def getgraph(mytable):                                     -when integrating into function, make sure it works
df = pd.read_excel('PyronicSF-Test-run-MOPS.xlsx')
mytable = df.to_numpy() 

plt.xlabel('Wavelength [nm]')
plt.ylabel('[RFU]')

wavelen=[]              #consider a prebuilt array of the wavelength values
for val in mytable[65]:
    if (isinstance(val, str)):
        continue
    wavelen.append(val)

for row in range(66, 78):
    values=[]
    for col in range(1, len(mytable[row])):
        values.append(mytable[row][col])
    plt.plot(wavelen, values, '-o', label=mytable[row][0])
plt.legend()
plt.show()


