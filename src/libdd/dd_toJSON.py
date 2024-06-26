# for creating default empty dictionary objects
from collections import defaultdict
import pdb

_missingRepresentation = 0
def missingRepresentation(msng = None):
    global _missingRepresentation
    if msng is not None:
        _missingRepresentation = msng
    return _missingRepresentation


def ddtoJSON(ddfile):
    """ Convert CSV to Dictionary/JSON Format
    Data dictionary as csv [read_csv(ddfile)] -> Data dictionary to JSON [ddtoJSON(ddfile)] -> 
    Data Dictionary clean null terms [cleanNullTerms(ddJSON)]

    input argument ddfile - the pandas representation of the data dictionary after loading it in 
    using read_csv()

    missingRepresentation - 0 is chosen as a placeholder for NA/None/null values imported in the
    data dictionary pandas object.
    
    """

    dictionaryObject = defaultdict(dict)

    ddfileReplaceMissing = ddfile.fillna(missingRepresentation())
    for i, row in ddfileReplaceMissing.iterrows():
        if row.allowed != 0:
            row.allowed = row.allowed.split(";")
        else:
            pass
            # row.allowed = []
        dictionaryObject[i] = row.to_dict()
    
    return dictionaryObject
