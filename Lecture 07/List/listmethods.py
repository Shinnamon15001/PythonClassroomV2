heroes1 = ["Ironman", "Thor", "Hulk","Superman", "Spiderman"]
heroes2 = ["Dr.Strange", "Cpt.America", "BlackPanther", "AntMan"]

heroes1.insert(0, heroes2[0])
print(heroes1.index("Thor"))
heroes1.insert(heroes1.index("Thor"))