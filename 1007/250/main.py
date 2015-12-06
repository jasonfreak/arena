class NamingConvention(object):
    def __init__(self):
        object.__init__(self)

    def toCamelCase(self, variableName):
        words = variableName.split('_')
        result = words[0]
        for word in words[1:]:
            result = result + word.title()
        return result

def main():
    obj = NamingConvention()
    print obj.toCamelCase('the_variable_name_can_be_very_long_like_this')

if __name__ == '__main__':
    main()


            
