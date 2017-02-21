#Chirag Kashyap TAC iiData 2017
library(stringr)
library(ggplot2)
library(reshape2)

ffclean6 <- read.csv("C:/Users/ckashyap/Downloads/ffclean6.csv")
food = ffclean6 #easier to type

#Question 1
#convert to character to find string "France"
food$countries_en = as.character(food$countries_en)

#find string "France" and make dataframe of all with string "France"
#https://www.rdocumentation.org/packages/stringr/versions/1.1.0/topics/str_detect
frenchfood = food[which(str_detect(food$countries_en, "France")),]
frenchfood$countries_en = as.factor(frenchfood$countries_en)
notfrench = food[!str_detect(food$countries_en, "France"),]
notfrench$countries_en = as.factor(notfrench$countries_en)
#making sure
levels(frenchfood$countries_en)

#all rows have french nutrition score
which(is.na(food$nutrition_score_fr_100g) == TRUE)

nrow(frenchfood)
#23680 products from France
nrow(notfrenchfood)
#7469 non french products

summary(notfrench$nutrition_score_fr_100g)
summary(frenchfood$nutrition_score_fr_100g)

frenchfood$product_name = as.character(frenchfood$product_name)
notfrench$product_name = as.character(notfrench$product_name)

#https://stat.ethz.ch/R-manual/R-devel/library/base/html/match.html
same = frenchfood[complete.cases(match(frenchfood$product_name, notfrench$product_name)),]
same = same[str_detect(same$product_name, ""),]

same2 = notfrench[complete.cases(match(notfrench$product_name, frenchfood$product_name)),]
same2 = same2[str_detect(same2$product_name, ""),]
same$product_name = as.factor(same$product_name)
same2$product_name = as.factor(same2$product_name)

#aggregate http://stackoverflow.com/questions/28274711/aggregating-according-to-factor-levels-in-r-create-new-columns
finalfrench = aggregate(nutrition_score_fr_100g ~ product_name, same, "mean")
finalnotfrench = aggregate(nutrition_score_fr_100g ~ product_name, same2, "mean")

#http://stackoverflow.com/questions/21236229/stacked-bar-chart
final = merge(finalfrench, finalnotfrench, by = "product_name")
final = melt(final)
ggplot(data = final, aes(final$product_name, final$value, fill = final$variable)) + geom_bar(stat = "identity")
  
#Question 2

type = food[which(str_detect(food$main_category_en, c("Sugary snacks", "Dairies", "Fresh foods", "Meats"  ))),]
type.1 = glm(main_category_en ~ sodium_100g + energy_100g + fat_100g + saturated_fat_100g
             + carbohydrates_100g + sugars_100g + fiber_100g + proteins_100g + salt_100g
             + nutrition_score_fr_100g + nutrition_score_uk_100g, data = type, family = binomial(link="logit"))
summary(type.1)
