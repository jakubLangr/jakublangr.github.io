library(ggplot2)
library(ggmap)

filepath = "results-20140921-223252.csv"

read.csv(filepath,na.strings="null") -> data

data = data[data$Actor1Geo_Lat!=35,]
data = data[data$Actor2Geo_Lat!=35,]

colSums(is.na(data))/dim(data)[1]
map = get_map(location="Syria",zoom=7)
mapPoints <- ggmap(map) + geom_point(aes(x=Actor1Geo_Long,y=Actor1Geo_Lat,size=abs(GoldsteinScale)),data=data,alpha=.1,col="red") + geom_point(aes(x=Actor2Geo_Long,y=Actor2Geo_Lat,size=abs(GoldsteinScale)),data=data,alpha=.1,col="red")
mapPoints

data$MonthYear = as.factor(data$MonthYear)

for(i in levels(data$MonthYear)){
  print(i)
  subset = data[data$MonthYear==i,]
  mapPoints <- ggmap(map) + geom_point(aes(x=Actor1Geo_Long,y=Actor1Geo_Lat,size=abs(GoldsteinScale)),data=subset,alpha=.1,col="red") + geom_point(aes(x=Actor2Geo_Long,y=Actor2Geo_Lat,size=abs(GoldsteinScale)),data=subset,alpha=.1,col="red")
  mapPoints
  ggsave(as.character(paste(i,".png",sep="")))
}

