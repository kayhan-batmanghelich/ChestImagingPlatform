import inspect
import CppHeaderParser
import os.path as path
import csv
from collections import OrderedDict

class Enum(object):
    @classmethod
    def elems_as_list(cls):
        """ Get a list of tuples (string, int) with all the elements
        Returns
        -------
        List of tuples (string, int)
        """
        return [i for i in inspect.getmembers(cls) if isinstance(i[1], int)]

    @classmethod
    def elems_as_dictionary(cls, key_is_integer=True):
        """  Return a dictionary with all the elems in the enum class
        Parameters
        ----------
        key_is_integer: if True, the key of the dictionary is the integer value. Otherwise, the key will be the string representation

        Examples
        -------
        ChestRegion.get_elems(key_is_integer=True) = {0:'UNDEFINEDREGION', 1:'WHOLELUNG', ... }
        ChestRegion.get_elems(key_is_integer=False) = {'UNDEFINEDREGION':0, 'WHOLELUNG':1, ... }

        Returns
        -------
        Dictionary with the values (see examples)
        """
        # Get just the "enum" elements of the class
        all_members = cls.elems_as_list()

        if key_is_integer:
            # dictionary int->string
            key = 1
            value = 0
        else:
            # dictionary string->int
            key = 0
            value = 1

        result = {}
        for elem in all_members:
            result[elem[key]] = elem[value]
        return result

    @classmethod
    def number_of_elems(cls):
        """ Get the total number of element in the class
        Returns
        -------
        int
        """
        return len(cls.elems_as_list())


#############################
# ENUMERATIONS
#############################
class ChestRegion(Enum):
    UNDEFINEDREGION = 0
    WHOLELUNG = 1
    RIGHTLUNG = 2
    LEFTLUNG = 3
    RIGHTSUPERIORLOBE = 4
    RIGHTMIDDLELOBE = 5
    RIGHTINFERIORLOBE = 6
    LEFTSUPERIORLOBE = 7
    LEFTINFERIORLOBE = 8
    LEFTUPPERTHIRD = 9
    LEFTMIDDLETHIRD = 10
    LEFTLOWERTHIRD = 11
    RIGHTUPPERTHIRD = 12
    RIGHTMIDDLETHIRD = 13
    RIGHTLOWERTHIRD = 14
    MEDIASTINUM = 15
    WHOLEHEART = 16
    AORTA = 17
    PULMONARYARTERY = 18
    PULMONARYVEIN = 19
    UPPERTHIRD = 20
    MIDDLETHIRD = 21
    LOWERTHIRD = 22
    LEFT = 23
    RIGHT = 24
    LIVER = 25
    SPLEEN = 26
    ABDOMEN = 27
    PARAVERTEBRAL = 28
    OUTSIDELUNG = 29
    OUTSIDEBODY = 30
    SKELETON = 31
    STERNUM = 32
    HUMERI = 33
    LEFTHUMERUS = 34
    RIGHTHUMERUS = 35
    SCAPULAE = 36
    LEFTSCAPULA = 37
    RIGHTSCAPULA = 38
    HILA = 39
    LEFTHILUM = 40
    RIGHTHILUM = 41
    KIDNEYS = 42
    LEFTKIDNEY = 43
    RIGHTKIDNEY = 44
    ASCENDINGAORTA = 45
    TRANSVERSALAORTA = 46
    DESCENDINGAORTA = 47
    LEFTSUBCLAVIAN = 48
    RIGHTSUBCLAVIAN = 49
    LEFTCORONARYARTERY = 50
    SPINE = 51
    LEFTVENTRICLE = 52
    RIGHTVENTRICLE = 53
    LEFTATRIUM = 54
    RIGHTATRIUM = 55
    LEFTPECTORALIS = 56
    RIGHTPECTORALIS = 57
    TRACHEA2 = 58
    LEFTMAINBRONCHUS = 59
    RIGHTMAINBRONCHUS = 60
    ESOPHAGUS = 61
    LEFTCHESTWALL = 62
    RIGHTCHESTWALL = 63
    LEFTDIAPHRAGM = 64
    RIGHTDIAPHRAGM = 65
    HIATUS = 66
    PECTORALIS = 67
    SPINALCORD = 68

