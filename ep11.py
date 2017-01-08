print "What do you create?",
product = raw_input()
print "What do you charge?",
price = int(raw_input())
print "What is your cost?",
cost = int(raw_input())

net_profit = (price - cost)

print "You make %r, it costs you %r and you charge %r. Your net profit is %r" % (product, cost, price, net_profit)
