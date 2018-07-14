def singleMapping (description, item1, item2, dataframe=True):
    """get the single description of from item1 for item2 based on mapping"""
    #description = w
    #item1 = v
    #item2 = testData
    # used for the list data
    if dataframe:
        description = description.tolist()
        item1 = item1.tolist()
        item2 = item2.tolist()
    else:
        pass
    index = [None]*len(item2)
    result = [None]*len(item2)
    tt = [None]*len(item2)
    for i in range(len(item2)):
        if item2[i] in item1:
            index[i] = item1.index(item2[i])
            result[i] = description[index[i]]
        else:
            index[i] = None
            result[i] = None
    return result

def multiMapping (description, item1, item2, dataframe=True):
    import pandas as pd
    """get multiple description of from item1 for item2 based on mapping"""
    #description = w
    #item1 = v
    #item2 = testData
    #used for the list data
    if dataframe:
        description = description.tolist()
        item1 = item1.tolist()
        item2 = item2.tolist()
    else:
        pass
    result = [None]*len(item2)
    for i in range(len(item2)):
        if item2[i] in item1:
            index0 = [description[index] for index in range(len(item1)) if item1[index] == item2[i]]
            index1 = pd.unique(index0).tolist()
            result[i] = ';'.join(str(e) for e in index1) #string cat
        else:
            result[i] = None
    return result



"""split and combine"""
def splitAndCombine(gene, rxn, sep0, moveDuplicate=False):
    ##one rxn has several genes, this function was used to splite the genes
    ##used for the dataframe data
    import pandas as pd
    gene0 = gene.tolist()
    rxn0 = rxn.tolist()

    s1 = list()
    s2 = list()
    for i in range(len(gene0)):
       s1 = s1 + [rxn0[i]]*len(gene0[i].split(sep0))
       s2 = s2 + gene0[i].split(sep0)
    df0 = pd.DataFrame({'V1': s1,
                   'V2':s2}
                   )
    if moveDuplicate==True:
       df00 = df0.drop_duplicates()
    else:
       df00 = df0

    return df00


"""AutoUpdate"""
def AutoUpdate(description1, para1, description2, para2):

    # using the description1 in para1 to update the description2 in para2
    description1 = description1.tolist()
    para1 = para1.tolist()
    description2 = description2.tolist()
    para2 = para2.tolist()
    ss = [None]*len(para2)
    for i in range(len(para2)):
       if para2[i] in para1:
          ss[i] = para1.index(para2[i])
       else:
          ss[i] = None

    for i in range(len(para2)):
        if ss[i] != None:
            description2[i] = description1[ss[i]]
        else:
            description2[i] = description2[i]
    return description2


## description of function
## get the similar target for rxn_newGPR0 from rxn_yeast0
def getSimilarTarget(rxn_yeast0,rxn_newGPR0,ss):
    from fuzzywuzzy import fuzz
    from fuzzywuzzy import process
    rxn_yeast1 = np.array(rxn_yeast0)  # np.ndarray()
    rxn_yeast2 = rxn_yeast1.tolist()
    rxn_yeast3 = pd.Series((v[0] for v in rxn_yeast2))
    rxn_newGPR1 = np.array(rxn_newGPR0)  # np.ndarray()
    rxn_newGPR2 = rxn_newGPR1.tolist()
    rxn_newGPR3 = pd.Series((v[0] for v in rxn_newGPR2))
    similarTarget = [None] * ss
    for i in range(ss):
        similarTarget[i] = process.extract(rxn_newGPR3[i], rxn_yeast3, limit=2)

    return similarTarget


"""example
newMet = pd.read_excel('new metabolite for check.xlsx')
newMet0 = newMet[['name_unify']]


gemMet = pd.read_excel('unique metabolite in yeastGEM.xlsx')
gemMet0 = gemMet[['Description_simple']]

ss0 = len(newMet0)
similarTarget0 = getSimilarTarget(gemMet0,newMet0,ss=ss0)

newMet['target from yeastGEM'] = similarTarget0
writer = pd.ExcelWriter('new metabolite for check with target from yeastGEM.xlsx')
newMet.to_excel(writer,'Sheet1')
writer.save()"""