class ChestType(Enum):
    UNDEFINEDTYPE = 0
    NORMALPARENCHYMA = 1
    AIRWAY = 2
    VESSEL = 3
    EMPHYSEMATOUS = 4
    GROUNDGLASS = 5
    RETICULAR = 6
    NODULAR = 7
    OBLIQUEFISSURE = 8
    HORIZONTALFISSURE = 9
    MILDPARASEPTALEMPHYSEMA = 10
    MODERATEPARASEPTALEMPHYSEMA = 11
    SEVEREPARASEPTALEMPHYSEMA = 12
    MILDBULLA = 13
    MODERATEBULLA = 14
    SEVEREBULLA = 15
    MILDCENTRILOBULAREMPHYSEMA = 16
    MODERATECENTRILOBULAREMPHYSEMA = 17
    SEVERECENTRILOBULAREMPHYSEMA = 18
    MILDPANLOBULAREMPHYSEMA = 19
    MODERATEPANLOBULAREMPHYSEMA = 20
    SEVEREPANLOBULAREMPHYSEMA = 21
    AIRWAYWALLTHICKENING = 22
    AIRWAYCYLINDRICALDILATION = 23
    VARICOSEBRONCHIECTASIS = 24
    CYSTICBRONCHIECTASIS = 25
    CENTRILOBULARNODULE = 26
    MOSAICING = 27
    EXPIRATORYMALACIA = 28
    SABERSHEATH = 29
    OUTPOUCHING = 30
    MUCOIDMATERIAL = 31
    PATCHYGASTRAPPING = 32
    DIFFUSEGASTRAPPING = 33
    LINEARSCAR = 34
    CYST = 35
    ATELECTASIS = 36
    HONEYCOMBING = 37
    TRACHEA = 38
    MAINBRONCHUS = 39
    UPPERLOBEBRONCHUS = 40
    AIRWAYGENERATION3 = 41
    AIRWAYGENERATION4 = 42
    AIRWAYGENERATION5 = 43
    AIRWAYGENERATION6 = 44
    AIRWAYGENERATION7 = 45
    AIRWAYGENERATION8 = 46
    AIRWAYGENERATION9 = 47
    AIRWAYGENERATION10 = 48
    CALCIFICATION = 49
    ARTERY = 50
    VEIN = 51
    PECTORALISMINOR = 52
    PECTORALISMAJOR = 53
    ANTERIORSCALENE = 54
    FISSURE = 55
    VESSELGENERATION0 = 56
    VESSELGENERATION1 = 57
    VESSELGENERATION2 = 58
    VESSELGENERATION3 = 59
    VESSELGENERATION4 = 60
    VESSELGENERATION5 = 61
    VESSELGENERATION6 = 62
    VESSELGENERATION7 = 63
    VESSELGENERATION8 = 64
    VESSELGENERATION9 = 65
    VESSELGENERATION10 = 66
    PARASEPTALEMPHYSEMA = 67
    CENTRILOBULAREMPHYSEMA = 68
    PANLOBULAREMPHYSEMA = 69
    SUBCUTANEOUSFAT = 70
    VISCERALFAT = 71
    INTERMEDIATEBRONCHUS = 72
    LOWERLOBEBRONCHUS = 73
    SUPERIORDIVISIONBRONCHUS = 74
    LINGULARBRONCHUS = 75
    MIDDLELOBEBRONCHUS = 76
    BRONCHIECTATICAIRWAY = 77
    NONBRONCHIECTATICAIRWAY = 78
    AMBIGUOUSBRONCHIECTATICAIRWAY = 79
    MUSCLE = 80
    HERNIA = 81
    BONEMARROW = 82
    BONE = 83
    INTERSTITIALLUNGDISEASE = 84
    SUBPLEURALLINE = 85
    NODULE = 86
    BENIGNNODULE = 87
    MALIGNANTNODULE = 88
    SEPTUM = 89

