import re
dauysty = "aeiou"
dauyssyz = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (dauyssyz, dauysty, dauyssyz), input(), flags = re.I)
print('\n'.join(m or ['-1']))