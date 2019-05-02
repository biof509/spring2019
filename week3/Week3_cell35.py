# Let's combine boston and boston second floor
boston = pd.merge(boston, boston_second_floor, on="Id")
boston.head()