class ImageFeature(Enum):
  UNDEFINEDFEATURE = 0
  CTARTIFACT = 1
  CTBEAMHARDENING = 2
  CTSTREAKARTIFACT = 3
  CTMOTION = 4
  CTCARDIACMOTION = 5
  CTBREATHINGMOTION = 6

class ReturnCode(Enum):
  EXITSUCCESS = 0
  HELP = 1
  EXITFAILURE = 2
  RESAMPLEFAILURE = 3
  NRRDREADFAILURE = 4
  NRRDWRITEFAILURE = 5
  DICOMREADFAILURE = 6
  ATLASREADFAILURE = 7
  LABELMAPWRITEFAILURE = 8
  LABELMAPREADFAILURE = 9
  ARGUMENTPARSINGERROR = 10
  ATLASREGISTRATIONFAILURE = 11
  QUALITYCONTROLIMAGEWRITEFAILURE = 12
  INSUFFICIENTDATAFAILURE = 13
  GENERATEDISTANCEMAPFAILURE = 14

class ChestConventionsInitializer(object):
    #root_folder = "/Users/jonieva/Projects/CIP/Resources/ChestConventions/"
    root_folder = path.realpath(path.join(path.dirname(__file__), "..", "Resources", "ChestConventions"))
    __chest_regions__ = None
    __chest_types__ = None
    __image_features__ = None
    __chest_regions_hierarchy__ = None
    __preconfigured_colors__ = None
    __body_composition_phenotypes__ = None


    @staticmethod
    def __loadCSV__(file_name):
        """ Return a "list of lists of strings" with all the rows read from a csv file
        Parameters
        ----------
        file_name: name of the file (including the extension). The full path will be concatenated with Root_Folder

        Returns
        -------
        Lists of lists (every row of the csv file will be a list of strings
        """
        if not path.isdir(ChestConventionsInitializer.root_folder):
            raise AttributeError("The directory where all the csv files should be saved has not been found ({0})".
                                 format(ChestConventionsInitializer.root_folder))

        csv_file_path = path.join(ChestConventionsInitializer.root_folder, file_name)
        if not path.exists(csv_file_path):
            raise NameError("File {0} not found".format(csv_file_path))
        with open(csv_file_path, 'rb') as f:
            reader = csv.reader(f)
            # Return the concatenation of all the rows in a list
            return [row for row in reader]

    @staticmethod
    def chest_regions():
        if ChestConventionsInitializer.__chest_regions__ is None:
            ChestConventionsInitializer.__chest_regions__ = OrderedDict()
            rows = ChestConventionsInitializer.__loadCSV__("ChestRegions.csv")
            chest_regions_enum = ChestRegion.elems_as_dictionary()
            for row in rows:
                elem_id = int(row[0])
                if not chest_regions_enum.has_key(elem_id):
                    raise AttributeError("The key {0} in the ChestRegions csv file does not belong to the enumeration"
                                         .format(elem_id))
                ChestConventionsInitializer.__chest_regions__[elem_id] = (
                    row[1].strip(),     # Description
                    float(row[2]),      # Color (R)
                    float(row[3]),      # Color (G)
                    float(row[4])       # Color (B)
                )
            # Validate the

        return ChestConventionsInitializer.__chest_regions__

    @staticmethod
    def chest_regions_hierarchy():
        if ChestConventionsInitializer.__chest_regions_hierarchy__ is None:
            ChestConventionsInitializer.__chest_regions_hierarchy__ = []
            rows = ChestConventionsInitializer.__loadCSV__("ChestRegionsHierarchy.csv")
            chest_regions_enum = ChestRegion.elems_as_dictionary()
            for row in rows:
                parent_id = eval("ChestRegion." + row[0].strip())
                child_id = eval("ChestRegion." + row[1].strip())
                if not chest_regions_enum.has_key(parent_id):
                    raise AttributeError("The key {0} in the ChestRegionsHierarchy csv file does not belong to the enumeration"
                                         .format(parent_id))
                if not chest_regions_enum.has_key(child_id):
                    raise AttributeError("The key {0} in the ChestRegionsHierarchy csv file does not belong to the enumeration"
                                         .format(child_id))

                ChestConventionsInitializer.__chest_regions_hierarchy__.append([
                    parent_id,        # Parent Id
                    child_id,         # Child Id
                ])
        return ChestConventionsInitializer.__chest_regions_hierarchy__

    @staticmethod
    def chest_types():
        if ChestConventionsInitializer.__chest_types__ is None:
            ChestConventionsInitializer.__chest_types__ = OrderedDict()
            rows = ChestConventionsInitializer.__loadCSV__("ChestTypes.csv")
            chest_types_enum = ChestType.elems_as_dictionary()
            for row in rows:
                elem_id = int(row[0])
                if not chest_types_enum.has_key(elem_id):
                    raise AttributeError("The key {0} in the ChestTypes.csv file does not belong to the enumeration"
                                         .format(elem_id))
                ChestConventionsInitializer.__chest_types__[elem_id] = (
                    row[1].strip(),     # Description
                    float(row[2]),      # Color (R)
                    float(row[3]),      # Color (G)
                    float(row[4])       # Color (B)
                )
        return ChestConventionsInitializer.__chest_types__

    @staticmethod
    def image_features():
        if ChestConventionsInitializer.__image_features__ is None:
            ChestConventionsInitializer.__image_features__ = OrderedDict()
            rows = ChestConventionsInitializer.__loadCSV__("ImageFeatures.csv")
            image_features_enum = ImageFeature.elems_as_dictionary()
            for row in rows:
                elem_id = int(row[0].strip())
                if not image_features_enum.has_key(elem_id):
                    raise AttributeError("The key {0} in the ImageFeatures.csv file does not belong to the enumeration"
                                         .format(elem_id))
                ChestConventionsInitializer.__image_features__[elem_id] = (row[1].strip())
        return ChestConventionsInitializer.__image_features__

    @staticmethod
    def preconfigured_colors():
        if ChestConventionsInitializer.__preconfigured_colors__ is None:
            ChestConventionsInitializer.__preconfigured_colors__ = OrderedDict()
            rows = ChestConventionsInitializer.__loadCSV__("PreconfiguredColors.csv")
            for row in rows:
                region = eval('ChestRegion.' + row[0].strip())
                _type = eval('ChestType.' + row[1].strip())
                ChestConventionsInitializer.__preconfigured_colors__[(region, _type)] = \
                    (float(row[2].strip()), float(row[3].strip()), float(row[4].strip()))
        return ChestConventionsInitializer.__preconfigured_colors__

    @staticmethod
    def body_composition_phenotypes():
        if ChestConventionsInitializer.__body_composition_phenotypes__ is None:
            ChestConventionsInitializer.__body_composition_phenotypes__ = \
                [row[0] for row in ChestConventionsInitializer.__loadCSV__("BodyCompositionPhenotypes.csv")]

        return ChestConventionsInitializer.__body_composition_phenotypes__

