print("Input: ")
budget = float(input())
floarkg = float(input())


coloredEggs = float(0)
cozonacsCount = 0

cozonacprice = (floarkg * 3 / 4) + floarkg + ((floarkg / 4 + floarkg) / 4)
budget = budget


while budget >= cozonacprice:
    cozonacsCount += 1
    budget = budget - cozonacprice
    coloredEggs += 3

    if cozonacsCount % 3 == 0:
        coloredEggs = coloredEggs - (cozonacsCount - 2)

# Output
print("You made " + str(cozonacsCount) + " cozonacs! Now you have " +
      str(coloredEggs) + " eggs and " + str(round(budget, 2)) +
      " BGN left.")
