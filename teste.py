def getFlags(args):
    return list(filter(lambda x: x[:2] == '--',args))

text = input()
args = text.replace('  ',' ').split(' ')


flags = getFlags(args)
group = dict()
for i , flag in enumerate(flags):
    start = args.index(flag)+1
    end = (len(args) + 1) if i == (len(flags)-1) else args.index(flags[i+1])
    collection = args[start:end]
    print(flag,collection)
    group[flag] = []
    group[flag] += collection

print(group)