#############################
# CHEST CONVENTIONS
#############################
class ChestConventions(object):
    ChestRegions = ChestConventionsInitializer.chest_regions()      # 1, WholeLung, 0.42, 0.38, 0.75
    ChestRegionsHierarchy = ChestConventionsInitializer.chest_regions_hierarchy()     # LEFTSUPERIORLOBE, LEFTLUNG
    ChestTypes = ChestConventionsInitializer.chest_types()          # 1, NormalParenchyma, 0.99, 0.99, 0.99
    ImageFeatures = ChestConventionsInitializer.image_features()    # 1, CTArtifact
    PreconfiguredColors = ChestConventionsInitializer.preconfigured_colors()

    BodyCompositionPhenotypes = ChestConventionsInitializer.body_composition_phenotypes()   # List of strings

    @staticmethod
    def GetNumberOfEnumeratedChestRegions():
        return len(ChestConventions.ChestRegions)

    @staticmethod
    def GetNumberOfEnumeratedChestTypes():
        return len(ChestConventions.ChestTypes)

    @staticmethod
    def GetNumberOfEnumeratedImageFeatures():
        return len(ChestConventions.ImageFeatures)

    @staticmethod
    def CheckSubordinateSuperiorChestRegionRelationship(subordinate, superior):
        if subordinate == superior:
            return True

        if ChestRegion.UNDEFINEDREGION in (subordinate, superior):
            return False

        for item in ChestConventions.ChestRegionsHierarchy:
            if item[0] == subordinate and item[1] == superior:
                return True

        return False

    @staticmethod
    def GetChestRegionFromValue(value):
        return value >> 8   # Most significant byte

    @staticmethod
    def GetChestTypeFromColor(color):
        for key, value in ChestConventions.ChestTypes.iteritems():
            if value[1] == color[0] and value[2] == color[1] and value[3] == color[2]:
                return key
        # Not found
        return ChestType.UNDEFINEDTYPE

    @staticmethod
    def GetChestRegionFromColor(color):
        for key, value in ChestConventions.ChestRegions.iteritems():
            if value[1] == color[0] and value[2] == color[1] and value[3] == color[2]:
                return key
        # Not found
        return ChestRegion.UNDEFINEDREGION

    @staticmethod
    def GetChestTypeFromValue(value):
        return 255 & value      # Less significant byte

    @staticmethod
    def GetChestWildCardName():
        # TODO: review this
        return "WildCard"

    @staticmethod
    def GetChestTypeName(whichType):
        if not ChestConventions.ChestTypes.has_key(whichType):
            raise IndexError("Key {0} is not a valid ChestType".format(whichType))
        return ChestConventions.ChestTypes[whichType][0]

    @staticmethod
    def GetChestTypeColor(whichType, color=None):
        """ Get the color for a ChestType.
        If color has some value, it will suppose to be a list where the color will be stored (just for compatibility purposes).
        In any case, the color will be returned as the result of the function
        Parameters
        ----------
        whichType
        color

        Returns
        -------
        3-Tuple with the color

        """
        if not ChestConventions.ChestTypes.has_key(whichType):
            raise IndexError("Key {0} is not a valid ChestType".format(whichType))
        col =  ChestConventions.ChestTypes[whichType][1:4]
        if color is not None:
            color[0] = col[0]
            color[1] = col[1]
            color[2] = col[2]
        return col


    @staticmethod
    def GetChestRegionColor(whichRegion, color=None):
        """ Get the color for a ChestRegion.
        If color has some value, it will suppose to be a list where the color will be stored (just for compatibility purposes).
        In any case, the color will be returned as the result of the function
        Parameters
        ----------
        whichRegion
        color

        Returns
        -------
        3-Tuple with the color
        """
        if not ChestConventions.ChestRegions.has_key(whichRegion):
            raise IndexError("Key {0} is not a valid ChestRegion".format(whichRegion))
        col =  ChestConventions.ChestRegions[whichRegion][1:4]
        if color is not None:
            color[0] = col[0]
            color[1] = col[1]
            color[2] = col[2]
        return col

    @staticmethod
    def GetColorFromChestRegionChestType(whichRegion, whichType, color=None):
        """ Get the color for a particular Region-Type.
        It can be preconfigured, a single region/type or the mean value.
        If color has some value, it will suppose to be a list where the color will be stored (just for compatibility purposes).
        In any case, the color will be returned as the result of the function
        Parameters
        ----------
        whichRegion
        whichType
        color

        Returns
        -------
        3-Tuple with the color
        """
        # TODO: override color in preconfigured combination (csv file)
        # Check first if the combination is preconfigured
        if ChestConventions.PreconfiguredColors.has_key((whichRegion, whichType)):
            col = ChestConventions.PreconfiguredColors[(whichRegion, whichType)]
        elif whichRegion == ChestRegion.UNDEFINEDREGION:
            col = ChestConventions.GetChestTypeColor(whichType)
        elif whichType == ChestType.UNDEFINEDTYPE:
            col = ChestConventions.GetChestRegionColor(whichRegion)
        else:
            reg_color = ChestConventions.GetChestRegionColor(whichRegion)
            type_color = ChestConventions.GetChestTypeColor(whichType)
            col = ((reg_color[0] + type_color[0]) / 2.0,
                   (reg_color[1] + type_color[1]) / 2.0,
                   (reg_color[2] + type_color[2]) / 2.0)

        if color is not None:
            color[0] = col[0]
            color[1] = col[1]
            color[2] = col[2]
        return col


    @staticmethod
    def GetChestRegionName(whichRegion):
        raise NotImplementedError()

    @staticmethod
    def GetChestRegionNameFromValue(value):
        raise NotImplementedError()

    @staticmethod
    def GetChestTypeNameFromValue(value):
        raise NotImplementedError()

    @staticmethod
    def GetValueFromChestRegionAndType(region, type):
        raise NotImplementedError()

    @staticmethod
    def GetChestRegionValueFromName(regionString):
        raise NotImplementedError()

    @staticmethod
    def GetChestTypeValueFromName(typeString):
        raise NotImplementedError()

    @staticmethod
    def GetChestRegion(i):
        raise NotImplementedError()

    @staticmethod
    def GetChestType(i):
        raise NotImplementedError()

    @staticmethod
    def GetImageFeature(i):
        raise NotImplementedError()

    @staticmethod
    def GetImageFeatureName(whichFeature):
        raise NotImplementedError()

    @staticmethod
    def IsBodyCompositionPhenotypeName(pheno):
        raise NotImplementedError()

    @staticmethod
    def IsParenchymaPhenotypeName(pheno):
        raise NotImplementedError()

    @staticmethod
    def IsHistogramPhenotypeName(pheno):
        raise NotImplementedError()

    @staticmethod
    def IsPulmonaryVasculaturePhenotypeName(pheno):
        raise NotImplementedError()

    @staticmethod
    def IsPhenotypeName(pheno):
        raise NotImplementedError()

    @staticmethod
    def IsChestType(chestType):
        raise NotImplementedError()

    @staticmethod
    def IsChestRegion(chestRegion):
        raise NotImplementedError()







#############################
# SANITY CHECKS
#############################
# def test_chest_conventions():
#    import CppHeaderParser     # Import here in order not to force the CppHeaderParser module to use ChestConventions (it's just needed for testing and it's not a standard module)

p = "/Users/jonieva/Projects/CIP/Common/cipChestConventions.h"
cppHeader = CppHeaderParser.CppHeader(p)
c_chest_conventions = cppHeader.classes["ChestConventions"]

def compare_c_python_enum(enum_name, c_enum, p_enum):
    """ Make sure that all the values in a C++ enumeration are the same in Python
    Parameters
    ----------
    enum_name: name of the enumeration
    c_enum: C++ enumeration
    p_enum: Python enumeration
    """
    for elem in c_enum:
        name = elem['name']
        int_value = elem['value']
        if not p_enum.has_key(int_value):
            raise Exception("Error in {0}: Key {1} was found in C++ object but not in Python".format(enum_name, int_value))
        if p_enum[int_value] != name:
            raise Exception("Error in {0}: {0}[{1}] (C++) = {2}, but {0}[{1}] (Python) = {3}".format(
                enum_name, int_value, name, p_enum[int_value]))

def compare_python_c_enum(enum_name, p_enum, c_enum):
    """ Make sure that all the values in a Python enumeration are the same in C++
    Parameters
    ----------
    enum_name: name of the enumeration
    p_enum: Python enumeration
    c_enum: C++ enumeration
    """
    for int_value, description in p_enum.iteritems():
        found = False
        for item in c_enum:
            if item['value'] == int_value:
                found = True
                if item['name'] != description:
                    raise Exception("Error in {0}. {0}[{1}} (Python) = {2}, but {0}[{1}] (C++) = {3}".format(
                        enum_name, int_value, description, item['name']))
                break
        if not found:
            raise Exception("Error in {0}. Elem '{1}' does not exist in C++".format(enum_name, description))

def compare_python_c_methods(p_methods, c_methods):
    """ Make sure all the python methods in ChestConventions are the same in Python that in C++
    Parameters
    ----------
    p_methods: Python methods
    c_methods: C++ methods
    """
    for p_method in p_methods:
        found = False
        p_name = p_method.func_name
        for c_method in c_methods:
            c_name = c_method["name"]
            if c_name == p_name:
                # Matching method found in C++. Check the parameters
                found = True
                p_args = p_method.func_code.co_varnames
                c_args = c_method["parameters"]
                if len(p_args) != len(c_args):
                    raise Exception ("Method '{0}' has {1} parameters in Python and {2} in C++".format(p_name,
                                                                                            len(p_args), len(c_args)))
                for i in range(len(p_args)):
                    if p_args[i] != c_args[i]["name"]:
                        raise Exception("The parameter number {0} in Python method '{1}' is '{2}', while in C++ it's '{3}'".
                                        format(i, p_name, p_args[i], c_args[i]["name"]))
                break
        if not found:
            raise Exception("Python method '{0}' was not found in C++".format(p_name))

def compare_c_python_methods(c_methods, p_methods):
    """ Make sure all the python methods in ChestConventions are the same in Python that in C++
    Parameters
    ----------
    c_methods: C++ methods
    p_methods: Python methods
    """
    for c_method in c_methods:
        if c_method["destructor"] or c_method["constructor"]:
            continue
        found = False
        c_name = c_method["name"]
        for p_method in p_methods:
            p_name = p_method.func_name
            if c_name == p_name:
                # Matching method found in Python. Check the parameters
                found = True
                c_args = c_method["parameters"]
                p_args = p_method.func_code.co_varnames
                if len(p_args) != len(c_args):
                    raise Exception ("Method '{0}' has {1} parameters in Python and {2} in C++".format(p_name,
                                                                                            len(p_args), len(c_args)))
                for i in range(len(p_args)):
                    if p_args[i] != c_args[i]["name"]:
                        raise Exception("The parameter number {0} in Python method '{1}' is '{2}', while in C++ it's '{3}'".
                                        format(i, p_name, p_args[i], c_args[i]["name"]))
                break
        if not found:
            raise Exception("C++ method '{0}' was not found in Python".format(c_name))

def total_checking():
    # Go through all the enumerations in C++ and make sure we have the same values in Python
    for i in range(len(cppHeader.enums)):
        c_enum = cppHeader.enums[i]["values"]
        enum_name = cppHeader.enums[i]['name']
        p_enum = eval("{0}.elems_as_dictionary()".format(enum_name))
        compare_c_python_enum(enum_name, c_enum, p_enum)
        compare_python_c_enum(enum_name, p_enum, c_enum)
        print(cppHeader.enums[i]['name'] + "...OK")

    # Make sure that all the methods in ChestConventions in C++ are implemented in Python and viceversa
    p_methods = [f[1] for f in inspect.getmembers(ChestConventions, inspect.isfunction)]
    c_methods = c_chest_conventions.get_all_methods()

    compare_c_python_methods(c_methods, p_methods)
    print("C++ --> Python checking...OK")

    compare_python_c_methods(p_methods, c_methods)
    print("Python --> C++ checking...OK")

print ChestConventions.GetChestTypeFromColor([0.47, 0.78, 0.45])


color = [0,0,0]
ChestConventions.GetChestTypeColor(1, color)